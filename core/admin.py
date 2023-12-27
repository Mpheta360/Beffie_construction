from django.contrib import admin

# Register your models here.
from .models import TrendProducts
from . models import Gallery
from . models import BlockProducts
from . models import SlabProducts
from . models import PaverProducts

admin.site.register(TrendProducts)
admin.site.register(Gallery)
admin.site.register(BlockProducts)
admin.site.register(SlabProducts)
admin.site.register(PaverProducts)