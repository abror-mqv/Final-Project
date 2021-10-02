from django.contrib import admin
from .models import Tablet, Laptop, Camera, Produccer, Ram, Mem_hdd, Mem_ssd, Cpu, Graph, OS, Resolution, DisplaySize, City
# Register your models here.

admin.site.register(Tablet)
admin.site.register(Laptop)
admin.site.register(Camera)
admin.site.register(City)
admin.site.register(Produccer)
admin.site.register(Ram)
admin.site.register(Mem_ssd)
admin.site.register(Mem_hdd)
admin.site.register(Cpu)
admin.site.register(Graph)
admin.site.register(OS)
admin.site.register(Resolution)
admin.site.register(DisplaySize)

