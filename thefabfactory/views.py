from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
import pickle
import json
from django.views.decorators.csrf import csrf_exempt
from function.recommender_implementation import RecommenderFunction

popular_df = pickle.load(open('data/popular.pkl', 'rb'))
clothing_data_df = pickle.load(open('data/clothing_df.pkl', 'rb'))

def index(request):

    # Convert the product details into a list of dictionaries
    product_list = [
        {
            'product_description': popular_df.iloc[i]['description'],
            'product_image': popular_df.iloc[i]['img'],
            'product_price': popular_df.iloc[i]['price'],
            'product_ratings': popular_df.iloc[i]['rating'],
            'product_rating_counts': popular_df.iloc[i]['rating_count'],
            'product_urls': popular_df.iloc[i]['url']
        } for i in range(len(popular_df))
    ]

    # Pass the list to the template
    return render(request, 'index.html', {'product_list': product_list})

def recommend(request):
    return render(request, 'recommend.html')

@csrf_exempt
def recommend_clothing_items(request):
    if request.method == 'POST':  # Checks if the request method is 'POST'
        try:
            input_text = request.POST['input_text']
            top_results = request.POST['top_results']
            
            recommendations = RecommenderFunction().recommend_clothes(input_text, top_results)
            
            return render(request, 'recommend.html', {'recommendations': recommendations})
        except json.JSONDecodeError:
            
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        
        return HttpResponseNotAllowed(['POST'])
    
def contact(request):
    return render(request, 'contact.html')