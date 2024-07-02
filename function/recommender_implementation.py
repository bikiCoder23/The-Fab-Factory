import json
import pickle
import re

from django.http import JsonResponse
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vec = CountVectorizer(max_features=5000, stop_words='english')


class RecommenderFunction:
    @staticmethod
    def clean_text(text: str) -> str:
        lemmatizer = WordNetLemmatizer()

        cleaned_text = re.sub('[^a-zA-Z]', ' ', text)

        cleaned_text = cleaned_text.lower()

        cleaned_text = cleaned_text.split()

        cleaned_text = [
            lemmatizer.lemmatize(word)
            for word in cleaned_text
            if not word in stopwords.words('english')
        ]

        return ' '.join(cleaned_text)

    def recommend_clothes(self, text: str, top_num: int):
        clothing_df = pickle.load(open('data/clothing_df.pkl', 'rb'))

        cleaned_text = self.clean_text(text)

        cleaned_text_as_series = pd.Series([cleaned_text])

        descriptions = clothing_df['cleaned_description']

        description_with_new_text = pd.concat([descriptions, cleaned_text_as_series]).reset_index(drop=True)

        vectors = vec.fit_transform(description_with_new_text).toarray()

        similarity_scores = cosine_similarity(vectors)

        input_description_index = description_with_new_text[description_with_new_text == cleaned_text].index[0]

        distances = similarity_scores[input_description_index]

        clothing_items_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:int(top_num) + 1]

        clothing_item_details = [(clothing_df.iloc[each[0]]).to_dict() for each in clothing_items_list]

        descriptions = descriptions[descriptions != cleaned_text]

        return clothing_item_details