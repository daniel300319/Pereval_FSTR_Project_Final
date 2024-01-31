from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Pereval(models.Model):
    STATUS = [('new', 'new'),
              ('pending', 'pending'),
              ('accepted', 'accepted'),
              ('rejected', 'rejected')]
    status = models.CharField(max_length=2, choices=STATUS, default='NEW')
    beauty_title = models.CharField(max_length=10, default='пер.')
    title = models.CharField(max_length=25)
    other_titles = models.CharField(max_length=25)
    connect = models.CharField(max_length=25, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    level_winter = models.CharField(max_length=2, blank=True)
    level_summer = models.CharField(max_length=2, blank=True)
    level_autumn = models.CharField(max_length=2, blank=True)
    level_spring = models.CharField(max_length=2, blank=True)



class Coord(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='coordinations')
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    height = models.CharField(max_length=15)


class Image(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=50)


class PerevalImage(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='photo')
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='pereval')