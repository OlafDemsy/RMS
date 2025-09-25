# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from logPermission.models import marketuser

class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=20)
    phone = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'customers'


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=20)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField(blank=True, default=9999, validators=[
                                                                                    MinValueValidator(0),
                                                                                    MaxValueValidator(9999)
                                                                                ])
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'products'


class SalesRecords(models.Model):
    sales_record_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(marketuser, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    sales_quantity = models.IntegerField()
    sales_total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    sales_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'sales_records'
