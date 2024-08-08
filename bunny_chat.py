import streamlit as st
import time as t
import PIL.Image as PI
import google.generativeai as genai
import random
import pyautogui as p
import speech_recognition as sr
import gtts
import face_recog as face_
import googlesearch as g
import datetime
import mysql.connector
import time as tt
try:
  import google_open
  import bunny_lang
  import pywhatkit
except Exception as e:
  print("Error :",e)
time=datetime.datetime.now()
#st.write(time)
class sql_:
 def __init__(self):
  self.con = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='bunny',
    auth_plugin='mysql_native_password'
  )
  self.cursor=self.con.cursor()
  self.cursor.execute('use chat_history;') 
  self.cursor.execute('select * from store_chat;')
  data=self.cursor.fetchall()
  if len(data)>=30:
    self.cursor.execute('Delete from store_chat order by date_ limit {}'.format(len(data)-30))
    self.con.commit()
  #cursor.execute('show tables;')
 def history_sql(self,input,output):
  input=input.replace("'",'')
  output=output.replace("'",'') 
  data="Insert into store_chat (Input,Anwser,date_) values('{}','{}','{}');".format(input,output,time)
  self.cursor.execute(data)
  self.con.commit()
 def show(self):
   st.markdown(':blue-background[The search data will be deleted automatically after reaching a length of 30]')
   self.cursor.execute('select * from store_chat;')
   for i,j,k in self.cursor.fetchall()[::-1]:
      random.choice(l)(f"'Input ({k}) : \n {i}")  
      random.choice(l)(f"'Anwser : \n {j}")
