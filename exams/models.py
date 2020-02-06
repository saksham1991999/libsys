from django.db import models
from core.models import User

Exam_Choices = (
    ('S', 'SSC'),
    ('U', 'UPSC'),
)

Month_Choices = (
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
)

class previous_year(models.Model):
    exam_type = models.CharField(max_length=1, choices=Exam_Choices)

    exam_category = models.CharField(max_length=70)
    exam_title = models.CharField(max_length=100)

    set = models.IntegerField()
    year = models.IntegerField()
    questions = models.FileField(upload_to='previous_years')
    answers = models.FileField(upload_to='previous_years')

    def __str__(self):
        title = self.exam_type + str(self.year)
        return title

    class Meta:
        verbose_name_plural = 'Previous Year Questions/Answers'

class current_affair(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    month = models.CharField(choices=Month_Choices, max_length=3)
    year = models.IntegerField()
    file = models.FileField()

    def __str__(self):
        return self.title
