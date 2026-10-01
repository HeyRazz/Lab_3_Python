def add_word(dictionary, word, translation):
    """Додає пару «слово — переклад». Повертає True, якщо запис додано."""
    word = word.strip().lower()
    translation = translation.strip()

    if not word or not translation:
        print("Помилка: слово і переклад не можуть бути порожніми.")
        return False

    # Валідація дублікатів
    if word in dictionary:
        print(f"Слово '{word}' вже є у словнику (переклад: {dictionary[word]}).")
        print("Щоб змінити переклад, скористайтеся функцією оновлення.")
        return False

    dictionary[word] = translation
    print(f"Додано: {word} - {translation}.")
    return True


def update_translation(dictionary, word, new_translation):
    """Оновлює переклад наявного слова. Повертає True, якщо переклад змінено."""
    word = word.strip().lower()
    new_translation = new_translation.strip()

    if not new_translation:
        print("Помилка: переклад не може бути порожнім.")
        return False

    try:
        old_translation = dictionary[word]
    except KeyError:
        print(f"Помилка: слова '{word}' немає у словнику.")
        return False

    dictionary[word] = new_translation
    print(f"Оновлено: {word} - {old_translation} -> {new_translation}.")
    return True


def delete_word(dictionary, word):
    """Видаляє слово зі словника. Повертає True, якщо запис видалено."""
    word = word.strip().lower()

    try:
        del dictionary[word]
    except KeyError:
        print(f"Помилка: слова '{word}' немає у словнику.")
        return False

    print(f"Видалено: {word}.")
    return True


# Перевірка роботи функцій (запускається лише при прямому запуску файлу)
if __name__ == "__main__":
    test_dict = {
        "apple": "яблуко",
        "book": "книга",
        "house": "будинок",
        "water": "вода",
        "sun": "сонце",
        "moon": "місяць",
        "tree": "дерево",
        "friend": "друг",
        "city": "місто",
        "school": "школа",
        "river": "річка",
        "mountain": "гора",
        "bread": "хліб",
        "window": "вікно",
        "door": "двері",
        "table": "стіл",
        "chair": "стілець",
        "street": "вулиця",
        "flower": "квітка",
        "night": "ніч",
    }

    print(f"Початковий словник ({len(test_dict)} слів):", test_dict, "\n")

    add_word(test_dict, "cat", "кіт")  # успішне додавання
    add_word(test_dict, "dog", "собака")  # успішне додавання
    add_word(test_dict, "Apple", "яблуко")  # дублікат (регістр не важливий)
    add_word(test_dict, "  ", "порожнє")  # порожнє слово
    add_word(test_dict, "car", "")  # порожній переклад

    update_translation(test_dict, "book", "книжка")  # успішне оновлення
    update_translation(test_dict, "sun", "сонечко")  # успішне оновлення
    update_translation(test_dict, "bird", "птах")  # слова немає
    update_translation(test_dict, "tree", "")  # порожній переклад

    delete_word(test_dict, "cat")  # успішне видалення
    delete_word(test_dict, "school")  # успішне видалення
    delete_word(test_dict, "cat")  # слова вже немає

    print(f"\nПідсумковий словник ({len(test_dict)} слів):", test_dict)
