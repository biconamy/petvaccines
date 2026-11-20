# === Stage 9: Сортировка записей ===
# Project: PetVaccines
def sort_by_name(records, reverse=False):
    """Сортировка записей 'питомец' по кличке (возрастание/убывание)."""
    return sorted(records, key=lambda rec: rec["кличка"], reverse=reverse)


def sort_by_created(records, reverse=False):
    """Сортировка записей 'питомец' по дате создания (возрастание/убывание)."""
    return sorted(records, key=lambda rec: rec["date_created"], reverse=reverse)


def sort_by_name_then_created(records, reverse=False):
    """Сортировка по кличке, а при равенстве — по дате создания."""
    return sorted(
        records,
        key=lambda rec: (rec["кличка"], rec["date_created"]),
        reverse=reverse,
    )


if __name__ == "__main__":
    data = [
        {
            "name": "Барон",
            "species": "dog",
            "birth_date": "2024-01-05",
            "weight": 12.5,
            "date_created": "2024-01-10",
        },
        {
            "name": "Алиса",
            "species": "cat",
            "birth_date": "2023-11-20",
            "weight": 4.2,
            "date_created": "2023-12-01",
        },
        {
            "name": "Алиса",
            "species": "dog",
            "birth_date": "2024-02-15",
            "weight": 6.0,
            "date_created": "2024-02-20",
        },
    ]

    print("По кличке (asc):")
    for rec in sort_by_name(data):
        print(rec["name"], rec["species"])

    print("По кличке (desc):")
    for rec in sort_by_name(data, reverse=True):
        print(rec["name"], rec["species"])

    print("По дате создания (asc):")
    for rec in sort_by_created(data):
        print(rec["name"], rec["date_created"])

    print("По дате создания (desc):")
    for rec in sort_by_created(data, reverse=True):
        print(rec["name"], rec["date_created"])

    print("По кличке и дате создания (asc):")
    for rec in sort_by_name_then_created(data):
        print(rec["name"], rec["date_created"])

    print("По кличке и дате создания (desc):")
    for rec in sort_by_name_then_created(data, reverse=True):
        print(rec["name"], rec["date_created"])
