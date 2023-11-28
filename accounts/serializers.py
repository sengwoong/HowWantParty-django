
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


    

# class CustomRegisterSerializer(RegisterSerializer):
#     # phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
#     # phone_number = serializers.CharField(validators=[phoneNumberRegex],help_text="휴대폰 번호는 다음과 같은 형식을 따라야 합니다: 010-1234-5678")
#     # date_of_birth = serializers.DateField()

#     def save(self, request):
#         print("CustomRegisterSerializer.self.__dict__")
#         print("CustomRegisterSerializer.self.__dict__")
#         print("CustomRegisterSerializer.self.__dict__")
#         print(self.__dict__)
#         user = super().save(request)
#         user.profile_image = self.data.get('profile_image')
#         user.user_id = self.data.get('user_id')
#         user.name = self.data.get('name')
#         user.user_nick_name = self.data.get('user_nick_name')
#         user.user_classification = self.data.get('user_classification')
#         user.age = self.data.get('age')
#         user.gender = self.data.get('gender')
#         user.save()
#         print("user")
#         print(user)
#         return user
    

