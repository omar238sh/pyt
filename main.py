import streamlit as st
import pytube as pt
import os

st.header('Download YouTube videos')

url = st.text_input('YouTube URL video')


def is_youtubr_url(url):
    try:
        y = pt.YouTube(url)
        return True
    except:
        return False

if is_youtubr_url(url):
    col1,col2,col3,col4 = st.columns(4)
    col5,col6 = st.columns(2)

    file_type = col5.selectbox('Type',['video','audio'])

    if url != '':

        

        if file_type == 'video':
            streams = pt.YouTube(url).streams.all()
            streams2 = []

            for stream in streams:
                if stream.resolution not in streams2 and stream.resolution != None:
                    streams2.append(stream.resolution)
            

            quality = col6.selectbox('choose quality', streams2)
            stream = pt.YouTube(url).streams.filter(res=quality).first()
        elif file_type == 'audio':

            streams = pt.YouTube(url).streams.filter(only_audio=True).all()

            audio_qualities = [stream.abr for stream in streams if stream.type == "audio"]
            quality = col6.selectbox('choose quality' , audio_qualities)
            stream = pt.YouTube(url).streams.filter(only_audio=True,abr=quality).first()
    genrate = st.button('generate')

    if genrate:
        stream.download()
        file = open(stream.default_filename,'rb')
        st.download_button('download',file,file_name=stream.default_filename)
        file.close()
        os.remove(stream.default_filename)
else:
    st.warning('please youtube only')