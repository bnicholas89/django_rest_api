# django_rest_api

## DIRENV required, .envrc should be in the root of the directory. / required at the end of each endpoint.

### Enpoints with requirements:

/api-auth/login/ (POST)

  Username
  
  Email
  
  Password

/api-auth/logout/ (POST)

/api-auth/password/change/ (POST)

  old_password
  
  new_password1
  
  new_password2

/api-auth/registration/ (POST)

  Username
  
  Password1
  
  Password2
  
  Email

/api-auth/user/ (PUT, GET, PATCH)

  Username
  
  Password


See more enpoint details at https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
