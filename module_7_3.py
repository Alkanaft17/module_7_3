class WordsFinder:

    def __init__(self, *files):
        self.file_names = [*files]

    def get_all_words(self):
        all_words = {}  # пустой словарь
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, encoding='utf-8') as file_txt:
                list_ = list() # список слов в файле
                for text in file_txt: # цикл для строк файла
                    text = text.lower()
                    for simbol in punctuation:
                        text = text.replace(simbol, '') # замена символов с списке punctuation на '' (удаление символов)
                    list_.extend(text.split())
            all_words[file] = list_
        return all_words

    def find(self, word):
        dict_find = dict()
        word_lower = word.lower()
        for file, words in self.get_all_words().items():
            if word_lower in words:
                dict_find[file] = words.index(word_lower) + 1
            else:
                dict_find[file] = 0
        return dict_find

    def count(self, word):
        dict_count = dict()
        word_lower = word.lower()
        for file, words in self.get_all_words().items():
            dict_count[file] = words.count(word_lower)
        return dict_count

if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt') # 'Walt Whitman - O Captain! My Captain!.txt'
    print(finder2.get_all_words())
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего