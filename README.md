# csv2Postgres
loads csv files into a Postgres db for analysis

# Prerequisites
need to create the db in Postgres before using this tool<br/>
  * CREATE DATABASE dbname;

# Usage
./convert.sh <postgres-db-name> /path/to/directory/with/csv/files/<br/>
Note: it needs the trailing '/' at the end of the directory since it appends it directly to the filename. The script can easily be modified to change this behavior.

# References
StackOverflow post: http://stackoverflow.com/a/29722393/1484710, which is from where I got most of the logic for load.py
