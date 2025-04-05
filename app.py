. #streamlit
import streamlit as st 

st.set_page_config(page_title= "growth mindset project",project_icon="⭐")   
st.title("Growth Mindset challenge: web app with streamlit ")

st.header("🚀welcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.this AI-powered app helps you build a growth mindset with reflection,challenges,and achievement!")

#quote section 
st.header("💡today's Growth Mindset Quote")
st.write("success is not final, failure is not fatal: it is the courage to continue that counts._winston chirchill")

st.header("🏚️what's your challenge today?")
user_input = st.text_input("describe a challenge you're facing:")


#condition
if user_input:
    st.sucess(f"🖖 you' re facing:{user_input}. keep pushing forward toward your goal!")
else:
    st.warning("Tell us about your challenge to get started!")
        
#reflexing
st.header("Reflect on your learning")
reflection = st.text_area("write your reflections here:")

if reflection:
    st.sucess(f"Great insight! your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")



#acheivements    
st.header("Celebrate your wins!")
acheivment = st.text_input("share something you' ve recently accomlished:")

if acheivment:
    st.success(f"Amazing! you achieved:{acheivment}")
else:
    st.info("Big or small , every achievement count! share one now")   


#footer
st.write("- - - ") 
st.write("keep believing in yourself. Growth is a journey, not a destination!") 
st.write("created by Sallu Aqib khan**")
