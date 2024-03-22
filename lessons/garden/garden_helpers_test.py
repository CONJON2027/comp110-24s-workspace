"""Test my garden functions."""

__author__ = "730665579"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_normal() -> None:
    """Test normal operations of add by kind."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(plants_by_kind, "flower", "daisy")
    assert "daisy" in plants_by_kind["flower"]


def test_add_by_kind_edge() -> None:
    """Test edge operations of add by kind."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(plants_by_kind, "tree", "oak")
    assert "oak" in plants_by_kind["tree"]


def test_add_by_date_normal() -> None:
    """Test normal operations of add by date."""
    plants_by_date: dict[str, list[str]] = {"January": ["marigold", "daisy"], "February": ["zinnia"]}
    add_by_date(plants_by_date, "January", "rose")
    assert "rose" in plants_by_date["January"]


def test_add_by_date_edge() -> None:
    """Test edge operations of add by date."""
    plants_by_date: dict[str, list[str]] = {"January": ["marigold", "daisy"], "February": ["zinnia"]}
    add_by_date(plants_by_date, "March", "tulip")
    assert "tulip" in plants_by_date["March"]


def test_lookup_by_kind_and_date_normal() -> None:
    """Test normal operations of lookup by date and kind."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"January": ["marigold", "daisy"], "February": ["zinnia"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "January")
    assert result == "flowers to plant in January: ['marigold']"


def test_lookup_by_kind_and_date_edge() -> None:
    """Test edge operations of lookup by date and kind."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"January": ["marigold", "daisy"], "February": ["zinnia"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "vegetable", "February")
    assert result == "No vegetables to plant in February"
