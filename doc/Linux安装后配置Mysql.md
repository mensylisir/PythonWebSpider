### 安装 gcc/g++编译环境

```
## ubuntu
sudo apt install build-essential
sudo apt install binutils bison
sudo apt install zip unzip

## centos
sudo dnf install gcc gcc-c++ gdb make cmake
sudo dnf install binutils bison
sudo dnf install zip unzip
```

### Anaconda3 环境配置

#### 安装

```
Anaconda3 will now be installed into this location:
/home/mensyli4/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/mensyli4/anaconda3] >>> **/home/mensyli4/install/anaconda3**
PREFIX=/home/mensyli4/install/anaconda3
Unpacking payload ...
Extracting : numexpr-2.7.0-py37h9e4a6bb_0.conda:   9%|███▌                                     | 25/291 [00:05<00:53,  4.97it/s]
```

#### 初始化

```
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>> **yes**
no change     /home/mensyli4/install/anaconda3/condabin/conda
no change     /home/mensyli4/install/anaconda3/bin/conda
no change     /home/mensyli4/install/anaconda3/bin/conda-env
no change     /home/mensyli4/install/anaconda3/bin/activate
no change     /home/mensyli4/install/anaconda3/bin/deactivate
no change     /home/mensyli4/install/anaconda3/etc/profile.d/conda.sh
no change     /home/mensyli4/install/anaconda3/etc/fish/conf.d/conda.fish
no change     /home/mensyli4/install/anaconda3/shell/condabin/Conda.psm1
no change     /home/mensyli4/install/anaconda3/shell/condabin/conda-hook.ps1
no change     /home/mensyli4/install/anaconda3/lib/python3.7/site-packages/xontrib/conda.xsh
no change     /home/mensyli4/install/anaconda3/etc/profile.d/conda.csh
modified      /home/mensyli4/.bashrc
```

#### 查看.bashrc

```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/mensyli4/install/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/mensyli4/install/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/mensyli4/install/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/mensyli4/install/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

#### 验证

```
source ~/.bashrc   #使环境变量生效

mensyli4@mensyli4:~$ source .bashrc
(base) mensyli4@mensyli4:~$ python
Python 3.7.4 (default, Aug 13 2019, 20:35:49)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

#### virtualenvwrapper 安装

```
pip install virtualenvwrapper
```

#### virtualenvwrapper 设置环境变量

```
export WORKON_HOME="/home/mensyli4/install/PyHome"
source ~/install/anaconda3/bin/virtualenvwrapper.sh
```

#### virtualenvwrapper 验证

```
base) mensyli4@mensyli4:~$ mkvirtualenv test
Using base prefix '/home/mensyli4/install/anaconda3'
New python executable in /home/mensyli4/install/PyHome/test/bin/python
Installing setuptools, pip, wheel...
```

### Java 环境配置

#### 解压

```
tar -zxvf jdk-8u231-linux-x64.tar.gz
```

#### 配置环境变量

```
# >>> java config >>>
# ADD JAVA ENV
export JAVA_HOME="/home/mensyli4/install/jdk1.8.0_231"
export PATH="$JAVA_HOME/bin:$PATH"
# >>> java config >>>
```

#### 验证

```
(base) mensyli4@mensyli4:~$ source .bashrc
(base) mensyli4@mensyli4:~$ java -version
java version "1.8.0_231"
Java(TM) SE Runtime Environment (build 1.8.0_231-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.231-b11, mixed mode)
```

### pyenv 配置

#### 安装

