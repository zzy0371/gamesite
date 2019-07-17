from django.db import models

# Create your models here.
class Ads(models.Model):
    image = models.ImageField(verbose_name='轮播图', upload_to='ads')
    desc = models.CharField(verbose_name='描述',max_length=20,blank=True,null=True)
    url = models.URLField(verbose_name='连接地址',null=True,blank=True)

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

class HotGame(models.Model):
    image = models.ImageField(verbose_name='主图',upload_to='hotgame')
    title = models.CharField(verbose_name="标题",max_length=20)
    desc = models.CharField(verbose_name="描述",max_length=50)
    url = models.URLField(blank=True,null=True)
    class Meta:
        verbose_name = '热门推荐游戏'
        verbose_name_plural = verbose_name

class GameVideo(models.Model):
    image = models.ImageField(verbose_name='主图',upload_to='gamevideo')
    video = models.FileField(verbose_name='视频',upload_to='gamevideo')
    title = models.CharField(verbose_name='标题',max_length=20)
    desc = models.CharField(verbose_name='描述',max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '游戏视频'
        verbose_name_plural = verbose_name

class Culture(models.Model):
    image = models.ImageField(verbose_name='主图',upload_to='culture')
    title = models.CharField(verbose_name='标题',max_length=20)
    desc = models.CharField(verbose_name='描述',max_length=250)
    class Meta:
        verbose_name = '公司文化'
        verbose_name_plural = verbose_name

class Life(models.Model):
    image = models.ImageField(verbose_name='主图',upload_to='life')
    title = models.CharField(verbose_name='标题',max_length=20)
    desc = models.CharField(verbose_name='描述',max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '生活'
        verbose_name_plural = verbose_name

class Recommend(models.Model):
    image = models.ImageField(verbose_name='主图',upload_to='recommend')
    title = models.CharField(verbose_name='标题',max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=250)
    class Meta:
        verbose_name = '推荐'
        verbose_name_plural = verbose_name

POSITION_TYPE = ((1,"技术"),(2,"策划"),(3,"美术"),(4,"市场"),(5,"运营"),(6,"品测"),(7,"行政"),)
class Position(models.Model):
    name = models.CharField(verbose_name="职位名称",max_length=20)
    type = models.IntegerField(choices=POSITION_TYPE,default=1)
    time = models.CharField(verbose_name='工作性质',max_length=20,default="全职")
    where = models.CharField(verbose_name='工作地点',max_length=20,default="郑州")
    num = models.IntegerField(verbose_name='招聘人数',default=100)
    pub_time = models.DateTimeField(verbose_name='发布时间',auto_now_add=True)
    duty = models.CharField(verbose_name='职责',max_length=500)
    require = models.CharField(verbose_name='任职要求',max_length=500)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '岗位表'
        verbose_name_plural = verbose_name

class Work(models.Model):
    title = models.CharField(max_length=30)
    qq = models.CharField(max_length=20)
    class Meta:
        verbose_name = '商务合作'
        verbose_name_plural = verbose_name


