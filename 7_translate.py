from textblob import TextBlob

data = open('data4.txt')
textData = data.read()
blobData = TextBlob(textData)
print(blobData.detect_language())  #will return langauge
arData=blobData.translate(from_lang='en', to ='mr')
print(arData)