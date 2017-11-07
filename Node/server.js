// TO DO:
// multiple file upload
// pass path of file to python

var express = require("express");
var app = express();
var formidable = require("formidable");
var fs = require("fs");
var path = require("path");
var PythonShell = require('python-shell');

app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', function(req, res){
    res.sendFile(path.join(__dirname, 'views/index.html'));
});

app.post('/upload', function(req, res){
    // create an incoming form object
    let form = new formidable.IncomingForm();

    // specify that we want to allow the user to upload multiple files in a single request
    // form.multiples = true;

    // store all uploads in the /uploads directory
    form.uploadDir = path.join(__dirname, '/uploads');

    // every time a file has been uploaded successfully,
    // rename it to it's original name
    let fileName = "";
    let p = new Promise((resolve, reject) => {
        form.on('file', function (field, file) {
            fs.rename(file.path, path.join(form.uploadDir, file.name), function (err) {
                if (err != null) {
                    console.log(err);
                }
                fileName = path.join(form.uploadDir, file.name);
                resolve(fileName);
            });
        });
    });

    p.then((fileName) => {
        // =====================================================//
        //                     Python                           //
        // =====================================================//

        let options = {
            mode: 'text',
            args: [fileName]
        };

        PythonShell.run('/python/generate.py', options, function (err, results) {
            if (err) {
                throw err;
            }

            results.forEach(function(result) {
                console.log('result: %j', result);
            });

            console.log('Finished running python');
        });
    });


    // log any errors that occur
    form.on('error', function(err) {
        console.log('An error has occured: \n' + err);
    });

    // once all the files have been uploaded, send a response to the client
    form.on('end', function() {
        res.end('success');
    });

    // parse the incoming request containing the form data
    form.parse(req);
});

app.listen(3000, "localhost", () => {
    console.log("Server up");
});
