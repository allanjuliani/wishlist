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

#### Ubuntu 20.04 Dependencies
```commandline
sudo apt-get install git python3-virtualenv libxml2-dev libxslt1-dev libevent-dev python3-dev libsasl2-dev libmysqlclient-dev libjpeg-dev libffi-dev libssl-dev -y
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
pytest apps/
```

#### Show coverage

```commandline
pytest apps/ --cov=apps/
```

#### Running the application

```commandline
./manage.py runserver 0.0.0.0:8000 --settings=wishlist.settings_dev
```

#### Admin URL to access on browser
http://localhost:8000/admin/

## REST API endpoints

#### Add Client
- POST /client/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "name": "Client Name",
    "email": "clientemail@example.com"
}
```

#### Load Client
- GET /client/`{{client_id}}`/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Load Clients
- GET /client/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Update Client
- PUT /client/`{{client_id}}`/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "name": "The New Name",
    "email": "new_email@example.com"
}
```

#### Delete Client
- DELETE /client/`{{client_id}}`/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Add Product
- POST /product/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "title": "Product Name",
    "brand": "Brand New",
    "image": "https://dummyimage.com/300",
    "price": 99.99,
    "review_score": 5
}

```

#### Load Product
- GET /product/`{{product_id}}`/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Load Products
- GET /product/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Update Product
- PUT /product/`{{product_id}}`/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "title": "Product New Name",
    "brand": "Brand New",
    "image": "https://dummyimage.com/300",
    "price": 199.99,
    "review_score": 5
}
```

#### Delete Product
- DELETE /product/`{{product_id}}`/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Add Favorite Product
- POST /client/product/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "client_id": 1,
    "product_id": 1
}
```

#### Load Favorites Product
- GET /client/`{{client_id}}`/products/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

If there is more than 3 products, is generated a pagination URL in the response:
- GET /client/`{{client_id}}`/products/?page=2
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json


#### Delete Favorite Product
- DELETE /client/product/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "client_id": 1,
    "product_id": 1
}
```
