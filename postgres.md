# 服务管理
- sudo service postgresql start
# 用户管理
## 打开shell会话
~~~shell
sudo su postgres  
psql
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