import Storage
import Crud_operations
import Search
import analytics


def determine_podium(table: dict) -> None:
    """
    визначення назви команди, яка стала чемпіоном та назви команд, які посіли друге і третє місця.
    """
    print("ПІДСУМКИ ПЕРШОСТІ З ФУТБОЛУ")

    if len(table) < 3:
        print("Помилка, для визначення призерів потрібно щонайменше 3 команди.")
        return

    try:
        ranked = sorted(table.items(), key=lambda item: int(item[1]), reverse=True)
        champion = ranked[0]
        runner_up = ranked[1]
        third_place = ranked[2]

        print(f"Команда, що посіла 1 місце:     {champion[0]} ({champion[1]} балів)")
        print(f"Команда, що посіла 2 місце:   {runner_up[0]} ({runner_up[1]} балів)")
        print(f"Команда, що посіла 3 місце:   {third_place[0]} ({third_place[1]} балів)")
    except ValueError:
        print("Помилка, знайдено некоректний числовий запис балів у таблиці.")


def print_table(table: dict) -> None:
    """Виведення на екран усіх значень словника."""
    print(f"{'Команда':<25} | {'Бали':<15}")
    if not table:
        print("Турнірна таблиця порожня.")
    else:
        for team, points in table.items():
            print(f"{team:<25} | {points:<15}")


def add_team_dialog(table: dict) -> None:
    """Додавання нової команди з використанням analytics.py та Crud_operations.py."""
    team = analytics.validate_text_input("Введіть назву нової команди: ")

    while True:
        points_input = input(f"Введіть кількість балів для '{team}': ").strip()
        
        if not points_input.isdigit():
            print("Помилка, кількість балів має бути цілим невід'ємним числом.")
            continue

        # Перевірка чи жодна пара команд не набрала однакову кількість балів
        if points_input in table.values():
            print(f"Помилка, кількість балів ({points_input}) вже належить іншій команді (бали мають бути унікальними).")
            return

        Crud_operations.add_word(table, team, str(points_input))
        break


def update_points_dialog(table: dict) -> None:
    """Оновлення кількості балів команди через Crud_operations.py."""
    team = input("Введіть назву команди для оновлення балів: ").strip()

    while True:
        points_input = input(f"Введіть нову кількість балів для '{team}': ").strip()
        
        if not points_input.isdigit():
            print("Помилка: кількість балів має бути цілим числом.")
            continue

        # Перевірка на унікальність очок при оновленні
        if points_input in table.values() and table.get(team) != points_input:
            print(f"Помилка: кількість балів ({points_input}) уже закріплена за іншою командою.")
            return

        Crud_operations.update_translation(table, team, str(points_input))
        break


def search_team_dialog(table: dict) -> None:
    """Пошук команди за назвою через Search.py."""
    query = input("Введіть назву команди для пошуку: ").strip()
    result = Search.find_case_insensitive(table, query)
    if result is not None:
        print(f"Команда '{query}' знайдена та має в активі {result} балів.")
    else:
        print(f"[Не знайдено команду '{query}' не знайдено.")


def reverse_search_dialog(table: dict) -> None:
    """Зворотний пошук команди за кількістю балів через Search.py."""
    query = input("Введіть кількість балів для пошуку команди: ").strip()
    results = Search.reverse_search(table, query)
    if results:
        print(f"Команди з показником {query} балів знайдено: {', '.join(results)}")
    else:
        print(f"Не знайдено, жодна команда не набрала {query} балів.")


def show_menu() -> None:
    """Головне діалогове консольне меню."""
    print("\n Головне меню турнірної таблиці")
    print("1. Показати всю турнірну таблицю")
    print("2. Визначити чемпіона та призерів")
    print("3. Переглянути команди за алфавітом")
    print("4. Додати нову команду")
    print("5. Оновити бали команди")
    print("6. Видалити команду з таблиці")
    print("7. Пошук команди за назвою")
    print("8. Пошук команди за набраними балами")
    print("9. Статистичний аналіз чемпіонату")
    print("10.Експортувати турнірну таблицю у TXT-файл")
    print("11. Зберегти таблицю у файл JSON")
    print("0.  Зберегти та вийти з програми")


def main() -> None:
    # Завантаження таблиці через модуль Storage.py
    tournament_table = Storage.load_dictionary("football_league.json")

    # Якщо файл відсутній або порожній - ініціалізуємо n = 10 команд
    if not tournament_table:
        tournament_table = {
            "Динамо": "68",
            "Шахтар": "65",
            "Кривбас": "57",
            "Полісся": "50",
            "Рух": "49",
            "Дніпро-1": "46",
            "Ворскла": "35",
            "Колос": "32",
            "Олександрія": "30",
            "Оболонь": "26"
        }
        Storage.save_dictionary(tournament_table, "football_league.json")

    while True:
        show_menu()
        choice = input("Оберіть пункт меню (0-11): ").strip()

        if choice == "1":
            print_table(tournament_table)
        elif choice == "2":
            determine_podium(tournament_table)
        elif choice == "3":
            analytics.display_sorted_dictionary(tournament_table)
        elif choice == "4":
            add_team_dialog(tournament_table)
        elif choice == "5":
            update_points_dialog(tournament_table)
        elif choice == "6":
            team_to_delete = input("Введіть назву команди для вилучення: ").strip()
            Crud_operations.delete_word(tournament_table, team_to_delete)
        elif choice == "7":
            search_team_dialog(tournament_table)
        elif choice == "8":
            reverse_search_dialog(tournament_table)
        elif choice == "9":
            analytics.display_statistics(tournament_table)
        elif choice == "10":
            Storage.export_to_txt(tournament_table, "football_export.txt")
        elif choice == "11":
            Storage.save_dictionary(tournament_table, "football_league.json")
        elif choice == "0":
            Storage.save_dictionary(tournament_table, "football_league.json")
            print("Усі дані збережено. Роботу програми завершено!")
            break
        else:
            print("Некоректний вибір. Введіть число від 0 до 11.")


if __name__ == "__main__":
    main()
