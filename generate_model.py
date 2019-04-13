from data import *
import nltk
from nltk.tokenize import RegexpTokenizer
import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
import sys





'''
Make every word lowercase, tokenize each line to remove any reamining non alpha-numeric characters,
train the dictionary model and return it
'''
def get_dict_model():
    # Tokenizer which removes all but alphabetical characters and numbers
    tokenizer = RegexpTokenizer("[a-zA-Z]+")

    # Make every word lowercase and tokenize each line 
    for t,row in enumerate(data):
        for i,element in enumerate(row):
            row[i] = element.lower()
        data[t] = tokenizer.tokenize(str(data[t]))

    # Train the model and save it in the current working directory
    model = gensim.models.Word2Vec(data,size=150,window=13,sg=1,min_count=7,hs=1,alpha=0.025)
    return model




'''
Make every word lowercase, tokenize each line to remove any reamining non alpha-numeric characters,
train the model and save it
'''
def create_and_save_model_dict():
    # Tokenizer which removes all but alphabetical characters and numbers
    tokenizer = RegexpTokenizer("[a-zA-Z]+")

    # Make every word lowercase and tokenize each line 
    for t,row in enumerate(data):
        for i,element in enumerate(row):
            row[i] = element.lower()
        data[t] = tokenizer.tokenize(str(data[t]))

    # Train the model and save it in the current working directory
    model = gensim.models.Word2Vec(data,size=150,window=13,sg=1,min_count=7,hs=1,alpha=0.025)
    model.save("./models/dict_model")




'''
Create a model using the pre-trained word vectors, and return it
'''
def get_glove_model():
    glove_file = datapath("glove.6B.50d.txt")
    tmp_file = get_tmpfile("test_word2vec.txt")
    _ = glove2word2vec(glove_file,tmp_file)

    model = KeyedVectors.load_word2vec_format(tmp_file)
    return model




'''
Create a model using the pre-trained word vectors, 
downloaded from     https://nlp.stanford.edu/projects/glove/ 


Note:    When replacing the currently used word vector file, make sure to place it in

/home/csunix/sc16rbs/Documents/Third_Year/Final_Year_Project/code/venv/lib/python2.7/site-packages/gensim/test/test_data

since it is required by the glove2word2vec function call.
'''
def create_and_save_model_glove():
    glove_file = datapath("glove.6B.50d.txt")
    tmp_file = get_tmpfile("test_word2vec.txt")
    _ = glove2word2vec(glove_file,tmp_file)

    model = KeyedVectors.load_word2vec_format(tmp_file)
    model.save("./models/glove_model_6B_50d")


def main():
    if len(sys.argv) != 2:
        print("Enter either   dict   or   glove   for the respective source.")        
    else:
        if sys.argv[1] == "dict":
            create_and_save_model_dict()
        elif sys.argv[1] == "glove":
            create_and_save_model_glove()
        else:
            print("Enter either   dict   or   glove   for the respective source.")




if __name__== "__main__":
    main()


