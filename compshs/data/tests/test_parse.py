import os
import tempfile
import unittest

from compshs.data.base import Dataset
from compshs.data.parse import from_directory


class TestPreprocess(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.dir_path = self.test_dir.name
        self.file_contents = {'file1.txt': 'The quick brown fox.', 'file2.txt': 'The lazier dog.'}
        for filename, content in self.file_contents.items():
            with open(os.path.join(self.dir_path, filename), 'w', encoding='utf-8') as f:
                f.write(content)

    def test_from_directory_with_names(self):
        dataset_name = 'xyz'
        dataset = from_directory(self.dir_path, dataset_name)

        self.assertIsInstance(dataset, Dataset)
        self.assertEqual(dataset.name, 'xyz')
        self.assertEqual(len(dataset.corpus), len(self.file_contents))
        self.assertCountEqual(dataset.corpus, list(self.file_contents.values()))

    def test_from_directory_without_names(self):
        dataset = from_directory(self.dir_path)

        self.assertIsInstance(dataset, Dataset)
        self.assertEqual(dataset.name, os.path.basename(self.dir_path))
        self.assertEqual(len(dataset.corpus), len(self.file_contents))
        self.assertCountEqual(dataset.corpus, list(self.file_contents.values()))

    def test_from_directory_empty(self):
        empty_dir = tempfile.TemporaryDirectory()
        dataset = from_directory(empty_dir.name, 'empty')

        self.assertIsInstance(dataset, Dataset)
        self.assertEqual(dataset.name, 'empty')
        self.assertEqual(len(dataset.corpus), 0)
        empty_dir.cleanup()