```
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

#### 环境变量配置

```
# <<< pyenv config >>>
export PATH="/home/mensyli4/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
# <<< pyenv config >>>
```

#### 验证

```
(base) mensyli4@mensyli4:~$ source .bashrc
(base) mensyli4@mensyli4:~$ pyenv
pyenv 1.2.15
Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   commands    List all available pyenv commands
   activate    Activate virtual environment
   commands    List all available pyenv commands
   deactivate   Deactivate virtual environment
   doctor      Verify pyenv installation and deevlopment tools to build pythons.
   exec        Run an executable with the selected Python version
   global      Set or show the global Python version
   help        Display help for a command
   hooks       List hook scripts for a given pyenv command
   init        Configure the shell environment for pyenv
   install     Install a Python version using python-build
   local       Set or show the local application-specific Python version
   prefix      Display prefix for a Python version
   rehash      Rehash pyenv shims (run this after installing executables)
   root        Display the root directory where versions and shims are kept
   shell       Set or show the shell-specific Python version
   shims       List existing pyenv shims
   uninstall   Uninstall a specific Python version
   --version   Display the version of pyenv
   version     Show the current Python version and its origin
   version-file   Detect the file that sets the current pyenv version
   version-name   Show the current Python version
   version-origin   Explain how the current Python version is set
   versions    List all Python versions available to pyenv
   virtualenv   Create a Python virtualenv using the pyenv-virtualenv plugin
   virtualenv-delete   Uninstall a specific Python virtualenv
   virtualenv-init   Configure the shell environment for pyenv-virtualenv
   virtualenv-prefix   Display real_prefix for a Python virtualenv version
   virtualenvs   List all Python virtualenvs found in `$PYENV_ROOT/versions/*'.
   whence      List all Python versions that contain the given executable
   which       Display the full path to an executable

See `pyenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/pyenv/pyenv#readme
```

#### 卸载

```
rm -fr ~/.pyenv
```

#### 更新

```
pyenv update
```

### nvm 配置

#### 安装

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash
```

#### 环境变量配置

```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

#### 验证

```
(base) mensyli4@mensyli4:~$ source .bashrc
(base) mensyli4@mensyli4:~$ nvm

Node Version Manager (v0.35.1)

Note: <version> refers to any version-like string nvm understands. This includes:
  - full or partial version numbers, starting with an optional "v" (0.10, v0.1.2, v1)
  - default (built-in) aliases: node, stable, unstable, iojs, system
  - custom aliases you define with `nvm alias foo`

 Any options that produce colorized output should respect the `--no-colors` option.

Usage:
  nvm --help                                Show this message
```

#### 列出 node.js 版本

```
(base) mensyli4@mensyli4:~$ nvm list-remote
        v0.1.14
        v0.1.15
        v0.1.16
        .......
        .......
        .......
        v12.12.0
        v12.13.0   (Latest LTS: Erbium)
        v13.0.0
        v13.0.1
