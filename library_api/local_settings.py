DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'library_api_db',
        'USER': 'fizi',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST':{
            'NAME': 'library_api_db'
        }
    }
}

