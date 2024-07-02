#1. Explain the concept of path parameters and query parameters in FastAPI.
'''
Path parameters are parameters that are part of the path. For example, in the path /users/{user_id}, user_id is a path parameter.
Query parameters are parameters that are appended to the path with a question mark. For example, in the
path /users?sort=asc, sort is a query parameter.
'''
#2. What are request and response models in FastAPI. How are they defined.
'''
Request models are models that define the structure of the data that is sent to the API. Response models
are models that define the structure of the data that is returned by the API.
Request models are defined using the @app.post() or @app.put() decorators, and response models
are defined using the @app.get() or @app.patch() decorators.
'''
#3. How do you define route operations in FastAPI.
'''
Route operations are defined using the @app.post(), @app.put(), @app.get(), and @app.patch() decorators. For example, to define a route operation that returns a list of users,
you would use the @app.get() decorator and define the route as follows:
@app.get("/users")
def get_users():
    return {"users": [{"name": "John Doe"}, {"name": "Jane Doe"}]}
'''
#4. What is dependancy injection in FastAPI. How it is used.
'''
Dependency injection is a design pattern that allows you to inject dependencies into your code. In FastAPI,
dependency injection is used to inject dependencies into route operations. For example, to inject a database
connection into a route operation, you would use the @app.get() decorator and define the route as
follows:
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return {"users": [{"name": "John Doe"}, {"name": "Jane Doe"}]}
'''
#5. How do you handle request validation in FastAPI.
'''
Request validation is handled using the @app.post() or @app.put() decorators. For example,
to validate the request body of a POST request, you would use the @app.post() decorator and
define the route as follows:
@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user": user}
'''
#6. What is automatic document generation in FastAPI and how do you enable it.
'''
Automatic document generation is a feature of FastAPI that generates documentation for your API automatically.
To enable automatic document generation, you need to install the uvicorn and fastapi packages and
then run the following command:
uvicorn main:app --reload
'''
#7. How do you handle file uploads in FastAPI.
'''
File uploads are handled using the @app.post() decorator and the File and UploadFile classes.
For example, to upload a file, you would use the @app.post() decorator and define the
route as follows:
@app.post("/files")
def upload_file(file: UploadFile = File(...)):
    with open("file.txt", "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename}
'''
#8. Explain the purpose of dependancy injection in FastAPI.
'''
Dependency injection is a design pattern that allows you to inject dependencies into your code. In FastAPI,
dependency injection is used to inject dependencies into route operations. For example, to inject a database
connection into a route operation, you would use the @app.get() decorator and define the route as
follows:
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
return {"users": [{"name": "John Doe"}, {"name": "Jane Doe"}]}
'''
#9. How do you handle CORS (cross origin resource sharing) in FastAPI.
'''
CORS (cross origin resource sharing) is a mechanism that allows you to control which origins can access
your API. In FastAPI, CORS is handled using the @app.middleware() decorator. For example
to allow all origins to access your API, you would use the @app.middleware() decorator and define
the route as follows:
@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
'''
#10. What is the purpose of middleware in FastAPI and how do you use it.
'''
Middleware is a concept in FastAPI that allows you to intercept and modify requests and responses. In Fast
API, middleware is used to add headers, cookies, and other information to requests and responses. For
example, to add a cookie to a request, you would use the @app.middleware() decorator and
define the route as follows:
@app.middleware("http")
async def add_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie("my_cookie", "my_value")
    return response
'''
#11. How do you handle authentication in FastAPI.
'''
Authentication is the process of verifying the identity of a user. In FastAPI, authentication is handled
using the @app.post() decorator and the Depends() function. For example, to authenticate a user
using a username and password, you would use the @app.post() decorator and define the route as
follows:
@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"token": "admin_token"}
    else:
        return {"error": "Invalid username or password"}
'''
#12. Explain the process of testing in FastAPI application.
'''
Testing is an important part of developing a FastAPI application. In FastAPI, testing is handled using
the @app.test_client() decorator and the assert() function. For example, to test a route
operation, you would use the @app.test_client() decorator and define the route as follows:
@app.test_client()
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"users": [{"name": "John Doe"}, {"name": "Jane Doe"}]}
'''
#13. How do you handle error responses in FastAPI.
'''
Error responses are handled using the @app.exception_handler() decorator and the raise() function.
For example, to handle a 404 error, you would use the @app.exception_handler() decorator
and define the route as follows:

@app.exception_handler(NotFound)
def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code,content={"error": "Not Found"}
)
'''
#14. What is the role of pydantic in FastAPI.
'''
Pydantic is a library that is used to validate and serialize data in FastAPI. It is
used to validate the data that is sent to the server and to serialize the data that is sent
from the server. For example, to validate a request body, you would use the @app.post
decorator and define the route as follows:
@app.post("/users")
def create_user(user: User):
    return {"message": "User created successfully"}
'''
#15. How do you deploy a FastAPI application to production.
'''
To deploy a FastAPI application to production, you would use a web server such as Nginx
or Apache. You would then configure the web server to serve the FastAPI application.
For example, to deploy a FastAPI application to a Nginx web server, you would use
the following configuration:
server {
listen 80;
server_name example.com;
location / {
proxy_pass http://localhost:8000;
}
}
'''
