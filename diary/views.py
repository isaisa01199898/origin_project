import time
from django.shortcuts import render, redirect
from django.views import View
from dotenv import load_dotenv
left_pupil_x = None
left_pupil_y = None
right_pupil_x = None
right_pupil_y = None
sensor_data = None
message=None
data_list=[]

response = None
from serpapi import GoogleSearch
import urllib.request
message_hito=None
from gtts import gTTS
import csv
import time

senosr_data = 80.95 
import numpy
# from .my_module.eye_object import data_get
def pitagorau(a,b):
    c2=a*a+b*b
    c2=numpy.sqrt(c2)
    print(c2)
    return c2
def handankyuu(r_x,r_y,l_x,l_y,sensor_data):
    r_long=pitagorau(r_x,r_y)
    l_long=pitagorau(l_x,l_y)
    dif = r_long - l_long 
    jude_box = "humei"
    if 80.8 <= sensor_data <= 81.1:                 #心拍が80.8から81.1の場合
        if all(-4 <= v <= 4 for v in [r_y, r_x, l_y, l_x]):
            jude_box = "focus"                      #集中している
        elif abs(dif) <= 3:                       #右と左の距離の差の雑多位置が3より小さかったら
            jude_box = "Notfocus"               #集中できていない
            if abs(l_x)>=5 :                      #左目のx座標が5以上なら
                jude_box="Notfocus"                    #集中している
                if abs(r_x) >= 7:                   #右目のX座標が７以上なら
                    jude_box="Notfocus"             #集中できていない
                    if abs(r_x)- abs(l_x) <= 4:     #両目のX座標が４以下なら
                        jude_box="Notfocus"         #集中している
    else:
        if  -4 <= r_y and r_x and l_y and l_x <=4 : #すべての目の座標が-3から3の範囲なら
            jude_box = "focus"                      #集中している
        elif 5 <= abs(l_x) <= 6:                    #左目のX座標が5以下6未満
            jude_box="focus"                        #集中している
        elif 10 <= abs(l_x) :                       #左目のX座標が10以上なら    
            jude_box="focus"                        #集中している
        else:                                       #なんでもなかったら
            jude_box="Notfocus"                     #集中できていない
    print(jude_box)
    return jude_box

from .forms import LoginForm # 追加
from django.contrib.auth.views import LoginView # 追加
from django.views import generic
import google.generativeai as genai
from .forms import TestForm, PageForm
from google import genai
from google.genai import types
def handan (l_x, sensor_data):
    if -0.15  <sensor_data <0.15 and 3 < abs(l_x) < 3  :
        jude_box = "focus"
        jude_box=1
        return jude_box  

    else:
        jude_box = "Notfocus"
        jude_box=0
# Load environment variables
load_dotenv()

GROQ_API_KEY = 'AIzaSyAcJIYLEK3aUww4J86BazAz9mE37GibTP0'
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



import subprocess

def run_program(port, filename):
    cmd = ["mpremote", "connect", port, "run", filename]
    subprocess.run(cmd)

from django.views import generic
from .forms import LoginForm
from django.shortcuts import redirect # 追加
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView # 追加
from django.contrib.auth import get_user_model # 追加
from django.contrib.auth.mixins import UserPassesTestMixin # 追加
from .forms import LoginForm, SignupForm # 追加
from django.shortcuts import redirect # 追加
from django.views import generic
global user

'''トップページ'''
class TopView(generic.TemplateView):
    global user
    template_name = 'diary/top.html'

'''サインアップ'''
class Signup(generic.CreateView):
    global user
    template_name = 'diary/user_form.html'
    form_class = SignupForm

    def form_valid(self, form):
        global user
        user = form.save() # formの情報を保存
        print(user.favorite_category)  # モデルにfavoritecategoryフィールドがあれば値が取れる
        return redirect('diary:signup_done')    
    
    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


'''サインアップ完了'''
class SignupDone(generic.TemplateView):
    global user
    template_name = 'diary/signup_done.html'

