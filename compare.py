import csv
import gensim
import sys
import os

from generate_model import get_dict_model, get_glove_model

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

from gensim.models import KeyedVectors




def update_statistics(diff,current_pair,pair_diff_list,running_diff,seen_differences):
    running_diff += diff
    rounded_diff = round(diff,2)
    if rounded_diff not in seen_differences and rounded_diff != 0.0:
        pair_diff_list.append(((current_pair[0],current_pair[1]),rounded_diff))
        seen_differences.append(rounded_diff)
    return running_diff, pair_diff_list, seen_differences


def takeSecondElement(words_and_diff_tuple):
    return words_and_diff_tuple[1]


def do_comparison(model):
    if not os.path.exists("./results"):
        os.makedirs("./results")
    with open("./test_words.csv") as csvfile:
        pairs = csv.reader(csvfile, delimiter=',')
        next(pairs)      # skip first line of the file (column headings)
        with open("./results/results.txt","w") as result:
            result.write("%-35s %-15s %-15s %s\n" % ("Word pairs","Subject score","Model score", "Difference"))
            
            # Initialize statistical variables
            running_diff, max_diff = (0,0)
            min_diff = 10
            pair_diff_list = []
            seen_differences = []

            for count ,pair in enumerate(pairs):
                # Calculate the cosine similarity and round it up
                cosine_sim = model.similarity(str(pair[0]),str(pair[1]))
                cosine_sim = round(cosine_sim,2)

                # normalize the cosine similarity scale to (0 to 1) and multiply by 10
                # to match the human score scale exactly
                normalized_sim = 10 * ((cosine_sim + 1) / (1.0 + 1.0))

                # Calculate the difference between model and human scores
                # and update statistical variables
                diff = abs(float(pair[2]) - float(normalized_sim))
                running_diff, pair_diff_list, seen_differences = update_statistics(diff,pair,pair_diff_list,running_diff,seen_differences)

                result.write("%-35s %-15s %-15s %s\n" % (str((pair[0],pair[1])),str(pair[2]),str(normalized_sim),str(diff)))
            
            # Some additional operations for the statistics
            # Calculate avg. diff, sort the list of pair-diff tuples,
            # build the strings for top 3 highest and smallest and for the max and min differences
            avg_diff = round(running_diff / count,2)
            
            pair_diff_list.sort(key=takeSecondElement)
            top_3_highest = str(pair_diff_list[-1]) + ",\n" + "\t"*9 + str(pair_diff_list[-2]) + ",\n" + "\t"*9 + str(pair_diff_list[-3])
            top_3_smallest = str(pair_diff_list[0]) + ",\n" + "\t"*13 + str(pair_diff_list[1]) + ",\n" + "\t"*13 + str(pair_diff_list[2])

            max_diff = str(pair_diff_list[-1])
            min_diff = str(pair_diff_list[0])


            # Write the statistic summary at the end of the file 
            result.write("\n\n%s\n%s\n%s\n" % ("Average difference: " + str(avg_diff),"Max difference: " + max_diff,
                "Min(non-zero) difference: " + min_diff))

            result.write("\n\n%s\n\n\n%s\n" % ("Top 3 pairs with largest difference:" + top_3_highest
                ,"Top 3 pairs with the smallest(non-zero) difference: " + top_3_smallest))


def compare_most_similar():
    dict_model = gensim.models.Word2Vec.load("./models/dict_model")
    glove_model = KeyedVectors.load("./models/glove_model_6B_50d")

    word = ""
    while word != "quit":
        word = raw_input("\nEnter word: ").lower()
        words = word.split()
        if words[0] == "quit" and len(words) == 1:
            break
        
        # If the user entered only 1 word, show the top 5 most similar words to it
        elif len(words) == 1:
            try:
                synonym_dict = dict_model.similar_by_word(str(word), topn=5)
                synonym_glove = glove_model.similar_by_word(str(word), topn=5)
            except Exception:
                print("Error! The word could not be found in the corpus. Perhaps try a different word?")
                continue
            # Show results
            print("The top 5 most similar words are:\n")
            for n,_ in enumerate(synonym_dict):
                # print(str(n+1) + ")\t(Word2Vec) " + str(synonym_dict[0]) + "\t\t(GloVe) " + str(synonym_glove[0]))
                print("%s)   (Word2Vec) %-20s (GloVe) %s\n" % (n+1,synonym_dict[n][0],synonym_glove[n][0]))



def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)
    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()



def main():
    if len(sys.argv) != 2:
        print("Enter either   dict   or   glove   for the respective source.")        
    else:
        if sys.argv[1] == "dict":
            # Generate model from the dictionary and pass it to the comparison function
            model = get_dict_model()

            # Uncomment to produce a plot of embeddings
            # !!! Takes ~10mins !!!
            # tsne_plot(model)
            
            do_comparison(model)
        elif sys.argv[1] == "glove":
            # Generate model from the pre-trained GloVe vectors and pass it to the comparison function
            model = get_glove_model()
            do_comparison(model)
        else:
            print("Enter either   dict   or   glove   for the respective source.")




if __name__ == "__main__":
    main()