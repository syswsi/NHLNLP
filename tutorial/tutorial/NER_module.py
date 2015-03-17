import csv
import nltk

activity_descriptions = []
activity_titles = []
#using open instead of codecs.open fixed the problem
with open(r"items.csv", "rU") as f:
    reader = csv.reader(f)
    for line in reader:
        article_title = line[0]
        article_text = line[1].decode('utf-8', 'ignore').encode('ascii', 'ignore') #to deal with tokenizer encoding problem
        tokens = nltk.word_tokenize(article_text)
        pos_tags = nltk.pos_tag(tokens)
        chunks =  nltk.ne_chunk(pos_tags, binary=False)
        print(chunks)
