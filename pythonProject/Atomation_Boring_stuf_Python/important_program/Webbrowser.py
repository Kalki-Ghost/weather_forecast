import webbrowser
import requests

webbrowser.open('https://in.search.yahoo.com/search?fr=mcafee&type=E210IN885G0&p=textfiles')
re = requests.get('https://in.search.yahoo.com/search?fr=mcafee&type=E210IN885G0&p=textfiles')
print(re.status_code)
print(re.raise_for_status())