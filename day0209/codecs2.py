import codecs
text=input('書き込む内容>>')
with codecs.open('diary.txt','a','utf-8') as file:
    file.write(text+'\n')