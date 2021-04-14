## How to install

### Install Docker

https://docs.docker.com/engine/install/

### Build project

```commandline
make build 
```

### Start project

```commandline
make up
```

### Create superuser for admin

```commandline
make createsuperuser
```

### Run tests

```commandline
make tests
```

#### Links
http://localhost:8000/admin/

http://localhost:8000/

#### Remove 
```commandline
make remove
make clean
```

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
./manage.py migrate
```

#### Create admin user

```commandline
./manage.py createsuperuser
```

#### Create API Token to your user

```commandline
./manage.py drf_create_token [your user]
```

#### Test the application

```commandline
./manage.py test
```

#### Running the application

```commandline
./manage.py runserver 0.0.0.0:8000 --settings=wishlist.settings_dev
```

#### Admin URL to access on browser
```
http://localhost:8000/admin/
```

## The REST API

#### Add Client
```json
POST /api/client/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "name": "Your Name",
    "email": "your_email@example.com"
}
```

#### Load Client
```json
GET /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

#### Edit Client
```json
PUT /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "name": "The New Name",
    "email": "new_email@example.com"
}

```

#### Delete Client
```json
DELETE /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

#### Add Product
```json
POST /api/product/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 188.89,
    "review_score": 5
}

```
#### Load Product

```json
GET /api/product/[product_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

#### Edit Product
```json
PUT /api/product/[product_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 159.99,
    "review_score": 4
}
```

#### Delete Product
```json
DELETE /api/product/[product_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```


#### Add Favorite Product
```json
POST /api/client/product/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "client_id": [client_id],
    "product_id": [product_id]
}
```

#### Load Favorites Product
```json
GET /api/client/[client_id]/products/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

If there is more than 3 products, is generated a pagination URL in the response:
```json
GET /api/client/[client_id]/products/?page=2
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

#### Delete Favorite Product
```json
DELETE /api/client/product/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "client_id": [client_id],
    "product_id": [product_id]
}
```
