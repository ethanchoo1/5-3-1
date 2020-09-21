from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    max_bench = models.IntegerField()
    max_squat = models.IntegerField()
    max_deadlift = models.IntegerField()
    max_ohp = models.IntegerField()
    def __str__(self):
        return self.pub_name + ' commented ' + self.comment_text