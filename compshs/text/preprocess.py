from compshs.text.base import BaseText
from compshs.utils import load_lang


class Preprocess(BaseText):
    """ Preprocessing of a textual Dataset.

    Attributes
    ----------
    lang: str
        Spacy language model name (`en_core_web_sm`).
    nlp:
        Spacy model build upon `lang` parameter.
    """
    def __init__(self, lang: str = 'en_core_web_sm'):
        self.lang = lang
        self.nlp = None

    def fit(self):
        """Fit algorithm to the data."""
        self.nlp = load_lang(self.lang)
        return self

    def transform(self, corpus: list, exclude_stop_words: bool = True, exclude_punctuation: bool = True,
                  lemmatize: bool = True, batch_size: int = 10) -> list:
        """ Preprocess corpus.

        Parameters
        ----------
        corpus: list
            List of documents.
        exclude_stop_words: bool
            If ``True``, exclude stopwords (default).
        exclude_punctuation: bool
            If ``True``, exclude punctuation (default).
        lemmatize: bool
            If ``True``, lemmatize tokens (default).
        batch_size: int
            Number of documents to process in each batch (default=10).

        Returns
        -------
        List of preprocessed documents.
        """
        transformed_corpus = []

        for doc in self.nlp.pipe(corpus, batch_size=batch_size):
            tokens = []
            for token in doc:
                if (exclude_stop_words and token.is_stop) or (exclude_punctuation and token.is_punct):
                    continue

                transformed_token = token.lemma_ if lemmatize else token.text
                tokens.append(transformed_token)

            transformed_corpus.append(tokens)

        return transformed_corpus
