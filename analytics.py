def validate_text_input(prompt: str) -> str:
    """
    Захист програми від некоректного введення даних користувачем.
    Перевіряє, що рядок не є порожнім і містить хоча б одну літеру.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Помилка: назва команди не може бути порожньою. Спробуйте ще раз.")
            continue
        
        # Перевірка на наявність літер у рядку
        if any(char.isalpha() for char in user_input):
            return user_input
        else:
            print("Помилка: назва команди повинна містити літери.")


def display_statistics(table: dict) -> None:
    """
    Аналітичний модуль для футбольної першості:
    загальна кількість команд;
    найдовша назва футбольного клубу;
    сумарна кількість набраних балів у чемпіонаті;
    середня кількість балів на одну команду;
    середня довжина назв клубів.
    """
    print("\n" + "=" * 50)
    print("           СТАТИСТИКА ТУРНІРНОЇ ТАБЛИЦІ")
    print("=" * 50)
    total_teams = len(table)
    print(f"Загальна кількість команд: {total_teams}")

    if total_teams == 0:
        print("Турнірна таблиця порожня, аналітика недоступна.")
        print("=" * 50)
        return

    # Пошук найдовшої назви команди
    longest_team = max(table.keys(), key=len)
    print(f"Найдовша назва команди:    '{longest_team}' ({len(longest_team)} симв.)")

    # Безпечний розрахунок балів 
    numeric_points = [int(p) for p in table.values() if str(p).isdigit()]
    
    if numeric_points:
        total_points = sum(numeric_points)
        avg_points = total_points / len(numeric_points)
        print(f"Сума балів усіх команд:    {total_points}")
        print(f"Середня кількість балів:   {avg_points:.1f}")

    # Розрахунок середньої довжини назв команд
    avg_name_length = sum(len(team) for team in table.keys()) / total_teams
    print(f"Середня довжина назви:     {avg_name_length:.1f} симв.")
    print("=" * 50)


def display_sorted_dictionary(table: dict, reverse: bool = False) -> None:
    """
    Виведення турнірної таблиці за відсортованими назвами команд (в алфавітному порядку).
    Підтримує пряме та зворотне сортування.
    """
    print("\n" + "-" * 50)
    order_type = "в зворотному порядку" if reverse else "за алфавітом (А-Я)"
    print(f"       ТУРНІРНА ТАБЛИЦЯ ({order_type})")
    print("-" * 50)

    if not table:
        print("Турнірна таблиця порожня.")
        print("-" * 50)
        return

    sorted_teams = sorted(table.keys(), key=lambda s: s.casefold(), reverse=reverse)

    print(f"{'№':<4} | {'Назва команди':<25} | {'Бали':<10}")
    print("-" * 50)
    for index, team in enumerate(sorted_teams, start=1):
        print(f"{index:>2}.  | {team:<25} | {table[team]:<10}")
    print("-" * 50)


# Автономне тестування модуля (запускається лише при прямому виконанні файлу)
if __name__ == "__main__":
    test_data = {
        "Динамо": "68",
        "Шахтар": "65",
        "Олександрія": "30",
        "Кривбас": "57"
    }
    print("[ТЕСТ] Виклик аналітики турніру:")
    display_statistics(test_data)
    
    print("\n[ТЕСТ] Сортування команд:")
    display_sorted_dictionary(test_data)
