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
            return 'UNK'
        if id not in self.storage.values():
            return 'UNK'

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
        for gram in self.gram_frequencies:
            sum_grams = 0
            for gram_i in self.gram_frequencies:
                if gram[:-1] == gram_i[:-1]:
                    sum_grams += self.gram_frequencies[gram_i]
            self.gram_log_probabilities[gram] = math.log(self.gram_frequencies[gram] / sum_grams)
        return self.gram_log_probabilities

    def predict_next_sentence(self, prefix: tuple) -> list:
        future_word = []
        if not isinstance(prefix, tuple) or len(prefix) != self.size - 1:
            return []
        predicted_sentence = list(prefix)
        flag = True
        while flag:
            probabilities_list = []
            for gram in list(self.gram_log_probabilities.keys()):
                if gram[:-1] == prefix:
                    probabilities_list.append(self.gram_log_probabilities[gram])
            if not probabilities_list:
                break
            probabilities_list.sort(reverse=True)
            big_probability = probabilities_list[0]
            for gram, probability in list(self.gram_log_probabilities.items()):
                if big_probability == probability:
                    future_word = gram[-1]
            predicted_sentence.append(future_word)
            new_prefix = list(prefix[1:])
            new_prefix.append(future_word)
            prefix = tuple(new_prefix)
        return predicted_sentence

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
        if not element.isalpha() and element not in '!?. ':
            text = text.replace(element, '')
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
            if word != sentence:
                new_sentence.append(word)
        new_sentence.append('</s>')
        new_sentences.append(new_sentence)
        if ['<s>', '</s>'] in new_sentences:
            new_sentences.remove(['<s>', '</s>'])


    return new_sentences

def start(REFERENCE_TEXT, n, prefix):
    word_storage = WordStorage()
    n_gram_trie = NGramTrie(n)
    corpus = split_by_sentence(REFERENCE_TEXT)
    for element in corpus:
        word_storage.from_corpus(tuple(element))
    encoded_corpus = encode(word_storage, corpus)
    for sentence in encoded_corpus:
        n_gram_trie.fill_from_sentence(tuple(sentence))
    n_gram_trie.calculate_log_probabilities()
    prefix_new = []
    for el in prefix:
        prefix_new.append(word_storage.get_id_of(el))
    final_sentence = n_gram_trie.predict_next_sentence(tuple(prefix_new))
    return(final_sentence)

test_text = 'Mar#y wa$nted, to swim! However, she was afraid of sharks.'
print(split_by_sentence(test_text))
print(start(REFERENCE_TEXT, 2, ('this',)))
