from django.http import HttpResponse

def my_view(request):
    user = request.user  # ログイン中のユーザー
    print(user.username)  # ユーザー名
    print(user.email)     # メールアドレス
    print(user.favorite_category)  # カスタムフィールドもOK
    return HttpResponse("ユーザー情報をコンソールに出力しました")