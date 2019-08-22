from textblob import TextBlob

data = open('data2.txt')
textData = data.read()
blobData = TextBlob(textData)
print(blobData)  # Will return extact data
print(blobData.correct()) # will return correct data