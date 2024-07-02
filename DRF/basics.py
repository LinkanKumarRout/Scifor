# DRF
# it is a micro web framework of python used to create a simple web application


# In python there is a module named json generally used to work with Json
'''
There are two function that we have to remember
- dumps() # this is used to convert python object into json
- loads() # this is used to convert json data to python object

import json
data = {'name':'Linkan','age':26}
json_data = json.dumps(data)
print(json_data)
org_data = json.loads(json_data)
print(org_data)
'''
# Serializers
'''
In Django REST Framework , serializers are responsible for converting complex data such as querysets andmodel instances to native python data types( called as serialization ) that can then be easily rendered into JSON, XML or other content types which can be understood by frontend.

Serializers are also responsible for decentra;ization which means it allows parsed data to be converted back into complex types, after first validating the incoming data.

Serializer Class: is very similar to django form or modelform 
'''
# complex data -----------> python data types ------------> json object
# steps to create a serializer class
'''
- create a separate serializers.py file to write all serializers.

# serializers.py
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)
'''
'''
# Let we have a complex datatype such as 
stu = Student.objects.get(id=id)
serializer = StudentSerializer(stu)
# or a QuerySet
stu = Student.onjects.all()
serializer = StudentSerializer(stu, many = True)
'''
# we have
'''
serializer.data # this gives serialized data
'''
# JSONRenderer
'''
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# converting serialized data into json
json_data  = JSONRenderer().render(seriaizer.data)

# JsonResponse
# it is a subclass of HTTPResponse class
'''
