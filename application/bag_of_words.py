from nltk.stem import PorterStemmer
import numpy
import re


class BagOfWords:

    def __init__(self, loaded_data):
        self.ps = PorterStemmer()
        load_data = loaded_data
        self.data = load_data.get_data()
        self.vocab = self.__build_vocab(self.data)


    def get_bag_of_words_vector(self, record_id: str):
        if record_id in self.data:
            title = self.data[record_id]
            words = self.__word_extraction(title)

            bag_vector = numpy.zeros(len(self.vocab))
            for w in words:
                for i, word in enumerate(self.vocab):
                    if word == w:
                        bag_vector[i] += 1
            # print("{0}\n{1}\n".format(self.data[id], numpy.array(bag_vector)))

            bag_vector = bag_vector.tolist()
            return [int(count) for count in bag_vector]



    def __word_extraction(self, sentence: str) -> list:
        ignore = ['a', "the", "is"]
        words = re.sub("[^\w]", " ", sentence).split()
        cleaned_text = [w for w in words if w not in ignore]
        return cleaned_text

    def __build_vocab(self, data: dict) -> list:
        vocab_set = set()
        for record_id in data:
            title = str(data[record_id])
            title = self.__stem_title(title)
            words = title.split()
            ignore = ['a', 'the', 'is']
            for word in words:
                if word not in ignore:
                    vocab_set.add(word)

        vocab = list(vocab_set)

        return vocab

    def __stem_title(self, title: str) -> str:
        new_title = []
        for word in title.split():
            new_title.append(self.ps.stem(word))

        return ' '.join(new_title)


