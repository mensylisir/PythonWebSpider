### Mysql 设置 root 密码

编辑/etc/mysql/my.cnf 文件,在最后加入以下设置

```
[mysqld]
skip-grant-tables=1
```

重启 mysql 服务

```
sudo systemctl stop mysql
sudo systemctl start mysql
```

修改 mysql root 密码

```
update mysql.user set authentication_string=password('123456') where user='root' and Host ='localhost';
update user set  plugin="mysql_native_password";
flush privileges;
```

### Mysql 添加新用户

#### 添加本地可访问用户

````
create user 'mensyli4'@'localhost' identified by 'xiaoming98';
grant all privileges on *.* to 'mensyli4'@'localhost' identified by 'xiaoming98';
flush privileges;```
````

#### 添加任意主机可访问用户

```
create user 'mensyli4'@'%' identified by 'xiaoming98';
grant all privileges on *.* to 'mensyli4'@'%' identified by 'xiaoming98';
flush privileges;
```

#### mysql 开启远程主机访问

```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
将 bind-address = 127.0.0.1
修改为 bind-address = 0.0.0.0
```
