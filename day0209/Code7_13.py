import requests
import codecs

response = requests.get('https://hashikake.com/library')
text=response.text
#print(text)

with codecs.open('index.html','w','utf-8') as file:
    file.write(text)
