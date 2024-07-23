import io
from pprint import pprint


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)



    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, "r", encoding="utf-8") as open_file:
                text = open_file.read()
                text = text.lower()
                for punc in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punc, ' ')
                words = text.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        word = word.lower()
        search_result = {}
        list_for_find = self.get_all_words()
        for file_name, words_list in list_for_find.items():
            for index, w in enumerate(words_list):
                if w == word:
                    search_result[file_name] = index + 1
                    break
        return search_result



    def count(self, word):
        word = word.lower()
        count_result = {}
        list_for_count = self.get_all_words()
        for file_name, words_list in list_for_count.items():
            count = words_list.count(word)
            count_result[file_name] = count
        return count_result


finder2 = WordsFinder("Walt Whitman - O Captain! My Captain!.txt")
print(finder2.get_all_words()) # Все слова
print(finder2.find('capitan')) # 3 слово по счёту
print(finder2.count('apitan')) # 4 слова teXT в тексте всего