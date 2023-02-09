import streamlit as st

from PIL import Image 
img = Image.open("pp.jpeg")
st.sidebar.image(img)

st.title("Class Allocation Web")

username = st.text_input('Username')
age = st.number_input("How old are you?", step = 1)

if st.button("you are in"):
    print(age)
    
    if age > 11:
        st.write("Primary 5")
    elif 8 < age < 11:
        st.write("Primary 4")
    elif 6 < age < 8:
        st.write("Primary 3")
    elif 4 < age < 6:
        st.write("Primary 2")
    elif 2 < age < 4:
        st.write("Primary 1")
    else:
        st.write("Go to nursery section")
        