# Analisis_Sentimientos_Texto
## Análisis sentimental en textos y subtítulos de películas

### Descripción del Dataset y cómo se obtuvo
Para obtener los archivos de los subtítulos se buscaron en internet colocando Harry Potter Movies SRT. Se puede seleccionar el primer link que aparece en Google y descargar desde allí todos los subtítulos. Cabe destavar que se debe seleccionar el mismo idioma para todas las películas, aunque aquí unicamente se analizó la primera película. 

Es recomendable que todos los subrítulos que se hayan descargado se coloquen juntos en una sola carpeta, la cual estará ubicada en la carpeta principal del proyecto. 

Tener en cuenta que el archivo principal es el llamado AnalisisSentimentalPeliculas.py

### Objetivos

El principal objetivo es poner en práctica conocimientos sobre análisis sentimental a textos y para ello lo primero que se hizo en el programa fue hacer un breve análisis sentimental a tres textos con diferentes opiniones acerca de un producto, uno con sentimientos negativos sobre un producto, uno con sentimientos positivos sobre el producto y otro neutro. Esto por medio de la librería nltk mediante el método SentimentIntensityAnalyzer.

Posteriormente se hizo un análisis sentimental de la película de Harry Potter para luego graficar los sentimientos que ocurren a lo largo de la película. Con la gráfica se observan los momentos felices y tristes de la trama así como el tiempo exacto en el que ocurren. Cabe destacar que este análisis se puede hacer con cualquier película que se desee, aunque la idea es que sean películas que cuenten con un lenguaje normal y no del tipo victoriano con términos o frases que no sean comúnmente utilizadas en nuestro día a día.

Para hacer el análisis sentimental fue importada la librería TextBlob, aunque cabe aclarar que existen más librerías para hacer este análisis y esta es una de las más básicas y fáciles por lo que fue utilizada. Gracias a esta herramienta es posible obtener valores entre -1 y 1 para indicar la intensidad del sentimiento. 

Se empleó el método rcParams de matplotlib para definir parámetros de la gráfica tales como grosor de las líneas y colores a utilizar (aunque en realidad pueden ser muchos más parámetros). Esto para meorar la presentación de las gráficas.

Se utiliza la librería datetime para marcar un inicio y final de tiempo para el gráfico, así como un intervalo de tiempo para realizar el análisis el cual fue de un minuto. Esto con el fin de ir haciendo el analisis sentimental minuto a minuto de la película, esto se logra gracias a un bucle for donde se va llenando la variable.  

Tras esto se obtiene el promedio de sentimientos el cual arroja un valor de 0.1017 lo cual indica que está por arriba de 0, indicando que en general es una película con sentimientos positivos.

Así luce la variación de sentimientos a lo largo de la película:

![image](https://user-images.githubusercontent.com/43154438/118346609-5a087d80-b502-11eb-9d19-45e11203750b.png)


### Conclusiones y resultados obtenidos

Como podemos ver el la gráfica, casi todas las lineas están por encima del cero, lo cual indica que esta película tiende a tener más momentos felices y positivos que tristes, coincidiendo esto con el valor del promedio obtenido. 

Al poder realizar este análisis para cualquier película, también podemos decir que es posible hacer este análisis para cualquier tipo de texto o de video aumentando así el alcance de estas librerías, tanto la de nltk como la de textblob

#### PD: Se agregó un código llamado Extraer_Datos_Twitter.ipynb donde se extrae cierta información de Twitter a partir de una cuenta de Developer, este código no está relacionado con el de análisis sentimental de la película, pero podrían combinarse los conocimientos en ambas cosas para obtener análisis sentimental de publicaciones en Twitter.
