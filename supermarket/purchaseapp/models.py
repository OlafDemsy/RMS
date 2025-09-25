# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from logPermission.models import marketuser
from salesapp.models import Products

class Inventory(models.Model):
    stock_id = models.AutoField(primary_key=True)
    product = models.OneToOneField(Products, models.DO_NOTHING, blank=True, null=True)
    inventory_quantity = models.IntegerField()
    INVENTORY_PLACE_CHOICES = [
        ('仓库A', '仓库A'),
        ('仓库B', '仓库B'),
        ('仓库C', '仓库C'),
        ('仓库D', '仓库D'),
    ]
    inventory_places = models.CharField(max_length=10, choices=INVENTORY_PLACE_CHOICES)
    reorder_threshold = models.IntegerField(default=10)

    def is_below_threshold(self):
        return self.inventory_quantity < self.reorder_threshold

    class Meta:
        managed = False
        db_table = 'inventory'


class Providers(models.Model):
    PROVIDER_CHOICES = [
        ('广州市食品供应有限公司', '广州市食品供应有限公司'),
        ('上海百货批发中心', '上海百货批发中心'),
        ('北京优选饮品贸易公司', '北京优选饮品贸易公司'),
        ('深圳农产品配送公司', '深圳农产品配送公司'),
        ('杭州休闲食品有限公司', '杭州休闲食品有限公司'),
    ]
    provider_id = models.IntegerField(primary_key=True)
    provider_name = models.CharField(max_length=50, choices=PROVIDER_CHOICES)
    contact = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'providers'


class PurchaseRecords(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    purchase_record_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(marketuser, models.DO_NOTHING, blank=True, null=True)
    provider = models.ForeignKey(Providers, models.DO_NOTHING, blank=True, null=True)
    stock = models.ForeignKey(Inventory, models.DO_NOTHING, blank=True, null=True)
    purchase_quantity = models.IntegerField()
    purchase_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    purchase_total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'purchase_records'
