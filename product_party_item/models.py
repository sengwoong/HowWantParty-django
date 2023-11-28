from django.db import models
from django.conf import settings

class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    index = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    location_x = models.CharField(max_length=100)
    location_y= models.CharField(max_length=100)

class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, related_name='product_id', on_delete=models.CASCADE)
    image = models.CharField(max_length=100,blank=True, null=True)


def user_directory_path(instance, filename):
    # 현재 날짜를 년/월/일 형태로 얻습니다.
    date_now = datetime.datetime.now().strftime('%Y/%m/%d')

    # 파일 확장자를 얻습니다.
    ext = filename.split('.')[-1]

    # 파일명을 UUID hex 형태로 설정합니다.
    filename = f'{uuid.uuid4().hex}.{ext}'

    # 경로를 'appname/modelname/년/월/일/uuid.ext' 형태로 설정합니다.
    return f'{instance._meta.app_label}/{instance._meta.model_name}/{date_now}/{filename}'
