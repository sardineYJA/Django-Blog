from django.contrib import admin


# 用于自动补充文章、分类、标签、侧边栏、友链Model的owner字段
class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner', )

    # 筛选当前用户的数据
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    # 自动补充owner字段
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
