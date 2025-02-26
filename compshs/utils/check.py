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
    try:
        return spacy.load(lang)
    except OSError:
        print(f'Error: Could not load spacy model {lang}.')
        print(f'Downloading the model...')
        spacy.cli.download(lang)

        try:
            return spacy.load(lang)
        except Exception as e:
            print(f'Failed to load the model: {e}.')
            print(f'Fall back to minimal blank model, i.e. tokenizer only.')
            return spacy.blank(lang)
