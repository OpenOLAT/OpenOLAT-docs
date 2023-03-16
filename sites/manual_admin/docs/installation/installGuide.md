## Installation guide for OpenOlat 15.3 and greater

This guide walks you through installing OpenOlat Version 15.3.x or newer on a local GNU/Linux or similar system using _Tomcat 9_, _Java 11_ and _PostgreSQL 12_. If you already have an up and running installation, see our [Update Guide](updateGuide.md)

_If you really want to install OpenOlat using MySQL as database, have a look at the [Special topics -> MySQL DB section](mysql.md) and try mixing it with the informations found in here. Please keep in mind that this is not recommended._

## Create a user for OpenOlat

The username is `openolat` in this guide with home directory in `/home/openolat/`. From here onwards do everything as the user `openolat` (unless pointed out differently). To create the user, you can simply use the command

	useradd -m -s /bin/bash openolat

## Download software

We recommend using the following software packages:

- Java-WM: AdoptOpenJDK 11 LTS  
  [https://adoptopenjdk.net/](https://adoptopenjdk.net/)
- Application server: Tomcat 9   
  [https://tomcat.apache.org/](https://tomcat.apache.org/)
- OpenOlat application code: as pre-compiled .war files   
  [https://www.openolat.com/releases/](https://www.openolat.com/releases/)
  
Create a directory downloads and keep the downloaded files there:

	openolat~$ cd && mkdir downloads && cd downloads
	openolat~$ ls -l downloads
	-rw-rw-r-- 1 openolat openolat  11437266 Dez  8 14:44 apache-tomcat-9.0.40.tar.gz
	-rw-rw-r-- 1 openolat openolat 194723798 Dez  8 14:44 OpenJDK11U-jdk_x64_linux_hotspot_11.0.9.1_1.tar.gz
	-rw-rw-r-- 1 openolat openolat 146225737 Dez  8 14:44 openolat_1535.war


You do not need to use the exact versions from this manual, this is just
an example. We recommend that you use the newest version within the
given major version: Java 11, Tomcat 9. As for OpenOlat, take the newest
release please. If not, make sure to use a version 15.3.x or newer. Note
that you do not need a JDK to run OpenOlat, a JRE will work as well.


## Prepare home directory

### Link code

In the home directory:

	openolat~$ cd
	openolat~$ tar xvf downloads/apache-tomcat-9.0.40.tar.gz
	openolat~$ ln -s apache-tomcat-9.0.40 tomcat
	 
	openolat~$ tar xvf downloads/OpenJDK11U-jdk_x64_linux_hotspot_11.0.9.1_1.tar.gz
	openolat~$ ln -s jdk-11.0.9.1+1 jre
 	
	openolat~$ unzip -d openolat-15.3.5 downloads/openolat_1535.war
	openolat~$ ln -s openolat-15.3.5 webapp
	
Note that this setup allows you to switch between different versions of JRE and tomcat by adjusting the symlinks jre and tomcat. An update works the same way, just stop OpenOlat, remove the symlink to webapp, unzip a new version and make a new symbolic webapp link.

### Create tomcat dirs

Set up tomcat in home directory

	openolat~$ mkdir bin conf lib run logs

### web.xml and catalina.sh

Link the following files:

	openolat~$ cd ~/conf
	openolat~$ ln -s ../tomcat/conf/web.xml web.xml
	openolat~$ cd ~/bin
	openolat~$ ln -s ../tomcat/bin/catalina.sh catalina.sh

Create additional, handy links:

	openolat~$ cd
	openolat~$ ln -s tomcat/bin/startup.sh start
	openolat~$ ln -s tomcat/bin/shutdown.sh stop

### setenv.sh

Create the file `~/bin/setenv.sh` containing

	CATALINA_HOME=~/tomcat
	CATALINA_BASE=~
	JRE_HOME=~/jre
	CATALINA_PID=~/run/openolat.pid
	CATALINA_TMPDIR=/tmp/openolat
	mkdir -p $CATALINA_TMPDIR
	
	CATALINA_OPTS=" \
	-Xmx1024m -Xms512m -XX:MaxMetaspaceSize=512m \
	-Duser.name=openolat \
	-Duser.timezone=Europe/Zurich \
	-Dspring.profiles.active=myprofile \
	-Djava.awt.headless=true \
	-Djava.net.preferIPv4Stack=true \
	-XX:+HeapDumpOnOutOfMemoryError \
	-XX:HeapDumpPath=. \
	"
	
The scripts of tomcat will parse this file at startup.


### server.xml

Create the file `~/conf/server.xml`

	<?xml version='1.0' encoding='utf-8'?>
	<Server port="8085" shutdown="SHUTDOWN">
	  <Service name="Catalina">
	    <Connector port="8088" protocol="HTTP/1.1" />
	    <Engine name="Catalina" defaultHost="localhost">
	      <Host name="localhost"  appBase="webapps" />
	    </Engine>
	  </Service>
	</Server>

Make sure the chosen ports (8085 and 8088 in this example) are available.
Set the environment variables `CATALINA_HOME` and `JRE_HOME`, for example by appending the following to your `~/.bashrc`

	export CATALINA_BASE=~
	export CATALINA_HOME=~/tomcat
	export JRE_HOME=~/jre

and activate them by issuing

	openolat~$ . .bashrc

## Test tomcat

	openolat~$ ./start
	
... should output something like this:

	Using CATALINA_BASE:   /home/openolat
	Using CATALINA_HOME:   /home/openolat/tomcat
	Using CATALINA_TMPDIR: /tmp/openolat
	Using JRE_HOME:        /home/openolat/jre
	Using CLASSPATH:       /home/openolat/tomcat/bin/bootstrap.jar:/home/openolat/	tomcat/bin/tomcat-juli.jar
	Using CATALINA_OPTS:   -Xmx1024m -Xms512m -XX:MaxMetaspaceSize=512m 	-Duser.name=openolat -Duser.timezone=Europe/Zurich  	-Dspring.profiles.active=myprofile -Djava.awt.headless=true 	-Djava.net.preferIPv4Stack=true -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=.
	Using CATALINA_PID:    /home/openolat/run/openolat.pid
	Existing PID file found during start.
	Removing/clearing stale PID file.
	Tomcat started.

Check whether these values make sense, then stop tomcat again

	openolat~$ ./stop

## Set up postgresql

This setupguide should work with all PostgreSQL Versions from 9.1 on. Our recommendation is to use the most recent, stable version. This manual has been tested with version 12.5.

### User and DB

Do the following as root user:

	root~# su - postgres

and then as user postgres (you may need the postgresql db password, but usually not):

	postgres~$ psql

Now while logged in to postgresql, we create the user and the database:

	postgres=# create user oodbu with password 'oodbpasswd';
	postgres=# create database oodb with owner oodbu;

### Test DB access

Test the account as `openolat` user:

	openolat~$ psql oodb -U oodbu -h localhost

You should get the postgresql client prompt after providing your password. 

### Create DB schema

The database schema is created automatically when starting OpenOlat the first time. If you want to have 
more control over the process you can setup it yourself: 

Create the `openolat` database schema, as user `openolat`:

	oodb=> \i /home/openolat/webapp/WEB-INF/classes/database/postgresql/setupDatabase.sql

!!! note
	As of 17.2.2 the database files are not in the compiled war file anymore as all files in the classes directory are delivered in a jar. 
	You can unpack the `openolat/WEB-INF/lib/openolat-lms-xx.x-SNAPSHOT` file to find the files or download it from GitHub. 

### Optionally 

Create a file named `~/.pgpass` containing

	#hostname:port:database:username:password
	localhost:5432:oodb:oodbu:oodbpasswd

This way you can access the database by typing `psql -h localhost` and will connect to the right db without pw

## OpenOlat configuration

Create the file `~/lib/olat.local.properties`

	db.source=jndi
	db.jndi=java:comp/env/jdbc/openolatDS
	db.vendor=postgresql
	installation.dir=/home/openolat
	log.dir=/home/openolat/logs
	server.contextpath=/openolat
	server.domainname=localhost
	server.port=8088
	server.port.ssl=0
	smtp.host=disabled
	tomcat.id=1
	userdata.dir=/home/openolat/olatdata

## Application context descriptor
	
Create the directory `~/conf/Catalina/localhost/` for the OpenOlat Application context descriptor:

	openolat~$ mkdir -p ~/conf/Catalina/localhost/

and create the file `~/conf/Catalina/localhost/ROOT.xml` containing:

	<?xml version="1.0" encoding="UTF-8" ?>
	<Context path="" docBase="/home/openolat/webapp" debug="0" reloadable="false" allowLinking="true">
	 	 <Resource name="jdbc/openolatDS" auth="Container" type="javax.sql.DataSource"
		     maxTotal="16" maxIdle="4" maxWaitMillis="60000"
		     username="oodbu" password="oodbpasswd"
		     driverClassName="org.postgresql.Driver"
		     validationQuery="SELECT 1" 
		     validationQueryTimeout="-1" 
		     testOnBorrow="true" 
		     testOnReturn="false"
		     url="jdbc:postgresql://localhost:5432/oodb"/>
	</Context>

Make sure the values of username, password and the `localhost:5432/oodb` part in the url value are the ones of your postgresql account for `openolat`.

## Configure log4j2

Create the file `~/lib/log4j2.xml` containing

	<?xml version="1.0" encoding="UTF-8"?>
	<Configuration status="WARN">
	   <Appenders>
	       <RollingFile name="RollingFile" fileName="/home/openolat/logs/olat.log"
	           filePattern="/home/openolat/logs/olat.log.%d{yyyy-MM-dd}">
	           <PatternLayout
	                   pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %marker %c{1} ^%%^ I%X{ref}-J%sn ^%%^ %logger{36} ^%%^ %X{identityKey} ^%%^ %X{ip} ^%%^ %X{referer} ^%%^ %X{userAgent} ^%%^ %msg%ex{full,separator( )}%n" />
	           <Policies>
	               <TimeBasedTriggeringPolicy interval="1" />
	           </Policies>
	       </RollingFile>
	   </Appenders>
	   <Loggers>
	       <Logger name="org.apache.commons.httpclient" additivity="false" level="warn">
	           <AppenderRef ref="RollingFile" />
	       </Logger>
	       <Logger name="org.apache.pdfbox" additivity="false" level="fatal">
	           <AppenderRef ref="RollingFile" />
	       </Logger>
	       <Logger name="org.apache.fontbox" additivity="false" level="fatal">
	           <AppenderRef ref="RollingFile" />
	       </Logger>
	       <Logger name="org.hibernate.engine.internal.StatisticalLoggingSessionEventListener" additivity="false" level="fatal">
	           <AppenderRef ref="RollingFile" />
	       </Logger>
	       <!-- Change the level to debug to see the SQL statements generated by Hibernate -->
	       <Logger name="org.hibernate.SQL" additivity="false" level="fatal">
	           <AppenderRef ref="RollingFile" />
	       </Logger>
	       <Logger name="org.hibernate.type.descriptor.sql.BasicBinder" additivity="false" level="fatal">
	           <AppenderRef ref="RollingFile" />
	       </Logger>
	       <Root level="info">
	           <AppenderRef ref="RollingFile" />
	       </Root>
	   </Loggers>
	</Configuration>
	
	
## Done

### Start OpenOlat

	./start

The file `~/log/catalina.out` should say

	INFO: Server startup in [19696] milliseconds

near the end (your numbers will vary). 

The next file to check would be `~/logs/olat.log`. It should say:

	Velocity cache filled with 1517 templates in (ms): 5847

but again, your numbers will vary.

### Try OpenOlat

Point your browser to:

	http://localhost:8088
	username: administrator
	password: openolat

_Happy testing!_


## Help

If you have problems or questions please use the [public mailing list](https://groups.google.com/g/openolat) or ask for [commercial support](https://www.openolat.com/kontakt/)


## Professional hosting

OpenOlat is a complex application. Installing and operating requires in-depth Java and OpenOlat application knowledge. 

[frentix](https://www.frentix.com) is the company behind OpenOlat, we are not only specialists in developing OpenOlat but also for hosting and operating OpenOlat in our own infrastructure or on-premises. Let us do what we can do best so you can concentrate on your actual learning scenarios. 

Learn more about the [OpenOlat services on the OpenOlat website](https://www.openolat.com/hosting-im-ueberblick/)
