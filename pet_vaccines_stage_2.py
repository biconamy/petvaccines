# === Stage 2: Проверка полей ===
# Project: PetVaccines
import datetime
from typing import Any


def normalize_input(raw: Any) -> Any:
    """Нормализует пользовательский ввод перед валидацией."""
    if isinstance(raw, str):
        text = raw.strip()
        if not text:
            return ""
        return text
    return raw


def validate_name(name: str) -> str:
    """Проверяет кличку питомца."""
    normalized = normalize_input(name)
    if not normalized:
        raise ValueError("Кличка питомца не может быть пустой.")
    if len(normalized) > 50:
        raise ValueError("Кличка питомца не может превышать 50 символов.")
    if not normalized.replace(" ", "").replace("-", "").isalnum():
        raise ValueError("Кличка питомца должна содержать только буквы, цифры, пробелы и дефисы.")
    return normalized


def validate_species(species: str) -> str:
    """Проверяет вид питомца."""
    normalized = normalize_input(species).lower()
    if not normalized:
        raise ValueError("Вид питомца не может быть пустым.")
    if len(normalized) > 30:
        raise ValueError("Вид питомца не может превышать 30 символов.")
    return normalized


def validate_birth_date(birth_date: Any) -> datetime.date:
    """Проверяет дату рождения питомца."""
    if isinstance(birth_date, datetime.datetime):
        date = birth_date.date()
    elif isinstance(birth_date, datetime.date):
        date = birth_date
    else:
        try:
            date = datetime.datetime.strptime(normalize_input(birth_date), "%d.%m.%Y").date()
        except (ValueError, TypeError):
            raise ValueError("Дата рождения должна быть в формате ДД.ММ.ГГГГ.")
    if date.year < 1990 or date.year > datetime.date.today().year:
        raise ValueError("Дата рождения питомца должна быть в диапазоне с 1990 года.")
    return date


def validate_weight(weight: Any) -> float:
    """Проверяет вес питомца."""
    try:
        value = float(normalize_input(weight))
    except (ValueError, TypeError):
        raise ValueError("Вес питомца должен быть числом.")
    if value <= 0:
        raise ValueError("Вес питомца не может быть меньше или равен нулю.")
    if value > 500:
        raise ValueError("Вес питомца не может превышать 500 килограммов.")
    return round(value, 2)


def validate_pet(name: Any, species: Any, birth_date: Any, weight: Any) -> dict[str, Any]:
    """Валидирует и собирает данные о питомце."""
    return {
        "name": validate_name(name),
        "species": validate_species(species),
        "birth_date": validate_birth_date(birth_date),
        "weight": validate_weight(weight),
    }
