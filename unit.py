import streamlit as st
st.title("🌍Unit Converter App")
st.markdown("### converts lenght,weight ans time Instantly")
st.write("WELCOME! select a category,enter a value and get the results")
category=st.selectbox("choose a category",["Lenght","Weight","Time"])
def convert_units(category,value,unit):
    if category == "Lenght":
        if unit == "kilometers to miles":
            return value*0.621371
        elif unit == "miles to kilometers":
            return value/0.621371
    elif category == "Weight":
        if unit == "kilogrames to pounds":
            return value*2.20462
        elif unit == "pounds to kilogrames":
            return value/2.20462
    elif category == "Time":
        if unit == "secands to minutes":
            return value/60
        elif unit == "minutes to secands":
            return value*60
        elif unit == "minutes to hours":
            return value/60
        elif unit == "hours to minutes":
            return value*60
        elif unit == "hours to days":
            return value/24
        elif unit == "days to hours":
            return value*24
if category == "Lenght":
    unit = st.selectbox("Select Conversation",["kilometers to miles","miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversation",["pounds to kilogrames","pounds to kilogrames"])      
elif category == "Time":
    unit = st.selectbox("Select Conversation",["secands to minutes","minutes to secands","minutes to hours","hours to minutes","hours to days","days to hours"])
                
value =st.number_input("Enterthe value to convert")
if st.button("converts"):
    results = convert_units(category,value,unit)
    st.success(f"The result is {results:.2f}")
               
                 
        
                 
                 
                     
