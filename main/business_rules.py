import string

def _normalize_words(text):
    """Remove puctuations from the words (removing also isolated puctuations)."""

    punct_translate_table = str.maketrans('', '', string.punctuation)
    return text.translate(punct_translate_table)


def word_counter(text):
    """Counts words in text."""

    return len(_normalize_words(text).split())


# TODO:
#   A word counting with more precise control can be achieved using Python NLTK's `tokenize()`,
#   including remotion of binding word, with a good data set according with the language used.
#   For this simple challenge I think this huge module doesn't make sense.
