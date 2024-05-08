from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.constants import NOTICE_SOURCE_LIST
from application.suggestion import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染意见反馈首页
from utils import R
@method_decorator(check_login, name="get")
class SuggestionListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:feedback:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询意见反馈分页数据方法
        result = services.SuggestionList(request)
        # 返回结果
        return result

@method_decorator(check_login, name="post")
class SuggestionAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:feedback:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加意见反馈服务方法
        result = services.SuggestionAdd(request)
        # 返回结果
        return result

@method_decorator(check_login, name="get")
class SuggestionDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:feedback:detail",)

    # GET请求渲染HTML模板
    def get(self, request, suggestion_id):
        # 调用查询意见反馈详情服务方法
        data = services.SuggestionDetail(suggestion_id)
        # 返回结果
        return R.ok(data=data)

@method_decorator(check_login, name="put")
class SuggestionUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:feedback:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新意见反馈服务方法
        result = services.SuggestionUpdate(request)
        # 返回结果
        return result

@method_decorator(check_login, name="delete")
class SuggestionDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:feedback:delete',)

    # 接收DELETE请求
    def delete(self, request, suggestion_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除意见反馈服务方法
        result = services.SuggestionDelete(suggestion_id)
        # 返回结果
        return result