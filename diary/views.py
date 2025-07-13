
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

from diary.my_module import eye_object
from diary.gaze_tracking import GazeTracking
import diary.gaze_tracking.tracking as gt

from gtts import gTTS

import time

from .forms import LoginForm # 追加
from django.contrib.auth.views import LoginView # 追加
from django.views import generic
import google.generativeai as genai
import random
from .forms import TestForm, PageForm
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Load environment variables
load_dotenv()

GROQ_API_KEY = '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'
data = []
#ーー変数一覧ーー#
text=None
datatime = None
left_x_box=[]
left_y_box=[]
right_x_box=[]
right_y_box=[]
left_eye_x=[]
left_eye_y=[]
eye_data = []
right_eye_x=[]
right_eye_y=[]
flat_list_left_x=[]
flat_list_left_y=[]
flat_list_right_x=[]
flat_list_right_y=[]
left_pupil_x = None
left_pupil_y = None
right_pupil_x = None
right_pupil_y = None
text = None
s= -1
m=8
line=''
i=3
data=[]
left_pupil = None
right_pupil = None
sor_data = 0.0
i=40
b=""
rine = 0.0
jude =""
sensor_data=""#心拍数のデータ
gaze_data = None
gaze= None
count=0
kigou=""#目線での判定結果
#ーー変数一覧ーー#
#modele= ["#class tracking_eyeye     eye = eye_tracking()     webcam = cv2.VideoCapture(0)     if not webcam.isOpened():         print("未接続")         exit()        while True:         i = 0         _, frame = webcam.read()         print(frame.shape, frame.dtype)         # 確認         eye.refresh(frame)                print("frame before refresh:", frame.shape, frame.dtype)            # 顔＋瞳に十字線を描画した結果を取得         frame = eye.annotated_frame()            text = " "            # 状態テキスト         text = ""         if eye.is_blinking():             text = "Blinking"         elif eye.is_right():             text = "Looking right"         elif eye.is_left():             text = "Looking left"         elif eye.is_center():             text = "Looking center"         cv2.putText(frame, text, (90, 60),                     cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)            # 瞳の座標を描画         left_pupil = eye.pupil_left_coords()         right_pupil = eye.pupil_right_coords()         cv2.putText(frame, "Left pupil:  " + str(left_pupil),                     (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)         cv2.putText(frame, "Right pupil: " + str(right_pupil),                     (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)         print(f"左目の座標：{left_pupil}")         print(f"右目の座標：{right_pupil}")         now = datetime.datetime.now()         with open('log.txt', 'a', encoding='UTF-8') as f:               f.write(f'リアルタイム: {now.strftime("%Y-%m-%d %H:%M:%S")} 左目の座標：{left_pupil} 右目の座標：{right_pupil}\n')                                                                        cv2.imshow("Demo", frame)                    # Escで終了         if cv2.waitKey(1) & 0xFF == 27:                 break        webcam.release()     cv2.destroyAllWindows() "]
    

#ーー変数一覧ーー#





from django.views import generic
from .forms import LoginForm
from django.shortcuts import redirect # 追加
from django.contrib.auth.views import LoginView, LogoutView # 追加
from django.contrib.auth import get_user_model # 追加
from django.contrib.auth.mixins import UserPassesTestMixin # 追加
from .forms import LoginForm, SignupForm # 追加
from django.shortcuts import redirect # 追加

from django.views import generic


'''トップページ'''
class TopView(generic.TemplateView):
    template_name = 'diary/top.html'

'''サインアップ'''
class Signup(generic.CreateView):
    template_name = 'diary/user_form.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('diary:signup_done')
    
    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''
class SignupDone(generic.TemplateView):
    template_name = 'diary/signup_done.html'

user=None
'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']
    
User = get_user_model()


'''マイページ'''
class MyPage(OnlyYouMixin, generic.DetailView):

    model = User
    template_name = 'diary/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される







class Logout(LogoutView):
    template_name = 'diary/logout_done.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'diary/login.html'

liking ="受験・試験が近づいている学生を勇気づける名言（説明はなしで）（現代人に限らないでよい）"
ser_data = 40
sample_values = {
    'data1': 100,
    'data2': 40,
    'data3': 50,
    'data4': 60,
    'data5': 30,
    'data6': 88,
    'data7': 68,
}

# ユーザーに返す形式: 1=四字熟語, 2=音楽, 3=history, 4=格言


