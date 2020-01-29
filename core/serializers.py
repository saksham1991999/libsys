from django.contrib.auth.models import User, Group
from rest_framework import serializers

from . import models


class PaymentMethodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.payment_methods
        fields = ['id', 'title']


class AmmenitiesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.ammenities
        fields = ['id','title', 'quantity']

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    ammenities = serializers.HyperlinkedIdentityField(view_name="core:ammenities-detail")
    payment_methods = serializers.HyperlinkedIdentityField(view_name="core:payment_methods-detail")
    class Meta:
        model = models.library
        fields = ['id', 'name', 'owner_first_name', 'owner_last_name', 'addr_line1', 'addr_line2', 'area', 'zipcode', 'state', 'email', 'mobile_no', 'landline', 'no_of_seats', 'opening_time', 'closing_time', 'ammenities', 'library_description', 'image_1', 'image_2', 'image_3', 'image_4', 'payment_methods', 'verified']
        depth = 2

