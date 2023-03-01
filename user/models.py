from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class Department(models.Model):
    """部门"""
    # year = models.CharField("年级", max_length=20)
    # major = models.CharField("专业", max_length=20)
    department  = models.CharField("部门", max_length=20, default="工程部")

    class Meta:
        ordering = ['id']
        verbose_name = "部门"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.year + self.major + self.department
        return self.department




class Teacher(models.Model):
    "考核管理员模型类"
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女')
    )
    TITLE_CHOICES = (
        ('审批员', '审批员'),
        # ('副教授', '副教授'),
        # ('教授', '教授')
    )
    name = models.CharField("姓名", max_length=20, default="")
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="男")
    title = models.CharField("角色", max_length=5, choices=TITLE_CHOICES, default="审批员")
    institute = models.CharField("项目组", max_length=20, default="")

    # 一对一关联字段
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")

    class Meta:
        ordering = ['id']
        db_table = 'user_teacher'
        verbose_name = '审批员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




# class MetaInfo(models.Model):
#     """根菜单元信息"""
#
#     title  = models.CharField("标题", max_length=20, default="")
#     icon  = models.CharField("图标", max_length=20, default="")
#
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_meta'
#         verbose_name = "菜单元信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         # return self.year + self.major + self.department
#         return self.roles

#
# class MenuInfo(models.Model):
#     """根菜单信息"""
#     path = models.CharField("路径", max_length=20, default="")
#     # 一对一关联字段
#     # user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)
#     component = models.CharField("组件", max_length=20, default="Layout")
#     alwaysShow = models.BooleanField("显示权限")
#     name = models.CharField("菜单名称", max_length=20, default="")
#     meta = models.ForeignKey(MetaInfo, verbose_name="元信息", on_delete=models.CASCADE, related_name='metainfo')
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_menu'
#         verbose_name = '菜单权限信息'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


# class MetaChildrenInfo(models.Model):
#     """子菜单元信息"""
#
#     title  = models.CharField("标题", max_length=20, default="")
#     icon  = models.CharField("图标", max_length=20, default="")
#     # roles = models.ForeignKey(RolesInfo, verbose_name="权限信息", on_delete = models.CASCADE, related_name='meta_children_roles')
#
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_meta_children'
#         verbose_name = "子菜单元信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         # return self.year + self.major + self.department
#         return self.roles

# class MenuChildren(models.Model):
#     """子菜单"""
#     path = models.CharField("路径", max_length=20, default="")
#     component = models.CharField("组件", max_length=20, default="Layout")
#     alwaysShow = models.BooleanField("显示权限")
#     name = models.CharField("菜单名称", max_length=20, default="")
#     meta = models.OneToOneField(MetaChildrenInfo, verbose_name="=子菜单元信息", on_delete=models.CASCADE)
#     menu = models.ForeignKey(MenuInfo, verbose_name="菜单信息", on_delete=models.CASCADE, related_name='children')
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_menu_children'
#         verbose_name = "子菜单信息"
#         verbose_name_plural = verbose_name
#
#
#     def __str__(self):
#         # return self.year + self.major + self.department
#         return self.name


class Student(models.Model):
    """员工模型类"""
    GENDER_CHOICES = (
        ('m', '男'),
        ('f', '女')
    )
    name = models.CharField("姓名", max_length=20, default="")
    # 一对一关联字段
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)
    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES, default="m")
    department = models.ForeignKey(Department, verbose_name="部门", on_delete=models.CASCADE, default="1",
                                   null=True)
    # roles = models.CharField("权限", max_length=20, default="")
    avatar = models.CharField("头像", max_length=20, default="", null=True, blank=True)
    introduction = models.CharField("介绍", max_length=20, default="", null=True, blank=True)
    # menu = models.ForeignKey(MenuInfo, verbose_name="菜单信息", on_delete=models.CASCADE, related_name='menuinfo')
    # menuroles = models.ManyToManyField(MenuInfo, through='StaffMenu', verbose_name="用户菜单关系", blank=True )


    class Meta:
        ordering = ['id']
        db_table = 'user_student'
        verbose_name = '员工'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class StaffMenu(models.Model):
#     staff = models.ForeignKey(Student, on_delete=models.CASCADE)
#     menu = models.ForeignKey(MenuInfo, on_delete=models.CASCADE)


# class RolesInfo(models.Model):
#     """子菜单权限"""
#
#     sys = models.CharField("权限名称", max_length=20, default="")
#     roles_meta_children = models.ForeignKey(MetaChildrenInfo, verbose_name="权限信息", on_delete = models.CASCADE, related_name='roles')
#     # roles_student = models.ForeignKey(Student, verbose_name="权限信息", on_delete = models.CASCADE, related_name='roles')
#
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_children_roles'
#         verbose_name = "子菜单按钮权限信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         # return self.year + self.major + self.department
#         return self.sys

# class UserLayoutRolesInfo(models.Model):
#     """用户根菜单权限"""
#
#     name = models.CharField("权限名称", max_length=20, default="")
#     roles_meta = models.ForeignKey(MetaInfo, verbose_name="权限信息", on_delete = models.CASCADE, related_name='roles')
#
#     class Meta:
#         ordering = ['id']
#         db_table = 'user_layout_roles'
#         verbose_name = "layout菜单按钮权限信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         # return self.year + self.major + self.department
#         return self.name

class UserRolesInfo(models.Model):
    """用户权限"""

    name = models.CharField("权限名称", max_length=20, default="")
    roles_student = models.ForeignKey(Student, verbose_name="权限信息", on_delete = models.CASCADE, related_name='roles')

    class Meta:
        ordering = ['id']
        db_table = 'user_roles'
        verbose_name = "权限信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return self.year + self.major + self.department
        return self.name
