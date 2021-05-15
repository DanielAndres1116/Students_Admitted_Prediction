# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:38:41 2020

@author: Daniel Andres
"""

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

x = "It is a charming and beautiful product"
y = "It was a horrible experience!"
z = "I have nothing to say. Normal so far"

sid = SentimentIntensityAnalyzer()
resultadox = sid.polarity_scores(x)
resultadoy = sid.polarity_scores(y)
resultadoz = sid.polarity_scores(z)

print(resultadox)
print(resultadoy)
print(resultadoz)

########### IMPORTAR LIBRERÍAS #############

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import date, datetime, timedelta, time
import pysrt
from textblob import TextBlob

#Configuramos las gráficas
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0) #16inX9in(LargoxAncho)
style.use('fivethirtyeight') #Estilo de grafico

######### IMPORTAR LOS DATOS #################
# El Encoding es la codificación de caracteres y es un método que permite convertir 
# un carácter de un lenguaje natural en un símbolo de otro sistema de representación, 
# para esto se tienen distintos números. Para nuestro caso debemos utilizar iso-8859-1, 
# en caso de que no coloquemos el encoding seguramente dará un error al momento de ejecutar la línea. 
movie = 'Harry Potter And The Sorcerers Stone1_1.srt'
subs = pysrt.open(movie, encoding='iso-8859-1')

#Intervalo de análisis
#Inicio
start = time(0, 0, 0)
print(start)

#Final
end = subs[-1].end.to_time()
print(end)

#Intervalo
delta = timedelta(minutes=1)
print(delta)

#Definir los intervalos de tiempo
intervals = []
now = start

while now <= end:
    now = (datetime.combine(date.today(), now) + delta).time()
    intervals.append(now)
print(intervals)

sentiments = []
index = 0
n = len(subs)
m = len(intervals)
#Iteración anidada para ir guardando los subtítulos en cada intervalo de la lista
for i in range(m):
    text = ""
    for j in range(index, n):
        #Encuentra todos los subtítulos en cada intervalo
        if subs[j].end.to_time() < intervals[i]:
            text += subs[j].text_without_tags + " "
        else:
            break
    #Realiza el análisis sentimental
    #Cada vez que la variable tenga su valor guardado, antes de reiniciarse
    #se analiza su sentimiento y se agrega a la variable pol, la cual va 
    #siendo añadida la lista sentiments
    blob = TextBlob(text)
    pol = blob.sentiment.polarity
    sentiments.append(pol)
    index = j
    
print(sentiments)

avg = float(sum(sentiments))/len(sentiments)
print("Promedio Análisis Sentimental: ", avg)

#Inicializando las variables
intervals.insert(0, time(0,0,0))
sentiments.insert(0, 0.0)

#Se grafican los resultados
x = intervals
y = sentiments

fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Harry Potter y la Piedra Filosofal", fontsize=32)
plt.ylim((-1, 1))
plt.ylabel("Sentimiento")
plt.xlabel("Intervalo de Tiempo")
plt.text(.5, 1.03, "Promedio Sentimental - " + str(round(avg, 4)), color="blue")
ttl = ax.title
ttl.set_position([.5, 1.05])
plt.show()

