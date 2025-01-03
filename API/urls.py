from django.urls import path
from .views import index_form, contact_form, ourbusiness_form


urlpatterns = [
    path('baseform/', index_form, name='form-a-data'),
    path('ourbusinessform/', ourbusiness_form, name='form-b-data'),
    path('contactform/', contact_form, name='form-c-data'),
]
