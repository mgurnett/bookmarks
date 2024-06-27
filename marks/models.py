from django.db import models

class Catagory (models.Model):
    name = models.CharField(max_length=200)

class Sub (models.Model):
    catagory = models.ForeignKey(
        "Catagory",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    

class Bookmark (models.Model):
    sub = models.ForeignKey(
        "Sub",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    url = models.URLField(max_length=200)
