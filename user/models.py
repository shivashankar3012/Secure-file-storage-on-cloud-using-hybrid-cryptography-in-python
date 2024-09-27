# from pyexpat import model
# from django.db import models
# from django.forms import CharField, EmailField, IntegerField

# # Create your models here.
# class RegisterModel(Model):
#     firstname=CharField(max_length=300)
#     lastname=CharField(max_length=200)
#     userid=CharField(max_length=200)
#     password=IntegerField()
#     mblenum=BigIntegerField()
#     email=EmailField(max_length=400)
#     gender=CharField(max_length=200)

# class UploadModel(model):
#     file_name=CharField(max_length=100)
#     category=CharField(max_length=100)
#     upload_user=ForeignKey(RegisterModel)
#     upload_file=FileField()
#     area=CharField(max_length=200)
#     add_count=IntegerField(default='0')

# class RequestModel(Model):
#     accessone = ForeignKey(RegisterModel)
#     accesstwo = ForeignKey(UploadModel)
#     request = CharField(max_length=200, default='pending')
#     cate=CharField(max_length=500)

# class FeedbackModel(Model):
#     username = ForeignKey(RegisterModel)
#     feedback = CharField(max_length=300)
# class UploadModel(Model):
#     upload_user = ForeignKey(RegisterModel, on_delete=CASCADE)
#     # other fields

from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.IntegerField()
    mblenum = models.BigIntegerField()
    email = models.EmailField(max_length=400)
    gender = models.CharField(max_length=200)

class UploadModel(models.Model):
    file_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    upload_user = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)  # Fix
    upload_file = models.FileField()
    area = models.CharField(max_length=200)
    add_count = models.IntegerField(default=0)

class RequestModel(models.Model):
    accessone = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)  # Fix
    accesstwo = models.ForeignKey(UploadModel, on_delete=models.CASCADE)  # Fix
    request = models.CharField(max_length=200, default='pending')
    cate = models.CharField(max_length=500)

class FeedbackModel(models.Model):
    username = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)  # Fix
    feedback = models.CharField(max_length=300)
