## 简介
使用Django搭建Blog系统

参考书籍《Django企业开发实战 高效Python Web框架指南》

参考：https://github.com/the5fire/typeidea

## 命令
创建项目：
django-admin startproject project_name

运行：
python manage.py runserver

创建app：
python manage.py startapp app_name

创建数据库：
python manage.py makemigrations

python manage.py migrate

创建用户：
python manage.py createsuperuser

## 流程
1. 创建项目
2. 拆分settings.py为base.py和develop.py，修改配置
3. 创建blog,config,comment三个App，编写models
4. 模型写好添加到settings中，创建数据库
5. 配置admin后台管理页面，开启展示日志记录
6. 创建blog/adminforms.py用作blog/admin.py的Form
7. 创建base_admin.py作为blog/admin.py的基础类
8. 创建custom_site.py，继承AdminSite来定义自己的site
9. view的两种编写：function view和class-base view
10. base.html为基础，list.html为文章列表首页，detail.html作文章内容
11. url.py链接名称的补充
12. 创建rss.py实现RSS输出
13. 创建sitemap.py和sitemap.xml实现sitemap输出

## 测试链接
首页：http://127.0.0.1:8000/

分类1：http://127.0.0.1:8000/category/1/

文章1：http://127.0.0.1:8000/post/1.html

搜索：http://127.0.0.1:8000/search/?keyword=hello

作者1的文章：http://127.0.0.1:8000/author/1/

友链：http://127.0.0.1:8000/links/

自定义后台：http://127.0.0.1:8000/admin/

原后台：http://127.0.0.1:8000/super_admin/

RSS：http://127.0.0.1:8000/rss/

Sitemap：http://127.0.0.1:8000/sitemap.xml
