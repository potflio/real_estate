$(document).ready(function(){  
    $('#land_create').on('click',function(){
        $plot_area = $('#plot_area').val();
        $length = $('#length').val();
        $width = $('#width').val();
        $city = $('#city').val();
        $locality = $('#locality').val();
        $landmark = $('#landmark').val();
        $expected_price = $('#expected_price').val();
        $description = $('#description').val();
        if($plot_area == "" || $length == "" || $width == "" || $city == "" || $locality == "" || $landmark == "" || $expected_price == "" || $description == ""){
            alert("please complete the required field");
        }else{
            $.ajax({
                url: 'land_create/',
                type: 'POST',
                data: {
                    plot_area : $plot_area,
                    length : $length,
                    width : $width,
                    city : $city,
                    locality : $locality,
                    landmark : $landmark,
                    expected_price : $expected_price,
                    description : $description,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(){
                    // Read()
                    $('#plot_area').val('');
                    $('#length').val('');
                    $('#width').val('');
                    $('#city').val('');
                    $('#locality').val('');
                    $('#landmark').val('');
                    $('#expected_price').val('');
                    $('#description').val('');
                    alert("New Property Inserted");
                }
            });
        }
    });
});

// function Read(){
//     $.ajax({
//         url:'land_result/',
//         type: 'POST',
//         async:false,
//         data:{
//             res:1,
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//         }
        
//     })
// }

