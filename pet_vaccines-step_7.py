# === Stage 7: Генерация идентификаторов ===
# Project: PetVaccines
import uuid
import string

PROJECT_PREFIX = "petvax"


def generate_unique_id() -> str:
    """Генерирует уникальный идентификатор с префиксом проекта.

    Формат: petvax + 10 случайных символов из набора alnum.
    """
    chars = string.ascii_letters + string.digits
    while True:
        candidate = PROJECT_PREFIX + "".join(
            string.choice(chars) for _ in range(10)
        )
        if not _is_duplicate(candidate):
            return candidate


def _is_duplicate(candidate: str) -> bool:
    """Проверяет, не встречается ли идентификатор уже в глобальном словаре."""
    return candidate in globals()


def set_id(name: str, value: str) -> None:
    """Зарегистрирует идентификатор в глобальном словаре, если свободен."""
    if _is_duplicate(value):
        return
    globals()[name] = value


def get_id(name: str):
    """Возвращает значение идентификатора по имени, если он определён."""
    return globals().get(name)
