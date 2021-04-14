
 sudo groupadd docker
## list
`docker ps`

## remove all
`docker rmi $(docker images -q)`

## stop all
`docker stop $(docker ps -a -q)`

## delete all
`docker rm $(docker ps -a -q)`


`docker pull mysql`

`docker images`

`docker run --name db-mysql -e MYSQL_ROOT_PASSWORD=1234 -d mysql:latest`

## Show IP
`docker inspect test-mysql`

`mysql -h 172.17.0.2 -u root -p`

`docker login`

`docker tag  a347a5928046 allanjuliani/mysql:first`

`docker push allanjuliani/mysql:first`


## get
`docker pull allanjuliani/mysql:first`

`docker run --name db-mysql -e MYSQL_ROOT_PASSWORD=1234 -d allanjuliani/mysql:first`