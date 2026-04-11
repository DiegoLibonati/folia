import os

from src.constants import paths


class TestPaths:
    def test_root_value(self) -> None:
        assert paths.ROOT == "./src"

    def test_root_assets_value(self) -> None:
        assert paths.ROOT_ASSETS == "./src/assets"

    def test_path_icon_is_string(self) -> None:
        assert isinstance(paths.PATH_ICON, str)

    def test_path_icon_contains_icon_filename(self) -> None:
        assert "icon.ico" in paths.PATH_ICON

    def test_path_icon_contains_assets(self) -> None:
        assert "assets" in paths.PATH_ICON

    def test_path_icon_is_absolute(self) -> None:
        assert os.path.isabs(paths.PATH_ICON)
