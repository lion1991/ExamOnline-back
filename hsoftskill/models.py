from django.db import models

# Create your models here.
from user.models import Student
from django.db import models

class Files(models.Model):
    """
    用户上传的文件
    """
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='文件名称', max_length=200, help_text='文件名称')
    period = models.IntegerField(verbose_name='考核期数', help_text='考核期数')
    # upload_to 会生成指定路径文件夹，文件会保存在其中，如果文件名称重复则会自动添加后缀
    file = models.FileField(upload_to="upload/%Y%m%d/")
    upload_time = models.DateTimeField("上传时间", auto_now_add=True)
    finger = models.CharField(verbose_name='浏览器指纹', max_length=200, help_text='浏览器指纹')

    uploader = models.ForeignKey(Student, on_delete=models.CASCADE) #多对一外键

    class Meta:
        db_table = 'tb_files'
        ordering = ['upload_time']
        verbose_name = "files"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




