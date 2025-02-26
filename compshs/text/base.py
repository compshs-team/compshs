from abc import ABC


class BaseText(ABC):
    """ Base class for text algorithms.
    """
    def __init__(self):
        """Fit algorithm to the data."""
        pass

    def transform(self, *args, **kwargs):
        """Transform the data."""
        pass
