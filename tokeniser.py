import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
# import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

# Example abstracts and titles
# documents = [
#     {"title": "Deep Learning for NLP", "abstract": "This paper explores the use of deep learning techniques in natural language processing..."},
#     {"title": "Machine Learning in Healthcare", "abstract": "The application of machine learning in healthcare has been growing rapidly..."},
#     {"title": "information retrieval","abstract": "for thousands of years, people have realized the importance of archiving and finding information. with the advent of computers, it became possible to store large amounts of information; and finding useful information from such collections became a necessity. the field of information retrieval (ir) was born in the 1950s out of this necessity. over the last forty years, the field has matured considerably. several ir systems are used on an everyday basis by a wide variety of users. this article is a brief overview of the key advances in the field of information retrieval, and a description of where the state-of-the-art is at in the field."}
# ]



def tokenise_papers(untokenised_papers):
    papers = []

    for untokenised_paper in untokenised_papers:
        paper = {
            "ss_id": untokenised_paper[0],
            "title": untokenised_paper[1],
            "abstract": untokenised_paper[2],
            "title_tokens": clean_and_tokenise(untokenised_paper[1], "title"),
            "abstract_tokens": clean_and_tokenise(untokenised_paper[2], "abstract", untokenised_paper[0])
        }
        papers.append(paper)
    
    return papers



def clean_and_tokenise(text, text_type, ss_id=None):
    if text_type == "abstract" and text == "no abstract available" or text == "No abstract available":
        # print("ss_id: ", ss_id) 
        return "" # for papers without abstracts, will put more weight into title

    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and numbers
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Apply stemming
    # ps = PorterStemmer()
    # tokens = [ps.stem(word) for word in words]

    # print("tokens: ", tokens)
    return tokens