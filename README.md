# 1. Sentimental Analysis: understanding the feelings of potential customers

# 1.1. Sentimental Analysis using the Natural Language Toolkit (nltk) – Python Library

Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotion behind a given text. The Natural Language Toolkit (nltk) library is a popular open-source toolkit for performing sentiment analysis in Python.

Using the nltk library, we can perform several tasks related to sentiment analysis, including:

1.	Tokenization: Breaking down the text into individual words or phrases to be analyzed.

2.	Sentiment Classification: Classifying the sentiment of the text as positive, negative, or neutral. This is typically done using machine learning algorithms such as Naive Bayes or Support Vector Machines (SVM).

3.	Sentiment Scoring: Assigning a score to the sentiment of the text, such as a numerical value from -1 to 1, where -1 indicates negative sentiment, 0 indicates neutral sentiment, and 1 indicates positive sentiment.

4.	Sentiment Visualization: Representing the sentiment analysis results in a visual format, such as a bar graph or pie chart.

In business, sentiment analysis has several important applications:

1.	Customer Feedback Analysis: Companies can use sentiment analysis to analyze customer feedback from sources such as product reviews, social media posts, and customer support tickets. This information can help companies to understand customer opinions about their products and services, identify areas for improvement, and respond to customer complaints more effectively.

2.	Brand Monitoring: Companies can use sentiment analysis to monitor and analyze mentions of their brand or products on social media and other online platforms. This can help companies to track their brand reputation, identify areas of concern, and take action to address any negative sentiment.

3.	Market Research: Companies can use sentiment analysis to gather insights about consumer preferences, opinions, and trends. For example, they can analyze customer reviews to understand what people like or dislike about a particular product or service.

4.	Social Media Analytics: Companies can use sentiment analysis to understand the sentiment behind social media posts and conversations about their brand, products, or competitors. This information can be used to inform marketing and advertising strategies.

In conclusion, sentiment analysis is important because it provides valuable insights into customer opinions and emotions. By using sentiment analysis, companies can better understand their customers and make informed decisions that can improve customer satisfaction, increase sales, and enhance their overall reputation. Additionally, sentiment analysis can provide valuable information for market research and help companies to stay ahead of the competition by monitoring trends and sentiment in the industry.

## 1.2. The potential of using Twitter API for marketing campaings in combination with Sentimental Analysis

Twitter API is an interface for accessing Twitter data, which allows developers to access and extract information from Twitter, including tweets, users, and other data. The API is used to build various applications, including but not limited to, marketing analysis.

In the field of marketing analysis, the Twitter API can be used to gather data on specific topics, hashtags, and users, which can then be analyzed to understand public sentiment and opinions. When used in conjunction with the Natural Language Processing (NLP) library, such as NLTK, it is possible to perform sentiment analysis on Twitter data. This involves analyzing tweets to determine the emotions and opinions expressed by users, which can be extremely valuable for businesses looking to understand customer sentiment and respond accordingly.

Sentiment analysis of Twitter data can be performed in several ways, including:

•	Classifying tweets as positive, negative, or neutral based on the words used

•	Identifying the sentiment of individual words or phrases within tweets

•	Analyzing the sentiment of entire conversations or threads of tweets

The potential advantages of using sentiment analysis on Twitter data include:

•	Understanding customer sentiment and opinions on specific products, services, or topics

•	Monitoring brand reputation and detecting potential problems or negative sentiment early on

•	Identifying opportunities for improvement or areas of customer dissatisfaction

•	Measuring the impact of marketing campaigns and PR efforts on customer sentiment

It’s important to note that sentiment analysis can be applied to other social media platforms as well, such as Facebook, Instagram, and YouTube, which also have APIs that allow for data access and analysis. The use of sentiment analysis in these platforms can provide similar benefits to businesses, allowing them to understand and respond to customer sentiment in a proactive and informed manner.

## 1.3. Dataset and Project Description

The main objective of this project was to perform sentiment analysis on texts. To achieve this, the program first conducted a brief sentiment analysis on three texts with different opinions about a product: one with negative sentiments, one with positive sentiments, and one with neutral sentiments. This was done using the nltk library through the 'SentimentIntensityAnalyzer' method.

Next, the program conducted a sentiment analysis of the movie “Harry Potter” and then plotted the sentiments that occur throughout the movie. The graph displays the happy and sad moments in the plot as well as the exact time they occur. It should be noted that this analysis can be done with any movie, although the idea is to choose movies that have a normal language and not of the Victorian type with terms or phrases that are not commonly used in our day-to-day lives.

For obtaining the subtitle files, a search was conducted on the internet for “Harry Potter Movies SRT”. The first link that appears on Google can be selected to download all the subtitles from there. It is important to note that the same language must be selected for all the movies, although only the first movie was analyzed in this case.

It is recommended that all the downloaded subtitles be placed together in one folder, which will be located in the main folder of the project.

To perform the sentiment analysis, the TextBlob library was imported, although it should be noted that there are many other libraries for sentiment analysis and this is one of the most basic and easiest to use. Thanks to this tool, it is possible to obtain values between -1 and 1 to indicate the intensity of the sentiment.

The rcParams method of matplotlib was used to define parameters for the graph such as line thickness and colors to be used (although there can actually be many more parameters). This was done to improve the presentation of the graphs.

The datetime library was used to mark a start and end time for the graph, as well as a time interval for the analysis, which was one minute. This was in order to conduct a sentiment analysis minute by minute of the movie, which was achieved through a for loop that fills the variable.

![image](https://user-images.githubusercontent.com/43154438/229917625-a59f6388-6bd3-4170-ab77-c297c488763c.png)

Figure 1: sentimental analysis rate along the movie of Harry Potter and the philosopher’s stone

After this, the average sentiment was obtained, which yields a value of 0.1017, indicating that it is above 0, indicating that in general it is a movie with positive sentiments.

In addition to the programming code that performs the sentiment analysis of the initial texts and the subtitles of the Harry Potter movies, a program was also developed to extract twitter comments from a developer account. The Twitter API was used to extract information from this social network. It should be noted that these.

No sentiment analysis of the information extracted from Twitter has been conducted yet using NLTK. However, I plan to continue working on this project or on some other project that involves these types of issues.
