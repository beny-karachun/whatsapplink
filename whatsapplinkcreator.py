import streamlit as st



def whatsappAPImessage(message):
   return message.replace(" ","%20")
def whatsappAPInumber(number):
    return str("972" + str(number[1:].replace(r"-",r"")))
def whatsappAPIlink(number,message):
    
    return "https://wa.me/" + (whatsappAPInumber(number)) +  "?text=" + (whatsappAPImessage(message))

with st.container():
    st.title("Custom WhatsApp message URL")
    number = st.text_input("Enter your phone number")
    message = st.text_input("Enter your custom message")
    submit = st.button("Generate")
    if submit and message and number:
    st.success("Your custom link is: " + whatsappAPIlink(number,message))
    if submit and message and not(number):
        st.error("Fill out the number field!")
    elif submit and number and not(message):
        st.error("Fill out the message field!")

