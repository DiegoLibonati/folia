import tkinter as tk

import pytest

from src.ui.components.font_config_form import FontConfigForm
from src.ui.styles import Styles


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def entry_number(root: tk.Tk) -> tk.StringVar:
    return tk.StringVar(master=root)


@pytest.fixture
def font_config_form(root: tk.Tk, styles: Styles, entry_number: tk.StringVar) -> FontConfigForm:
    form: FontConfigForm = FontConfigForm(
        parent=root,
        styles=styles,
        font_families=["Arial", "Roboto", "Courier"],
        entry_number=entry_number,
    )
    yield form
    form.destroy()


class TestFontConfigForm:
    def test_is_a_frame(self, font_config_form: FontConfigForm) -> None:
        assert isinstance(font_config_form, tk.Frame)

    def test_get_font_returns_empty_string_when_nothing_is_selected(
        self, font_config_form: FontConfigForm
    ) -> None:
        result: str = font_config_form.get_font()

        assert result == ""

    def test_get_font_returns_selected_value(self, font_config_form: FontConfigForm) -> None:
        font_config_form._combo_fonts.set("Arial")

        result: str = font_config_form.get_font()

        assert result == "Arial"

    def test_stores_provided_font_families(self, font_config_form: FontConfigForm) -> None:
        assert font_config_form._font_families == ["Arial", "Roboto", "Courier"]

    def test_combo_contains_provided_font_families(self, font_config_form: FontConfigForm) -> None:
        values: list[str] = list(font_config_form._combo_fonts["values"])

        assert "Arial" in values
        assert "Roboto" in values
        assert "Courier" in values
