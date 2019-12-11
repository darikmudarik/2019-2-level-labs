"""
Labour work #3
 Building an own N-gram model
"""

import math

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:

    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if type(word) == str and word not in self.storage:
            self.storage[word] = len(self.storage)
            return self.storage[word]
        return -1

    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage.get(word)
        return -1

    def get_original_by(self, id: int) -> str:
        if type(id) == int:
            for key, value in self.storage.items():
                if value == id:
                    return key
        else:
            return str(None)
        if id not in self.storage.values():
            return str(None)

    def from_corpus(self, corpus: tuple):
        if type(corpus) == tuple:
            for el in corpus:
                self.put(el)
            return self.storage

class NGramTrie:

    def __init__(self, n):

        self.size = n
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if type(sentence) != tuple or len(sentence) < self.size or sentence is None:
            return 'ERROR'
        num = self.size
        for i, j in enumerate(sentence):
            n_gram = sentence[i:num]
            if len(n_gram) is self.size and n_gram not in self.gram_frequencies:
                self.gram_frequencies[n_gram] = 1
            elif n_gram in self.gram_frequencies:
                self.gram_frequencies[n_gram] += 1
            num += 1
        return 'OK'

    def calculate_log_probabilities(self):
        for n_gram in self.gram_frequencies:
            finded_part = n_gram[:self.size - 1]
            n_gram_frequency = self.gram_frequencies[n_gram]
            n_grams_frequency = 0
            for n_grams in self.gram_frequencies:
                compared_part = n_grams[:self.size - 1]
                if compared_part == finded_part:
                    n_grams_frequency += self.gram_frequencies[n_grams]
            probability = n_gram_frequency / n_grams_frequency
            self.gram_log_probabilities[n_gram] = log(probability)

    def predict_next_sentence(self, prefix: tuple) -> list:
        sentence = []
        if type(prefix) == tuple and len(prefix) == self.size + 1 and prefix:
            sentence.extend(prefix)
            n_grams = list(self.gram_log_probabilities.keys())
            prefixes = [gram[:-1] for gram in n_grams]
            while prefix in prefixes:
                with_prefix = [gram for gram in n_grams if gram[:-1] == prefix]
                values = [value for key, value in self.gram_log_probabilities.items() if key in with_prefix]
                ind = values.index(max(values))
                sentence.append(with_prefix[ind][-1])
                prefix = tuple(sentence[-(self.size - 1):])
        return sentence

def encode(storage_instance, corpus) -> list:
    code_list = []
    for sentence in corpus:
        code_sentence = []
        for word in sentence:
            code_word = storage_instance.get_id_of(word)
            code_sentence.append(code_word)
        code_list.append(code_sentence)
    return code_list

def split_by_sentence(text: str) -> list:
    if type(text) != str or text is None or ' ' not in text:
        return []
    for element in text:
        if not element.isalpha() and element not in '!?.':
            text = text.replace(element, ' ')
    for element in text:
        if element in '!?':
            text = text.replace(element, '.').lower()
            text += ' '
    sentences = text.split('.')
    new_sentences = []
    for element in sentences:
        new_sentence = ['<s>']
        sentence = element.split()
        for word in sentence:
            if word != sentence or word != '':
                new_sentence.append(word)
        new_sentence.append('</s>')
        new_sentences.append(new_sentence)


    return new_sentences
