#### Install Django:

``` sudo pip3 install django==1.11 ```

#### Create a project:

``` django-admin startproject ecommerce . ```

### In settings.py:

``` ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')] ```

#### In the terminal:

``` python3 manage.py runserver $IP:$C9_PORT ```

#### Show Home in Favourites, in .bash_aliases - add the following:

``` alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT" ```

#### Create a .gitignore file and add the following:

``` *.sqlite3 ```

#### Transfer the files from the accounts app created previously and update the settings.py:

```
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
```

```
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CaseInsensitiveAuth']
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]
```

#### Run the following to check any changed:

``` python3 manage.py makemigrations accounts ```

``` python3 manage.py makemigrations accounts ```

``` python3 manage.py migrate ```

#### On ecommerce > urls.py, add the following:

``` 
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
]

```

#### Install bootstrap forms:

``` 
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
]
```

#### Create a superuser:

``` python3 manage.py createsuperuser ```

#### In settings.py:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'accounts',
]
```

#### We have mulitple templates folders so we need to specify that we want to use any of them:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        """ In the DIRS section """
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### Create a new app called 'home'

``` python3 manage.py startapp home ```

#### Since we are allowing image uploads, we need to install Pillow:

``` sudo pip3 install Pillow ```

#### After creating models in the products app (or any models created in others),

We need to migrate these changes into our db:

``` python3 manage.py makemigrations <appname> ```

``` python3 manage.py migrate <appname> ```

#### To run any tests we write for any of the apps:

``` python3 manage.py test <appname> ```

#### Create a new app called cart:

``` python3 manage.py startapp cart ```

