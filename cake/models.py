from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone=models.CharField(max_length=12)
    adress=models.CharField(max_length=200)



class CakeCategory(models.Model):
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.name


class CakeOccation(models.Model):
    options=(
        ('birthday cake','birthday cake'),
        ('anniverssary cake','anniverssary cake'),
        ('congratulation cake','congratulation cake'),
        ('marriage cake','marriage cake')
    )
    occation=models.CharField(max_length=200,choices=options)
    images=models.ImageField(upload_to='images',)
    category=models.ForeignKey(CakeCategory,on_delete=models.CASCADE)
    @property
    def varients(self):
        qs=self.cakevarient_set.all()
        return qs
    
    
    def __str__(self):
        return self.occation

class CakeVarient(models.Model):
    price=models.PositiveIntegerField()
    shape=models.CharField(max_length=200)
    weight=models.CharField(max_length=200,null=True)
    occation=models.ForeignKey(CakeOccation,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.occation.occation

class CakeCart(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    cakename=models.ForeignKey(CakeVarient,on_delete=models.SET_NULL,null=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

   
class CakeOrder(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    cakename=models.ForeignKey(CakeCategory,on_delete=models.CASCADE)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakename=models.ForeignKey(CakeCategory,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)




