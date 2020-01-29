from django.db import models
from core.models import User

Exam_Choices = (
    ('E', 'Exam'),
    ('R', 'Result'),
)

class current_affair_categories(models.Model):
    title = models.CharField(max_length = 100)
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Current Affairs Categories'

class previous_year(models.Model):
    exam_type = models.CharField(max_length=1, choices=Exam_Choices)
    year = models.IntegerField()
    questions = models.FileField()
    answers = models.FileField()

    def __str__(self):
        title = self.exam_type + str(self.year)
        return title

    class Meta:
        verbose_name_plural = 'Previous Year Questions/Answers'

class current_affair(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    postedon = models.DateField(auto_now_add=True)
    postedby = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(current_affair_categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def no_of_likes(self):
        count = current_affairs_likes.objects.filter(current_affair = self).count()
        return count

    def get_short_content(self):
        if len(self.description) > 500:
            short_content = self.description[:500]
            short_content += "..."
            return short_content
        return self.description


class current_affairs_likes(models.Model):
    current_affair = models.ForeignKey(current_affair, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class current_affairs_uplifts(models.Model):
    current_affair = models.ForeignKey(current_affair, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class comment(models.Model):
    current_affair = models.ForeignKey(current_affair, on_delete=models.CASCADE, related_name = 'current_affair')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'current_affair_user')
    name = models.CharField(max_length=100)
    date = models.DateField()
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text

    def get_username(self):
        username = self.user.username
        return username

    def get_profileimage(self):
        profileimage = 'http://placehold.it/50x50'
        return profileimage