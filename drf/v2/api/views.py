from django.shortcuts import render
from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer

# Create your views here.
def create(request):
    if request.method == 'POST':
        # Get the Raw JSON Data from Request Body
        json_data = request.body
        
        # Convert Raw Json Data into Stream of Bytes
        stream = BytesIO(json_data)
        
        # Parse Byte Stream into Python Dict
        data = JSONParser().parser(stream)
        
        # Initialize Serializer with Parsed Data
        serializer = StudentSerializer(data)
        
        # Check if Data is Valid
        if serializer.is_valid():
            # Save New Student to Database
            serializer.save()
            
            # Create a Success Response
            response = {'message': 'created'}
            
            # Render Response Data as JSON Data
            json_data = JSONRenderer().render(response)

            # Return the Response with JSON Content
            return HttpResponse(json_data, content="application/json")
    
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
        return Response({'message': 'student created'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        