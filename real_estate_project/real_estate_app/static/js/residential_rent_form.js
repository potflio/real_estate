$(document).ready(function(){  
    $('#residential_rent_create').on('click',function(){
        $bhkType = $('#bhkType').val();
        $floor = $('#floor').val();
        $totalFloor = $('#totalFloor').val();
        $propertyAge = $('#propertyAge').val();
        $builtUpArea = $('#builtUpArea').val();
        $city = $('#city').val();
        $locality = $('#locality').val();
        $landmark = $('#landmark').val();
        $rentalOnly = $('#rentalOnly').val();
        $leaseOnly = $('#leaseOnly').val();
        $expectedRent = $('#expectedRent').val();
        $expectedDeposit = $('#expectedDeposit').val();
        $expectedLeaseAmount = $('#expectedLeaseAmount').val();
        $monthlyMaintenance = $('#monthlyMaintenance').val();
        $description = $('#description').val();
//         if($bhkType == "" || $floor == "" || $totalFloor == "" || $propertyAge == "" || 
//         $builtUpArea == "" || $city == "" || $locality == "" || $landmark == "" || $rentalOnly == ""
//     || $leaseOnly == "" || $expectedRent == "" || $expectedDeposit == "" ||
// $expectedLeaseAmount == "" || $monthlyMaintenance == "" || $description == ""){
//             alert("Please Fill the form");
//         }else{
            $.ajax({
                url: 'residential_rent_create/',
                type: 'POST',
                data: {
                    bhk : $bhkType,
                    floor : $floor,
                    totalfloor : $totalFloor,
                    property_age : $propertyAge,
                    builtup_area : $builtUpArea,
                    city : $city,
                    locality : $locality,
                    landmark : $landmark,
                    rent: $rentalOnly,
                    lease : $leaseOnly,
                    expected_rent : $expectedRent,
                    expected_deposit : $expectedDeposit,
                    expected_lease_amount : $expectedLeaseAmount,
                    maintenance : $monthlyMaintenance,
                    description : $description,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(){
                    // Read()
                    $('#bhkType').val('');
                    $('#floor').val('');
                    $('#totalfloor').val('');
                    $('#property_age').val('');
                    $('#builtup_area').val('');
                    $('#city').val('');
                    $('#locality').val('');
                    $('#landmark').val('');
                    $('#rent').val('');
                    $('#lease').val('');
                    $('#expected_rent').val('');
                    $('#expected_deposit').val('');
                    $('#expected_lease_amount').val('');
                    $('#maintenance').val('');
                    $('#description').val('');
                    alert("New Property Inserted");
                }
            
            });
        // }
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

