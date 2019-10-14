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
        signs = '.,:;!?-()"«»<>0123456789\'\n'
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

text = """ 52 45 45456How did she keep her eyes that way, thought Scarlett, looking at her enviously. She knew her own eyes sometimes had the look of a hungry cat. What was it Rhett had said once about Melanie's eyes -- some foolishness about them being like candles? Oh, yes, like two good deeds in a naughty world. Yes, they were like candles, candles shielded from every wind, two soft lights glowing with happiness at being home again among her friends.
The little house was always full of company. Melanie had been a favorite even as a child and the town flocked to welcome her home again. Everyone brought presents for the house, bric-a-brac, pictures, a silver spoon or two, linen pillow cases, napkins, rag rugs, small articles which they had saved from Sherman and treasured but which they now swore were of no earthly use to them.
Old men who had campaigned in Mexico with her father came to see her, bringing visitors to meet "old Colonel Hamilton's sweet daughter." Her mother's old friends clustered about her, for Melanie had a respectful deference to her elders that was very soothing to dowagers in these wild days when young people seemed to have forgotten all their manners. Her contemporaries, the young wives, mothers and widows, loved her because she had suffered what they had suffered, had not 'become embittered and always lent them a sympathetic ear. The young people came, as young people always come, simply because they had a good time at her home and met there the friends they wanted to meet.
"""
stop_words = ('the', 'a', 'to', 'had')
n = 10000

print(get_top_n(filter_stop_words(calculate_frequences(text), stop_words), n))
