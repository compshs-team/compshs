"""
Created in 2025
@author: Simon Delarue <simon.delarue@telecom-paris.fr>
"""
import spacy


def is_zero(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError(f'Expected an integer but got {type(value).__name__}.')
    else:
        return value == 0


def load_lang(lang: str = 'en_core_web_sm'):
    """Load (trained) Spacy pipeline.

    Parameters
    ----------
    lang: str
        Spacy pipeline name (default is the english pipeline `en_core_web_sm`).

    Returns
    -------
    Trained spacy pipeline, otherwise blank minimal pipeline.
    """
    try:
        return spacy.load(lang)
    except OSError:
        print(f'Error: Could not load spacy pipeline {lang}.')
        print(f'Downloading the Spacy pipeline...')
        spacy.cli.download(lang)

        try:
            return spacy.load(lang)
        except Exception as e:
            print(f'Failed to load the Spacy pipeline: {e}.')
            print(f'Fall back to minimal blank pipeline, i.e. tokenizer only.')
            return spacy.blank(lang)
