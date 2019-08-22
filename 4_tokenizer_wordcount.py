from textblob import TextBlob

data = open('data.txt')
textData = data.read()
blobData = TextBlob(textData)
print(blobData.word_counts)
# iT will return how many times word is used (count of words)