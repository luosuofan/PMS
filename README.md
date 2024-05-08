# 1.后端环境部署
下载python3.9
项目采用 pip 进行依赖和版本的管理，在 requirements.txt 文件中定义了依赖软件和版本，使用 pip 依赖管理工具进行安装：
pip3 install -r requirements.txt
## 1.1后端运行配置
项目运行前需要我们根据自己本地或者生产环境的实际情况更改相关配置文件信息，包括 数据库名、数据库账号、图片存储目录、图片域名 等相内容，配置文件路径为 config/env.py，具体内容如下：
 ======================= 应用配置 ==========================

# 开启DEBUG调试
DEBUG = False

 ======================= 数据库配置 ==========================

#数据库 ENGINE ，默认演示使用 sqlite3 数据库，正式环境建议使用 mysql 数据库
#sqlite3 设置

#DATABASE_ENGINE = "django.db.backends.sqlite3"

#DATABASE_NAME = os.path.join(BASE_DIR, "db.sqlite3")

#使用mysql时，改为此配置

DATABASE_ENGINE = "django.db.backends.mysql"
#数据库库名

DATABASE_NAME = 'djangoadmin.django.elevue'  # mysql 时使用

#数据库地址 改为自己数据库地址

DATABASE_HOST = "127.0.0.1"

#数据库端口

DATABASE_PORT = 3306

#数据库用户名

DATABASE_USER = "数据库账号"

#数据库密码

DATABASE_PASSWORD = "数据库密码"

#数据表前缀

TABLE_PREFIX = "django_"

#全局变量

#图片地址

IMAGE_URL = "http://images.django.elevue"

#附件存储目录

ATTACHMENT_PATH = "/www/webroot/djangoadmin/public/uploads"

IMAGE_PATH = '{}/images'.format(ATTACHMENT_PATH)

TEMP_PATH = '{}/temp'.format(ATTACHMENT_PATH)

参数说明：

DATABASE_NAME：数据库名，根据实际需要自定义；

IMAGE_URL：图片域名，实际部署时需要解析有效可用的域名配置；

ATTACHMENT_PATH：附件上传存放目录，所有上传的文件都存放至该目录下及其子目录下，实际部署时根据实际情况配置；


## 1.2数据迁移
实际项目开发中，我们新增或更新模块对象文件时可以使用迁移命令来动态更新同步表结构，命令执行后相关内容会同步到表结构中，可以实时查看变化，命令如下：

#生成建表文件
python manage.py makemigrations

#执行建表文件
python manage.py migrate
## 1.3启动软件
一切准备就绪后即可启动应用，启动入口文件在根目录下的 manage.py 文件；

执行命令 python manage.py runserver 0.0.0.0:8000
# 2 前端环境部署
下载node
推荐使用微软的 VSCode 开发工具打开前端项目；
## 2.1依赖安装
前端项目使用 npm 进行依赖包管理，进入解压包前端项目 evui 根目录执行安装依赖，依赖配置存放在 package.json 文件中

### 查看环境：

$ node -v

v16.13.1

$ npm -v

8.1.2
### 执行命令安装依赖：
$ npm install
## 2.2启动项目
前端项目依赖安装完毕后，在本地启动前端应用时需要将 .env.development 开头的配置文件中的 VUE_APP_API_BASE_URL 参数值设置成您本地已部署好的后端服务的地址；如下所示：

VUE_APP_VERSION=2.1.0

VUE_APP_NAME=xxx

NODE_ENV=development

VUE_APP_API_BASE_URL=http://localhost:8000
### 在 VSCode 开发工具中执行启动命令 npm run serve 启动应用，内容如下：
$ npm run serve
