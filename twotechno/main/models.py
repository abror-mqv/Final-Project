from django.db import models

# Create your models here.
class Cpu(models.Model):
    name = models.CharField(verbose_name="Процессор", max_length=63)
    core = models.IntegerField(verbose_name="Кол-во ядер")
    def __str__(self):
        return self.name

class Produccer(models.Model):
    name = models.CharField(verbose_name="Имя производителя", max_length=63)
    def __str__(self):
        return self.name

class Ram(models.Model):
    ram = models.PositiveIntegerField(verbose_name="Оперативная память")
    def __str__(self):
        return str(self.ram)

class Mem_ssd(models.Model):
    mem_ssd = models.PositiveIntegerField(verbose_name="Обём ссдшника")
    def __str__(self):
        return str(self.mem_ssd)

class Mem_hdd(models.Model):
    mem_hdd = models.PositiveIntegerField(verbose_name="Обём хддшника")
    def __str__(self):
        return str(self.mem_hdd)

class Graph(models.Model):
    name = models.CharField(verbose_name="Видеокарта", max_length=63)
    def __str__(self):
        return self.name

class OS(models.Model):
    name = models.CharField(verbose_name="Наименование ОС", max_length=127)
    x = models.PositiveIntegerField(verbose_name="Разряд ОС")
    def __str__(self):
        return self.name

class Resolution(models.Model):
    screen_resolution = models.CharField(verbose_name="Разрешение дисплея", max_length=127)
    def __str__(self):
        return self.screen_resolution

class DisplaySize(models.Model):
    display_size = models.CharField(verbose_name="Диагональ дисплея", max_length=127)
    def __str__(self):
        return self.display_size

class City(models.Model):
    city = models.CharField(verbose_name="Город", max_length=127)
    def __str__(self):
        return str(self.city)

class Laptop(models.Model):
    city = models.ForeignKey(City, verbose_name="Город", default="Бишкек", on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name="Наименование товара", max_length=255)
    description = models.TextField(verbose_name="Описание", max_length=255)
    main_image = models.ImageField(verbose_name="Лицевое изображение")
    image_2 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_3 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_4 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_5 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    cpu = models.ForeignKey(Cpu, verbose_name="CPU", on_delete=models.PROTECT) #
    year = models.PositiveIntegerField(verbose_name="Год выпуска", null=True, blank=True)
    produccer = models.ForeignKey(Produccer, verbose_name="Производитель", on_delete=models.PROTECT) #
    ram = models.ForeignKey(Ram ,verbose_name="RAM", on_delete=models.PROTECT) 
    mem_ssd = models.ForeignKey(Mem_ssd,verbose_name="SSD", on_delete=models.PROTECT, null=True, blank=True) 
    mem_hdd = models.ForeignKey(Mem_hdd, verbose_name="HDD", on_delete=models.PROTECT, null=True, blank=True)     
    graph = models.ManyToManyField(Graph, verbose_name="Видеокарта")
    display_size = models.ForeignKey(DisplaySize, verbose_name="Диагональ дисплея", on_delete=models.PROTECT)    
    display_resolution = models.ForeignKey(Resolution, verbose_name="Разрешение дисплея", on_delete=models.PROTECT)
    operating_system = models.ForeignKey(OS, verbose_name="OS", on_delete=models.PROTECT, null=True, blank=True) 
    price = models.PositiveIntegerField(verbose_name='Цена')



    def __str__(self):
        return self.fullname


class Camera(models.Model):
    city = models.ForeignKey(City, verbose_name="Город", default="Бишкек", on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name="Наименование товара", max_length=255)
    description = models.TextField(verbose_name="Описание", max_length=255)
    main_image = models.ImageField(verbose_name="Лицевое изображение")
    image_2 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_3 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_4 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_5 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    produccer = models.ForeignKey(Produccer, verbose_name="Производитель", on_delete=models.PROTECT)
    price = models.PositiveIntegerField(verbose_name='Цена')
    def __str__(self):
        return self.fullname




class Tablet(models.Model):
    city = models.ForeignKey(City, verbose_name="Город", default="Бишкек", on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name="Наименование товара", max_length=255)
    description = models.TextField(verbose_name="Описание", max_length=255)
    main_image = models.ImageField(verbose_name="Лицевое изображение")
    image_2 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_3 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_4 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    image_5 = models.ImageField(verbose_name="Дополнительное изображение", null=True, blank=True)
    produccer = models.ForeignKey(Produccer, verbose_name="Производитель", on_delete=models.PROTECT) #
    ram = models.ForeignKey(Ram ,verbose_name="RAM", on_delete=models.PROTECT, null=True, blank=True) 
    mem_ssd = models.ForeignKey(Mem_ssd,verbose_name="SSD", on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.fullname
