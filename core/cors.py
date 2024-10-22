# settings/cors.py




CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'X-Requested-With',
    'x-csrftoken',
    'accept',
    'origin',
]
CORS_PREFLIGHT_MAX_AGE = 86400
