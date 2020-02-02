from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = 'Power2Create.in'

admin.site.register(models.User)
admin.site.register(models.library)
admin.site.register(models.payment_methods)
admin.site.register(models.ammenities)
admin.site.register(models.library_images)
admin.site.register(models.library_videos)
admin.site.register(models.bookmark)

admin.site.register(models.weekday)
admin.site.register(models.testimonial)
admin.site.register(models.enquiry)
admin.site.register(models.bug_report)

admin.site.register(models.comaprison)
admin.site.register(models.faq)
admin.site.register(models.Contact)

