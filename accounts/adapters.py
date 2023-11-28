
from allauth.account.adapter import DefaultAccountAdapter



class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'profile_image', request.data.get('profile_image'))
        user_field(user, 'user_id', request.data.get('user_id'))
        user_field(user, 'name', request.data.get('name'))
        user_field(user, 'user_nick_name', request.data.get('user_nick_name'))
        user_field(user, 'user_classification', request.data.get('user_classification'))
        user_field(user, 'age', request.data.get('age'))
        user_field(user, 'gender', request.data.get('gender'))

        user.save()
        return user