```

#### 安装 node.js

```
(base) mensyli4@mensyli4:~$ nvm install 13.0.0
Downloading and installing node v13.0.0...
Downloading https://nodejs.org/dist/v13.0.0/node-v13.0.0-linux-x64.tar.xz...
##################                                                                                                    16.4%
```

#### 验证

```
(base) mensyli4@mensyli4:~$ nvm list
->     v12.13.0
default -> 13.0.0 (-> N/A)
node -> stable (-> v12.13.0) (default)
stable -> 12.13 (-> v12.13.0) (default)
iojs -> N/A (default)
unstable -> N/A (default)
lts/* -> lts/erbium (-> v12.13.0)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.17.1 (-> N/A)
lts/carbon -> v8.16.2 (-> N/A)
lts/dubnium -> v10.17.0 (-> N/A)
lts/erbium -> v12.13.0
(base) mensyli4@mensyli4:~$ node
Welcome to Node.js v12.13.0.
Type ".help" for more information.
```

### gvm 配置

#### 安装

```
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

#### 验证

```
(base) mensyli4@mensyli4:~$ source /home/mensyli4/.gvm/scripts/gvm
(base) mensyli4@mensyli4:~$ gvm version
Go Version Manager v1.0.22 installed at /home/mensyli4/.gvm
```

#### 列出 go 版本

```
gvm listall
```

#### 安装 go

```
gvm install 1.13.2 -B
```

#### 设置为默认

```
gvm use go1.13.2 --defult
```

#### 验证

```
(base) mensyli4@mensyli4:~$ gvm use go1.13.2 --defult
Now using version go1.13.2
(base) mensyli4@mensyli4:~$ go version
go version go1.13.2 linux/amd64
```

### sdkman 配置

#### 安装

```
sudo apt install zip unzip
curl -s https://get.sdkman.io | bash
```

#### 环境变量配置

```
#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/mensyli4/.sdkman"
[[ -s "/home/mensyli4/.sdkman/bin/sdkman-init.sh" ]] && source "/home/mensyli4/.sdkman/bin/sdkman-init.sh"
```

#### 验证

```
(test) (base) mensyli4@mensyli4:~$ source .bashrc
(base) mensyli4@mensyli4:~$ sdk list
==== BROADCAST =================================================================
* 2019-11-05: Micronaut 1.2.6 released on SDKMAN! #micronautfw
* 2019-11-05: Gradle 6.0-rc-3 released on SDKMAN! #gradle
* 2019-11-01: Gradle 5.6.4 released on SDKMAN! #gradle
================================================================================
```

### rvm

#### 安装

```
curl -sSL https://rvm.io/pkuczynski.asc | gpg --import -
curl -sSL https://get.rvm.io | bash -s stable
```

#### 环境变量配置

```
# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
```

#### 验证

```
base) mensyli4@mensyli4:~$ source .bashrc
(base) mensyli4@mensyli4:~$ rvm version
rvm 1.29.9 (latest) by Michal Papis, Piotr Kuczynski, Wayne E. Seguin [https://rvm.io]
```

#### rvm 列出所有 ruby 版本

```
rvm list known
```

#### rvm 安装 ruby

```
rvm install 2.6.3
```

#### 验证 ruby

```
base) mensyli4@mensyli4:~$ echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"' >>~/.bashrc
(base) mensyli4@mensyli4:~$ source ~/.bashrc
(base) mensyli4@mensyli4:~$ rvm use 2.6.3 --default
Using /home/mensyli4/.rvm/gems/ruby-2.6.3
(base) mensyli4@mensyli4:~$ ruby -v
ruby 2.6.3p62 (2019-04-16 revision 67580) [x86_64-linux]
```

#### 安装 rails

```
gem install rails
```

### lamp-server

#### 安装

```
## ubuntu
sudo apt install lamp-server^

## centos
1. install httpd
// We will be installing Apache with dnf, which is the default package manager for CentOS 8:
sudo dnf install httpd
// After installing Apache services on your system, start all required services:
systemctl restart httpd
systemctl status httpd
systemctl enable httpd
// Then, allow Apache HTTP server via the firewall:
firewall-cmd --add-port=80/tcp --zone=public --permanent
firewall-cmd --add-port=443/tcp --zone=public --permanent
firewall-cmd --reload
2. install MariaDB
// MariaDB is a drop in replacement for MySQL. It is a robust, scalable and reliable SQL server that comes rich set of enhancements. We will also be using yum to install MariaDB:
sudo dnf install mariadb-server
// By default, MariaDB is not hardened. You can secure MariaDB using the mysql_secure_installation script. you should read and below each steps carefully which will set root password, remove anonymous users, disallow remote root login, and remove the test database and access to secure MariaDB:
mysql_secure_installation
// To log into MariaDB, use the following command (note that it’s the same command you would use to log into a MariaDB database):
mysql -u root -p
// Then, restart the MariaDB database server and enable it to start on system start-up using:
systemctl restart mariadb
systemctl status mariadb
systemctl enable mariadb
3. install PHP
// Finally, run the commands below to install PHP along with other good-to-have modules:
sudo dnf install php php-common php-pecl-apcu php-cli php-pear php-pdo php-mysqlnd php-pgsql php-gd php-mbstring php-xml
// Restart Apache using systemctl for the changes to take effect:
sudo systemctl restart httpd
// Now, it is time to test it. Create a new file called test.php on /var/www/html and add the following:
sudo nano /var/www/html/test.php
<?php
phpinfo();
?>

```

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
update mysql.user set authentication_string=password('123456') where User='root' and Host ='localhost';
update user set  plugin="mysql_native_password";
flush privileges;

## 8.0
flush privileges;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
```

### Mysql 添加新用户

#### 添加本地可访问用户

```
create user 'mensyli4'@'localhost' identified by '123456';
grant all privileges on *.* to 'mensyli4'@'localhost' identified by '123456';
flush privileges;

## 8.0
create user 'mensyli4'@'localhost' identified by '123456';
GRANT ALL PRIVILEGES ON *.* TO 'mensyli4'@'localhost';
flush privileges;
```

#### 添加任意主机可访问用户

```
create user 'mensyli4'@'%' identified by '123456';
ALTER USER 'mensyli4'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'
grant all privileges on *.* to 'mensyli4'@'%' identified by '123456';
flush privileges;


## 8.0
create user 'mensyli4'@'%' identified by '123456';
ALTER USER 'mensyli4'@'%' IDENTIFIED WITH mysql_native_password BY '123456'
GRANT ALL PRIVILEGES ON *.* TO 'mensyli4'@'%';
flush privileges;

```

#### mysql 开启远程主机访问

```
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
将 bind-address = 127.0.0.1
修改为 bind-address = 0.0.0.0
```
