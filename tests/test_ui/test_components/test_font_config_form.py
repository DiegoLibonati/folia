import tkinter as tk
from typing import Any

import pytest

from src.ui.components.font_config_form import FontConfigForm
from src.ui.styles import Styles


@pytest.fixture(scope="function")
def entry_number(root: tk.Tk) -> tk.StringVar:
    return tk.StringVar()


@pytest.fixture(scope="function")
def form(root: tk.Tk, entry_number: tk.StringVar) -> FontConfigForm:
    styles: Styles = Styles()
    font_families: list[tuple[str, Any]] = [("Arial", None), ("Roboto", None)]
    return FontConfigForm(parent=root, styles=styles, font_families=font_families, entry_number=entry_number)


class TestFontConfigForm:
    def test_is_created_successfully(self, form: FontConfigForm) -> None:
        assert form is not None

    def test_is_frame(self, form: FontConfigForm) -> None:
        assert isinstance(form, tk.Frame)

    def test_get_font_returns_empty_by_default(self, form: FontConfigForm) -> None:
        result: str = form.get_font()
        assert result == ""

    def test_get_font_returns_selected_value(self, root: tk.Tk, entry_number: tk.StringVar) -> None:
        styles: Styles = Styles()
        font_families: list[tuple[str, Any]] = [("Arial", None), ("Roboto", None)]
        f: FontConfigForm = FontConfigForm(parent=root, styles=styles, font_families=font_families, entry_number=entry_number)
        f._combo_fonts.set("Arial")
        assert f.get_font() == "Arial"

    def test_get_font_returns_second_option(self, root: tk.Tk, entry_number: tk.StringVar) -> None:
        styles: Styles = Styles()
        font_families: list[tuple[str, Any]] = [("Arial", None), ("Roboto", None)]
        f: FontConfigForm = FontConfigForm(parent=root, styles=styles, font_families=font_families, entry_number=entry_number)
        f._combo_fonts.set("Roboto")
        assert f.get_font() == "Roboto"

    def test_entry_number_initial_value_is_empty(self, form: FontConfigForm, entry_number: tk.StringVar) -> None:
        assert entry_number.get() == ""

    def test_entry_number_set_reflects_in_var(self, form: FontConfigForm, entry_number: tk.StringVar) -> None:
        entry_number.set("14")
        assert entry_number.get() == "14"

    def test_font_families_accepted_as_list(self, root: tk.Tk, entry_number: tk.StringVar) -> None:
        styles: Styles = Styles()
        font_families: list[tuple[str, Any]] = [("Comic Sans", None)]
        f: FontConfigForm = FontConfigForm(parent=root, styles=styles, font_families=font_families, entry_number=entry_number)
        f._combo_fonts.set("Comic Sans")
        assert f.get_font() == "Comic Sans"
