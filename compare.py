from embeddings import *
import csv
import gensim


model = gensim.models.Word2Vec.load("./models/dict_model")


with open("../externals/WordSim353_test_words/set1.csv") as csvfile:
    pairs = csv.reader(csvfile, delimiter=',')
    next(pairs)     # skip first line of the file
    with open("results.txt","w") as result:
        result.write("%-35s %-35s %-35s\n" % ("Pairs","Human result","Model result"))
        for pair in pairs:
            try:
                res = model.similarity(str(pair[0]),str(pair[1]))
                res = round(res,2)

                # normalize the cosine similarity scale to (0 to 1)
                normalized_res = (res + 1) / (1.0 + 1.0)        
            except Exception:
                normalized_res = "N/A"
            result.write("%-35s %-35s %-35s\n" % (str((pair[0],pair[1])),str(pair[2]),str(normalized_res)))