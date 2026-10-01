def display_all_teams(table: dict) -> None:
    """Виведення на екран усіх значень словника."""
    print(f"{'Назва команди':<25} {'Кількість балів':<15}")
    if not table:
        print("Турнірна таблиця порожня.")
    else:
        for team, points in table.items():
            print(f"{team:<25} | {points:<15}")


def add_team_record(table: dict) -> None:
    """Додавання нового запису до словника з обробкою винятків."""
    print("\nДодавання нової команди")
    team_name = input("Введіть назву команди: ").strip()

    if not team_name:
        print("Помилка: назва команди не може бути порожнім рядком.")
        return

    if team_name in table:
        print(f"Помилка: команда '{team_name}' уже присутня в таблиці.")
        return

    try:
        points = int(input(f"Введіть кількість балів для команди '{team_name}': "))
        if points < 0:
            print("Помилка: кількість балів не може бути від'ємною.")
            return

        # Умова варіанта: жодна пара команд не має однакової кількості балів
        if points in table.values():
            print(f"Помилка: кількість балів ({points}) вже закріплена за іншою командою, бали мають бути унікальними.")
            return

        table[team_name] = points
        print(f"Успішно додано: {team_name} — {points} балів.")
    except ValueError:
        print("Кількість балів має бути цілим числом.")


def remove_team_record(table: dict) -> None:
    """Видалення запису зі словника з обробкою виняткової ситуації."""
    print("\nВидалення команди зі словника")
    team_name = input("Введіть назву команди для видалення: ").strip()

    try:
        del table[team_name]
        print(f"Успішно видалено команду '{team_name}' зі словника.")
    except KeyError:
        print(f"Команди '{team_name}' немає у словнику.")


def view_sorted_by_keys(table: dict) -> None:
    """
    Перегляд вмісту словника за відсортованими ключами
    (перетворення об'єкта представлення ключів у список та використання sorted).
    """
    print("\nПерегляд команд за відсортованими ключами")
    if not table:
        print("Турнірна таблиця порожня.")
        return

    # Перетворення об'єкта представлення ключів у список
    keys_list = list(table.keys())
    # Застосування функції sorted
    sorted_keys = sorted(keys_list, key=lambda s: s.casefold())

    print(f"{'№':<4} | {'Назва команди':<25} | {'Бали':<10}")
    print("-" * 45)
    for idx, team in enumerate(sorted_keys, start=1):
        print(f"{idx:<4} | {team:<25} | {table[team]:<10}")
    print("-" * 45)


def determine_podium(table: dict) -> None:
    """
    визначення назви команд, яка стала чемпіоном та які посіли друге і третє місця.
    """
    print("\n")
    print("            ПІДСУМКИ ПЕРШОСТІ З ФУТБОЛУ")

    if len(table) < 3:
        print("Помилка: для визначення призерів потрібно щонайменше 3 команди.")
        return

    # Сортування пар (команда, бали) за спаданням балів
    ranked_teams = sorted(table.items(), key=lambda item: item[1], reverse=True)

    champion = ranked_teams[0]
    runner_up = ranked_teams[1]
    third_place = ranked_teams[2]

    print(f"    Команда-чемпіон (1 місце):     {champion[0]} ({champion[1]} балів)")
    print(f"    Команда, що посіла 2 місце:   {runner_up[0]} ({runner_up[1]} балів)")
    print(f"    Команда, що посіла 3 місце:   {third_place[0]} ({third_place[1]} балів)")


def show_menu() -> None:
    """Діалогове меню роботи зі словником."""
    print("\nОберіть дію:")
    print("1. Вивести всю турнірну таблицю")
    print("2. Визначити чемпіона (1 місце) та призерів (2 і 3 місця)")
    print("3. Переглянути вміст словника в алфавітному порядку")
    print("4. Додати нову команду")
    print("5. Видалити команду за назвою")
    print("0. Вийти з програми")


def main() -> None:
    # Початковий словник у коді: n = 10 команд з унікальними балами
    football_standings = {
        "Динамо": 68,
        "Шахтар": 65,
        "Кривбас": 57,
        "Полісся": 50,
        "Рух": 49,
        "Дніпро-1": 46,
        "Ворскла": 35,
        "Колос": 32,
        "Олександрія": 30,
        "Оболонь": 26
    }

    print("Програма обліку даних першості з футболу готова до роботи.")

    while True:
        show_menu()
        choice = input("Ваш вибір (0-5): ").strip()

        if choice == "1":
            display_all_teams(football_standings)
        elif choice == "2":
            determine_podium(football_standings)
        elif choice == "3":
            view_sorted_by_keys(football_standings)
        elif choice == "4":
            add_team_record(football_standings)
        elif choice == "5":
            remove_team_record(football_standings)
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Некоректний вибір! Введіть цифру від 0 до 5.")


if __name__ == "__main__":
    main()