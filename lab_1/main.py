"""
Labour work №1
Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    if type(text) != str or text == "" or text is None:
        return {}
    else:
        text = text.lower()
        text = text.split()
        signs = '.,:;!?-()"«»<>0123456789@$%*&^%~\'\n'
        word_freq = {}
        for sign in text:
            word = sign.strip(signs)
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1
        if '' in word_freq:
            del word_freq['']
        return word_freq
    
def filter_stop_words(frequencies, stop_words):
    new_dict = {}
    if frequencies == {} or frequencies is None:
        return {}
    if stop_words == () or stop_words is None:
        return frequencies
    if frequencies is None and stop_words is None:
        return {}
    for key, value in frequencies.items():
        if key == str(key):
            if key not in stop_words:
                new_dict.update({key: value})
    return new_dict

def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    frequencies = {}
    new_text = ''
    if text is None:
        return frequencies
    if not isinstance(text, str):
        text = str(text)
    for symbol in text:
        if symbol.isalpha() or symbol == ' ':
            new_text += symbol
    new_text = new_text.lower()
    words = new_text.split()
    for key in words:
        key = key.lower()
        if key in frequencies:
            value = frequencies[key]
            frequencies[key] = value + 1
        else:
            frequencies[key] = 1
    return frequencies


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    if frequencies is None:
        frequencies = {}
        return frequencies
    for word in list(frequencies):
        if not isinstance(word, str):
            del frequencies[word]
    if not isinstance(stop_words, tuple):
        return frequencies
    for word in stop_words:
        if not isinstance(word, str):
            continue
        if frequencies.get(word) is not None:
            del frequencies[word]
    return frequencies


def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    :param
    """
    if not isinstance(top_n, int):
        frequencies = ()
        return frequencies
    if top_n < 0:
        top_n = 0
    elif top_n > len(frequencies):
        top_n = len(frequencies)
    top_words = sorted(frequencies, key=lambda x: int(frequencies[x]), reverse=True)
    best = tuple(top_words[:top_n])
    return best


def read_from_file(path_to_file: str, lines_limit: int) -> str:
    """
    Read text from file
    """
    file = open(path_to_file)
    counter = 0
    text = ''
    if file is None:
        return text
    for line in file:
        text += line
        counter += 1
        if counter == lines_limit:
            break
    file.close()
    return text


def write_to_file(path_to_file: str, content: tuple):
    """
    Creates new file
    """
    file = open(path_to_file, 'w')
    for i in content:
        file.write(i)
        file.write('\n')
    file.close()
