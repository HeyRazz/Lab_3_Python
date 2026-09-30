def validate_text_input(prompt: str) -> str:
    """
    Захист програми від некоректного введення даних користувачем.
    Перевіряє, що рядок не є порожнім і містить хоча б одну літеру.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Помилка: рядок не може бути порожнім. Спробуйте ще раз.")
            continue
        
        # Перевірка на наявність літер у рядку
        if any(char.isalpha() for char in user_input):
            return user_input
        else:
            print("Помилка: введення повинно містити літери.")


def display_statistics(dictionary: dict) -> None:
    """
    Аналітичний модуль: загальна кількість слів у словнику,
    найдовше слово (англійський термін), 
    найдовший переклад (українське значення), середня довжина слів.
    """
    print("\n" + "=" * 45)
    print("           СТАТИСТИКА СЛОВНИКА")
    print("=" * 45)
    total_words = len(dictionary)
    print(f"Загальна кількість записів: {total_words}")

    if total_words == 0:
        print("Словник порожній, аналітика недоступна.")
        print("=" * 45)
        return

    # Пошук найдовшого слова (ключа)
    longest_word = max(dictionary.keys(), key=len)
    print(f"Найдовше слово: '{longest_word}' ({len(longest_word)} симв.)")

    # Пошук найдовшого перекладу (значення)
    longest_translation = max(dictionary.values(), key=len)
    print(f"Найдовший переклад: '{longest_translation}' ({len(longest_translation)} симв.)")

    # Розрахунок середньої довжини слів
    avg_length = sum(len(word) for word in dictionary.keys()) / total_words
    print(f"Середня довжина термінів: {avg_length:.1f} симв.")
    print("=" * 45)


def display_sorted_dictionary(dictionary: dict, reverse: bool = False) -> None:
    """
    Виведення вмісту словника за відсортованими ключами (в алфавітному порядку).
    Підтримує пряме та зворотне сортування.
    """
    print("\n" + "-" * 45)
    order_type = "в зворотному порядку" if reverse else "за алфавітом (A-Z)"
    print(f"  ВМІСТ СЛОВНИКА ({order_type})")
    print("-" * 45)

    if not dictionary:
        print("Словник порожній.")
        print("-" * 45)
        return

    sorted_keys = sorted(dictionary.keys(), key=lambda s: s.casefold(), reverse=reverse)

    for index, key in enumerate(sorted_keys, start=1):
        print(f"{index:>2}. {key:<18} — {dictionary[key]}")
    print("-" * 45)


# Автономне тестування модуля (запускається лише при прямому виконанні файлу)
if __name__ == "__main__":
    test_data = {
        "apple": "яблуко",
        "watermelon": "кавун",
        "sun": "сонце",
        "extraordinary": "надзвичайний"
    }
    print("[ТЕСТ] Виклик аналітики:")
    display_statistics(test_data)
    
    print("\n[ТЕСТ] Сортування:")
    display_sorted_dictionary(test_data)