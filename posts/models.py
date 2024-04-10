from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    level = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='')
    desc = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Make:
        db_table = 'posts_user'

    def __str__(self):
        return self.username


class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255)

    class Make:
        db_table = 'posts_categories'

    def __str__(self):
        return self.name


class Topics(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Make:
        db_table = 'posts_topics'

    def __str__(self):
        return self.subject


class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
