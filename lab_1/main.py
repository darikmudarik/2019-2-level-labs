"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    if type(text) != str or text == "" or text is None:
        print('Error: enter text(str).')
    else:
        text = text.lower()
        text = text.split()
        signs = '.,:;!?()"«»<>'
        word_freq = {}
        for sign in text:
            word = sign.strip(signs)
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1

        return word_freq

def filter_stop_words(frequencies, stop_words):
    for element in stop_words:
        if element in frequencies:
            del frequencies[element]
    return frequencies

def get_top_n(frequencies, top_n):
    if frequences == {} or n <= 0:
        return ()
    word_frequencies = list(frequencies.items())
    word_frequencies.sort(key=lambda x: x[1], reverse=True)
    top_words = []
    for i in range(top_n):
        top_words.append(word_frequencies[i][0])
    top_words = tuple(top_words)
    return top_words
