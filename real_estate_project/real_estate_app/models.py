from django.db import models
from django.core.validators import EmailValidator



class LandResale(models.Model):
    email = models.EmailField(validators=[EmailValidator()], unique=False)
    length = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 10.5
    width = models.DecimalField(max_digits=10, decimal_places=2)   # Example: 20.25
    plot_area = models.DecimalField(max_digits=10,decimal_places=2)  # Example: '100 sq. ft.'
    cent = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    acre = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    district = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    price_per_cent = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 50000.00
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 50000.00
    price_per_square_feet = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 50000.00
    description = models.CharField(max_length=500)
    primary_number = models.CharField(max_length=20, unique=False)
    secondary_number = models.CharField(max_length=20, unique=False)
    images = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "land_resale"


class ResidentialRent(models.Model):
    bhk = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    totalfloor = models.CharField(max_length=50)
    property_age = models.CharField(max_length=50)
    builtup_area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    rent = models.CharField(max_length=50)
    lease = models.CharField(max_length=50)
    expected_rent = models.CharField(max_length=50)
    expected_deposit = models.CharField(max_length=50)
    expected_lease_amount = models.CharField(max_length=50)
    maintenance = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "residential_rent"

class LoginDetails(models.Model):
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    otp = models.CharField(max_length=6)  # Assuming OTP length is 6 digits
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "login_details"