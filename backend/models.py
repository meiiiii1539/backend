from django.db import models

class Member(models.Model):
    class Meta:
        managed = False
        db_table = 'Member'
    mId = models.AutoField(primary_key=True)

# Create your models here.
class Product(models.Model):
    class Meta:
        managed = False
        db_table = 'Product'
    pId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    brand = models.CharField(max_length=255)
    age = models.IntegerField()
    size = models.CharField(max_length=100, default=' ')
    likes = models.IntegerField()
    state= models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    class Meta:
        managed = False
        db_table = 'Cart'
        unique_together = [['mId', 'pId']]

    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId", primary_key=True)
    mId = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="mId")
    cartTime = models.DateTimeField(db_column="cartTime")
    startTime = models.DateField(db_column="startTime")
    endTime = models.DateField(db_column="endTime")
   
class Picture(models.Model):
    class Meta:
        managed = False
        db_table = 'Picture'
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId", primary_key=True)
    picture = models.CharField(max_length=760)

