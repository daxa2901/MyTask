from django.db import models

# Create your models here.
class MyList(models.Model):
    SINO = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    ParentId= models.ForeignKey('self', on_delete=models.CASCADE,parent_link=True,related_query_name='child',null=True, related_name='child')
# Create your models here.

    def __str__(self):
        return self.Title
