from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests

def amazon_search(request):

    keyword = request.GET.get('keyword')
    url = f'https://www.amazon.com/s?k={keyword}'
    response = requests.get(url)

   
    soup = BeautifulSoup(response.text, 'html.parser')

    
    products = []
    for result in soup.find_all('div', {'data-index': True}):
        title = result.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        price = result.find('span', {'class': 'a-price-whole'})
        if title and price:
            products.append({
                'title': title.text,
                'price': price.text
            })
    return JsonResponse({'products': products})
