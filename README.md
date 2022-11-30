# Let's Form a Team

## An Account Type-Based Authorization/Authentication System using DRF (Django Rest Framework)

### Project Setup:

N.B: Using sqlite , the default db provided by django first. This is not standard practice. Keeping a different db as to-do at the moment, it is very simple integrating databases like POSTGREsql or MySql in Django. 

Setting up the project:
```sh
python -m venv env_team
source env_team/bin/activate
git clone https://github.com/thedrowsywinger/lets-form-a-team-ts.git
cd lets-form-a-team-ts
pip install -r requirements.txt
cd team
python manage.py runserver
```

Run the migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

Create a Super User:

```sh
python manage.py createsuperuser
```

## The Project

###### Account Types:

Super Admin: 1
Manager: 2
Employee 3

##### Login:

URL: 127.0.0.1:8000/api/core/token/

Sample POST request

```sh
{
    "username": "superAdmin",
    "password": "super_admin1"
}
```

Sample Response:

```sh
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDMyNDY3OSwiaWF0IjoxNjY5NzE5ODc5LCJqdGkiOiJkM2ZjN2YzYjhiMWI0MDFhYTQ3YjJlMjAwNjczNjM5OSIsInVzZXJfaWQiOiI1NjkyNWM4Ny1hODY0LTRiM2QtYWRlYi00ZmE2YTcyMDg2YTMifQ.xFqgWScUilQCjhG5S6lXYI7lhV0Kd4glQ5GWCLkx0M4",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5NzIwMTc5LCJpYXQiOjE2Njk3MTk4NzksImp0aSI6IjUwNWNlY2MzNjZlODQ1ZmY4MjBhNjFkMjI0NDhmYWVmIiwidXNlcl9pZCI6IjU2OTI1Yzg3LWE4NjQtNGIzZC1hZGViLTRmYTZhNzIwODZhMyJ9.TuQupNSJOpJZE-UtBsPQQtgr5C2h_-xea__f5a2SOgo"
}
```

This access token must be used in requests that require Authorization. The Authorization header must be set like this: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIxIiwiaWF0IjoxNjYyMDQ0NDk0LCJleHAiOjE2NjIxMzA4OTR9.mFKmXAoViHdZ4M2icaI5Vf8s0NI2djehBJyeHFvZlxc"

##### Refresh Token:

URL: http://127.0.0.1:8000/api/core/token/refresh/

Sample POST request
Use the refresh token from the response when you used login api
```sh
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDQxMjkxMSwiaWF0IjoxNjY5ODA4MTExLCJqdGkiOiJjOWExYjU0ZWNkYzg0NTEyYWYzMzM2MDE3OTRhZDAyNSIsInVzZXJfaWQiOiI1NjkyNWM4Ny1hODY0LTRiM2QtYWRlYi00ZmE2YTcyMDg2YTMifQ.S_bPo1KJ6nczZIgi84Tiz3hZm8bYWIraDcmtn4n6HkE"
}
```

Sample Response:

```sh
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5ODA4NDIzLCJpYXQiOjE2Njk4MDgxMTEsImp0aSI6IjQ3NWRmMjA3NDZmNjRlZWE5ZTcyNTczNTA3Mjg4ZWIzIiwidXNlcl9pZCI6IjU2OTI1Yzg3LWE4NjQtNGIzZC1hZGViLTRmYTZhNzIwODZhMyJ9.w0IzRa_xQEqMpxkbOAcab80UxItPRm134bGX5LQer6Q",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDQxMjkyMywiaWF0IjoxNjY5ODA4MTIzLCJqdGkiOiJkMjc1ZjA4NDlmMGI0NTM4OThkMTA0ZmE5NWE1ZDZjNyIsInVzZXJfaWQiOiI1NjkyNWM4Ny1hODY0LTRiM2QtYWRlYi00ZmE2YTcyMDg2YTMifQ.lrHZS2Fm_Amr3FDP_MNGFPqfqKpnLxd6Bx_itEKZ90A"
}
```

##### Register Manager:

A superAdmin can only add a manager.
URL: http://127.0.0.1:8000/api/core/sign-up/

Sample POST request

```sh
{
    "username": "h_maguire",
    "name": "Harry Maguire",
    "email": "h_m@mufc.com",
    "password": "20times",
    "account_type": 3
}
```

##### Get Profile:

Sample URL: http://127.0.0.1:8000/api/profiles/?id=1

Make sure to input the authorization header of the person with permission

Sample Response:

```sh
{
    "message": "Successful",
    "data": {
        "name": "Harry Maguire"
    }
}
```