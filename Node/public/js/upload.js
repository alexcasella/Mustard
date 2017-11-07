$('#upload-btn').on('click', function(){

    let files = $("#upload-input").get(0).files;

    if (files.length > 0){
        // create a FormData object which will be sent as the data payload in AJAX request
        let formData = new FormData();

        // loop through all the selected files and add them to the formData object
        for (let i = 0; i < files.length; i++) {
            let file = files[i];

            // add the files to formData object for the data payload
            formData.append('uploads[]', file, file.name);
        }

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                console.log('upload successful!\n' + data);
            }
        });
    }
});