from django.contrib.admin import AdminSite


# 自定义后台页面
class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')
