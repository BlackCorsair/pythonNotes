# How to start coding MongoDB + Python in Ubuntu 17.10
## Installing pip
First we need to install pip so we can start using a virtual environment so we doesn't mess with our system.
* sudo apt install python-pip

## Creating our virtualenv directory
The next step is to create our code directory using virtualenv.
* mkdir mongo-test && cd mongo-test
* virtualenv pymongo
* pymongo/bin/pip install pymongo

## Installing MongoDB
We don't want to mess with our system and then call IT, so we're gonna install docker (https://docs.docker.com/install/linux/docker-ce/ubuntu/) and then we'll run a MongoDB instance listening in port 27017
* sudo docker run --name some-mongo -d mongo
* sudo docker network inspect bridge | grep -i ipv4address _# this will let us know the ip of the container_

## Start coding!!!
Now we create a file inside the folder _mongo-test_ (for example m.py) and start testing mongoDB!!!
```
#!pymongo/bin/python

def get_db():
    from pymongo import MongoClient
    client = MongoClient('172.17.0.2:27017')
    db = client.myFirstMB
    return db


def add_country(db):
    db.countries.insert({"name": "Canada"})


def get_country(db):
    return db.countries.find_one()


if __name__ == "__main__":
    db = get_db()
    add_country(db)
    print get_country(db)

```
The above code have been taken from (http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php)
