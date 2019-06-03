import nltk
from nltk import word_tokenize

stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
stopwords.append("http")

# lemmatize by pos verb, noun or adv
def lemmatize(word):
    """ Lemmatize using wordnet
    Parameters:
        word (string): Word to lemmatize
    Returns:
        Lemmatized word
    """

    lemma = lemmatizer.lemmatize(word,'v')
    
    if lemma == word:
        lemma = lemmatizer.lemmatize(word,'n')
        
    if lemma == word:
        lemma = lemmatizer.lemmatize(word,'a')
        
    return lemma

def preprocess_raw(corpus):
    """ Clean the document using nltk library
    Parameters:
        corpus (string): text to preprocess
    Returns:
        Document cleaned
    """
    new_corpus=list()
    for post in corpus:
        for document in post.split("|||"):
            for word in word_tokenize(document):
                    new_word=word.lower()
                    if word.isalpha() and new_word not in stopwords:
                        new_word = lemmatize(new_word)
                        if new_word not in stopwords:
                            new_corpus.append(new_word)
                
def preprocess(corpus):
    """ Clean the document using nltk library
    Parameters:
        corpus (list): words to preprocess
    Returns:
        Corpus cleaned
    """
    new_corpus=list()
    
    for word in corpus:
        new_word=word.lower()
        if word.isalpha() and new_word not in stopwords:
            new_word = lemmatize(new_word)
            if new_word not in stopwords:
                new_corpus.append(new_word)    
    return new_corpus