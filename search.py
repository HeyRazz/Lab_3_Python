def find_exact(dictionary: dict, word: str):
    """
    Точний пошук за ключем.
    Повертає переклад або None, якщо слово не знайдено.
    """
    return dictionary.get(word, None)


def find_case_insensitive(dictionary: dict, word: str):
    """
    Пошук без урахування регістру (case-insensitive).
    """
    search_word = word.strip().lower()
    for key, value in dictionary.items():
        if key.lower() == search_word:
            return value
    return None


def reverse_search(dictionary: dict, translation: str):
    """
    Зворотний пошук: знайти оригінальне слово за його перекладом.
    Повертає список знайдених слів або None.
    """
    search_trans = translation.strip().lower()
    results = [key for key, val in dictionary.items() if val.lower() == search_trans]
    return results if results else None