from tkinter import BOTH, BOTTOM, CENTER, END, HORIZONTAL, NONE, RIGHT, X, Y

from src.ui.styles import Styles


class TestStyles:
    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_font_arial_10(self) -> None:
        assert Styles.FONT_ARIAL_10 == "Arial 10"

    def test_font_roboto_10(self) -> None:
        assert Styles.FONT_ROBOTO_10 == "Roboto 10"

    def test_font_roboto_12(self) -> None:
        assert Styles.FONT_ROBOTO_12 == "Roboto 12"

    def test_font_roboto_20(self) -> None:
        assert Styles.FONT_ROBOTO_20 == "Roboto 20"

    def test_wrap_none_equals_tkinter_none(self) -> None:
        assert Styles.WRAP_NONE == NONE

    def test_fill_both_equals_tkinter_both(self) -> None:
        assert Styles.FILL_BOTH == BOTH

    def test_fill_y_equals_tkinter_y(self) -> None:
        assert Styles.FILL_Y == Y

    def test_fill_x_equals_tkinter_x(self) -> None:
        assert Styles.FILL_X == X

    def test_side_right_equals_tkinter_right(self) -> None:
        assert Styles.SIDE_RIGHT == RIGHT

    def test_side_bottom_equals_tkinter_bottom(self) -> None:
        assert Styles.SIDE_BOTTOM == BOTTOM

    def test_orient_horizontal_equals_tkinter_horizontal(self) -> None:
        assert Styles.ORIENT_HORIZONTAL == HORIZONTAL

    def test_position_end_equals_tkinter_end(self) -> None:
        assert Styles.POSITION_END == END

    def test_anchor_center_equals_tkinter_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER
