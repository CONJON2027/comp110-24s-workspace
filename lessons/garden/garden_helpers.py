"""Some functions for my garden plan!"""

__author__ = "730665579"

plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}

plant: str = 'daisy'
plant_kind: str = "flower"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Add a plant by its kind to the dictionary."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = [plant]


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add a plant by date to the dictionary."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = [plant]


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Look up plants by their kind and date."""
    assert plant_kind in plants_by_kind
    assert month in plants_by_date
    # Look up list of plants by plant kind
    list_of_plants_by_kinds: list[str] = plants_by_kind[plant_kind]
    list_of_plants_by_dates: list[str] = plants_by_date[month]
    combined: list[str] = []
    for plant in list_of_plants_by_kinds:
        for other_plant in list_of_plants_by_dates:
            if other_plant == plant:
                combined.append(other_plant)
    if len(combined) > 0:
        return f"{plant_kind}s to plant in {month}: {combined}"
    else:
        return f"No {plant_kind}s to plant in {month}"
