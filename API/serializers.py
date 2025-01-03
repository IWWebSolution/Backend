from rest_framework import serializers
from .models import BaseForm, OurBusiness, Contact

class BaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model= BaseForm
        fields = ['name', 'email', 'phone_No', 'city', 'company_name']
        
class OurBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model= OurBusiness
        fields = ['name', 'email', 'phone_No', 'city', 'company_name', 'message']
        


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields = ['name', 'email', 'subject', 'message']
