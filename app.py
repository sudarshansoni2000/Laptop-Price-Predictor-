import streamlit as st
import pickle
import numpy as np

pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

# Brand
company=st.selectbox('Brand',df['Company'].unique())

# type Of laptop
type=st.selectbox('Type Of Laptop',df['TypeName'].unique())

#RAM
ram=st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])

#Weight
weight=st.number_input('Weight Of Laptop')

#TouchScreen
touchscreen=st.selectbox('TouchScreen',['No','Yes'])

#IPS
ips=st.selectbox('IPS',['Yes','No'])

# ScrreSize
screen_size=st.number_input('Screen Size')

#Resolution
resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800',
                                             '2560x1600','2560x1440','2304x1440'])

#cpu

cpu=st.selectbox('Cpu Brand',df['Cpu brand'].unique())

#HDD
hdd=st.selectbox('HDD(in GB)', [0,128,256,512,1024,2048]  )

#SSD
ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024] )

#GPU
gpu=st.selectbox('Gpu Brand', df['Gpu brand'].unique())

# OS
os=st.selectbox('OS',df['OS'].unique())


if st.button('Predict Price'):
    #query=
    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])


    ppi= ((x_res**2) + (y_res**2))**0.5/screen_size

    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0

    if ips =='Yes':
        ips=1
    else:
        ips=0

    query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query=query.reshape(1,12)
    st.title("The predicted price of this configuration is-: "+str(int(np.exp(pipe.predict(query)[0]))))