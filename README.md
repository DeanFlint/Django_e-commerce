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

#### Install Stripe:

``` sudo pip3 install stripe ```

#### In settings, add the following:

``` 
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')
```

#### Now create a new file called env.py which will contain our keys:

``` 
import os

os.envrion.setdefault("STRIPE_PUBLISHABLE", "paste key here")
os.envrion.setdefault("STRIPE_SECRET", "paste key here")
```

#### Add env to your settings.py:

```
import env
```

### Getting an AWS Account:

On amazon.com, login (or create an account).

aws.amazon.com

Sign in to console.

Create new account.

Fill in the details on the personal account form.

Choose the plan, and launch.

Find S3 and create bucket.

Click next and on Set Permissions, "Grant public read access to this bucket" on the dropdown then finish.

Click on Static Website hosting and enter index.html and error.html (we don't actually need these at the moment).


Click on permissions and select Bucket Policy.

```
{
    "Version":"2012-10-17",
    "Statement":[{
      "Sid":"PublicReadGetObject",
        "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":[" enter bucket arn ---> arn:aws:s3:::example-bucket/*<--- "]
    }
  ]
}
```

Save then go onto the main page of AWS. 

Search for IAM.

Create group, and click next on the options.

Create policy and import S3. Give it a name and edit the json to:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "--> bucket name <--",
                "--> bucket name but with /* at the end <--*"
            ]
        }
    ]
}
```

After this, you can then search for this policy.

Click on policy actions and attach to the group you created earlier.

Now we can add a user - like admin or shopkeeper.

Give it the group permissions and download the csv file which contains the keys.


#### Connecting Django to S3

Install the following:

``` sudo pip3 install django-storages ```

``` sudo pip3 install boto3 ```

Update INSTALLED_APPS:

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
    'products',
    'cart',
    'checkout',
    'storages',
]
```

```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = 'dean-django-project'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

In env.py, add the aws keys:

```
os.environ.setdefault("AWS_ACCESS_KEY_ID", "ADD KEY HERE")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY_ID", "ADD SECRET KEY HERE")
```

In the terminal:

```
python3 manage.py collectstatic
```

#### Store Media on S3

Create a new file called custom_storqges

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
```

In settings.py:

```
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
```

Now in the terminal:

```
python3 manage.py collectstatic
```

Now delete all folders in the S3 bucket apart from static.

In bucket permissions, add the following line under GET:

```
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
```

Set up travis.ci.

Create a new file called .travis.yml

```
language: python
python:
- "3.4"
install: "pip install -r requirements.txt"
script:
- SECRET_KEY="whatever" .manage.py test
```

[![Build Status](https://travis-ci.org/DeanFlint/Django_e-commerce.svg?branch=master)](https://travis-ci.org/DeanFlint/Django_e-commerce)