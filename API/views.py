from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BaseFormSerializer, OurBusinessSerializer, ContactSerializer
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

