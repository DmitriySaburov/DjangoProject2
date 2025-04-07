from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"модель: {self.__class__.__name__}, name={self.name}"


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    
    def __str__(self):
        return f"модель: {self.__class__.__name__}, name={self.name}, price={self.price}, company={self.company}"