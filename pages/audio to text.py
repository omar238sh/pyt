import streamlit as st
import whisper as ws

def Transcripe():
    try:
        with open("file.mp3" , 'wb') as f:
            f.write(file)
        model = ws.load_model('large-v3')
        result = model.transcribe('file.mp3')['text']
        st.write(result)
    except:
        st.error('please check file')

file = st.file_uploader(label='choose audio file')
generate__text = st.button(label='Transcripe' , on_click=Transcripe)




