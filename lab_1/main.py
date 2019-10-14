"""
Labour work №1
Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    if type(text) != str or text == "" or text is None:
        return {}
    word_freq = {}
    for sign in text:
        if not sign.isalpha():
            text = text.lower()
            text = text.replace(sign, ' ')
            text_list = text.split()
            for word in text_list:
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
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

def get_top_n(frequencies, top_n):
    word_frequencies = list(frequencies.items())
    word_frequencies.sort(key=lambda x: x[1], reverse=True)
    top_words = []
    if top_n > 0:
        for i in word_frequencies:
            top_words += i
            top_n -= 1
            if top_n == 0:
                break
        for i in top_words:
            if type(i) is int:
                top_words.remove(i)
        top_words = tuple(top_words)
        return top_words
    else:
        top_words = tuple(top_words)
        return top_words

