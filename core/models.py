from django.db import models

# Create your models here.
class TrendProducts(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 1000)
    price = models.FloatField()
    product_image = models.ImageField(upload_to="media")
    def __str__(self):
        return f"({self.id}) {self.product_image} {self.name} ({self.price})"

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")
    def __str__(self):
            return f"({self.id}) {self.image}"


class BlockProducts(models.Model):
    bname = models.CharField(max_length = 200)
    bdescription = models.TextField(max_length = 1000)
    bprice = models.FloatField()
    b_image = models.ImageField(upload_to="block_products")
    def __str__(self):
        return f"({self.id}) {self.b_image} {self.bname} ({self.bprice})"

class PaverProducts(models.Model):
    pname = models.CharField(max_length = 200)
    pdescription = models.TextField(max_length = 1000)
    pprice = models.FloatField()
    p_image = models.ImageField(upload_to="paver_products")
    def __str__(self):
        return f"({self.id}) {self.p_image} {self.pname} ({self.pprice})"

class SlabProducts(models.Model):
    sname = models.CharField(max_length = 200)
    sdescription = models.TextField(max_length = 1000)
    sprice = models.FloatField()
    s_image = models.ImageField(upload_to="slab_products")
    def __str__(self):
        return f"({self.id}) {self.s_image} {self.sname} ({self.sprice})"