# Django Wishlist

## Using Docker

### Install Docker

https://docs.docker.com/engine/install/

https://docs.docker.com/compose/install/

### Install project
```commandline
make install
```

### Run tests
```commandline
make tests
```

### Show coverage
```commandline
make cov
```

### Create superuser for admin
This command will create a user based on environment var defined at .env file
```commandline
make createsuperuser
```

### Create token to rest api
```commandline
make createtoken username=admin
```

#### Admin URL to access on browser
http://localhost/admin/

### Without Docker

#### Ubuntu Dependencies
```commandline
sudo apt-get install git python-virtualenv memcached libxml2-dev libxslt1-dev libevent-dev python-dev python3-dev libsasl2-dev libmysqlclient-dev libjpeg-dev libffi-dev libssl-dev -y
```

#### Create the Virtualenv
```commandline
virtualenv venv
```

#### Activate Virtualenv
```commandline
source venv/bin/activate
```

#### Install Python Dependencies

```commandline
pip install -r requirements.txt
```

#### Install Database

```commandline
./manage.py migrate --settings=wishlist.settings_dev
```

#### Create admin user

```commandline
./manage.py createsuperuser --settings=wishlist.settings_dev
```

#### Create API Token to your user

```commandline
./manage.py drf_create_token {{YOUR_USER}} --settings=wishlist.settings_dev
```

#### Test the application

```commandline
./manage.py test --settings=wishlist.settings_dev
```

#### Running the application

```commandline
./manage.py runserver 0.0.0.0:8000 --settings=wishlist.settings_dev
```

#### Admin URL to access on browser
http://localhost:8000/admin/

## The REST API

#### Add Client
- POST /client/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json
```json
{
    "name": "Client Name",
    "email": "clientemail@example.com"
}
```

#### Load Client
- GET /client/{{client_id}}/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json

#### Edit Client
- PUT /client/{{client_id}}/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json
```json
{
    "name": "The New Name",
    "email": "new_email@example.com"
}
```

#### Delete Client
- DELETE /client/{{client_id}}/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json

#### Add Product
- POST /product/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json
```json
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 188.89,
    "review_score": 5
}

```
#### Load Product
- GET /product/{{product_id}}/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json

#### Edit Product
- PUT /product/{{product_id}}/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json
```json
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 159.99,
    "review_score": 4
}
```

#### Delete Product
- DELETE /product/{{product_id}}/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json

#### Add Favorite Product
- POST /client/product/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json
```json
{
    "client_id": 1,
    "product_id": 1
}
```

#### Load Favorites Product
- GET /client/{{client_id}}/products/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json

If there is more than 3 products, is generated a pagination URL in the response:
- GET /client/{{client_id}}/products/?page=2
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json


#### Delete Favorite Product
- DELETE /client/product/
- Authorization: Token {{AUTHORIZATION_TOKEN}}
- Content-Type: application/json
```json
{
    "client_id": 1,
    "product_id": 1
}
```
