'''
In the HTTP protocol, there are several methods (or verbs) that define the action to be performed for a given resource. The most commonly used HTTP methods are:

GET: Requests data from a specified resource. GET requests should only retrieve data and should have no other effect on the server.

POST: Submits data to be processed to a specified resource. The data is included in the body of the request. POST requests are commonly used for form submissions, file uploads, and other actions that may have side effects on the server.

PUT: Uploads a representation of the specified resource. PUT requests are used to update or replace the entire resource at the specified URL.

DELETE: Deletes the specified resource. DELETE requests are used to remove resources from the server.

HEAD: Similar to the GET method, but retrieves only the headers of the response without the body. HEAD requests are often used to check for the existence of a resource or to retrieve metadata about a resource.

PATCH: Applies partial modifications to a resource. PATCH requests are used to apply changes to part of a resource.

OPTIONS: Returns the HTTP methods that the server supports for a specified URL. OPTIONS requests are often used to determine the capabilities of a server.

TRACE: Echoes the received request back to the client. TRACE requests are used for diagnostic purposes and are typically disabled for security reasons.

CONNECT: Establishes a tunnel to the server identified by the target resource. CONNECT requests are used to establish a secure connection through proxy servers.

These HTTP methods define the actions that can be performed on resources identified by URLs. They form the basis of communication between clients (such as web browsers or mobile apps) and servers on the World Wide Web.
'''
# requests module
'''
# GET Request
import requests
response = requests.get('https://api.example.com/data')
print(response.text)  # Content of the response

# POST Request
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.text)  # Content of the response

# Handling Response
import requests
response = requests.get('https://api.example.com/data')
print(response.status_code)  # HTTP status code
print(response.headers)      # HTTP headers
print(response.text)         # Response content as string
print(response.json())      # Response content parsed as JSON

# Passing Parameters
import requests
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=payload)
print(response.url)  # Final URL with parameters

# Handling errors
import requests
try:
    response = requests.get('https://api.example.com/nonexistent-endpoint')
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
except requests.exceptions.HTTPError as err:
    print(err)

# Setting Headers
import requests
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://api.example.com/data', headers=headers)

# Session Object (for maintaining session state across multiple requests)
import requests 
with requests.Session() as session:
    session.get('https://api.example.com/login', params={'username': 'user', 'password': 'pass'})
    response = session.get('https://api.example.com/protected-resource')
'''

'''
import requests # importing requests nodule

payload = {'firstName':"Linkan", "lastName":"Rout"}

# http/https GET request
response = requests.get("https://httpbin.org/get", params=payload)
print(response.url) # it will give query string url with parameters
print(response.status_code) # it will give the status code of the response

print(response.text) # it will give the content inside the response
print(response.content)

print(response.json()) # convert response to json format
print(response.headers) # gives header part of the response

# http/https POST request

r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

# upload a file

url = "https://httpbin.org/post"
# upload a single file

files = {'file': open('test.txt', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

# upload multiple files

files = [
    ('copy1', ('file1', open('test.txt', 'rb'), 'txt')),
    ('copy2', ('file2', open('test.txt', 'rb'), 'txt'))
]
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
#---------------------------------------
# json formating the response
r = requests.get("https://api.github.com/events")
print(r.json()[0])
# send data as a JSON object in the request body
data = {'firstName':'Linkan'}
r1 = requests.post('https://httpbin.org/post', json=data)
print(r1.text)
#-------------------------------------
headers = {"content-type":"multipart/form-data"}
r = requests.get("https://httpbin.org/get", headers=headers)

print("Headers to the Server: \n",r.request.headers) # it will give header sent to the server
print("Headers from the server: \n",r.headers) # this will give headers from the server
'''