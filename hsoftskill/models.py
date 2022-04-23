import uuid

from django.db import models

# Create your models here.
from user.models import Student
from django.db import models

def user_directory_path(instance, filename):
  # ext = filename.split('.')[-1]
  # filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
  # return the whole path to the file
  return "upload/{1}/{2}".format(instance.period, "第" + str(instance.period) + "期考核", filename)


class LimitFile(models.Model):
    """
    考核期数限制
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    limit_period = models.IntegerField(verbose_name='设定考核期数', help_text='设定考核期数')


    class Meta:
        db_table = 'tb_limit_period'
        # verbose_name = "limit_period"
        # verbose_name_plural = verbose_name

    def __str__(self):
        return self.limit_period


class Files(models.Model):
    """
    用户上传的文件
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    limit_period = models.IntegerField(verbose_name='设定考核期数', help_text='设定考核期数')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    # upload_to 会生成指定路径文件夹，文件会保存在其中，如果文件名称重复则会自动添加后缀
    # file = models.FileField(upload_to="upload/%Y%m%d/")
    file = models.FileField(upload_to=user_directory_path)
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)
    finger = models.CharField(verbose_name='浏览器指纹', max_length=200, help_text='浏览器指纹')

    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键
    limit_period = models.ForeignKey(LimitFile, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_files'
        ordering = ['upload_time']
        verbose_name = "files"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
