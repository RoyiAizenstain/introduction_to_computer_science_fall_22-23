import math

# Global Variables
stop_words = [
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "have",
    "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "with",
    "i", "you", "we", "he", "she", "it", "my", "your", "our", "his", "her", "its", "their",
    "this", "these", "those", "here", "there", "where", "when", "how", "all", "any",
    "many", "much", "more", "most", "other", "some", "such"
]
punctuations = ['.', ',', ':', ';', '!', '?', '"', "'", '(', ')', '[', ']', '{', '}',
                '-', '/', '\\', '&', '@', '#', '$', '%', '*', '_', '~']


corpus = {1: "The cat played the piano",
          2: "5 cats are playing ball in the backyard!",
          3: "The grand piano is in the house"}


####### Part A #########
def royi():
    print("")

def remove_punctuation(text):
    pass


def remove_digits(text):
    pass


def remove_spaces(text):
    pass


def remove_stopwords(words_list):
    pass


def stemming(words_list):
    pass


def preprocessing(text):
    pass


###### Part B #######
def get_documents_data(corpus):
    pass


def create_inverted_index(corpus):
    pass


def add_to_data(inverted_index, documents_data, doc_id, text):
    pass


def remove_from_data(inverted_index, documents_data, doc_id):
    pass


###### Part C #######
def calculate_tf_idf(word, doc_id, inverted_index, documents_data):
    pass


def get_scores_of_relevance_docs(query, inverted_index, documents_data):
    pass


###### Part D #######
def menu(corpus):
    pass
        # choice = input('Choose an option from the menu:\n\t(1) Insert a query.\n\t(2) Add document to corpus.\n\t(3) Calculate TF-IDF Score for a word in a document.\n\t(4) Delete a document from the corpus.\n\t(5) Exit.\nYour choice: ')
        # query_choice = input('Choose the type of results you would like to retrieve:\n\t(A) All relevant documents.\n\t(B) The most relevant document.\n\t(C) Back to the main menu.\nYour choice: ')