sql=sql_()   
   
 
button_css = """
    <style>
        .stButton {
            background-color: white; 
            color: green; 
            border-radius: 5px; 
        }
        body {
        background-color: blue;
        }
    </style>
"""
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f0f0f0; /* Change this to your desired color */
    }
    
    </style>
    """, unsafe_allow_html=True)
try:  
  cap_=0;a=1
  st.markdown(button_css, unsafe_allow_html=True)
  st.title("Chat With Bunny ")
  st.header("Chat Here:")
  api='AIzaSyCBHTmgKXbiputUhfU9PlFUufQYVGqsMHs'
  genai.configure(api_key=api)
  
  model = genai.GenerativeModel('gemini-pro') 
  img_model=genai.GenerativeModel('gemini-1.5-flash')
  chat=model.start_chat(history=[])
  l=[st.write,st.success,st.warning,st.info]
  if 'History' not in st.session_state:
     st.session_state['History']=[]
  choice=st.selectbox(" ",("Select the following option :  ",'Present Chat','History of chat','both previous and present chat',"Know about the Image",'Exit'))
  if choice=='both previous and present chat':
     for i,j in st.session_state['History']:
      random.choice(l)(f"{i} : \n {j}")
     chat_c=st.radio(" ",("text","speak"))
     if(chat_c=="speak"):
       with sr.Microphone() as mic:
          random.choice(l)("Speak:")
          sound=rec.listen(mic)
          text_rec=rec.recognize_google(sound)
          random.choice(l)("IS this your Text   :   "+text_rec)
          random.choice(l)(" If not try again by pressing the button again")
          input_text=text_rec
     if chat_c=="text":
         input_text=st.text_area("Type your Querry Here :",height=100)
     #if (st.button('Search your Querry')):
     if (input_text):
      response = chat.send_message(input_text)
      with st.spinner("Finding your Querry"):
       t.sleep(8)
      if ("Input",) not in st.session_state['History']:
       sql_input=input_text
       st.session_state['History'].append(("Input",input_text))
      st.header("Your response:")
      for i in response:
       random.choice(l)(i.text)
       to_speak=i.text
       if ("Anwser",) not in st.session_state['History']:
        sql.history_sql(sql_input,i.text)
        st.session_state['History'].append(("Anwser",i.text))
       try:
        st.header("Relevant video link")
        st.write(pywhatkit.playonyt(input_text,open_video=False))
       except Exception:
         pass
       for _ in range(5):
        try:
         query=input_text
         g_s=g.search(query,5)
         for j in g_s:
          st.write(j)
         break
        except Exception:
          pass
  
  if (choice=="Present Chat"):
    while 1:
     chat_c=st.radio(" ",("text","speak"))
     if(chat_c=="speak"):
       rec=sr.Recognizer()
       with sr.Microphone() as mic:
          random.choice(l)("Speak:")
          sound=rec.listen(mic)
          text_rec=rec.recognize_google(sound)
          random.choice(l)("IS this your Text   :   "+text_rec)
          random.choice(l)(" If not try again by pressing the button again")
          input_text=text_rec
     if chat_c=="text":
         input_text=st.text_area("Type your Querry Here :",height=100)
     #if (st.button('Search your Querry')):
     if (input_text):
      response = chat.send_message(input_text)
      with st.spinner("Finding your Querry"):
       t.sleep(8)
  
      sql_input=input_text
      st.session_state['History'].append(("Input",input_text))
      st.header("Your response:")
      order=0
      for i in response:
       random.choice(l)(i.text)
       to_speak=i.text
       #if ("Anwser",i.text) not in st.session_state['History']:
       st.session_state['History'].append(("Anwser",i.text))
       sql.history_sql(sql_input,i.text)
       order=1
      if order:
       choice_trans=st.selectbox(" ",('Select the language:(if you want output in another language)','Telugu','Hindi','Marati','Tamil','Kannada','Spanish'))
       to=None
       if choice_trans=='Telugu':to='te'
       if choice_trans=='Hindi':to='hi'
       if choice_trans=='Marati':to='mr'
       if choice_trans=='Tamil':to='ta'
       if choice_trans=='Kanada':to='kn'
       if choice_trans=='Spanish':to='es'
       if to:
        st.write(bunny_lang.trans(to_speak,to))
       try:
        st.header("Relevant video link")
        st.write(pywhatkit.playonyt(input_text,open_video=False))
        if st.button("geting information in google"):
          pywhatkit.search(input_text)
       except Exception:
         pass
       try:
        query=input_text
        g_s=g.search(query,num_results=5)
        for j in g_s:
          st.write(j)
       except Exception as e:
          j=str(e)[45:]
          st.write(j)
          #random.choice(l)("sorry,I can't found a link")
       sound_text=gtts.gTTS(to_speak,lang="en",slow=False)
       sound_text.save("chat_speak.mp3")
       random.choice(l)("To listen the output play audio:")
       st.audio("chat_speak.mp3")
  if(choice=="History of chat"):
    #for i,j in st.session_state['History']:
    sql.show()
  if (choice=='Exit'):
    st.warning('Press the Button to exit')
    st.balloons()
    t.sleep(2)
    if (st.button("Exit")):
     p.hotkey("Alt","f4")
  if(choice=="Know about the Image"):
    flag=0
    img__=st.radio("",("From Device","Capture from camera"))
    if img__=="From Device":
      img_name=st.file_uploader("Upload the file")
      if img_name != None:
        img=PI.open(img_name)
        flag=100
    elif img__=="Capture from camera":
      if cap_==0:
        cap_=face_.face(a)
      if cap_ ==100:
        img=PI.open("bunny_cap.jpg")
        flag=100
    if flag==100:
     st.image(img)
     chat_c=st.radio(" ",("text","speak"))
     if(chat_c=="speak"):
       with sr.Microphone() as mic:
          random.choice(l)("Speak:")
          sound=rec.listen(mic)
          text_rec=rec.recognize_google(sound)
          random.choice(l)("IS this your Text   :   "+text_rec)
          random.choice(l)(" If not try again by pressing the button again")
          input_text=text_rec
     if chat_c=="text":
         a=0
         input_text=st.text_input("Describtion of the picture","")
         #st.error("It is optional")
     if (input_text):
      st.header('Details about image')
      response = img_model.generate_content([input_text,img])
      
      with st.spinner("Finding your Querry"):
       t.sleep(2)

      st.header("Your response:")
      def g():
        text= response.text
        for i in text:
          yield i
          tt.sleep(0.02)
      st.write_stream(g)
      if 1:
       to_speak=i.text
       sound_text=gtts.gTTS(to_speak,lang="en",slow=False)
       sound_text.save("chat_speak.mp3")
       random.choice(l)("To listen the output play audio:")
       st.audio("chat_speak.mp3")
except Exception as e:
  st.warning(e)
