from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.current_affair_categories)
admin.site.register(models.current_affair)
admin.site.register(models.current_affairs_likes)
admin.site.register(models.current_affairs_uplifts)
admin.site.register(models.comment)
admin.site.register(models.previous_year)