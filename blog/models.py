from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=15)
    content = models.TextField()
    image = models.ImageField(upload_to="images", default="default.png", blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    STATUS_OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    status = models.CharField(max_length=1, choices=STATUS_OPTIONS, default='p')

    def __str__(self):
        return self.title
    
    @property
    def comment_count(self):
        # return self.comment_set
        return self.comments.all().count()
    
    @property
    def comments(self):
        return self.comments.all()
    
    @property
    def like_count(self):
        return self.like_set.all().count()
    
    @property
    def view_count(self):
        return self.postview_set.all().count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username