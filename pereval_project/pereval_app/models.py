from django.db import models

ADD_STATUS = [('new', 'new'),
              ('pending', 'pending'),
              ('accepted', 'accepted'),
              ('rejected', 'rejected')]


class User(models.Model):
    email = models.EmailField(unique=True)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'pereval_user'


class Coord(models.Model):
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    height = models.CharField(max_length=15)

    class Meta:
        db_table = 'pereval_coord'


class Pereval(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coord, on_delete=models.CASCADE)
    winter_level = models.CharField(max_length=10, blank=True)
    summer_level = models.CharField(max_length=10, blank=True)
    autumn_level = models.CharField(max_length=10, blank=True)
    spring_level = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=50, choices=ADD_STATUS, default=ADD_STATUS[0])

    class Meta:
        db_table = 'pereval'


class Image(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=50)
    img = models.BinaryField()
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pereval_images'

