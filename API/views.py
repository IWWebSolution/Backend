from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import BaseFormSerializer, OurBusinessSerializer, ContactSerializer,ReviewSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.

@csrf_exempt  # Disable CSRF for development purposes
def index_form(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data
            data = json.loads(request.body)
            print(data)  # Log the data for debugging
            serializer = BaseFormSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
            # Process the data as needed
            #response = {'message': 'Thank You You successfully submitted !', 'data': data}
            response = {'msg':'Thank You, You have successfull submitted !'}
            return JsonResponse(response, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt  # Disable CSRF for development purposes
def contact_form(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data
            data = json.loads(request.body)
            print(data)  # Log the data for debugging
            serializer = ContactSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
            # Process the data as needed
            #response = {'message': 'Thank You You successfully submitted !', 'data': data}
            response = {'msg':'Thank You, You have successfull submitted !'}
            return JsonResponse(response, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt  # Disable CSRF for development purposes
def ourbusiness_form(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data
            data = json.loads(request.body)
            print(data)  # Log the data for debugging
            serializer = OurBusinessSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
            # Process the data as needed
            #response = {'message': 'Thank You You successfully submitted !', 'data': data}
            response = {'msg':'Thank You, You have successfull submitted !'}
            return JsonResponse(response, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def submit_review(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)

            # Initialize the serializer with the incoming data
            serializer = ReviewSerializer(data=data)

            if serializer.is_valid():
                # Save the valid data to the database
                serializer.save()
                return JsonResponse({'message': 'Review submitted successfully!'}, status=201)
            else:
                # Return errors if validation fails
                return JsonResponse({'errors': serializer.errors}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # If the method is not POST, return a method not allowed response
    return JsonResponse({'error': 'Invalid request method. Only POST allowed. MS '}, status=405)

@csrf_exempt
def get_reviews(request):
    if request.method == 'GET':
        try:
            # Retrieve all reviews from the database
            reviews = Review.objects.all().order_by('-created_at')
            serializer = ReviewSerializer(reviews, many=True)

            # Return serialized data as JSON
            return JsonResponse(serializer.data, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # If the method is not GET, return a method not allowed response
    return JsonResponse({'error': 'Invalid request method. Only GET allowed.'}, status=405)
