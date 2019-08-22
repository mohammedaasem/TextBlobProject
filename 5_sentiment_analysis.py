from textblob import TextBlob

data = open('data1.txt')
textData = data.read()
blobData = TextBlob(textData)
print(blobData.sentiment)
print("Polarity is =",blobData.polarity)
print("Subjectivity is =",blobData.subjectivity)