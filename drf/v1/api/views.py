from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

# Model Instance
def model_instance(request, pk):
    # Get Student Object from Student Model
    # student = StudentModel.objects.get(id=1)
    student = StudentModel.objects.get(id=pk)
    
    # Serialize Student Object
    serializer = StudentSerializer(student)
    
    # Render JSON
    json_data = JSONRenderer().render(serializer.data)
    
    # Send Response to Client
    return HttpResponse(json_data, content_type='application/json')

# Query Set
def query_set(request):
    # Get All Student Objects from Student Model
    students = StudentModel.objects.all()
    
    # Serialize Students Query Set
    serializer = StudentSerializer(students, many=True)
    
    # Render JSON
    json_data = JSONRenderer().render(serializer.data)
    
    # Send Response to Client
    return HttpResponse(json_data, content_type="application/json")
