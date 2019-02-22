import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "dev.myapp",
    "flatpickr"
]

DATABASES = {
}

FLATPICKR_SETTINGS = {
    'theme_name': 'theme_name',
    'options': {
        'locale': 'bn',
    }
}
