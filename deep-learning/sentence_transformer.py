# pip install sentence_transformers
# The first time this script is run, the sentence_transformers library will
# download a pre-trained model.

# This example is derived from examples at https://www.sbert.net/docs/quickstart.html

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ['The IRS has new tax laws.',
             'Congress debating the economy.',
             'The polition fled to South America.',
             'Canada and the US will be in the playoffs.',
             'The cat ran up the tree',
             'The meal tasted good but was expensive and perhaps not worth the price.']

#Sentences are encoded by calling model.encode()
sentence_embeddings = model.encode(sentences)

#Compute cosine similarity between all pairs
cos_sim = util.cos_sim(sentence_embeddings, sentence_embeddings)

#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append([cos_sim[i][j], i, j])

#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

print("Top-8 most similar pairs:")
for score, i, j in all_sentence_combinations[0:8]:
    print("{} \t {} \t {:.4f}".format(sentences[i], sentences[j], cos_sim[i][j]))
