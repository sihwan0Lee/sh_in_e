from django.db import models
from user.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    published_date = models.DateTimeField(
        auto_now_add=True, verbose_name='게시 날짜')

# admin page
    def __str__(self):
        return '%s - %s' % (self.id, self.title)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        db_table = 'boards'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.user)

    class Meta:
        db_table = 'comments'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'