class Login(LoginView):
    form_class = LoginForm
    template_name = 'diary/login.html'

# --- Main view for index ---
class IndexView(View):
    template_name = "C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\diary\\templates\\diary\\index.html"

    def get(self, request):
        # Initial render without AI message
        context = {
            'ser_data': ser_data,
            **sample_values,
            'form': TestForm(),
            'insert_forms': '初期値',
            'message': None,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
            message_hito = None
            #sinpakusuuyomitori
            # ser = serial.Serial('com3',9600)
            # line=''
            # i=0
            # data=[]
            # while len(data)<3:     #forではできない
            #     line = ser.readline().decode('utf-8').strip()
            #     data.append(line)

            
            #     print(data)
            # ser.close()
            # try:
            #     sensor_data = float(data[-1])
            #     print(f"{sensor_data}")
            # except :
            #     sensor_data = None
            #     print("you lose")
            sensor_data = 78  # Simulated sensor data for testing
            # Simulate sensor data
            # sensor_data,left_pupil_x,left_pupil_y,left_pupil,right_pupil_x,right_pupil_y,right_pupil,time_now = eye_object.data_get()
            # print(sensor_data,left_pupil_x,left_pupil_y,left_pupil,right_pupil_x,right_pupil_y,right_pupil,time_now)
            print("start")
            sensor_data=78
            print(f"{sensor_data}")
            judebox = None
            message = None
            sensor_data=sensor_data/2
            
            if sensor_data is not None:
                if 75 < sensor_data < 85:
                    judebox = "集中できる"



            client = genai.Client(api_key="AIzaSyCcDqS18vRebeRB8t8f4s-i8kFYElq_m1I")

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f'勉強中に{judebox}人を励ます{liking}を日本語で一つ挙げてください。（情報はweb検索してください)',
            )
            message = response.text
            print(message)


            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f'「勉強中に{judebox}人を励ます{liking}を日本語で一つ挙げてください。」というプロンプトをべつのAIに送って帰ってきたのが{message}。これを言った人は誰ですか？（日本語で）（{message}は一言一句あってなくてもいいから、近い言葉を言った誰かの名前を挙げて）（「誰々」みたいにひとことで）',
            )
            message_hito = response.text
            print(message_hito)
            
                # 四字熟語
            



            contents = (f"{message_hito}（横画面）")  #画像を生成するためのプロンプト

            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",  #モデルの指定
                contents=contents,
                config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
                )
            )

            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    print(part.text)
                elif part.inline_data is not None:
                    image = Image.open(BytesIO((part.inline_data.data)))
                    image.save('C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/ground_v2.0.png')
                    image.show()
            # client = OpenAI(
            # api_key="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"
            # )

            # completion = client.chat.completions.create(
            # model="gpt-4o-mini",
            # store=True,
            # messages=[
            #     {"role": "user", "content": f"{message}はあなたとは違うAIに、「勉強中に{judebox}人を励ます{liking}を一つだけ挙げてください。（名言・格言関係の場合は、誰が言ったのか、何時代に行ったのかもお願い。）(その言葉の説明も入れて)（簡単に、「名言」いった人  説明 の形で）（嘘をついたりせず、WEBを検索して出力して）（勉強に集中できない人を励ますように）（自分で考えずにネットで調べて）（日本語で）」とプロンプトを送ったらかえってきた文章です。間違いがあったら修正してください。日本語でお願いします。"}
            # ]
            # )
            # message=completion.choices[0].message.content


            text = f"{message}"
            tts = gTTS(text=text, lang='ja')
            tts.save("C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/output.mp3") 
            bg_image = 'diary/white.png'
            if request.method == 'POST' and request.POST.get('change_bg') == '1':
                bg_image = 'diary/ground_v2.0.png'


            # Prepare context for rendering
            context = {
                'ser_data': ser_data,
                'form': TestForm(),
                'insert_forms': '初期値',
                'message': message,
                'bg_image': bg_image,
                'message_hito':message_hito,
            }
            time.sleep(10)

            return render(request, self.template_name, context)


# --- Page creation view ---
class PageCreateView(View):
    def get(self, request):
        return render(request, 'diary/prompt.html', {'form': PageForm()})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary:index')
        return render(request, 'diary/prompt.html', {'form': form})


# URL configuration
index = IndexView.as_view()
prompt = PageCreateView.as_view()


