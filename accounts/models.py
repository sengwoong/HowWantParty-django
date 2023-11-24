from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager
import uuid
from datetime import datetime


# GENDER_CHOICES 상수
GENDER_OPTIONS = [
    ('male', '남자'),
    ('female', '여자'),
]

# USER_CLASSIFICATION_OPTIONS 상수
USER_CLASSIFICATION_OPTIONS = [
    {"PartyLeader", "파티장"},
    {"Member", "회원"},
    {"Seller", "판매자"},
]

# AGE_OPTIONS 상수
AGE_OPTIONS = [
    (0, 'none'),
    (10, '10'),
    (20, '20'),
    (30, '30'),
    (40, '40'),
    (50, '50'),
    (60, '60'),
    (70, '70+'),
]


def user_directory_path(instance, filename):
    # 현재 날짜를 년/월/일 형태로 얻습니다.
    date_now = datetime.now().strftime('%Y/%m/%d')

    # 파일 확장자를 얻습니다.
    ext = filename.split('.')[-1]

    # 파일명을 UUID hex 형태로 설정합니다.
    filename = f'{uuid.uuid4().hex}.{ext}'

    # 경로를 'appname/modelname/년/월/일/uuid.ext' 형태로 설정합니다.
    return f'{instance._meta.app_label}/{instance._meta.model_name}/{date_now}/{filename}'

#AbstractUser
class CustomUser(AbstractUser, PermissionsMixin):
    profile_image = models.ImageField(upload_to=user_directory_path ,
                                      default='static/images/default_gray.png',)
    user_id = models.CharField(max_length=255, unique=True,default='')
    name = models.CharField(max_length=100, null=True)
    user_nick_name = models.CharField(max_length=150, unique=True)

    user_classification = models.CharField(max_length=50, choices=USER_CLASSIFICATION_OPTIONS, default="Member")
    age = models.IntegerField(choices=AGE_OPTIONS, default=0)
    gender = models.CharField(max_length=6, choices=GENDER_OPTIONS)
    objects = CustomUserManager()

    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # user_nick_name이 없는 경우에만 설정
        if not self.user_nick_name:
            self.user_nick_name = f'user_{str(uuid.uuid4())[:8]}'  # 랜덤 값 생성

        # user_id가 null이면 롤백
        if self.user_id is None:
            raise ValueError('user_id cannot be null.')

        super().save(*args, **kwargs)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_image'] = self.validated_data.get('profile_image', '')

        return data
    

#     {
#       "id": "aas,
#     "password1": "asdsadasd",
#     "password2": "asdsadasd"
#   "name": "Sample User",
#   "username": "sample_username",
#   "email": "sample@example.com",
#   "UserClassification": "Member",
#   "age": 20,
#   "gender": "female"
# }


