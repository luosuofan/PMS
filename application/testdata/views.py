
from django.utils.decorators import method_decorator
from django.views import View
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired
from application.testdata import services
from utils import R


# 查询数据
@method_decorator(check_login, name='dispatch')
class TestDataListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:testdata:list',)

    # POST查询分页数据
    def get(self, request):
        # 调用查询职级分页数据服务方法
        result = services.TestDataList(request)
        # 返回结果
        return result


# 查询详情
@method_decorator(check_login, name='dispatch')
class TestDataDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:testdata:detail',)

    # GET请求渲染HTML模板
    def get(self, request, testdata_id):
        # 调用查询职级详情服务方法
        data = services.TestDataDetail(testdata_id)
        # 返回结果
        return R.ok(data=data)


# 添加

class TestDataAddView(View):

    # 接收POST网络请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加职级服务
        result = services.TestDataAdd(request)
        # 返回结果
        return result


@method_decorator(check_login, name="put")
class TestDataUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:testdata:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新服务方法
        result = services.TestDataUpdate(request)
        # 返回结果
        return result

# 删除
@method_decorator(check_login, name="delete")
class TestDataDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:testdata:delete',)

    # 接收DELETE请求
    def delete(self, request, testdata_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除用户服务方法
        result = services.TestDataDelete(testdata_id)
        # 返回结果
        return result

@method_decorator(check_login, name='dispatch')
class TestDataNewestListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:testdata:list',)

    # POST查询分页数据
    def get(self, request):
        # 调用查询职级分页数据服务方法
        result = services.TestDataNewestList(request)
        # 返回结果
        return result
