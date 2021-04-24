# JobBoard-Fastapi
A job board app using fastapi

![](backend/static/images/lite.gif)

## Technology Stack:
* FastAPI
* Uvicorn (server)
* Pytest
* Sqlalchemy
* Postgres


## How to start the app ?
```
git clone https://github.com/nofoobar/JobBoard-Fastapi.git
cd .\JobBoard-Fastapi\
python -m venv env   #create a virtual environment
.\env\Scripts\activate  #activate your virtual environment
cd .\backend\
pip install -r .\requirements.txt
uvicorn main:app --reload     #start server
visit  127.0.0.1:8000/
```

Features:
 - ✔️ Course [FastAPI Course](https://www.fastapitutorial.com/blog/fastapi-course/)
 - ✔️ Serving Template
 - ✔️ Static Files in Development
 - ✔️ Connecting to Database
 - ✔️ Schemas
 - ✔️ Dependency Injection
 - ✔️ Password Hashing
 - ✔️ Unit Testing (What makes an app stable)
 - ✔️ Authentication login/create user/get token
 - ✔️ Authorization/Permissions 
 - ✔️ Webapp (Monolithic)
 - 🚧 Load Testing using Locust
 - 🚧 Fully Asyc
 - 🚧 Migration by alembic
 - 🚧 Caching
 - 🚧 Dockerization
 - 🚧 Creating a frontend using Vue/React
 - 🚧 Getting ready for Production e.g. load balancing,NGINX,HTTPS 
 - 🚧 Deployment
 - 🚧 CI and CD
