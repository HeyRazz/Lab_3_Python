import json
import os

DEFAULT_JSON_FILE = "dictionary.json"
DEFAULT_TXT_FILE = "dictionary_export.txt"


def load_dictionary(filepath: str = DEFAULT_JSON_FILE) -> dict:
    #Завантажує словник із JSON-файлу при старті програми.
    #Якщо файл відсутній або пошкоджений — повертає порожній словник.
    
    if not os.path.exists(filepath):
        print(f"[INFO] Файл '{filepath}' не знайдено. Ініціалізовано новий словник.")
        return {}

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"[SUCCESS] Дані успішно завантажено з файлу '{filepath}'.")
            return data
    except json.JSONDecodeError:
        print(f"[WARNING] Файл '{filepath}' пошкоджено або він порожній. Створено новий словник.")
        return {}
    except Exception as error:
        print(f"[ERROR] Помилка зчитування файлу: {error}")
        return {}


def save_dictionary(dictionary: dict, filepath: str = DEFAULT_JSON_FILE) -> bool:
    # Зберігає поточний стан словника у JSON-файл із підтримкою кирилиці.
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
        print(f"[SUCCESS] Словник успішно збережено у '{filepath}'.")
        return True
    except Exception as error:
        print(f"[ERROR] Не вдалося зберегти файл: {error}")
        return False


def export_to_txt(dictionary: dict, filepath: str = DEFAULT_TXT_FILE) -> bool:
    # Експортує пари «слово — переклад» у текстовий файл .txt.
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            for word, translation in sorted(dictionary.items()):
                file.write(f"{word} — {translation}\n")
        print(f"[SUCCESS] Словник експортовано у текстовий файл '{filepath}'.")
        return True
    except Exception as error:
        print(f"[ERROR] Помилка експорту у TXT: {error}")
        return False