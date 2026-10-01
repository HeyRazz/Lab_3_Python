def add_word(table: dict, team: str, points: str) -> bool:
    """
    Додає нову футбольну команду та її бали до турнірної таблиці.
    Повертає True, якщо запис успішно додано.
    """
    team = team.strip()
    points = str(points).strip()

    if not team or not points:
        print("Помилка: назва команди та кількість балів не можуть бути порожніми.")
        return False

    # Перевірка наявності команди в таблиці (без урахування регістру)
    team_keys_lower = [k.lower() for k in table.keys()]
    if team.lower() in team_keys_lower:
        existing_team = next(k for k in table.keys() if k.lower() == team.lower())
        print(f"Команда '{existing_team}' вже є у таблиці (має {table[existing_team]} балів).")
        print("Щоб змінити кількість балів, скористайтеся функцією оновлення.")
        return False

    table[team] = points
    print(f"Успішно додано: {team} — {points} балів.")
    return True


def update_translation(table: dict, team: str, new_points: str) -> bool:
    """
    Оновлює кількість балів наявної футбольної команди.
    Повертає True, якщо дані успішно змінено.
    """
    team = team.strip()
    new_points = str(new_points).strip()

    if not new_points:
        print("Помилка: кількість балів не може бути порожньою.")
        return False

    # Пошук ключа без чутливості до регістру для надійного оновлення
    target_key = next((k for k in table.keys() if k.lower() == team.lower()), None)

    if target_key is None:
        print(f"Помилка: команди '{team}' немає в турнірній таблиці.")
        return False

    old_points = table[target_key]
    table[target_key] = new_points
    print(f"Оновлено: {target_key} — {old_points} -> {new_points} балів.")
    return True


def delete_word(table: dict, team: str) -> bool:
    """
    Видаляє футбольну команду з турнірної таблиці.
    Повертає True, якщо команду успішно вилучено.
    """
    team = team.strip()

    # Пошук точного ключа в словнику
    target_key = next((k for k in table.keys() if k.lower() == team.lower()), None)

    if target_key is None:
        print(f"Помилка: команди '{team}' немає в турнірній таблиці.")
        return False

    del table[target_key]
    print(f"Команду '{target_key}' успішно видалено з таблиці.")
    return True


# Автономна перевірка функцій при прямому запуску файлу
if __name__ == "__main__":
    test_league = {
        "Динамо": "68",
        "Шахтар": "65",
        "Кривбас": "57",
        "Полісся": "50"
    }

    print("Початкова таблиця:", test_league, "\n")

    # Перевірка додавання
    add_word(test_league, "Рух", "49")
    add_word(test_league, "динамо", "70")
    add_word(test_league, " ", "30") 

    # Перевірка оновлення
    update_translation(test_league, "Шахтар", "66")
    update_translation(test_league, "Металіст", "40")

    # Перевірка видалення
    delete_word(test_league, "Полісся")
    delete_word(test_league, "Ворскла") 

    print("\nПідсумкова таблиця:", test_league)
