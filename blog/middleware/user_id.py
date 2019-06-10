import uuid

USER_KEY = 'uid'
TEN_YEARS = 60*60*24*365*10


# Django 的 middleware 在项目启动时会被初始化，等接受请求后，
# 会根据 settings 中的 MIDDLEWARE 配置顺序挨个调用，传递 request 作为参数
class UserIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        # 设置cookie，httponly 只能在服务器端能访问
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)
        return response

    def generate_uid(self, request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uid
