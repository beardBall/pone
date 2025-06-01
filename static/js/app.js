// alert('app here');

$(document).ready(
    function() {
    // alert('doc ready');

    $('.btn').click(function(){
        $.ajax({
            url: '',
            type: 'GET',
            contentType: 'application/json',
            data: {
                button_text: $(this).text()
            },
            success: function(response){
                $('#results').append("<li>" + response.seconds + "</li>");
                // alert('success' + response);
            }

        }); //end btn.click
        $('#results').on('click', 'li', function(){
            // console.log('paragraph clicked');
            // alert('paragraph clicked');
            console.log("data: " + $(this).text());


            $.ajax({
                url: '',
                type: 'post',
                contentType: 'application/json',
                console: true,
                data: JSON.stringify({
                    text: $(this).text(),
                }),

                success: function(response) {
                    // alert('Success!! ' + response);
                    console.log("suceess!! response: " + response.data)
                    $('#right-list').append('<li>' + response.data + '</li>');
                }

            })

        })




    }); //end function document.ready inner function

});//end function document.ready