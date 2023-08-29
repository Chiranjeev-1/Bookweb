from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Statusupload(models.Model):
    CHOICES = (
        ('completed', 'completed'),
        ('reading', 'reading'),
        ('planning', 'planning'),
        ('dropped','dropped')
    )

    reader = models.ForeignKey(User,on_delete=models.CASCADE)
    title =models.CharField(max_length=255,null=True)
    author = models.CharField(max_length=255,null=True)
    publisheddate = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=20, choices=CHOICES)
    score = models.PositiveIntegerField(blank=True,null=True,default=0)
    image = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(max_length=500,null=True)
    startdate = models.DateField(default=timezone.now ,null=True)
    completedate = models.DateField(default=timezone.now ,null=True)
    note = models.TextField(null=True,max_length=5000,blank=True)
    Bookid = models.CharField(max_length=255,null=True)
    

class followrequestNotifs(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    requestby = models.CharField(max_length=255)


class followers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    follower = models.CharField(max_length=255)

class Notifs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    notifstatement = models.CharField(max_length=1000,blank=True,null=True)
    notifby = models.CharField(max_length=255,blank=True,null=True)


class Bio(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=255,blank=True,null=True)
    profileimage = models.ImageField(blank=True,null=True,upload_to='images/')
    Banner = models.ImageField(blank=True,null=True,upload_to='images/')
    selfdescription = models.TextField(max_length=10000,blank=True,null=True)


class following(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    following = models.CharField(max_length=255)


class Forumdata(models.Model):

    

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    postdate = models.DateField(default=timezone.now,blank=True,null=True)
    profilephoto = models.ImageField(upload_to='images/',blank=True,null=True,default=r'Bibilocheck\static\images\usericon.png')
    posttitle = models.TextField(max_length=1000,blank=True,null=True)

    post = models.TextField(max_length=1000000,blank=True,null=True)


class OriginalPOST(models.Model):
    CHOICES = (
        ('Novel','Novel'),
        ('Fanfic','Fanfic'),
        ('Short-story','Short-story'),
        ('Poem','Poem'),
         ('other',"other")
    )
    UP_FOR_REVIEW = (('Yes','Yes'),
                     ('NO','No'))
    

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.FileField(upload_to='pdfs/',blank=True,null=True)
    posttype = models.CharField(max_length=255, choices=CHOICES)
    Bookcover = models.ImageField(upload_to='images/',blank=True,null=True)
    Synopsis = models.TextField(max_length=10000,blank=True,null=True)
    upload_date = models.DateField(default=timezone.now,blank=True,null=True)
    authorname = models.CharField(max_length=255,blank=True,null=True)
    Booktitle = models.CharField(max_length=255,blank=True,null=True)
    UpforReview = models.CharField(max_length=255,choices=UP_FOR_REVIEW,blank=True,null=True)


class Subscribe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    postby = models.CharField(max_length=255,blank=True,null=True)
    postname = models.CharField(max_length=255,blank=True,null=True)
