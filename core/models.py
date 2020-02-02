from django.db import models
from django.contrib.auth.models import AbstractUser

Weekdays_Choices = (
    ('M', 'Monday'),
    ('Tu', 'Tuesday'),
    ('W', 'Wednesday'),
    ('Th', 'Thursday'),
    ('F', 'Friday'),
    ('Sa', 'Saturday'),
    ('Su', 'Sunday'),
)
class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class ammenities(models.Model):
    title = models.CharField(max_length=50)
    quantity = models.IntegerField(blank= True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ammenities'

class payment_methods(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Payment Methods'

class weekday(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self):
        return self.day

    class Meta:
        verbose_name_plural = 'Weekdays'

class library(models.Model):
    name = models.CharField(max_length=50)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_fname= models.CharField(max_length=50)
    owner_lname= models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.IntegerField()

    addr1 = models.CharField(max_length=50)
    addr2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    state = models.CharField(max_length=50)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    landline = models.IntegerField(blank=True, null=True)

    ammenities = models.ManyToManyField(ammenities)
    library_description = models.TextField(max_length=500)
    past_record_of_students = models.TextField(max_length=500, blank=True, null=True)
    payment_methods = models.ManyToManyField(payment_methods)
    fb_url = models.CharField(max_length=200, blank=True, null=True)
    insta = models.CharField(max_length=100, blank=True, null=True)
    google_map = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    main_image = models.ImageField()

    no_of_seats = models.IntegerField()
    opening_days = models.ManyToManyField(weekday)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    non_refundable_charges = models.IntegerField(blank=True, null=True)
    min_monthly_charges = models.IntegerField()
    min_price_range = models.IntegerField(blank=True, null=True)
    max_price_range = models.IntegerField(blank=True, null=True)

    verified = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Libraries'

class library_images(models.Model):
    image = models.ImageField()
    library = models.ForeignKey(library, on_delete=models.CASCADE)

    def __str__(self):
        return self.library.name

    class Meta:
        verbose_name_plural = 'Library Images'

class library_videos(models.Model):
    video = models.FileField()
    youtube_url = models.CharField(max_length=250)
    library = models.ForeignKey(library, on_delete=models.CASCADE)

    def __str__(self):
        return self.library.name

    class Meta:
        verbose_name_plural = 'Library Videos'

class bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    libraries = models.ManyToManyField(library)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Bookmarks'

class comaprison(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    libraries = models.ManyToManyField(library)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Comparison of Libraries'




    '''
    
    name, owner_first_name, owner_last_name, addr_line1, addr_line2, area, zipcode, state, email, mobile_no, landline, no_of_seats, opening_time, closing_time, ammenities, library_description, image_1, image_2, image_3, image_4, more_images, payment_methods, verified
    '''

class testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Testimonials'

class enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.IntegerField()
    preferred_joining_date = models.DateField()
    preferred_time_slot = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Enquiries'

class newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Newsletter Subscribers'

class bug_report(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    email = models.EmailField()
    issue = models.TextField()
    image = models.ImageField(blank= True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bug Reports'

class faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'FAQ'

class TermsAndConditions(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Terms And Conditions'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Us Form'