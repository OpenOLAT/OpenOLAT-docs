# Install OpenOlat with MySQL

This installation guide is an extension to the general [Installation Guide](installGuide.md). Replace the database relevant parts with the MySQL counterparts you will find here. 

_We strongly advice to use Postgres and not MySQL. Postgres will have better performance and stability and it way more tested. We support MySQL because of historic reasons, support might not be guaranteed in the long term._

## Set up mysql
If you have any choice, use MySQL 5.6. If you can't, use 5.5. Do not use 5.1, there are many issues with 5.1. 

### User and DB
Do the following as mysql root user (you may need the mysql root password):

	mysql -u root -p

and do this:

	create database oodb character set utf8 collate utf8_unicode_ci;
	create user oodbu@localhost identified by 'oodbpasswd';
	grant all on oodb.* to oodbu@localhost;

### Test DB access

Test the mysql account as openolat user

	mysql oodb -u oodbu -poodbpasswd

You should get the mysql cli prompt. 

	Exit

### Create DB schema

Create the OpenOLAT database schema

	cd /home/openolat/webapp/WEB-INF/classes/database/mysql/
	mysql oodb -u oodbu -poodbpasswd < setupDatabase.sql

	
### Optionally	

Create a file named `.my.cnf` containing

	[client]
	database=oodb
	user=oodbu
	password=oodbpasswd

then you can access the database by just typing `mysql`.
