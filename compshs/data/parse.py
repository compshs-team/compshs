from glob import glob
import os

from compshs.data import Dataset


def from_directory(directory_path: str, dataset_name: str = None) -> Dataset:
    """Load a corpus from a directory containing text files.

    Parameters
    ----------
    directory_path: str
        Path to the directory containing text files (.txt).
    dataset_name: str
        Dataset name. Directory name is used if not specified.
    """
    directory_path = os.path.expanduser(directory_path)
    txt_files = glob(os.path.join(directory_path, "*.txt"))

    corpus = []
    for file_path in txt_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            corpus.append(f.read())

    if dataset_name is None:
        dataset_name = os.path.basename(os.path.normpath(directory_path))

    return Dataset(name=dataset_name, corpus=corpus)
