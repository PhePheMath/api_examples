'''
This is an example of APIs

Be positive: https://www.affirmations.dev/
Know your cat: https://catfact.ninja/fact?max_length=140
Know your news: http://api.nytimes.com/svc/search/v2/articlesearch.json?q=obamacare+socialism&api-key=b75da00e12d54774a2d362adddcc9bef

'''

from requests import get, request

def r_u_a_coach__q():
    url = "https://www.affirmations.dev/"
    response = get(url)
    return response.json()['affirmation']

def cat_fcat():
    url = "https://catfact.ninja/fact?max_length=140"
    response = get(url)
    print(response)
    return response.json()['fact']

def a_quote():
    url = "https://quotes.rest/qod.json"
    response = get(url).json()
    if 'success' in response:
        quote = response['contents']['quotes'][0]['quote']
    elif 'error' in response:
        quote = 'Let them eat cake'
    return quote

if __name__ == "__main__":
    print(r_u_a_coach__q())
    print(cat_fcat())
    print(a_quote())
