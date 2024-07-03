# The-Fab-Factory

This project involves implementing web scraping techniques and their real-life use case in the development of a fashion e-commerce website for the Internet Technology course (IT4172) at IIEST Shibpur.

![Python](https://img.shields.io/badge/Python-3.9-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Django-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/Bootstrap-green)

## Overview

**The Fab Factory** is an E-Commerce platform that brings you the latest and greatest fashion and all thats trendings across the globe. It is multi-paged web-application which is based on django framework and scrapes the clothing data for men and women from amazon.in, where those can be purchased too. The appication consists of three pages, out of which the `Featured` page displays the _Top 60_ of the most trending fashion based on **_Popularity-based Recommendation_** using _mean-threshold algorithm_. The next page `Recommend` is a clothing recommendation system designed to provide personalized clothing suggestions based on user preferences and various other factors by calculating _similarity scores_ with different products available based on user ratings & counts. Lastly the `Contact` page is a form where the user can share their valuable feedbacks in order to indroduce new products and to enhance the platform for seamless shopping experience.

## Dataset Preparation

To get the clothing data and to train the recommendation system, a dataset of various clothing items for men and women was prepared through web scraping from e-commerce website of Amazon using the BeautifulSoup library. The dataset includes textual descriptions of the clothing items.

## Data Preprocessing

Before training the recommendation system, the textual data from the dataset undergoes several preprocessing steps:

1. Convert the text to lowercase.
2. Remove stopwords to eliminate common words that do not carry much meaning.
3. Tokenize the text to split it into individual words.
4. Lemmatize the words to reduce them to their base form.
5. Remove special characters to clean the text further.
   These preprocessing steps help to normalize the textual data and remove noise.

## Writing Recommendation Function

The recommendation function in the code performs the following steps:

1. Clean the text input given by the user and add it to the dataset.
2. Convert the textual descriptions in the dataset to vectors using the bag-of-words technique.
3. Calculate the popularity of the products based on filtering algorithm such as thresholding.
   - Thresholding: It is a type of algorithm used to filter out the top rated product by the userbase based on certain threshold criteria.
   - _Top Trending_ fashion can be seen in the `Featured` page, where Top 60 products are displayed.
4. Calculate the similarity score between the user input vector and the vectors of clothing items using cosine similarity.
   - Similarity score: It is a numerical value ranges between zero to one which helps to determine how much two products are similar to each other on a scale of zero to one.
   - Cosine similarity: Cosine similarity is a metric used to measure how similar the products are irrespective of their size. The smaller the angle, higher the cosine similarity.
   - Recommend the top clothing items with the highest similarity scores to the user.
     These steps ensure that the recommendation system provides relevant clothing suggestions based on the user's input.

## Features

1. Personalized clothing recommendations
2. User friendly interface.
3. Real-time shopping from amazon.in.

## How to clone the repository?

The following command should be used to clone the repository:

```
git clone https://github.com/bikiCoder23/The_Fab_Factory
```

### Project UI
![image](https://github.com/bikiCoder23/The-Fab-Factory/assets/76732539/770e0241-1086-4b49-b60c-f17e297bd198)
![image](https://github.com/bikiCoder23/The-Fab-Factory/assets/76732539/cdece51a-71d6-409b-9642-52f5ca86b140)
![image](https://github.com/bikiCoder23/The-Fab-Factory/assets/76732539/de0a6d7f-f6be-451f-9bbb-73ce3f0665af)
