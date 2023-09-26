import streamlit as st 
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import pandas as pd 

st.set_page_config(page_title=" CyberSecurity Website",page_icon="GHOST",layout = 'wide')
st.markdown(
    """
<style>
.css-6q9sum.ef3psqc3
{
  visibility: hidden;
}
.css-10pw50.ea3mdgi1
{
visibility : hidden;
}
</style>""",unsafe_allow_html=True)
st.title("Feel Safe")
st.header("Cyber Security Website")

st.markdown("# Admin *CRYPTO*")
# st.markdown('[Google](https://www.google.com)')
st.markdown('---')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://lottie.host/ee843e00-d9b7-4155-92b6-1ec4fed3ead6/E5W8RPu27W.json")
lottie_coding1 = load_lottieurl("https://lottie.host/9c58cf82-061b-4d3d-ac87-537b1dd0b008/7xK6hzgt5G.json")
lottie_coding2 = load_lottieurl("https://lottie.host/f85bc4e8-d786-4f06-b1ec-a756cf90b8e5/EhKFD6nlyr.json")
with st.container():
    right_column,left_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding,height=300,key="coding")
        st_lottie(lottie_coding1,height=300,key="coding1")
        st_lottie(lottie_coding2,height=300,key="coding2")
    with right_column :
        
        st.header("Welcome to Feel Safe")
        st.markdown("---")
        st.write(
    """
# This website is created to provide information about cyber security  and how it can be prevented or
# mitigated in order for users of the internet to feel safe while browsing online on various websites and applications..
""")

        st.write("##")

json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)

code ="""
print("Hello World ")
def func():
   return 0;
"""
st.code(code,language="python")
st.write('# What we offer ')
st.write(
    """"
    We have a wide range of services that include web designing, development, hosting solutions etc., We
    
    
    
         """)
st.metric(label="Wind Speed",value="120ms⁻¹",delta="-1.4ms⁻¹")



table = pd.DataFrame({"Column 1":[1,2,3,4,5,6] , "Column 2 ":[7,8,9,10,11,12]})
st.table(table)

def change():
    print(st.session_state.checker)
state = st.checkbox("CheckBox",value=True,on_change=change,key = "checker")
if state:
    st.write("[terms and Condition](https://www.opentext.com.br/file_source/OpenText/en_US/PDF/opentext-it-security-terms-and-conditions-en.pdf)")
else:
    pass

radio_btn = st.radio("In which Country Do you live in ? ",options= ("US","Pak","UK"))
def btn_click():
    print("Button Clicked !")
butt = st.button("Click Me",on_click=btn_click)
print(butt)
select = st.selectbox("Whats Your Favourite Car " ,options = ("Audi","BMW","Ferrari"))
print(select)
date = st.date_input('Pick a Date')
mult_sel= st.multiselect("Whats Your Favourite tech Brand ? " ,options = ("Microsoft","Apple","Oracle","Amazon"))   
st.write(mult_sel)
st.slider('Rate My Website', min_value=0, max_value=10)
images =st.file_uploader("Please upload an Image ",type = ["jpg","png","jpeg"],accept_multiple_files=True)
if images is not None:
    for image in images:
      st.image(image)
      



