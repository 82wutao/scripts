# 服务管理
- sudo service postgresql start
# 用户管理
## 打开shell会话
~~~shell
sudo su postgres  
psql
~~~
## 用户shell中执行命令
~~~shell
prompt [PGpassword=xxyyzz] psql -h<host> [-P<port>] -u<username> <database>
-c"sql statement or command"
~~~

## 权限管理
~~~sql
ALTER USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE exampledb to dbuser;

-- protype
GRANT privilege [, ...]
ON object [, ...]
TO { PUBLIC | GROUP group | username }

-- privilege {SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER,CREATE,CONNECT,TEMPORARY,EXECUTE,USAGE}
    
~~~
# CREATE
~~~sql
CREATE DATABASE exampledb OWNER dbuser;
~~~
# 数据表间复制
~~~SQL
insert into tbl_b(tbl_b.clmn1,[tbl_b.clmn2,...]) 
select tbl_a.clmn1|expression|constant[,...] from tbl_a;

-- len(tbl_b.clmns[]) == len(tbl_a.select clmns)
~~~
# 数据/SCHEMA 备份
~~~SQL
PGPASSWORD=xx pg_dump -U $ -h $ -p $ -d $ -t $ [--column-inserts] -f $.sql -F P -v
~~~
