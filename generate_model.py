from data import *
import nltk
from nltk.tokenize import RegexpTokenizer
import gensim


'''
Make every word lowercase, tokenize each line, train the model and save it
'''
def create_model():
    # Tokenizer which removes all but alphabetical characters and numbers
    tokenizer = RegexpTokenizer(r'\w+')

    # Make every word lowercase and tokenize each line 
    for t,row in enumerate(refined_data):
        for i,element in enumerate(row):
            row[i] = element.lower()
        refined_data[t] = tokenizer.tokenize(str(refined_data[t]))

    # Train the model and save it in the current working directory
    model = gensim.models.Word2Vec(refined_data,min_count=1,size=10)
    model.save("./mymodel")

