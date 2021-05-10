# MySQL Maxwell Kafka Python Consumer CDC Flow

This is a PoC I prepared to demonstrate CDC (change data capture).

[Here](https://mert.codes/and-you-could-have-it-all-change-data-capture-with-maxwell-7ec3f0812a7f) is my post about this PoC.

### The Ingredients

- Source database
- Message broker
- Destination (consumer)

### Technologies Used

- MySQL
- Maxwell
- Kafka
- Python

### To Run

Open up a terminal and browse to the cloned folder and execute the following command to see the magic happen:

`docker-compose up`

Or to have everything run at the background silently, add -d

`docker-compose up -d`

Open another terminal to observe the Kafka consumer output:

`docker ps`

Note the container id of the Kafka consumer container (that is spawned using the image `python:3`)

`docker logs <noted-container-id> --follow`

Open an SQL client (like Sequel Pro) and use the following information to connect:
> Host: 127.0.0.1  
Port:13306  
User: root  
Password: root

Add a new database, a new table, insert, delete and update some rows and observe the logs on the Python consumer console (which is the final Kafka consumer, subscribed to the topic called `maxwell`).