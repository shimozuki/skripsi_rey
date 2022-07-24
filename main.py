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
#memisahkan data dengan label
X = data_acuan.drop(columns=['Kecanduan','No', 'Narkoba'])
y = data_acuan['Kecanduan']
z = data_acuan['Narkoba']
#proses retrival
classifier = KNeighborsClassifier(n_neighbors = 5, algorithm='kd_tree', metric = 'euclidean', p = 2)
classifier = classifier.fit(X,y)
def input_user() :
     jenis = st.selectbox('Jenis Narkoba', ('--- pilih --', 'Morfin', 'Heroin', 'Ganja', 'Putaw', 'Kokain', 'Extasi', 'Sabu-sabu', 'LSD', 'Hamfetamin', 'Opium'))
     if jenis == 'Morfin':
          jawaban1 = st.radio(
               "1. Seberapa Sering Anda Berkeringat ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban3 = st.radio(
               "2. Seberapa Sering Anda Suasana Suasana hati berubah ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban5 = st.radio(
               "3. Seberapa sering Anda Merasa Tidak Nafsu Makan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban6 = st.radio(
               "6. Seberapa sering Anda Sulit Berkonsentrasi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban7 = st.radio(
               "5. Seberapa sering Anda Merasa Nafas Menjadi Pendek?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban4 = st.radio(
               "4.Seberapa sering Anda Merasa Mulut Kering?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban26 = st.radio(
               "26. Seberapa sering Anda Merasa Kebingungan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == 'Heroin':
          jawaban8 = st.radio(
               "8. Seberapa sering Anda Suka Menyendiri?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban9 = st.radio(
               "9. Seberapa sering Anda Merasa Hilang Percaya Diri?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban10 = st.radio(
               "10. Seberapa sering Anda Tidur?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban11 = st.radio(
               "11. Seberapa sering Mata Anda Merah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban12 = st.radio(
               "12. Seberapa sering Anda Muntah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban7 = st.radio(
               "7. Seberapa sering Anda Merasa Nafas Menjadi Pendek?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Ganja":
          jawaban6 = st.radio(
               "6. Seberapa sering Anda Sulit Berkonsentrasi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban13 = st.radio(
               "13. Seberapa sering Anda Merasa Gelisah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban2 = st.radio(
               "2. Seberapa Sering Sulit dalam mengingat ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban32 = st.radio(
               "32. Seberapa sering Anda Merasa Depresi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban11 = st.radio(
               "11. Seberapa sering Mata Anda Merah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban15 = st.radio(
               "15. Seberapa sering Anda Merasa Panik / Cemas?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban16 = st.radio(
               "16. Seberapa sering Anda Merasa Lapar?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Putaw":
          jawaban17 = st.radio(
               "17. Seberapa sering Birahi Anda Meningkat?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban12 = st.radio(
               "12. Seberapa sering Anda Muntah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban22 = st.radio(
               "22. Seberapa sering Anda Merasa Insomnia?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban1 = st.radio(
               "1. Seberapa Sering Anda Berkeringat ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban26 = st.radio(
               "26. Seberapa sering Anda Merasa Kebingungan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Kokain":
          jawaban21 = st.radio(
               "21. Seberapa sering Anda Susah dinasehati?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban23 = st.radio(
               "23. Seberapa sering Anda Berbohong?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban24 = st.radio(
               "24. Seberapa sering Anda Merasa Pusing?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban10 = st.radio(
               "10. Seberapa sering Anda Tidur?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban11 = st.radio(
               "11. Seberapa sering Mata Anda Merah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Extasi":
          jawaban19 = st.radio(
               "19. Seberapa sering Anda Mual?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban20 = st.radio(
               "20. Seberapa sering Anda Dehidrasi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban22 = st.radio(
               "22. Seberapa sering Anda Merasa Insomnia?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban24 = st.radio(
               "24. Seberapa sering Anda Merasa Pusing?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban11 = st.radio(
               "11. Seberapa sering Mata Anda Merah?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban1 = st.radio(
               "1. Seberapa Sering Anda Berkeringat ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban26 = st.radio(
               "26. Seberapa sering Anda Merasa Kebingungan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban31 = st.radio(
               "31. Seberapa sering Anda Pulang larut malam?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Sabu-sabu":
          jawaban27 = st.radio(
               "27. Seberapa sering Anda Merasa Percaya diri tinggi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban25 = st.radio(
               "25. Seberapa sering Jantung Anda berdebar-debar ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban22 = st.radio(
               "22. Seberapa sering Anda Merasa Insomnia?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban1 = st.radio(
               "1. Seberapa Sering Anda Berkeringat ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban8 = st.radio(
               "8. Seberapa sering Anda Suka Menyendiri?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban18 = st.radio(
               "18. Seberapa sering Anda Berhalusinasi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban15 = st.radio(
               "15. Seberapa sering Anda Merasa Panik / Cemas?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban5 = st.radio(
               "5. Seberapa sering Anda Merasa Tidak Nafsu Makan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban29 = st.radio(
               "29. Seberapa sering Anda Merasa gembira?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "LSD":
          jawaban22 = st.radio(
               "22. Seberapa sering Anda Merasa Insomnia?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban14 = st.radio(
               "14. Seberapa sering Anda Merasa Sulit dalam mengingat?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban6 = st.radio(
               "6. Seberapa sering Anda Sulit Berkonsentrasi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban8 = st.radio(
               "8. Seberapa sering Anda Suka Menyendiri?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban19 = st.radio(
               "19. Seberapa sering Anda Mual?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban30 = st.radio(
               "30. Seberapa sering Anda Merasa mengalami halusinasi pada pendengaran?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban28 = st.radio(
               "28. Seberapa sering Anda Merasa Paranoid / masalah mental?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban20 = st.radio(
               "20. Seberapa sering Anda Dehidrasi?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Hamfetamin":
          jawaban30 = st.radio(
               "30. Seberapa sering Anda Merasa mengalami halusinasi pada pendengaran?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban5 = st.radio(
               "3. Seberapa sering Anda Merasa Tidak Nafsu Makan?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban8 = st.radio(
               "8. Seberapa sering Anda Suka Menyendiri?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban15 = st.radio(
               "15. Seberapa sering Anda Merasa Panik / Cemas?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban22 = st.radio(
               "22. Seberapa sering Anda Merasa Insomnia?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban29 = st.radio(
               "29. Seberapa sering Anda Merasa gembira?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     elif jenis == "Opium":
          jawaban24 = st.radio(
               "24. Seberapa sering Anda Merasa Pusing?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban30 = st.radio(
               "30. Seberapa sering Anda Merasa mengalami halusinasi pada pendengaran?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban8 = st.radio(
               "8. Seberapa sering Anda Suka Menyendiri?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban25 = st.radio(
               "25. Seberapa sering Jantung Anda berdebar-debar ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban1 = st.radio(
               "1. Seberapa Sering Anda Berkeringat ?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban19 = st.radio(
               "19. Seberapa sering Anda Mual?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban10 = st.radio(
               "10. Seberapa sering Anda Tidur?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
          jawaban29 = st.radio(
               "29. Seberapa sering Anda Merasa gembira?",
               ('tidak pernah', 'Kadang-kadang', 'sering'))
     data = {
          'C01' : jawaban1,
          'C02' : jawaban2,
          'C03' : jawaban3,
          'C04' : jawaban4,
          'C05' : jawaban5,
          'C06' : jawaban6,
          'C07' : jawaban7,
          'C08' : jawaban8,
          'C09' : jawaban9,
          'C10' : jawaban10,
          'C11' : jawaban11,
          'C12' : jawaban12,
          'C13' : jawaban13,
          'C14' : jawaban14,
          'C15' : jawaban15,
          'C16' : jawaban16,
          'C17' : jawaban17,
          'C18' : jawaban18,
          'C19' : jawaban19,
          'C20' : jawaban20,
          'C21' : jawaban21,
          'C22' : jawaban22,
          'C23' : jawaban23,
          'C24' : jawaban24,
          'C25' : jawaban25,
          'C26' : jawaban26,
          'C27' : jawaban27,
          'C28' : jawaban28,
          'C29' : jawaban29,
          'C30' : jawaban30,
          'C31' : jawaban31,
          'C32' : jawaban32,
     }
     pertanyaan = pd.DataFrame(data, index=[0])
     if (pertanyaan['C01'] == 'sering' ).any():
          pertanyaan['C01'] = 1.00
     elif(pertanyaan['C01'] == 'Kadang-kadang' ).any():
          pertanyaan['C01'] = 0.5
     else:
          pertanyaan['C01'] = 0.0
     if (pertanyaan['C02'] == 'sering' ).any():
          pertanyaan['C02'] = 1.00
     elif(pertanyaan['C02'] == 'Kadang-kadang' ).any():
          pertanyaan['C02'] = 0.5
     else:
          pertanyaan['C02'] = 0.0
     if (pertanyaan['C03'] == 'sering' ).any():
          pertanyaan['C03'] = 1.00
     elif(pertanyaan['C03'] == 'Kadang-kadang' ).any():
          pertanyaan['C03'] = 0.5
     else:
          pertanyaan['C03'] = 0.0
     if (pertanyaan['C04'] == 'sering' ).any():
          pertanyaan['C04'] = 1.00
     elif(pertanyaan['C04'] == 'Kadang-kadang' ).any():
          pertanyaan['C04'] = 0.5
     else:
          pertanyaan['C04'] = 0.0
     if (pertanyaan['C05'] == 'sering' ).any():
          pertanyaan['C05'] = 1.00
     elif(pertanyaan['C05'] == 'Kadang-kadang' ).any():
          pertanyaan['C05'] = 0.5
     else:
          pertanyaan['C05'] = 0.0
     if (pertanyaan['C06'] == 'sering' ).any():
          pertanyaan['C06'] = 1.00
     elif(pertanyaan['C06'] == 'Kadang-kadang' ).any():
          pertanyaan['C06'] = 0.5
     else:
          pertanyaan['C06'] = 0.0
     if (pertanyaan['C07'] == 'sering' ).any():
          pertanyaan['C07'] = 1.00
     elif(pertanyaan['C07'] == 'Kadang-kadang' ).any():
          pertanyaan['C07'] = 0.5
     else:
          pertanyaan['C07'] = 0.0
     if (pertanyaan['C08'] == 'sering' ).any():
          pertanyaan['C08'] = 1.00
     elif(pertanyaan['C08'] == 'Kadang-kadang' ).any():
          pertanyaan['C08'] = 0.5
     else:
          pertanyaan['C08'] = 0.0
     if (pertanyaan['C09'] == 'sering' ).any():
          pertanyaan['C09'] = 1.00
     elif(pertanyaan['C09'] == 'Kadang-kadang' ).any():
          pertanyaan['C09'] = 0.5
     else:
          pertanyaan['C09'] = 0.0
     if (pertanyaan['C10'] == 'sering' ).any():
          pertanyaan['C10'] = 1.00
     elif(pertanyaan['C10'] == 'Kadang-kadang' ).any():
          pertanyaan['C10'] = 0.5
     else:
          pertanyaan['C10'] = 0.0
     if (pertanyaan['C11'] == 'sering' ).any():
          pertanyaan['C11'] = 1.00
     elif(pertanyaan['C11'] == 'Kadang-kadang' ).any():
          pertanyaan['C11'] = 0.5
     else:
          pertanyaan['C11'] = 0.0
     if (pertanyaan['C12'] == 'sering' ).any():
          pertanyaan['C12'] = 1.00
     elif(pertanyaan['C12'] == 'Kadang-kadang' ).any():
          pertanyaan['C12'] = 0.5
     else:
          pertanyaan['C12'] = 0.0
     if (pertanyaan['C13'] == 'sering' ).any():
          pertanyaan['C13'] = 1.00
     elif(pertanyaan['C13'] == 'Kadang-kadang' ).any():
          pertanyaan['C13'] = 0.5
     else:
          pertanyaan['C13'] = 0.0
     if (pertanyaan['C14'] == 'sering' ).any():
          pertanyaan['C14'] = 1.00
     elif(pertanyaan['C14'] == 'Kadang-kadang' ).any():
          pertanyaan['C14'] = 0.5
     else:
          pertanyaan['C14'] = 0.0
     if (pertanyaan['C15'] == 'sering' ).any():
          pertanyaan['C15'] = 1.00
     elif(pertanyaan['C15'] == 'Kadang-kadang' ).any():
          pertanyaan['C15'] = 0.5
     else:
          pertanyaan['C15'] = 0.0
     if (pertanyaan['C16'] == 'sering' ).any():
          pertanyaan['C16'] = 1.00
     elif(pertanyaan['C16'] == 'Kadang-kadang' ).any():
          pertanyaan['C16'] = 0.5
     else:
          pertanyaan['C16'] = 0.0
     if (pertanyaan['C17'] == 'sering' ).any():
          pertanyaan['C17'] = 1.00
     elif(pertanyaan['C17'] == 'Kadang-kadang' ).any():
          pertanyaan['C17'] = 0.5
     else:
          pertanyaan['C17'] = 0.0
     if (pertanyaan['C18'] == 'sering' ).any():
          pertanyaan['C18'] = 1.00
     elif(pertanyaan['C18'] == 'Kadang-kadang' ).any():
          pertanyaan['C18'] = 0.5
     else:
          pertanyaan['C18'] = 0.0
     if (pertanyaan['C19'] == 'sering' ).any():
          pertanyaan['C19'] = 1.00
     elif(pertanyaan['C19'] == 'Kadang-kadang' ).any():
          pertanyaan['C19'] = 0.5
     else:
          pertanyaan['C19'] = 0.0
     if (pertanyaan['C20'] == 'sering' ).any():
          pertanyaan['C20'] = 1.00
     elif(pertanyaan['C20'] == 'Kadang-kadang' ).any():
          pertanyaan['C20'] = 0.5
     else:
          pertanyaan['C20'] = 0.0
     if (pertanyaan['C21'] == 'sering' ).any():
          pertanyaan['C21'] = 1.00
     elif(pertanyaan['C21'] == 'Kadang-kadang' ).any():
          pertanyaan['C21'] = 0.5
     else:
          pertanyaan['C21'] = 0.0
     if (pertanyaan['C22'] == 'sering' ).any():
          pertanyaan['C22'] = 1.00
     elif(pertanyaan['C22'] == 'Kadang-kadang' ).any():
          pertanyaan['C22'] = 0.5
     else:
          pertanyaan['C22'] = 0.0
     if (pertanyaan['C23'] == 'sering' ).any():
          pertanyaan['C23'] = 1.00
     elif(pertanyaan['C23'] == 'Kadang-kadang' ).any():
          pertanyaan['C23'] = 0.5
     else:
          pertanyaan['C23'] = 0.0
     if (pertanyaan['C24'] == 'sering' ).any():
          pertanyaan['C24'] = 1.00
     elif(pertanyaan['C24'] == 'Kadang-kadang' ).any():
          pertanyaan['C24'] = 0.5
     else:
          pertanyaan['C24'] = 0.0
     if (pertanyaan['C25'] == 'sering' ).any():
          pertanyaan['C25'] = 1.00
     elif(pertanyaan['C25'] == 'Kadang-kadang' ).any():
          pertanyaan['C25'] = 0.5
     else:
          pertanyaan['C25'] = 0.0
     if (pertanyaan['C26'] == 'sering' ).any():
          pertanyaan['C26'] = 1.00
     elif(pertanyaan['C26'] == 'Kadang-kadang' ).any():
          pertanyaan['C26'] = 0.5
     else:
          pertanyaan['C26'] = 0.0
     if (pertanyaan['C27'] == 'sering' ).any():
          pertanyaan['C27'] = 1.00
     elif(pertanyaan['C27'] == 'Kadang-kadang' ).any():
          pertanyaan['C27'] = 0.5
     else:
          pertanyaan['C27'] = 0.0
     if (pertanyaan['C28'] == 'sering' ).any():
          pertanyaan['C28'] = 1.00
     elif(pertanyaan['C28'] == 'Kadang-kadang' ).any():
          pertanyaan['C28'] = 0.5
     else:
          pertanyaan['C28'] = 0.0
     if (pertanyaan['C29'] == 'sering' ).any():
          pertanyaan['C29'] = 1.00
     elif(pertanyaan['C29'] == 'Kadang-kadang' ).any():
          pertanyaan['C29'] = 0.5
     else:
          pertanyaan['C29'] = 0.0
     if (pertanyaan['C30'] == 'sering' ).any():
          pertanyaan['C30'] = 1.00
     elif(pertanyaan['C30'] == 'Kadang-kadang' ).any():
          pertanyaan['C30'] = 0.5
     else:
          pertanyaan['C30'] = 0.0
     if (pertanyaan['C31'] == 'sering' ).any():
          pertanyaan['C31'] = 1.00
     elif(pertanyaan['C31'] == 'Kadang-kadang' ).any():
          pertanyaan['C31'] = 0.5
     else:
          pertanyaan['C31'] = 0.0
     if (pertanyaan['C32'] == 'sering' ).any():
          pertanyaan['C32'] = 1.00
     elif(pertanyaan['C32'] == 'Kadang-kadang' ).any():
          pertanyaan['C32'] = 0.5
     else:
          pertanyaan['C32'] = 0.0
     return pertanyaan
inputan = input_user()




















