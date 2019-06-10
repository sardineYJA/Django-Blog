from django.contrib import admin
from .models import Post, Category, Tag
from django.urls import reverse
from django.utils.html import format_html
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry
# Register your models here.


# 分类内置文章编辑功能
class PostInline(admin.TabularInline):   # StackedInline 样式不同
    fields = ('title', 'desc')
    extra = 1    # 控制额外多几个
    model = Post


# 分类
@admin.register(Category, site=custom_site)
# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(BaseOwnerAdmin):
    # list_display 是每条数据展示的字段
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count', 'owner')
    # fields 是 admin 中 add 所需填写的字段
    fields = ('name', 'status', 'is_nav')
    # 分类内置文章编辑
    inlines = [PostInline, ]

    # request.user 就是当前登录用户， obj 是当前要保存的对象
    # form 是页面提交过来的表单之后的对象，change 标记本次保存的数据是新增还是更新
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user       # 自动设置owner为当前登录用户
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)

    # 展示该分类下有多少篇文章
    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


# 标签
@admin.register(Tag, site=custom_site)
# class TagAdmin(admin.ModelAdmin):
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'owner')
    fields = ('name', 'status')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


# 自定义过滤器只展示当前用户分类
class CategoryOwnerFilter(admin.SimpleListFilter):
    title = "分类过滤器"               # 展示标题
    parameter_name = 'owner_category'  # 查询时URL参数的名字

    # 返回要展示的内容和查询用的id
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    # 根据URL Query的内容返回列表页数据
    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


# 文章
@admin.register(Post, site=custom_site)
# class PostAdmin(admin.ModelAdmin):
class PostAdmin(BaseOwnerAdmin):
    # 加载自定义Form
    form = PostAdminForm

    # 显示的字段
    list_display = ['title', 'category', 'status', 'created_time', 'owner', 'operator']

    # 字段作为链接，点击进入编辑页面
    list_display_links = []

    # 页面过滤器
    # list_filter = ['category']
    # 侧边栏的过滤器只能看到自己创建的分类
    list_filter = [CategoryOwnerFilter]

    # 配置搜索字段
    search_fields = ['title', 'category__name']

    actions_on_top = True     # 动作相关的配置，是否展示在顶部
    actions_on_bottom = True  # 动作相关的配置，是否展示在底部

    # 保存、编辑、编辑并新建按钮是否在顶部展示
    save_on_top = True

    exclude = ['owner']
    # filter_vertical = ('tag', )  # 垂直布局
    filter_horizontal = ('tag', )  # 水平布局

    # fieldset或者fields 配置add页面展示字段顺序与布局
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),

        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),

        ('额外信息', {
            'classes': ('wide', ),
            'fields': ('tag', ),
        })
    )

    # 展示自定义字段
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'   # 表头的展示题目

    # 自动赋值给某个字段
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)

    # 当前登录的用户在列表页中只能看到自己创建的文章
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    # 加载静态文件
    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


# 重写日志
@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
