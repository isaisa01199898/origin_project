from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model # ユーザーモデルを取得するため
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django import forms
from .models import Diary

class TestForm(forms.Form):
    user_input = forms.CharField(label='入力', max_length=100)

class PageForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'body', 'diary_date']
User=get_user_model()  # ユーザーモデルを取得するための関数
'''サインアップ用フォーム'''
class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email','favorite_category','username',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = '' # 全フィールドを入力必須
            
            # オートフォーカスとプレースホルダーの設定
            print(field.label)
            if field.label == '姓':
                field.widget.attrs['autofocus'] = '' # 入力可能状態にする
                field.widget.attrs['placeholder'] = '田中'
            elif field.label == '名':
                field.widget.attrs['placeholder'] = '一郎'
            elif field.label == 'メールアドレス':
                field.widget.attrs['placeholder'] = '***@gmail.com'
            elif field.label == '好きなカテゴリ':
                field.widget.attrs['placeholder'] = '音楽or映画orゲームorスポーツ'



# ユーザーモデル取得
User = get_user_model()


'''ログイン用フォーム'''
class LoginForm(AuthenticationForm):

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
