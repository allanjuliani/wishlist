# Wishlist - Dev

#### Ubuntu 20.04 Dependencies
```commandline
sudo apt-get install git build-essential python3-virtualenv libxml2-dev libxslt1-dev libevent-dev python3-dev libsasl2-dev libmysqlclient-dev libjpeg-dev libffi-dev libssl-dev -y
```

#### Create the Virtualenv
```commandline
virtualenv .venv
```

#### Activate Virtualenv
```commandline
source .venv/bin/activate
```

#### Install Python Dependencies

```commandline
pip install -r requirements.txt
```
#### Export env variables
```commandline
export $(cat .env.example | xargs)
```
#### Install Database

```commandline
./manage.py migrate --settings=wishlist.settings_dev
```

#### Create admin user

```commandline
./manage.py createsuperuser --noinput --settings=wishlist.settings_dev
```

#### Create API Token to your user

```commandline
./manage.py drf_create_token admin --settings=wishlist.settings_dev
```

#### Test the application

```commandline
pytest -v apps/ --ds=wishlist.settings_test
```

#### Show coverage

```commandline
pytest -v apps/ --cov=apps/  --ds=wishlist.settings_test
```

#### Running the application

```commandline
./manage.py runserver 0.0.0.0:8000 --settings=wishlist.settings_dev
```

#### Admin URL to access on browser
http://localhost:8000/admin/
