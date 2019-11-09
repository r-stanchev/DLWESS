# Final Year Project

**This is the Github repository for my final year project.**

**Author**: Radomir Stanchev  
**Title**: Deep Learning of Word Embeddings for Semantic Search  



To use any of the services of this project, follow the following steps:  
1.  Clone the repository
2.  Execute *pre_processing_script.py* (This script takes the raw dictionary, cleans and reformats it)

  
<br />
  
The available services are as follows:  
*  *keyword_matcher.py* - allows you to see all definitions of the input word, that are available in the dictionary;
*  *generate_model.py* - generates a model form either the reformatted dictionary or the pre-trained word vectors;  
When executing, add "dict" or "glove" as command-line arguments to generate the respective model;  
The pre-trained word vectors used for this project can be downloaded from [here](http://nlp.stanford.edu/data/glove.6B.zip);  
This service **must** be executed before *embeddings.py* and *compare.py*
*  *embeddings.py* - allows you to see semantically similar words to the one you have entered;  
Again, add "dict" as a command-line argument to use the model buit using the dictionary or "glove" to use the pre-trained one;  
This service has other features as well. They are displayed in the beginning, when you run the file.
*  *compare.py* - runs an evaluation script on either one of the models, hence add "dict" or "glove" as command-line arguments;  
  
**A model is evaluated by comapring the cosine similarity it outputs with the human-assigned similarity value(mode information can be found [here](http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/).**     
**More specifically, for each word in the test set, the model's cosine similarity is subtracted from the human score.**  

*  For example, the words "doctor" and "professor" have a cosine similarity of 7.45(on a 0 to 10 scale) and a human score of 6.62(on a 0 to 10 scale).  
The absolute difference between the two is 0.83, hence the score for that word pair is 0.83. With the pair (coast,forest), the cosine similarity is 5.85,
the human score, 3.15, therefore the difference would be 2.7 and so on

**Apart from the result for each individual word pair in the test set, an average difference value is also recorded.**  
