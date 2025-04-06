import streamlit  as  st

 
st.title("🌍unit converter App")
st.markdown("### converts length, weight And Time Instantly")
st.write("welcome! select a category,enter a value and get the converted result in real-time")

category = st.selectbox("choose a categoty",["Lenght","Weight","Time"])

def convert_unites(category,value,unit):
    if category =="Lenght":
        if unit == "Kilometers to Miles":
            return value * 0.6213371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
        elif category == "weight":
            if unit == "kilograms to pounds":
                return value / 2.20462
            elif unit == "pounds to kilograms":
                return value / 2.20462
        elif category =="Time":
            if unit == "seconds to minutes":
                return value / 60 
            elif unit == "Minutes to seconds":
                return value * 60 
            elif unit == "minutes to hours":
                return value / 60
            elif unit == "hours to minutes":
                return value * 60
            elif unit == "hours to days":
                return value /24 
            elif unit == "Days to hours":
                return value * 24
            
if category ==   "Lenght":
    unit = st.selectbox("🎞Select conversation",["Miles to Kilometers","kilometers to Miles",])
elif category == "Weight":
    unit =st.selectbox("⚖️Select conversation",["kilograms to pounds","pounds to kilograms"])
 
value = st.number_input("Enter the value to convert")

if st.button("convert"):
    result = convert_unites(category, value,unit)             
    st.success(f"The result is {result:2f}")    







