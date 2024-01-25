from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=255,null=True,blank=True)
    registered_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Contact Page'

class Room(models.Model):
    room_status=[('presidential','presidential'),
    ('luxury','luxury'),
    ('deluxe','deluxe')]
    room_number=models.CharField(max_length=20)
    feature_name=models.CharField(max_length=50)
    image=models.FileField(upload_to='room',blank=True,null=True)
    people=models.IntegerField()
    area=models.IntegerField()
    details=models.TextField(max_length=250,null=True,blank=True)
    price=models.CharField(max_length=50)
    Featured_image=models.BooleanField(default=False)
    normal_display=models.BooleanField(default=False)
    created_at=models.DateField()
    room_quality=models.CharField(choices=room_status,default='deluxe',max_length=50)


    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name_plural='Room'

class Book(models.Model):
    arrival_date=models.DateField()
    departure_time=models.DateField()
    room=models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    no_guests=models.CharField(max_length=20)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    phone=models.CharField(max_length=20)

    def __str__(self):
        try:
            return self.room.room_name
        except:
            return self.no_guests

    class Meta:
        verbose_name_plural='Book'

class Staff(models.Model):
    Type=[('staff','staff'),
    ('cook','cook')]
    name=models.CharField(max_length=50)
    image=models.FileField(upload_to='staff_images')
    depart=models.CharField(choices=Type,max_length=50)
    about=models.CharField(max_length=250,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='staff'

class Blog(models.Model):
    category=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    about=models.CharField(max_length=250)
    image=models.FileField(upload_to='blog',null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural='Blog'


class AboutUs(models.Model):
    company_name=models.CharField(max_length=100)
    company_motto=models.CharField(max_length=255)
    about_us=models.CharField(max_length=255)
    description=models.CharField(max_length=250,null=True,blank=True)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()

    email=models.CharField(max_length=40)
    images=models.FileField(upload_to='company_image',null=True,blank=True)
    about_page_image=models.FileField(upload_to='company_image',null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural='AboutUs'

class BlogComment(models.Model):
    main_blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    profile=models.FileField(upload_to='comment_profile',null=True,blank=True)
    commenter=models.CharField(max_length=40)
    comment_date=models.DateField()

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural='BlogComment'



