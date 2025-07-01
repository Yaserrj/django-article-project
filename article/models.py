from django.db import models

# Create your models here.
class Articleitem(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    date=models.DateField(auto_now_add=True)
    mainTF = models.BooleanField(default=True)
    def __str__(self):
        return f"{ self.title } "
    class Meta:
        verbose_name = "Article Item"
    
class contactos (models.Model):
    fname_lname = models.CharField( max_length=60)
    Message = models.TextField(default="")
    Email = models.EmailField(default="",max_length=254)
    date =models.DateField( auto_now_add=True)
        
    def __str__(self):
        return f"{ self.fname_lname }  /  { self.title } "
    class Meta:
        verbose_name = "Contact Us"
    
# models.py
class Comment(models.Model):
    article = models.ForeignKey(Articleitem, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"