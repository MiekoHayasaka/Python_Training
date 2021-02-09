import codecs

file=codecs.open('diary.txt','a','utf-8')
text='こんにちは'
file.write(text)
file.close()