'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):

    raise_exception = True

    def test_func(self):
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
        user = request.user
        if user.is_authenticated:
            favorite = getattr(user, "favorite_category", None)
        else:
            favorite = None

        print("未ログイン")
        print(favorite)
        jude_box = "brain"
        # i=0
        # for i in range(5):

        #     r_y,r_x,l_y,l_x,sensor_data= None, None, None, None,None
        #     r_y_kyuu,r_x_kyuu,l_y_kyuu,l_x_kyuu,sensor_data_kyuu= None, None, None, None,None

        #     r_x, r_y, l_x, l_y, sensor_data=data_get()

        #     r_x_kyuu, r_y_kyuu, l_x_kyuu, l_y_kyuu, sensor_data_kyuu=data_get()

        #     r_x=r_x_kyuu-r_x
        #     r_y=r_y_kyuu-r_y
        #     l_x=l_x_kyuu-l_x
        #     l_y=l_y_kyuu-l_y
        #     sensor_data=sensor_data_kyuu-sensor_data
        #     jude_box=handan(l_x,sensor_data)
        #     if jude_box==1:
        #         data_list.append([jude_box])
        #     else:
        #         print("sippai2")
        #     distant=len(data_list)
        #     print(distant)
        #     print(f"data:{data_list}")
        #     print(distant)

            
        # if distant > 3:
        #     print(data_list)
        #     jude_box="focus"
        # elif 2 <= distant <3:
        #     print(data_list)
        #     jude_box="yayafocus"
        # elif 0 <= distant <1:
        #     print(data_list)
        #     jude_box="Notfocus"



    
        print("データ取得完了")
        print(user)
        favorite="スポーツ"
        jude_box="Notfocus"
        if jude_box =="Notfocus" :
            judebox = "集中していない"  # ← これを追加！
            r_y,r_x,l_y,l_x= None, None, None, None
            message="nasi"
            message_hito="nasi"
            client = genai.Client(api_key="AIzaSyAi541WuxVD8ZMb2YalkjCS90bjG2MspMk")
            grounding_tool = types.Tool(
                google_search=types.GoogleSearch()
            )

            # Configure generation settings
            config = types.GenerateContentConfig(   
                tools=[grounding_tool]
            )






            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f'勉強中に{judebox}人を励ます{favorite}にかんする名言を日本語で一つ挙げてください。（名言のみを上げよ）（情報はweb検索してください)',
                config=config,

            )
            message = response.text
            print(message)


            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f'「勉強中に{judebox}人を励ます{favorite}に関する名言を日本語で一つ挙げてください。」というプロンプトをべつのAIに送って帰ってきたのが{message}。これを言った人は誰ですか？必ず一言で答えなさい（日本語で）（{message}は一言一句あってなくてもいいから、近い言葉を言った誰かの名前を挙げて）（「誰々」みたいにひとことで）',
                config=config,

            )
            message_hito = response.text
            print(message_hito)
            
                # 四字熟語
            

            params = {
                "engine": "google_images",  # ← Google画像検索を指定
                "q": message_hito,
                "hl": "en",
                "gl": "us",
                "google_domain": "google.com",
                "api_key": "ad05af9e948cb95d6f4e2cf9082e6568a9a98682cc2374e6d218848cfaf46b0f"
            }

            search = GoogleSearch(params)
            results = search.get_dict()

            images_results = results.get("images_results", [])

            if images_results:
                first_img = images_results[0]
                first_img_url = first_img.get("original")
                print(first_img_url)
                if first_img_url:
                    print(first_img_url)
                    safe_url = first_img_url
                    save_path = r"C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/ground_v6.0.png"
                    urllib.request.urlretrieve(safe_url, save_path)
                    print("画像保存完了:", save_path)
                else:
                    print("eee")
            else:
                print("iie")





            text = f"{message}"
            tts = gTTS(text=text, lang='ja')
            tts.save("C:/Users/isami/OneDrive/Desktop/myproject/diary/static/diary/put.mp3") 
            bg_image = 'diary/white.png'
            bg_image = 'diary/ground_v6.0.png'
            run_program("COM6", "C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\user_program.py")

            box='diary/15.png'
            # Prepare context for rendering
            context = {
                'ser_data': ser_data,
                'form': TestForm(),
                'back_clor': '#FF0000',
                'insert_forms': '初期値',
                'message': message,
                'bg_image': bg_image,
                'message_hito':message_hito,
                'should_click':True,
                'box':box
            }


            return render(request, self.template_name, context)
        elif jude_box=="focus":

            r_y,r_x,l_y,l_x= None, None, None, None
            bg_image = ''

            box= 'diary/13.png'
            context = {
                'ser_data': ser_data,
                **sample_values,
                'form': TestForm(),
                'insert_forms': '初期値',
                'message': None,
                'back_clor': '#00bf63',
                'bg_image': '',
                'box': box,
            }
            return render(request, self.template_name, context)

        elif jude_box=="yayafocus":
            r_y,r_x,l_y,l_x= None, None, None, None

            box= 'diary/14.png'
            context = {
                'ser_data': ser_data,
                **sample_values,
                'form': TestForm(),
                'back_clor': "#E0F900",
                'insert_forms': '初期値',
                'message': None,
                'bg_image': '',
                'box': box,
            }
            return render(request, self.template_name, context)



        

    def post(self, request, *args, **kwargs):
        pass
        

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


