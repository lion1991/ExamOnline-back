import uuid

from django.db import models

# Create your models here.
from user.models import Student
from django.db import models

def user_directory_path(instance, filename):
  # ext = filename.split('.')[-1]
  # filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
  # return the whole path to the file
    #各组员答题上传路径,在upload根路径
    return "upload/{1}/{2}".format(instance.period, "exam" + str(instance.period), filename)

def captain_directory_path(instance, filename):
    #组长答题上传路径
    return "upload/captain/{1}/{2}".format(instance.period, "exam" + str(instance.period), filename)

def exam_directory_path(instance, filename):
    #考核题上传路径
    return "upload/exam/{1}/{2}".format(instance.period, "exam" + str(instance.period), filename)

def judge_directory_path(instance, filename):
    #组长评分上传路径
    return "upload/judge/{1}/{2}".format(instance.period, "exam" + str(instance.period), filename)

def personalgrade_directory_path(instance, filename):
    #个人成绩上传路径
    return "upload/personalgrade/{1}/{2}".format(instance.period, "exam" + str(instance.period), filename)

def totalgrade_directory_path(instance, filename):
    #所有人成绩上传路径
    return "upload/totalgrade/{1}/{2}".format(instance.period, "exam" + str(instance.period), filename)

class LimitFile(models.Model):
    """
    考核期数限制
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    limit_period = models.IntegerField(verbose_name='考核期数', help_text='设定考核期数')
    limit_upload = models.IntegerField(verbose_name='上传开关(1:开启，0:关闭)', help_text='设定上传开关', default=0)
    limit_captain_upload = models.IntegerField(verbose_name='组长答题上传开关(1:开启，0:关闭)', help_text='组长答题上传开关', default=0)
    limit_captain_judge = models.IntegerField(verbose_name='组长评分上传开关(1:开启，0:关闭)', help_text='组长评分上传开关', default=0)
    limit_exam_upload = models.IntegerField(verbose_name='考核题上传开关(1:开启，0:关闭)', help_text='考核题上传开关', default=0)
    limit_personal_grade = models.IntegerField(verbose_name='个人成绩上传开关(1:开启，0:关闭)', help_text='个人成绩上传开关', default=0)
    limit_total_grade = models.IntegerField(verbose_name='总成绩上传开关(1:开启，0:关闭)', help_text='总成绩上传开关', default=0)


    class Meta:
        db_table = 'tb_limit_period'
        verbose_name = "上传限制"
        # verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.limit_period

class RandomFileId(models.Model):
    """
    随机组员
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    team_one = models.TextField(verbose_name='第一组文件id', max_length=10000, help_text='第一组文件id')
    team_two = models.TextField(verbose_name='第二组文件id', max_length=10000, help_text='第二组文件id')
    team_three = models.TextField(verbose_name='第三组文件id', max_length=10000, help_text='第三组文件id')
    team_four = models.TextField(verbose_name='第四组文件id', max_length=10000, help_text='第四组文件id')
    team_five = models.TextField(verbose_name='第五组文件id', max_length=10000, help_text='第五组文件id')
    team_six = models.TextField(verbose_name='第六组文件id', max_length=10000, help_text='第六组文件id')

    period = models.OneToOneField(LimitFile, on_delete=models.CASCADE) #一对一外键

    class Meta:
        db_table = 'tb_team_random_id'
        verbose_name = "随机判分组"

