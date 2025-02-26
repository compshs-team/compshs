from compshs.text.base import BaseText
from compshs.utils import load_lang


class Preprocess(BaseText):
    """ Preprocessing of a corpus of documents.

    Attributes
    ----------
    lang: str
        Spacy language model name (`en_core_web_sm`).
    exclude_stop_words: bool
        If ``True``, exclude stopwords (default).
    exclude_punctuation: bool
        If ``True``, exclude punctuation (default).
    lemmatize: bool
        If ``True``, lemmatize tokens (default).
    batch_size: int
        Number of documents to process in each batch (default=10).
    nlp:
        Spacy model build upon `lang` parameter.
    """
    def __init__(self, lang: str = 'en_core_web_sm', exclude_stop_words: bool = True, exclude_punctuation: bool = True,
                  lemmatize: bool = True, batch_size: int = 10):
        super().__init__()
        self.lang = lang
        self.exclude_stop_words = exclude_stop_words
        self.exclude_punctuation = exclude_punctuation
        self.lemmatize = lemmatize
        self.batch_size = batch_size
        self.nlp = None

    def fit(self):
        """Fit algorithm to the data."""
        self.nlp = load_lang(self.lang)
        return self

    def transform(self, corpus: list) -> list:
        """ Preprocess corpus.

        Parameters
        ----------
        corpus: list
            List of documents.

        Returns
        -------
        List of preprocessed documents.
        """
        transformed_corpus = []

        for doc in self.nlp.pipe(corpus, batch_size=self.batch_size):
            tokens = []
            for token in doc:
                if (self.exclude_stop_words and token.is_stop) or (self.exclude_punctuation and token.is_punct):
                    continue

                transformed_token = token.lemma_ if self.lemmatize else token.text
                tokens.append(transformed_token)

            transformed_corpus.append(tokens)

        return transformed_corpus
