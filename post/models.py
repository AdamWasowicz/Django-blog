from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=48)
    register_date = models.DateField()
    email = models.EmailField()
    hashed_password = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    is_visible = models.BooleanField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return f"{self.author.username} - {self.title} - {self.date}"


class Comment(models.Model):
    content = models.TextField(max_length=256)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return f"{self.author.username} - {self.content}"