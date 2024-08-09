Serializers and Serialization in Django REST Framework :

# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types for easily readable by Front-End. 

# Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

# to complete this process we need to create serializers class where we serialize (convert) data into python datatype and then only complex data means queryset objects (SQLite DB records) convert into native Python datatypes and then easily using python json package using dumps() and loads() method easily data can convert into string and vice-versa 

# Note: What is QuerySet: A QuerySet represents a collection of database query results, typically matching certain criteria. It acts as a high-level, Pythonic representation of the SQL queries that would be executed to retrieve data from the database. Instead of writing raw SQL queries, developers can use QuerySets to perform various database operations such as filtering, sorting, aggregating, and more.


How to create Serializer Class:

step 1) create a seperate serializers.py file in your app where you can write all serializers in this new file.

In that serializers.py file:

from rest_framework import serializers

# as serializers module is in rest_framework package therefore we need to import 

class enquiry_tableSerializer(serializers.Serializer):
    # Rememer serializers.Serializer - S is capital of Serializer
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=10)
    

# Here in this serializers.py file work is done, now using views.py file using function we can access this class and work on serialization concept


Step 2) Now the process of Serialization :

# Means converting queryset data converting into native python datatype and then using json send data on front-end 

# Serialization process done in views.py file under new method for rest api, create new function and write serialization process.

So need to create path() in urls.py file and from where url hit and above student_data() function will execute and other web application or any device can access this data.

In urls.py file :

from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    
    path('student_data', views.student_data.as_view(), name ='student_data'),

]

# So now student_data will be Resource of API or End-Point, using data will be fetch.

and in views.py file, REST Web API function looks like:

Browsable APIView : 

# Showing data thorugh web api but in browsable view for that we need to do some changes in views.py as well urls.py

# in views.py we need to add few modules as:

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import enquiry_tableSerializer

# Now in views.py instead of function we need to create class and in that class, create view as get() and post()

class student_data(APIView):
    def get(self, request, format=None):
        data = enquiry_table.objects.all()
        serializer = enquiry_tableSerializer(data, many=True)
        return Response(serializer.data)

# path('student_data', views.student_data.as_view(), name ='student_data'),
# for browsable apiview data you want to fetch, then in urls.py above path you need to add
# views.student_data.as_view() - calling class as a function












































