from embeddings import *
import csv
import gensim



'''
IMPORTANT!

-Cases where one of the words in a pair can not be found in the dict, 
are skipped entirely.

-For calculating the min difference, I have skipped the 0-diff cases entirely.

-Saw which words from set1.csv couldn't be looked up in the dictionary and 
created a new test_words set, from which those words are excluded.
Hence, no more need for the try-expect block, since all words in test_words.csv
are defenitely in the dictionary.
'''



model = gensim.models.Word2Vec.load("./models/dict_model")

# model = KeyedVectors.load("./models/glove_model_6B_50d")


def update_statistics(diff,current_pair):
    global pair_diff_list, running_diff
   
    running_diff += diff
    rounded_diff = round(diff,2)
    if rounded_diff not in seen_differences and rounded_diff != 0.0:
        print(rounded_diff)
        pair_diff_list.append(((pair[0],pair[1]),rounded_diff))
        seen_differences.append(rounded_diff)



def takeSecondElement(pair_diff_tuple):
    return pair_diff_tuple[1]


with open("./test_words.csv") as csvfile:
    pairs = csv.reader(csvfile, delimiter=',')
    next(pairs)      # skip first line of the file (column headings)
    with open("results.txt","w") as result:
        result.write("%-35s %-15s %-15s %-15s\n" % ("Pairs","Human result","Model result", "Difference"))
        
        # Initialize statistical variables
        running_diff, max_diff = (0,0)
        min_diff = 10
        pair_diff_list = []
        seen_differences = []

        for count ,pair in enumerate(pairs):
            # Calculate the cosine similarity and round it up
            res = model.similarity(str(pair[0]),str(pair[1]))
            res = round(res,2)

            # normalize the cosine similarity scale to (0 to 1) and multiply by 10
            # to match the human score scale exactly
            normalized_res = 10 * ((res + 1) / (1.0 + 1.0))

            # Calculate the difference between model and human scores
            # and update statistical variables
            diff = abs(float(pair[2]) - float(normalized_res))
            update_statistics(diff,pair)

            
            result.write("%-35s %-15s %-15s %-15s\n" % (str((pair[0],pair[1])),str(pair[2]),str(normalized_res),str(diff)))
        
        # Some additional operations for the statistics
        avg_diff = round(running_diff / count,2)
        
        pair_diff_list.sort(key=takeSecondElement)
        top_3_highest = str(pair_diff_list[-1]) + ", " + str(pair_diff_list[-2]) + ", " + str(pair_diff_list[-3])
        top_3_smallest = str(pair_diff_list[0]) + ", " + str(pair_diff_list[1]) + ", " + str(pair_diff_list[2])

        max_diff = str(pair_diff_list[-1])
        min_diff = str(pair_diff_list[0])


        # Write the statistic summary at the end of the file 
        result.write("\n\n%s\n%s\n%s\n" % ("Average difference: " + str(avg_diff),"Max difference: " + max_diff,
            "Min(non-zero) difference: " + min_diff))

        result.write("\n\n%s\n%s\n" % ("Top 3 pairs with largest difference: " + top_3_highest
            ,"Top 3 pairs with the smallest(non-zero) difference: " + top_3_smallest))
