from data import *
import nltk
from nltk.tokenize import RegexpTokenizer
import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
import sys
import os





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
    model = gensim.models.Word2Vec(data,size=150,window=13,min_count=7,sg=0,hs=1,cbow_mean=1,alpha=0.025)
    return model




'''
Make every word lowercase, tokenize each line to remove any reamining non alpha-numeric characters,
train the model and save it
'''
def create_and_save_model_dict():
    # Create a folder to store the models if one doesn't already exist
    if not os.path.exists("./models"):
        os.makedirs("./models")

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
Create a model using the pre-trained word vectors from  https://nlp.stanford.edu/projects/glove/

Download link: http://nlp.stanford.edu/data/glove.6B.zip 
     

Note: Make sure to palce the files(after extracting the downloaded ZIP file) in the following directory,
in order to be able to use the pre-trained word vectors:

virtual-environment-folder/lib/python2.7/site-packages/gensim/test/test_data

where virtual-environment-folder is the name of your virtual environment folder.
'''
def create_and_save_model_glove():
    # Create a folder to store the models if one doesn't already exist
    if not os.path.exists("./models"):
        os.makedirs("./models")

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


