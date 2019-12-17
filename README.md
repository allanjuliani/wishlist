# How to install

Is recommended to run the project:

- Ubuntu 18.08 or later
- Python 3.6 or later
- MySQL 5.7 or 8.0 or SQLite 3.24 or later

## Dependencies

`sudo apt-get install git python-virtualenv memcached gettext libmysqlclient-dev -y`

### Create the Virtualenv
`cd ~/ && virtualenv wishlist --python=/usr/bin/python3 && mkdir wishlist/src && cd wishlist/src`

### Activate Virtualenv
`source ~/wishlist/bin/activate`

### Clone the Project
`git clone https://github.com/allanjuliani/wishlist.git`

### Install Python Dependencies

`pip install -r requirements.txt`

### Install Database

Default is set SQLite. If you want to use MySQL, created the database:

`CREATE DATABASE wishlist CHARACTER SET utf8 COLLATE utf8_general_ci;`

Comment lines 83 to 86 and uncomment the line 88 to 97 on settings.py. Fill the default settings with your database.  

`./manage.py migrate`

### Create admin user

`./manage.py createsuperuser`

### Create API Token to your user

`./manage.py drf_create_token [your user]`

### Start Project 

`./manage.py runserver 0.0.0.0:8000` 


### Test application

If you are running on localhost

#### Add Client
##### POST http://localhost:8000/api/client/
`
POST http://localhost:8000/api/client/
Authorization Token [token generated]
Content-Type application/json
{
    "name": "Allan Juliani",
    "email": "allan.s.juliani3@gmail.com"
}`

#### Edit Client
`
PUT http://192.168.0.100:8000/api/product/
Accept: application/json, text/javascript
// Authorization key=123
// Content-Type application/json
{
    "user": {
        "first_name": "Allan",
        "last_name": "Juliani",
        "email": "allan.s.juliani3@gmail.com"
    },
    "product": {
        "title": "Generic Product 2",
        "brand": "Generic Brand",
        "price": 9.99,
        "review_score": 5
    }
}