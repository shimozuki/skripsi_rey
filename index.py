from cProfile import label
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, euclidean_distances
from sklearn import metrics
import streamlit as st
from math import sqrt

st.title('Aplikasi Perbandingan Sistem Pakar Metode CBR Dan Data Mining Metode K-NN')
data_acuan = pd.read_excel('data_rey.xlsx')
st.subheader('Retrieval')
st.write('proses retrieval menggunakan algoritma K-Nearest Neighbour dengan nilai K = 5 ')
st.write('perhitungan distance menggunakan minkowski')
st.write('indexing yang digunakan adalah KD Tree')
X = data_acuan.drop(columns=['Kecanduan','No', 'Narkoba'])
y = data_acuan['Kecanduan']
z = data_acuan['Narkoba']
classifier = KNeighborsClassifier(n_neighbors = 5, algorithm='kd_tree', metric = 'euclidean', p = 2)
classifier = classifier.fit(X,y)
#pertanyaan
def morfin():
    jawaban1 = st.radio(
                "1. Seberapa Sering Anda Berkeringat ?",
                ('tidak pernah', 'Kadang-kadang', 'sering'))
    jawaban26 = st.radio(
               "2. Seberapa sering Anda Merasa Kebingungan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
    jawaban3 = st.radio(
               "3. Seberapa Sering Anda Suasana Suasana hati berubah ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
    jawaban4 = st.radio(
               "4.Seberapa sering Anda Merasa Mulut Kering?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
    jawaban5 = st.radio(
               "5. Seberapa sering Anda Merasa Tidak Nafsu Makan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
    jawaban7 = st.radio(
               "6. Seberapa sering Anda Merasa Nafas Menjadi Pendek?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
    data = {
          'C01' : jawaban1,
          'C02' : '0',
          'C03' : jawaban3,
          'C04' : jawaban4,
          'C05' : jawaban5,
          'C06' : 'tidak pernah',
          'C07' : jawaban7,
          'C08' : 'tidak pernah',
          'C09' : 'tidak pernah',
          'C10' : 'tidak pernah',
          'C11' : 'tidak pernah',
          'C12' : 'tidak pernah',
          'C13' : 'tidak pernah',
          'C14' : 'tidak pernah',
          'C15' : 'tidak pernah',
          'C16' : 'tidak pernah',
          'C17' : 'tidak pernah',
          'C18' : 'tidak pernah',
          'C19' : 'tidak pernah',
          'C20' : 'tidak pernah',
          'C21' : 'tidak pernah',
          'C22' : 'tidak pernah',
          'C23' : 'tidak pernah',
          'C24' : 'tidak pernah',
          'C25' : 'tidak pernah',
          'C26' : jawaban26,
          'C27' : 'tidak pernah',
          'C28' : 'tidak pernah',
          'C29' : 'tidak pernah',
          'C30' : 'tidak pernah',
          'C31' : 'tidak pernah',
          'C32' : 'tidak pernah',
    }
    pertanyaan = pd.DataFrame(data, index=[0])
    return pertanyaan
jenis = st.selectbox('Jenis Narkoba', ('--- pilih --', 'Morfin', 'Heroin', 'Ganja', 'Putaw', 'Kokain', 'Extasi', 'Sabu-sabu', 'LSD', 'Hamfetamin', 'Opium'))
inputan = 0;
if jenis == "Morfin":
    inputan = morfin()
st.write(inputan)   
    

