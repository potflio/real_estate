function calculate() {
    var length = parseFloat(document.getElementById('length').value) || 0;
    var width = parseFloat(document.getElementById('width').value) || 0;
    var price_per_cent = parseFloat(document.getElementById('price_per_cent').value) || 0;

    var plot_area = length * width;
    var cent = plot_area / 436;
    var acre = cent / 100;
    var total = cent * price_per_cent;
    var price_per_squre_feet = total / plot_area;

    document.getElementById('plot_area').value = plot_area.toFixed(2);
    document.getElementById('cent').value = cent.toFixed(2);
    document.getElementById('acre').value = acre.toFixed(2);
    document.getElementById('total_price').value = total.toFixed(2);
    document.getElementById('price_per_square_feet').value = price_per_squre_feet.toFixed(2);
}


function create(){
    let email = document.getElementById('email').value;
    let length = document.getElementById('length').value;
    let width = document.getElementById('width').value;
    let plot_area = document.getElementById('plot_area').value;
    let cent = document.getElementById('cent').value;
    let acre = document.getElementById('acre').value;
    let district = document.getElementById('district').value;
    let block = document.getElementById('block').value;
    let landmark = document.getElementById('landmark').value;
    let price_per_cent = document.getElementById('price_per_cent').value;
    let total_price = document.getElementById('total_price').value;
    let price_per_square_feet = document.getElementById('price_per_square_feet').value;
    let description = document.getElementById('description').value;
    let primary_number = document.getElementById('primary_number').value;
    let secondary_number = document.getElementById('secondary_number').value;
    var formData = new FormData();
    var files = document.getElementById('imageUpload').files;
    for (var i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
    }

    // Add CSRF token
    formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

    if(length == '' || width == '' || district == '' || block == '' || landmark == ''
        || price_per_cent == '' || description == '' || primary_number == '' || 
        secondary_number == ''){

            alert("Please required the Fields");
    }else{
        $.ajax({
            url : '/land/land_create/',
            type : 'POST',
            data : {
                email : email,
                length : length,
                width : width,
                plot_area : plot_area,
                cent : cent,
                acre : acre,
                district : district,
                block : block,
                landmark : landmark,
                price_per_cent : price_per_cent,
                total_price : total_price,
                price_per_square_feet : price_per_square_feet,
                description : description,
                primary_number : primary_number,
                secondary_number : secondary_number,
                files : formData,
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success : function(){
                document.getElementById('length').value = '';
                document.getElementById('width').value = '';
                document.getElementById('plot_area').value = '';
                document.getElementById('cent').value = '';
                document.getElementById('acre').value = '';
                document.getElementById('district').value = '';
                document.getElementById('block').value = '';
                document.getElementById('landmark').value = '';
                document.getElementById('price_per_cent').value = '';
                document.getElementById('total_price').value = '';
                document.getElementById('price_per_square_feet').value = '';
                document.getElementById('description').value = '';
                document.getElementById('primary_number').value = '';
                document.getElementById('secondary_number').value = '';
                alert("Property Insert Successfully");
            }
        });
    }

}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.view').forEach(function(element) {
        element.addEventListener('click', function() {
            var id = this.getAttribute('name');
            window.location.href = "land_view/" + id;
        });
    });
});