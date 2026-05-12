from src.constants.paths import PATH_ICON


class TestPaths:
    def test_path_icon_is_string(self) -> None:
        assert isinstance(PATH_ICON, str)

    def test_path_icon_is_non_empty(self) -> None:
        assert PATH_ICON != ""

    def test_path_icon_ends_with_ico(self) -> None:
        assert PATH_ICON.endswith(".ico")

    def test_path_icon_contains_icons_directory(self) -> None:
        assert "icons" in PATH_ICON