class Files(models.Model):
    """
    各组员上传的文件
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    limit_period = models.IntegerField(verbose_name='设定考核期数', help_text='设定考核期数')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    # first_score = models.IntegerField(verbose_name='第一题分数', help_text='第一题分数', null=True, blank=True)
    # second_score = models.IntegerField(verbose_name='第二题分数', help_text='第二题分数', null=True, blank=True)
    # third_score = models.IntegerField(verbose_name='第三题分数', help_text='第三题分数', null=True, blank=True)
    # upload_to 会生成指定路径文件夹，文件会保存在其中，如果文件名称重复则会自动添加后缀
    # file = models.FileField(upload_to="upload/%Y%m%d/")
    file = models.FileField(upload_to=user_directory_path)
    #个人评分合集下载地址
    downloadfile = models.CharField(verbose_name='下载链接', max_length=200, help_text='下载链接',null=True, blank=True)
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)
    finger = models.CharField(verbose_name='浏览器指纹', max_length=200, help_text='浏览器指纹')

    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键
    limit_period = models.ForeignKey(LimitFile, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_files'
        ordering = ['upload_time']
        verbose_name = "上传文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return (self.name)

class PersonalGradeFiles(models.Model):
    """
    各组员成绩文件
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    file = models.FileField(upload_to=personalgrade_directory_path)
    #个人评分合集下载地址
    downloadfile = models.CharField(verbose_name='下载链接', max_length=200, help_text='下载链接', null=True, blank=True)
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)
    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键
    limit_period = models.ForeignKey(LimitFile, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_personal_grade_files'
        ordering = ['upload_time']
        verbose_name = "个人成绩文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return (self.name)

# class TotalGradeFiles(models.Model):
#     """
#     每期总成绩文件
#     """
#     id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
#     name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
#     period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
#     file = models.FileField(upload_to=totalgrade_directory_path)
#     downloadfile = models.CharField(verbose_name='下载链接', max_length=200, help_text='下载链接', null=True, blank=True)
#     upload_time = models.DateTimeField("上传时间", auto_now_add=True)
#     uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键
#     limit_period = models.ForeignKey(LimitFile, on_delete=models.CASCADE) #多对一外键
#
#     class Meta:
#         db_table = 'tb_total_grade_files'
#         ordering = ['upload_time']
#         verbose_name = "总成绩文件"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return (self.name)

class CaptainFiles(models.Model):
    """
    各组长上传考核的文件
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    limit_period = models.IntegerField(verbose_name='设定考核期数', help_text='设定考核期数')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    # upload_to 会生成指定路径文件夹，文件会保存在其中，如果文件名称重复则会自动添加后缀
    # file = models.FileField(upload_to="upload/%Y%m%d/")
    file = models.FileField(upload_to=captain_directory_path)
    downloadfile = models.CharField(verbose_name='下载链接', max_length=200, help_text='下载链接',null=True, blank=True)
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)
    finger = models.CharField(verbose_name='浏览器指纹', max_length=200, help_text='浏览器指纹')

    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键
    limit_period = models.ForeignKey(LimitFile, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_captain_files'
        ordering = ['upload_time']
        verbose_name = "组长考核文件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return (self.name)

class ExamFiles(models.Model):
    """
    考核题文件
    """
    QUESTION_CHOICES = (
        ('1', '文档'),
        ('2', '数通'),
        ('3', '服务器'),
        ('4', '集合'),
    )

    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    # upload_to 会生成指定路径文件夹，文件会保存在其中，如果文件名称重复则会自动添加后缀
    # file = models.FileField(upload_to="upload/%Y%m%d/")
    file = models.FileField(upload_to=exam_directory_path)
    downloadfile = models.CharField(verbose_name='下载链接', max_length=200, help_text='下载链接',null=True, blank=True)
    exam_questions_type = models.CharField('考题类型', max_length=1, choices=QUESTION_CHOICES, default="4")
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)

    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_exam_files'
        ordering = ['upload_time']
        verbose_name = "考核题发布"
        verbose_name_plural = verbose_name

    def __str__(self):
        return (self.name)

class JudgeFiles(models.Model):
    """
    评分文件
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    limit_period = models.IntegerField(verbose_name='设定考核期数', help_text='设定考核期数')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    # upload_to 会生成指定路径文件夹，文件会保存在其中，如果文件名称重复则会自动添加后缀
    # file = models.FileField(upload_to="upload/%Y%m%d/")
    file = models.FileField(upload_to=judge_directory_path)
    downloadfile = models.CharField(verbose_name='下载链接', max_length=200, help_text='下载链接',null=True, blank=True)
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)

    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键
    limit_period = models.ForeignKey(LimitFile, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_judge_files'
        ordering = ['upload_time']
        verbose_name = "评分上传"
        verbose_name_plural = verbose_name

    def __str__(self):
        return (self.name)

#定义每期考核成绩模型
# 第三期
class Score3(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    office_score = models.FloatField(verbose_name='文档成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=3)

    class Meta:
        db_table = 'exam_score_total_3'
        verbose_name = '总成绩3'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore3(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=3)
    # 评分项列名
    item1 = models.FloatField(verbose_name='修改主机名(5分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='开启firewalld(5分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='文件正确拷贝(10分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='Samba全局配置（10分）', null=True, blank=True)
    item5 = models.FloatField(verbose_name='用户配置(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='ACL设定目录权限（10）', null=True, blank=True)
    item7 = models.FloatField(verbose_name='远端可挂载，权限正确（20）', null=True, blank=True)
    item8 = models.FloatField(verbose_name='简答题第一题（10分）', null=True, blank=True)
    item9 = models.FloatField(verbose_name='简答题第二题（10分）', null=True, blank=True)
    item10 = models.FloatField(verbose_name='简答题第三题（10分）', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_3'
        verbose_name = '服务器成绩3'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore3(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=3)
    # 评分项列名
    item1 = models.FloatField(verbose_name='规范分第一题（500分制）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='规范分分数（百分制30分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='配置第一题（10分', null=True, blank=True)
    item4 = models.FloatField(verbose_name='配置第二题(10分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='配置第三题(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='配置第四题(10分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='配置第五题(10分)', null=True, blank=True)
    item8 = models.FloatField(verbose_name='配置第六题(20分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_3'
        verbose_name = '数通成绩3'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
class OfficeScore3(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=3)
    # 评分项列名
    item1 = models.FloatField(verbose_name='文件名标准(10分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='按照模板编写（20分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='表格字体统一（5分）', null=True, blank=True)
    item4 = models.FloatField(verbose_name='表格边框统一（5分）', null=True, blank=True)
    item5 = models.FloatField(verbose_name='线缆数量正确（15分）', null=True, blank=True)
    item6 = models.FloatField(verbose_name='线缆规格准确（15分）', null=True, blank=True)
    item7 = models.FloatField(verbose_name='设备准确（15分）', null=True, blank=True)
    item8 = models.FloatField(verbose_name='端口准确（15分）', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_office_3'
        verbose_name = '文档成绩3'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
# 第四期
class Score4(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    office_score = models.FloatField(verbose_name='文档成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=4)

    class Meta:
        db_table = 'exam_score_total_4'
        verbose_name = '总成绩4'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore4(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=4)
    # 评分项列名
    item1 = models.FloatField(verbose_name='修改YUM源(10分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='服务端TEAM(10分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='服务端VLAN(10分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='客户端TEAM（10分）', null=True, blank=True)
    item5 = models.FloatField(verbose_name='客户端VLAN(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='DHCP通用参数（20）', null=True, blank=True)
    item7 = models.FloatField(verbose_name='DHCP分配固定IP（20）', null=True, blank=True)
    item8 = models.FloatField(verbose_name='简答题第一题（5分）', null=True, blank=True)
    item9 = models.FloatField(verbose_name='简答题第二题（5分）', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_4'
        verbose_name = '服务器成绩4'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore4(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=4)
    # 评分项列名
    item1 = models.FloatField(verbose_name='简述VRRP协议及作用（10分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='简述VGMP协议及作用（10分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='简述HRP协议及作用（10分', null=True, blank=True)
    item4 = models.FloatField(verbose_name='FW1可以web登陆，管理地址配置正确(10分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='FW2可以web登陆，管理地址配置正确(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='FW1/FW2默认密码更改正确(5分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='trust区域、untrsut区域配置正确(5分)', null=True, blank=True)
    item8 = models.FloatField(verbose_name='trust区域vrrp配置正确（vrid、ip）(10分)', null=True, blank=True)
    item9 = models.FloatField(verbose_name='untrust区域vrrp配置正确（vrid、ip）(10分)', null=True, blank=True)
    item10 = models.FloatField(verbose_name='心跳接口配置正确（5分）', null=True, blank=True)
    item11 = models.FloatField(verbose_name='策略允许防火墙ping直连地址（5分）', null=True, blank=True)
    item12 = models.FloatField(verbose_name='策略包含trust允许访问untrust（10分）', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_4'
        verbose_name = '数通成绩4'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
class OfficeScore4(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=4)
    # 评分项列名
    item1 = models.FloatField(verbose_name='文件名标准(10分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='按照模板编写（15分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='表格字体统一（5分）', null=True, blank=True)
    item4 = models.FloatField(verbose_name='表格边框统一（5分）', null=True, blank=True)
    item5 = models.FloatField(verbose_name='表格中没有标记颜色（5分）', null=True, blank=True)
    item6 = models.FloatField(verbose_name='机柜编号使用公式，且公式准确（15分）', null=True, blank=True)
    item7 = models.FloatField(verbose_name='设备编码使用公式，且公式准确（15分）', null=True, blank=True)
    item8 = models.FloatField(verbose_name='标签本端信息使用公式，且公式准确（15分）', null=True, blank=True)
    item9 = models.FloatField(verbose_name='标签对端信息使用公式，且公式准确（15分）', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_office_4'
        verbose_name = '文档成绩4'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
# 第五期
class Score5(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    office_score = models.FloatField(verbose_name='文档成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=5)

    class Meta:
        db_table = 'exam_score_total_5'
        verbose_name = '总成绩5'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore5(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=5)
    # 评分项列名
    item1 = models.FloatField(verbose_name='客户端启用firewall（10分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='服务端启用iptables服务(10分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='服务端iptables规则1（20分）', null=True, blank=True)
    item4 = models.FloatField(verbose_name='服务端iptables规则2（20分）', null=True, blank=True)
    item5 = models.FloatField(verbose_name='服务端保存iptables规则(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='服务端ssh端口(10分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='服务端ssh限制用户配置(20分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_5'
        verbose_name = '服务器成绩5'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore5(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=5)
    # 评分项列名
    item1 = models.FloatField(verbose_name='正确完成IP及网络配置(20分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='R3路由器提供DHCP全局地址池服务且租期、保留地址、指定地址正确。(20分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='正确配置TRUST/UNTRUST/DMZ区域确(10分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='防火墙配置网页登录，并允许访问所有直连地址(10分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='配置10.0.10.0段可以访问server6，限制10.0.10.5不可以访问(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='client9 可以访问server1的ftp服务(15分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='client2可以访问server6的http服务，但不允许ping(15分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_5'
        verbose_name = '数通成绩5'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
class OfficeScore5(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=5)
    # 评分项列名
    item1 = models.FloatField(verbose_name='文件名标准(5分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='表格字体统一（10分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='表格使用边框，并且格式统一（10分）', null=True, blank=True)
    item4 = models.FloatField(verbose_name='序号使用公式，能够自动排序（15分）', null=True, blank=True)
    item5 = models.FloatField(verbose_name='机柜编号使用公式，且公式准确（15分）', null=True, blank=True)
    item6 = models.FloatField(verbose_name='设备编码使用公式，且公式准确（15分）', null=True, blank=True)
    item7 = models.FloatField(verbose_name='标签本端信息使用公式，且公式准确（15分）', null=True, blank=True)
    item8 = models.FloatField(verbose_name='标签对端信息使用公式，且公式准确（15分）', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_office_5'
        verbose_name = '文档成绩5'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
# 第六期
class Score6(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=6)

    class Meta:
        db_table = 'exam_score_total_6'
        verbose_name = '总成绩6'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore6(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=6)
    # 评分项列名
    item1 = models.FloatField(verbose_name='iptables配置（20分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='Apache服务安装（20分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='默认目录设置(10分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='浏览内容正确(10分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_6'
        verbose_name = '服务器成绩6'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore6(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=6)
    # 评分项列名
    item1 = models.FloatField(verbose_name='正确完成IP及网络配置(20分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='AR5/AR6/CE1 使用路由协议互联互通(15分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='PC6-PC7的IPV6地址互联互通(15分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='CE1/CE2/CE3按照拓扑需求配置OSPF，保证网络互通(10分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='dis ospf peer ##CE1交换机ospf邻居正常(10分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='按需求配置Vxlan(VNI一致)(15分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='dis vxlan tunnel verbose ##State UP(15分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_6'
        verbose_name = '数通成绩6'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
# 第七期
class Score7(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=7)

    class Meta:
        db_table = 'exam_score_total_7'
        verbose_name = '总成绩7'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore7(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=7)
    # 评分项列名
    item1 = models.FloatField(verbose_name='服务端NFS服务（10分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='tmp目录配置（10分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='public目录配置(15分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='upload目录配置(20分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='hsoft目录配置(15分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='客户端autofs配置(30分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_7'
        verbose_name = '服务器成绩7'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore7(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=7)
    # 评分项列名
    item1 = models.FloatField(verbose_name='正确完成IP及网络配置(20分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='正确配置area区域(15分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='area 10/area 20配置NSSA区域(20分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='AR5/AR7引入默认路由(15分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='实验1栋和实验2栋可以访问网络(15分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='trunk禁止vlan 1通过(15分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_7'
        verbose_name = '数通成绩7'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')
# 第八期
class Score8(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=8)

    class Meta:
        db_table = 'exam_score_total_8'
        verbose_name = '总成绩8'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore8(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=8)
    # 评分项列名
    item1 = models.FloatField(verbose_name='下载ntp服务源码（10分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='ntp服务编译（30分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='ntp服务配置(40分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='开机启动ntp服务(20分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_8'
        verbose_name = '服务器成绩8'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore8(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=8)
    # 评分项列名
    item1 = models.FloatField(verbose_name='正确完成IP及网络配置(20分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='PC1不能访问Server1/2 但可以访问PC2(20分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='PC2可以访问Server2 但不能访问Server1(20分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='PC2不能ping通Server1,但可以访问Server1的FTP服务(20分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='AR1不能ping通AR2,但可以ssh(20分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_8'
        verbose_name = '数通成绩8'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

# 第九期
class Score9(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    network_score = models.FloatField(verbose_name='数通成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=9)

    class Meta:
        db_table = 'exam_score_total_9'
        verbose_name = '总成绩9'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore9(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=9)
    # 评分项列名
    item1 = models.FloatField(verbose_name='禁止所有Ipv4/Ipv6客户端同步NTP时间（20分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='允许10.0.10段客户端同步（10分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='firewalld服务配置(30分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='systemd服务配置(40分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_9'
        verbose_name = '服务器成绩9'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class NetworkScore9(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=9)
    # 评分项列名
    item1 = models.FloatField(verbose_name='正确完成IP及网络配置(20分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='DHCP服务器配置正确(20分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='LACP配置正确(15分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='AR2路由器单臂路由配置正确(15分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='SW6\SW7 vrrp配置正确(15分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='bfd配置正确(15分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_9'
        verbose_name = '数通成绩9'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

#第十期
class Score10(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    linux_score = models.FloatField(verbose_name='服务器成绩', null=True, blank=True)
    period = models.IntegerField(verbose_name='考核期数', default=10)

    class Meta:
        db_table = 'exam_score_total_10'
        verbose_name = '总成绩10'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

class LinuxScore10(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=10)
    # 评分项列名
    item1 = models.FloatField(verbose_name='开机启动vsftpd服务(5分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='设置ftp登陆公告(5分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='匿名用户权限(20分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='本地用户权限(10分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='ftpuser1用户权限(20分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='ftpuser2用户权限(20分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='用户限速配置(10分)', null=True, blank=True)
    item8 = models.FloatField(verbose_name='用户连接数限制配置(10分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_10'
        verbose_name = '服务器成绩10'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

#第十一期
class NetworkScore11(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=11)
    team = models.CharField(max_length=100, verbose_name='小组')
    # 评分项列名
    item1 = models.FloatField(verbose_name='按要求配置路由协议（10分）', null=True, blank=True)
    item2 = models.FloatField(verbose_name='按要求配置IP地址（10分）', null=True, blank=True)
    item3 = models.FloatField(verbose_name='解决客户端获取不到IP地址问题(20分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='客户端按要求获取指定IP地址(20分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='AR4/AR8 链路及chap认证正确，并使用本人姓名作为用户名密码，链路状态正常(10分', null=True, blank=True)
    item6 = models.FloatField(verbose_name='10段、20段可以访问OA Service，70段、80段可以访问Mail Service(20分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='其余网段不可访问非允许服务(10分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...
    class Meta:
        db_table = 'exam_score_network_11'
        verbose_name = '数通成绩11'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')

#第十二期
class LinuxScore12(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    period = models.IntegerField(verbose_name='考核期数', default=12)
    team = models.CharField(max_length=100, verbose_name='小组')
    # 评分项列名
    item1 = models.FloatField(verbose_name='安装并启动httpd服务(10分)', null=True, blank=True)
    item2 = models.FloatField(verbose_name='开机自启动httpd服务(10分)', null=True, blank=True)
    item3 = models.FloatField(verbose_name='创建虚拟主机配置文件(10分)', null=True, blank=True)
    item4 = models.FloatField(verbose_name='设置虚拟主机目录、端口(10分)', null=True, blank=True)
    item5 = models.FloatField(verbose_name='设置虚拟主机权限(15分)', null=True, blank=True)
    item6 = models.FloatField(verbose_name='设置虚拟主机日志(15分)', null=True, blank=True)
    item7 = models.FloatField(verbose_name='设置虚拟主机域名及权限(30分)', null=True, blank=True)
    total = models.FloatField(verbose_name='总分', null=True, blank=True)
    # ...

    class Meta:
        db_table = 'exam_score_linux_12'
        verbose_name = '服务器成绩12'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'period')