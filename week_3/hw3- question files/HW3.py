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
def remove_punctuations(text):  # check if remove_punctuations or remove_punctuation
    """takes a string, returns the string without punctuations from the punctuations list"""
    text_without_punctuations = text
    for letter in text:
        if letter in punctuations:
            text_without_punctuations = text_without_punctuations.replace(letter, " ")
    return text_without_punctuations


def remove_digits(text):
    """takes a string, returns the string without digits"""
    text_without_digits = text
    for letter in text:
        if letter.isdigit():
            text_without_digits = text_without_digits.replace(letter, " ")
    return text_without_digits


def remove_spaces(text):
    """takes a string, returns the string without a sequence of white spaces"""
    format_text = ""
    space_count = 0
    for letter in text:
        if letter == " " and space_count == 0:
            format_text += letter
            space_count += 1
        elif letter == " ":
            space_count += 1
            continue
        else:
            space_count = 0
            format_text += letter
    return format_text


def remove_stopwords(words_list):
    """takes a list of words, returns the list without words from stop_words"""
    format_list = words_list.copy()
    for word in words_list:
        if word in stop_words:
            format_list.pop(format_list.index(word))
    return format_list


def remove_stopwords_inplace(words_list):
    """takes a list of words, returns the list without words from stop_words"""
    counter = 0
    for i in range(len(words_list)):
        if words_list[counter] in stop_words:
            words_list.pop(counter)
            counter -= 1
        counter += 1
    return words_list


def stem_word(word):
    """takes a string that represents word, returns a string edited by question rules"""
    if word[-3:] == "ies":
        return word[:-3] + "y"
    elif word[-4:] == "sses":
        return word[:-4] + "ss"
    elif word[-1:] == "s":
        return word[:-1]
    elif word[-2:] == "ed":
        return word[:-2]
    elif word[-3:] == "ing":
        return word[:-3]
    else:
        return word


def stemming(words_list):
    """takes a list of words, returns a list of edited words by their ends"""
    format_word_list = []
    for word in words_list:
        format_word_list.append(stem_word(word))
    return format_word_list


def preprocessing(text):
    """takes text, returns a list of format words"""
    format_text = remove_punctuations(text)
    format_text = remove_digits(format_text)
    format_text = remove_spaces(format_text)
    format_text = format_text.lower()
    format_text = format_text.split(" ")
    format_text = remove_stopwords(format_text)
    format_text = stemming(format_text)
    while "" in format_text:
        format_text.remove("")
    return format_text


###### Part B #######
def get_documents_data(corpus):
    """takes dictionary that represents corpus, returns a dictionary that represents documents data"""
    documents_data = {}
    for key, value in corpus.items():
        documents_data[key] = len(preprocessing(value))
    return documents_data


def create_inverted_index(corpus):
    """takes dictionary that represents corpus, returns a dictionary that represents inverted index"""
    inverted_index = {}
    for text_id, text in corpus.items():
        text_words = preprocessing(text)
        for word in text_words:
            if word not in inverted_index.keys():
                inverted_index[word] = {}
                inverted_index[word][text_id] = 1
            else:
                if text_id not in inverted_index[word].keys():
                    inverted_index[word][text_id] = 1
                else:
                    inverted_index[word][text_id] += 1
    return inverted_index


def add_to_data(inverted_index, documents_data, doc_id, text):
    """takes inverted_index, documents_data, doc_id and text, returns inverted_index, documents_data with new data"""
    new_doc = {doc_id: text}
    new_doc_inverted_index = create_inverted_index(new_doc)
    new_doc_data = get_documents_data(new_doc)
    for word, value in new_doc_inverted_index.items():
        if word not in inverted_index.keys():
            inverted_index[word] = {}
            inverted_index[word].update(new_doc_inverted_index[word])
        else:
            inverted_index[word].update(new_doc_inverted_index[word])
    documents_data.update(new_doc_data)
    return inverted_index, documents_data


def remove_from_data(inverted_index, documents_data, doc_id):
    """takes inverted_index, documents_data, doc_id and text, returns inverted_index, documents_data without doc data"""
    documents_data.pop(doc_id)
    for word, value in list(inverted_index.items()):
        if doc_id in value:
            inverted_index[word].pop(doc_id)
        if not value:
            inverted_index.pop(word)
    return inverted_index, documents_data


###### Part C #######
def calculate_tf_idf(word, doc_id, inverted_index, documents_data):
    """takes word, doc_id, inverted_index, documents_data, returns tf_idf"""
    number_of_documents = len(documents_data)
    number_of_documents_with_word = len(inverted_index[word])
    number_of_word_in_document = 0
    total_terms_in_doc = documents_data[doc_id]
    if doc_id in inverted_index[word]:
        number_of_word_in_document = inverted_index[word][doc_id]
    tf_const = number_of_word_in_document / total_terms_in_doc
    idf_const = math.log2(number_of_documents / number_of_documents_with_word)
    return round(tf_const * idf_const, 3)



def get_scores_of_relevance_docs(query, inverted_index, documents_data):
    """takes query, inverted_index, documents_data returns total tf_idf per doc"""
    scores_of_relevance_docs = {}
    for doc_id in documents_data.keys():
        total_tf_idf_doc = 0
        for word in query:
            if word not in inverted_index.keys():
                continue
            total_tf_idf_doc += calculate_tf_idf(word, doc_id, inverted_index, documents_data)
        if total_tf_idf_doc != 0:
            scores_of_relevance_docs[doc_id] = round(total_tf_idf_doc, 3)
    return scores_of_relevance_docs



###### Part D #######
def menu(corpus):
    pass
    # choice = input('Choose an option from the menu:\n\t(1) Insert a query.\n\t(2) Add document to corpus.\n\t(3) Calculate TF-IDF Score for a word in a document.\n\t(4) Delete a document from the corpus.\n\t(5) Exit.\nYour choice: ')
    # query_choice = input('Choose the type of results you would like to retrieve:\n\t(A) All relevant documents.\n\t(B) The most relevant document.\n\t(C) Back to the main menu.\nYour choice: ')
