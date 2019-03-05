from data import *
import nltk
from nltk.tokenize import RegexpTokenizer
import gensim



# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# Tokenizer which removes all but alphabetical characters and numbers
tokenizer = RegexpTokenizer(r'\w+')

# Make every word lowercase and tokenize each line 
for t,row in enumerate(data):
    for i,element in enumerate(row):
        row[i] = element.lower()
    data[t] = tokenizer.tokenize(str(data[t]))


# Train our model
model = gensim.models.Word2Vec(data,min_count=1,size=10)

res = model.similarity('marriage', 'wedding')
print(res)
