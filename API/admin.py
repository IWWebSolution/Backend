from django.contrib import admin

# Register your models here.
from .models import BaseForm, OurBusiness, Contact, Review

@admin.register(BaseForm)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_No', 'city', 'company_name')
    search_fields = ('name', 'email', 'phone_No', 'city', 'company_name')
 
    
@admin.register(OurBusiness)
class OurBusinessAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', 'phone_No', 'city', 'company_name')
    search_fields = ('name', 'email', 'phone_No', 'city', 'company_name')
    
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', 'subject', 'message')
    search_fields = ('name', 'email')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'company_name', 'review', 'rating', 'created_at')
    search_fields= ('name', 'email', 'company_name', 'review')
    