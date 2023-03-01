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