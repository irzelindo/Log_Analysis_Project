## Log_Analysis_Project
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The main purpose of this project is to put both python and postgresql in work, so the task is to create a reporting tool that prints out reports (*in plain text*) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
* * *
### Knoledge Requirements
In order to achieve the goal of this project we will need some additional knowledge as:
1. Linux server basics
    * Navegate between folders
    * List folders in current directory
    * Move folders
    * Vagrant for building and managing virtual machine environments
2. PostgreSQL
    * [Select statements](https://www.postgresql.org/docs/9.5/static/sql-select.html)
    * [SQL String functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
    * [Agregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)
3. Python
    * Writing code with DB-API
    * String format function
    * psycopg2 to make connections to postgresql database
4. HTML
    * Build webpages using html
* * *    
### Requirements to run the project
1. [install virtual box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [vagrant](https://www.vagrantup.com/) for more info about how to install and first start with these tools you can find this [video](https://www.youtube.com/watch?v=djnqoEO2rLc) usefull, it explanes the conceptual overview of virtual machines and Vagrant.
2. Once you have done with step *1*, You will have to download and unzip the [database file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
3. Then switch to database using command **psql -d news -f newsdata.sql**.
4. Once you have the data loaded into your database, connect to your database using **psql -d news** and explore the tables using the \dt and \d table commands and select statements.
* * *
### Requirements to run DB queries

In order to make the job easier, I've created [views](https://www.postgresql.org/docs/9.2/static/sql-createview.html) for answering two of folowing questions: (2 and 3),

1. What are the most popular three articles of all time? 
  * select articles.slug as article, *count(*)* as views from articles, log where log.path like(concat('%',articles.slug,'%')) group         by article order by views desc limit 3;
2. Who are the most popular article authors of all time?
  * create view article_views as select authors.name, articles.slug,*count(*)* as views from articles, log, authors where log.path           like(concat('%',articles.slug,'%')) AND authors.id = articles.author group by authors.name, articles.slug order by authors.name         desc;
  *_Next_* can make a query
  * select name, sum(views) as views from article_views group by name order by views desc;
    
3. On which days did more than 1% of requests lead to errors? 
  * create view requests as select time::date as day,sum((status like '%4%' OR status like '%5%')::int) as errors,
    sum((status like '%1%' OR status like '%2%' OR status like '%3%' OR status like '%4%' OR status like '%5%')::int) as total
    from log group by day;
  *_Next_* can make a query
  * select * from (select day, *round((round(errors,2)*100)/round(total,2),2)* as percentage from requests) 
    as bad_day where percentage>1;
 * * *
After all put **log.py** and **dbnews.py** in the same file, copy this file into vagrant directory in order to make this file available. access the file from virtual machine and run **python log.py** thne you can open a web browser and access to **_(http://localhost:8000/)_**
 
    


