import csv
import gensim

from generate_model import get_dict_model


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
    with open("./test_words.csv") as csvfile:
        pairs = csv.reader(csvfile, delimiter=',')
        next(pairs)      # skip first line of the file (column headings)
        with open("./results/results.txt","w") as result:
            result.write("%-35s %-15s %-15s %s\n" % ("Pairs","Human result","Model result", "Difference"))
            
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




def main():
    # Generate model and pass it to the comparison function
    do_comparison(get_dict_model())



if __name__ == "__main__":
    main()