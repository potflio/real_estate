from django.db import models
class LandResale(models.Model):
    plot_area = models.CharField(max_length=50)  # Example: '100 sq. ft.'
    length = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 10.5
    width = models.DecimalField(max_digits=10, decimal_places=2)   # Example: 20.25
    city = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    expected_price = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 50000.00
    description = models.CharField(max_length=500)

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

  