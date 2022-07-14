# Wishlist

[![codecov](https://codecov.io/gh/allanjuliani/wishlist/branch/main/graph/badge.svg?token=OMRJY70MGP)](https://codecov.io/gh/allanjuliani/wishlist)

### 🐋 Install Docker

https://docs.docker.com/engine/install/

https://docs.docker.com/compose/install/

### 🖥️ Install project
```commandline
make install
```

### 🧪 Run tests
```commandline
make tests
```

### 🔍 Show coverage
```commandline
make cov
```

### 👤 Create superuser for admin
This command will create a user based on environment var defined at .env file
```commandline
make createsuperuser
```

### 🔐 Create token to rest api
```commandline
make createtoken username=admin
```

#### 🔗 Admin URL to access on browser
http://localhost/admin/

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
- POST /product/favorite/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
```json
{
    "client": 1,
    "product": 1
}
```

#### Load Favorite Product
- GET /product/favorite/1/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Load Favorites Products
- GET /product/favorite/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

### Pagination
- GET /product/favorite/?page=2
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json

#### Delete Favorite Product
- DELETE /product/favorite/1/
- Authorization: Token `{{AUTHORIZATION_TOKEN}}`
- Content-Type: application/json
