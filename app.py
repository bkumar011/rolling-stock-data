import streamlit as st
import datetime

st.title("Vaccination Data")
st.write("Enter Vaccine information")


id=st.text_input("ID", value="Enter ID",max_chars=10)

text=st.text_area("Enter Info", "Enter here")

n = st.number_input("Age", min_value=10, max_value=50, step = 1)

birth_date = st.date_input("Date of Birth", min_value=datetime.date(1950,1,1), max_value=datetime.date(2022,1,1))

smoke = st.checkbox("Do you smoke?")

wing=st.radio("Department", options=['Coaching','Workshop','Freight','Planning'])

physical_form = st.selectbox("Select level of your physical condition",
                             options=["Bad", "Normal", "Good"])
colors = st.multiselect('What are your favorite colors',
                        options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])


image = st.file_uploader("Upload your photo", type=['jpg', 'png'])

submit = st.button("Submit")

if submit:
    st.write("You submitted the form")

click = st.sidebar.button('Click me!')
if click:
    st.sidebar.write("You clicked the button")