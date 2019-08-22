from textblob import TextBlob

data = open('data.txt')
textData = data.read()
blobData = TextBlob(textData)
print(blobData.words)