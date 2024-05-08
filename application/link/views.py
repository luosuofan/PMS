# +----------------------------------------------------------------------
# | DjangoAdmin敏捷开发框架 [ 赋能开发者，助力企业发展 ]
# +----------------------------------------------------------------------
# | 版权所有 2021~2023 北京DjangoAdmin研发中心
# +----------------------------------------------------------------------
# | Licensed LGPL-3.0 DjangoAdmin并不是自由软件，未经许可禁止去掉相关版权
# +----------------------------------------------------------------------
# | 官方网站: https://www.djangoadmin.cn
# +----------------------------------------------------------------------
# | 作者: @一米阳光 团队荣誉出品
# +----------------------------------------------------------------------
# | 版权和免责声明:
# | 本团队对该软件框架产品拥有知识产权（包括但不限于商标权、专利权、著作权、商业秘密等）
# | 均受到相关法律法规的保护，任何个人、组织和单位不得在未经本团队书面授权的情况下对所授权
# | 软件框架产品本身申请相关的知识产权，禁止用于任何违法、侵害他人合法权益等恶意的行为，禁
# | 止用于任何违反我国法律法规的一切项目研发，任何个人、组织和单位用于项目研发而产生的任何
# | 意外、疏忽、合约毁坏、诽谤、版权或知识产权侵犯及其造成的损失 (包括但不限于直接、间接、
# | 附带或衍生的损失等)，本团队不承担任何法律责任，本软件框架禁止任何单位和个人、组织用于
# | 任何违法、侵害他人合法利益等恶意的行为，如有发现违规、违法的犯罪行为，本团队将无条件配
# | 合公安机关调查取证同时保留一切以法律手段起诉的权利，本软件框架只能用于公司和个人内部的
# | 法律所允许的合法合规的软件产品研发，详细声明内容请阅读《框架免责声明》附件；
# +----------------------------------------------------------------------

from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.constants import LINK_TYPE_LIST, LINK_PLATFORM_LIST, LINK_FORM_LIST
from application.link import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染友链首页
from utils import R


# 查询友链分页数据
@method_decorator(check_login, name="get")
class LinkListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询友链分页数据方法
        result = services.LinkList(request)
        # 返回结果
        return result


# 查询友链详情
@method_decorator(check_login, name="get")
class LinkDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:detail",)

    # GET请求渲染HTML模板
    def get(self, request, link_id):
        # 调用查询友链详情服务方法
        data = services.LinkDetail(link_id)
        # 返回结果
        return R.ok(data=data)


# 添加友链
@method_decorator(check_login, name="post")
class LinkAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加友链服务方法
        result = services.LinkAdd(request)
        # 返回结果
        return result


# 更新友链
@method_decorator(check_login, name="put")
class LinkUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:link:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新友链服务方法
        result = services.LinkUpdate(request)
        # 返回结果
        return result


# 删除友链
@method_decorator(check_login, name="delete")
class LinkDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:link:delete',)

    # 接收DELETE请求
    def delete(self, request, link_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除友链服务方法
        result = services.LinkDelete(link_id)
        # 返回结果
        return result


# 设置友链状态
@method_decorator(check_login, name='put')
class LinkStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:link:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置友链状态服务方法
        result = services.LinkStatus(request)
        # 返回结果
        return result
