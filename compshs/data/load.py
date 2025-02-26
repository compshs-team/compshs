from glob import glob
from os import makedirs
from os.path import exists
from pathlib import Path
import urllib.request
import zipfile

from compshs.data import Dataset


def load_wpenchiroptera(version: float = 1.0) -> Dataset:
    """ Load the chiroptera dataset.

    Parameters
    ----------
    version: float
        Version number of the dataset (1.0).

    Returns
    -------
    dataset: :class:`Dataset`
        Returned dataset.
    """
    name = 'wp-en-chiroptera'
    distant_file = 'https://perso.telecom-paristech.fr/tviard/SES105/chiro.zip'

    if not exists(Path.home() / '.compshs' / name):
        makedirs(Path.home() / '.compshs' / name)

    with urllib.request.urlopen(distant_file) as f:
        data = f.read()

    with open(Path.home() / '.compshs' / name / f'{name}_{version}.zip', 'wb+') as f_write:
        f_write.write(data)

    documents = []

    with zipfile.ZipFile(Path.home() / f'.compshs/{name}/{name}_{version}.zip', 'r') as zip_ref:
        zip_ref.extractall(Path.home() / f'.compshs/{name}/')

    for file in glob(f'{str(Path.home())}/.compshs/{name}/chiro/*.txt'):
        with open(file, 'r') as f:
            content = f.read()
            documents.append(content)

    return Dataset(corpus=documents, name=name, version=version)
