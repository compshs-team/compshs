import unittest

from compshs.text.preprocess import Preprocess


class TestPreprocess(unittest.TestCase):

    def setUp(self):
        self.preprocessor = Preprocess(lang='en_core_web_sm')
        self.preprocessor.fit()
        self.corpus = ['The quick brown fox.', 'The dog is lazier.']

    def test_fit(self):
        self.assertIsNotNone(self.preprocessor.nlp, 'Model should be loaded after calling .fit().')

    def test_transform(self):
        # Default settings
        result = self.preprocessor.transform(self.corpus)
        self.assertEqual(len(result), 2)
        for doc in result:
            self.assertTrue(all(isinstance(token, str) for token in doc))
            self.assertNotIn('is', doc)
            self.assertNotIn('.', doc)
            self.assertNotIn('lazier', doc)

        # Including stopwords
        result = self.preprocessor.transform(self.corpus, exclude_stop_words=False)
        self.assertIn('the', result[0])

        # Punctuation included
        result = self.preprocessor.transform(self.corpus, exclude_punctuation=False)
        self.assertIn('.', result[0])

        # Without lemmatization
        result = self.preprocessor.transform(self.corpus, lemmatize=False)
        self.assertEqual(result[1][-1], "lazier")

        # Empty corpus
        result = self.preprocessor.transform([])
        self.assertEqual(result, [])

        # Batch size
        result = self.preprocessor.transform(self.corpus, batch_size=2)
        self.assertEqual(len(result), len(self.corpus))
