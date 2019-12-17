## How to install

Is recommended to run the project:

- Ubuntu 18.08 or later
- Python 3.6 or later
- MySQL 5.7 or 8.0 or SQLite 3.24 or later

### Dependencies

`sudo apt-get install git python-virtualenv memcached gettext libmysqlclient-dev -y`

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

Comment lines 83 to 86 and uncomment the line 88 to 97 on settings.py. Fill the default settings with your database.  

`./manage.py migrate`

#### Create admin user

`./manage.py createsuperuser`

#### Create API Token to your user

`./manage.py drf_create_token [your user]`

#### Start Project 

`./manage.py runserver 0.0.0.0:8000` 


#### Test application

If you are running on localhost

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

#### Edit Client
```
PUT /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

{
    "name": "The New Name",
    "email": "new_email@example.com"
}

```

#### Load Client
```
GET /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json
```

#### Delete Client
```
PUT /api/client/[client_id]/
Authorization: Token [TOKEN_GENERATED]
Content-Type: application/json

```

##### Add Product
```
POST /api/product/
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 188.89,
    "review_score": 5
}

```
##### Add Client
```
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 188.89,
    "review_score": 1
}

```
##### Add Client
```
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 188.89,
    "review_score": 1
}

```
##### Add Client
```
{
    "title": "Carregador Sony com 8 Pilhas Kit 4 AA + 4 AAA Recarregável",
    "brand": "Sony",
    "image": "https://a-static.mlcdn.com.br/618x463/carregador-sony-com-8-pilhas-kit-4-aa-4-aaa-recarregavel/vitrinedosimportados/26386/e402cd8f4e0e0a24ed2f43d0896370fd.jpg",
    "price": 188.89,
    "review_score": 1
}

```