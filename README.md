#### Install Django:

``` sudo pip3 install django==1.11 ```

#### Create a project:

``` django-admin startproject ecommerce . ```

### In settings.py:

``` ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')] ```

#### In the terminal:

``` python3 manage.py runserver $IP:$C9_PORT ```

#### Show Home in Favourites, in .bash_aliases - add the following:

``` alias run="python3 ~/workspace/manage.py runserver $IP:C9_PORT" ```