from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    url = models.URLField()  
    albums_sold = models.IntegerField()
    active_since = models.DateField()

    def __str__(self):
        return self.name
    
 

class Songs(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.DurationField()
    url = models.URLField()  


    def __str__(self):
        return self.title



class BrowseAll(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='browse_all_images/')
    url = models.URLField()
                                                           
    def __str__(self):
        return self.name
   
   
