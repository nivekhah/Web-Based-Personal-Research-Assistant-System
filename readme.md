## 1. 环境搭建

Ubuntu + Python2.7
使用以下命令行安装pip
```
sudo apt-get install python-pip python-dev build-essential
```
在当前路径下，requirements.txt中存放系统所需要的依赖，使用如下命令进行一键安装依赖
```
pip install -r requirements.txt
```

安装MySQL数据库
```
sudo apt-get install mysql-server
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev
```

安装MySQL服务器过程中会出现输入密码的对话框，设置为123456
安装成功数据库后使用命令进入数据库
```
mysql -u root -p123456
```
创建一个名为test的数据库，然后使用以下命令创建表
```
create table user(id int,email varchar(30) primary key,name varchar(30),phonenumber varchar(30),password varchar(200))  character set = utf8;

create table people (realname varchar(30),EnglishRealname varchar(30),email varchar(30),username varchar(30) primary key,domainName varchar(30),researchInterest varchar(30),myself varchar(500),Research_institutions varchar(30),department varchar(30),position varchar(30),ProfilePicturePath varchar(50),FOREIGN KEY (username) REFERENCES user(email)) character set = utf8;

create table bibtex (username varchar(30),bibtex varchar(50),pdfpath varchar(100),FOREIGN KEY (username) REFERENCES user(email),PRIMARY KEY (username,bibtex)) character set = utf8;
```

创建成功后，在当前路径下运行
python app.py即可启动程序，然后打开浏览器，在地址栏里输入127.0.0.1:7000，即可进入系统，使用系统。


## 2. 程序说明

（1）当前路径下的app.py为flask的主程序，是服务器的基础，其余的python文件都为有特定功能的某一个类，会在app.py中调用
（2）当前路径下的templates文件夹下的html文件，是系统所有前端显示的html，如果需要修改，找到该文件夹下对应的文件修改即可
（3）当前路径下的static文件，存放html文件所需要的静态文件，如果对flask不熟悉，建议先去看看static文件夹的作用，这里特别说明的是，前端有一个上传头像的功能，这里我将前端上传的头像全都保存在了static/pic/文件夹在，因为这样前端再次显示时，之间读取该文件夹即可，而放在其他地方肯定不能奏效。这里如果不懂，建议还是看看flask中static的作用
（4）当前路径下的file文件夹，用于存放生成的论文报表
（5）当前路径下的pdf文件夹，用于存放用户上传的pdf文件
（6）当前路径下的bib文件夹，用于存放用户上传的bibtex文件


## 3. 代码说明
程序中一些关键的地方有注释，并且在毕业论文里有一些介绍，可以相互结合着看

## 4. 如有问题请联系QQ：542021581，添加好友时请加备注
