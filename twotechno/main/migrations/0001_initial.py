# Generated by Django 3.2.5 on 2021-08-26 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=127, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Процессор')),
                ('core', models.IntegerField(verbose_name='Кол-во ядер')),
            ],
        ),
        migrations.CreateModel(
            name='DisplaySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_size', models.CharField(max_length=127, verbose_name='Диагональ дисплея')),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Видеокарта')),
            ],
        ),
        migrations.CreateModel(
            name='Mem_hdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_hdd', models.PositiveIntegerField(verbose_name='Обём хддшника')),
            ],
        ),
        migrations.CreateModel(
            name='Mem_ssd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_ssd', models.PositiveIntegerField(verbose_name='Обём ссдшника')),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Наименование ОС')),
                ('x', models.PositiveIntegerField(verbose_name='Разряд ОС')),
            ],
        ),
        migrations.CreateModel(
            name='Produccer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Имя производителя')),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram', models.PositiveIntegerField(verbose_name='Оперативная память')),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_resolution', models.CharField(max_length=127, verbose_name='Разрешение дисплея')),
            ],
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('main_image', models.ImageField(upload_to='', verbose_name='Лицевое изображение')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city', verbose_name='Город')),
                ('mem_ssd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.mem_ssd', verbose_name='SSD')),
                ('produccer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.produccer', verbose_name='Производитель')),
                ('ram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.ram', verbose_name='RAM')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('main_image', models.ImageField(upload_to='', verbose_name='Лицевое изображение')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city', verbose_name='Город')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.cpu', verbose_name='CPU')),
                ('display_resolution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.resolution', verbose_name='Разрешение дисплея')),
                ('display_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.displaysize', verbose_name='Диагональ дисплея')),
                ('graph', models.ManyToManyField(null=True, to='main.Graph', verbose_name='Видеокарта')),
                ('mem_hdd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.mem_hdd', verbose_name='HDD')),
                ('mem_ssd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.mem_ssd', verbose_name='SSD')),
                ('operating_system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.os', verbose_name='OS')),
                ('produccer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.produccer', verbose_name='Производитель')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.ram', verbose_name='RAM')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('main_image', models.ImageField(upload_to='', verbose_name='Лицевое изображение')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Дополнительное изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city', verbose_name='Город')),
                ('produccer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.produccer', verbose_name='Производитель')),
            ],
        ),
    ]