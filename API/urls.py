from django.urls import path
from .views import index_form, contact_form, ourbusiness_form, submit_review, get_reviews


urlpatterns = [
    path('baseform/', index_form, name='form-a-data'),
    path('ourbusinessform/', ourbusiness_form, name='form-b-data'),
    path('contactform/', contact_form, name='form-c-data'),
    path('submit-review', submit_review, name='submit-review'),
    path('get-reviews', get_reviews, name='get-reviews')
]
