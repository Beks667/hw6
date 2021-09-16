palindromes = ['hello', 'sentences where punctuation', 45,'Able was I, ere I saw Elba',
 34.0, 78.87, 'found', 'level', '12/11/21', 'radar','stats']


def palindrom_search(word):
    word = word.replace(' ', '')
    word = word.lower()
    return word == word[::-1]

print(palindrom_search(str(palindromes)))
