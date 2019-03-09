import gensim
from gensim.models import KeyedVectors
import sys
from gensim.scripts.glove2word2vec import glove2word2vec
import os

if sys.argv[1] == "dict":
    # Load a previously saved model
    # In this case this is the model, trained from the dictionary
    model = gensim.models.Word2Vec.load("./mymodel")
elif sys.argv[1] == "glove":
    # Load a previously saved model
    # In this case this is the model, composed using Glove's pre-trained word vectors(6B,50d)
    # path = os.path.dirname(os.path.realpath(""))
    model = KeyedVectors.load("./glove_model_6B_50d")
    


print("\nWelcome to Rado's word similarity service!")
print("\nIf you'd like to learn the synonyms of a particular word - simply enter the word to see which 5 words are the most similar to it.\n")
print("Or, if you'd like to find out how semantically similar two words are - enter the two words to see the similarity percentage.\n")
word = ""
while word != "quit":
    word = raw_input("\nEnter word: ")
    words = word.split()
    if words[0] == "quit" and len(words) == 1:
        break
    elif len(words) == 1:
        print("The top 5 most similar words are:")
        synonims = model.similar_by_word(str(word), topn=5)
        for synonym in synonims:
            print(synonym)
    elif len(words) == 2:
        res = model.similarity(str(words[0]),str(words[1]))
        res = round(res,3)
        print("The cosine similarity between " + str(words[0]) + " and " + str(words[1]) + " is " + str(res))
    else:
        print("Please enter at most 2 words!")
