from django.db import models


class Secretaria(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='STRIA Y/O DIRECCIONES')
    number = models.CharField(max_length=9, verbose_name='Nº TELEFONO')
    fax = models.CharField(max_length=9, verbose_name='FAX')
    address = models.CharField(max_length=50, verbose_name='DIRECCION')
    lat = models.CharField(max_length=50, verbose_name='Latitud')
    lng = models.CharField(max_length=50, verbose_name='Longitud')

    def __str__(self):
        return self.name


class Unidad(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, default=1, verbose_name='SECRETARIA')
    name = models.CharField(max_length=100, unique=True, verbose_name='STRIA Y/O DIRECCIONES')
    number = models.CharField(max_length=9, verbose_name='Nº TELEFONO')
    fax = models.CharField(max_length=9, verbose_name='FAX')
    address = models.CharField(max_length=50, verbose_name='DIRECCION')
    lat = models.CharField(max_length=50, verbose_name='Latitud')
    lng = models.CharField(max_length=50, verbose_name='Longitud')

    def __str__(self):
        return self.name


class Personal_unidad(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, default=1, verbose_name='UNIDAD')
    name = models.CharField(max_length=50, verbose_name='NOMBRE')
    lastname = models.CharField(max_length=50, verbose_name='APELLIDO')
    position = models.CharField(max_length=100, verbose_name='POSITION')
    telephone = models.CharField(max_length=9, verbose_name='Nº TELEFONO')
    phone = models.CharField(max_length=9, verbose_name='Nº CELULAR')
    image = models.ImageField(upload_to='fotos', verbose_name='FOTO', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.lastname)


class Personal_secretaria(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, default=1, verbose_name='SECRETARIA')
    name = models.CharField(max_length=50, verbose_name='NOMBRE')
    lastname = models.CharField(max_length=50, verbose_name='APELLIDO')
    position = models.CharField(max_length=100, verbose_name='POSITION')
    telephone = models.CharField(max_length=9, verbose_name='Nº TELEFONO')
    phone = models.CharField(max_length=9, verbose_name='Nº CELULAR')
    image = models.ImageField(upload_to='fotos', verbose_name='FOTO', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.lastname)

# Create your models here.
