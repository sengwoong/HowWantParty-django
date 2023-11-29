from allauth.account.adapter import DefaultAccountAdapter
import uuid


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        # user_nick_name이 없는 경우에만 랜덤 값 생성
        if not request.data.get('user_nick_name'):
            user_nick_name = f'user_{str(uuid.uuid4())[:8]}'  # 랜덤 값 생성
        else:
            user_nick_name = request.data.get('user_nick_name')

        user = super().save_user(request, user, form, False)
        print("request.data.get('name')")
        print(request.data.get('user_nick_name'))
        user_field(user, 'profile_image', request.data.get('profile_image'))
        user_field(user, 'name', request.data.get('name'))
        user_field(user, 'user_nick_name', user_nick_name)
        user_field(user, 'user_classification', request.data.get('user_classification'))
        user_field(user, 'age', request.data.get('age'))
        user_field(user, 'gender', request.data.get('gender'))

        if commit:
            user.save()

        print("save_user2")
        return user
