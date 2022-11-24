from django.db import models

class category(models.model):
    category_name=models.CharField(max_length=45)
    
        