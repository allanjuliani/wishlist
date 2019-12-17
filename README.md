## How to install

Is recommended to run the project:

- Ubuntu 18.08 or later
- Python 3.6 or later
- MySQL 5.6 or later or SQLite 3.24 or later

#### Ubuntu Dependencies

`sudo apt-get install git python-virtualenv memcached libxml2-dev libxslt1-dev libevent-dev python-dev python3-dev libsasl2-dev libmysqlclient-dev libjpeg-dev libffi-dev libssl-dev -y`

#### Create the Virtualenv
`cd ~/ && virtualenv wishlist --python=/usr/bin/python3 && mkdir wishlist/src && cd wishlist/src`

#### Clone the Project
`git clone https://github.com/allanjuliani/wishlist.git`

#### Activate Virtualenv
`source ~/wishlist/bin/activate`

#### Install Python Dependencies

`cd ~/wishlist/src/wishlist && pip install -r requirements.txt`

#### Install Database

Default is set SQLite. If you want to use MySQL, created the database:

`CREATE DATABASE wishlist CHARACTER SET utf8 COLLATE utf8_general_ci;`

Comment the lines 83 to 86 and uncomment the lines 88 to 97 on settings.py. Fill the default settings with your database configurations.  

`./manage.py migrate`

#### Create admin user

`./manage.py createsuperuser`

#### Create API Token to your user

`./manage.py drf_create_token [your user]`

#### Test application

`./manage.py test`

#### Running application

`./manage.py runserver 0.0.0.0:8000` 

or, start in english

`make start_en`

start in portuguese

`make start_br`

##### The admin URL to access on browser
`http://localhost:8000/admin/`

## The REST API

##### Add Client
```
POST /api/client/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "name": "Your Name",
    "email": "your_email@example.com"
}
```

##### Load Client
```
GET /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

##### Edit Client
```
PUT /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "name": "The New Name",
    "email": "new_email@example.com"
}

```

##### Delete Client
```
DELETE /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

##### Add Product
```
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
##### Load Product

```
GET /api/product/[product_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

##### Edit Product
```
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

##### Delete Product
```
DELETE /api/product/[product_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```


##### Add Favorite Product
```
POST /api/client/product/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "client_id": [client_id],
    "product_id": [product_id]
}
```

##### Load Favorites Product
```
GET /api/client/[client_id]/products/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

##### Delete Client
```
DELETE /api/client/product/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "client_id": [client_id],
    "product_id": [product_id]
}
```