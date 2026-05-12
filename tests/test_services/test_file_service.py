from unittest.mock import MagicMock, mock_open, patch

from src.services.file_service import FileService


class TestFileService:
    def test_open_file_returns_file_content_when_file_is_selected(self) -> None:
        with patch(
            "src.services.file_service.filedialog.askopenfilename", return_value="/path/file.txt"
        ):
            with patch("builtins.open", mock_open(read_data="hello world")):
                result: str | None = FileService.open_file()

        assert result == "hello world"

    def test_open_file_returns_none_when_dialog_is_cancelled(self) -> None:
        with patch("src.services.file_service.filedialog.askopenfilename", return_value=""):
            result: str | None = FileService.open_file()

        assert result is None

    def test_open_file_returns_none_when_dialog_returns_none(self) -> None:
        with patch("src.services.file_service.filedialog.askopenfilename", return_value=None):
            result: str | None = FileService.open_file()

        assert result is None

    def test_save_file_writes_content_when_file_is_selected(self) -> None:
        mock_file: MagicMock = MagicMock()
        with patch("src.services.file_service.filedialog.asksaveasfile", return_value=mock_file):
            FileService.save_file("some content")

        mock_file.write.assert_called_once_with("some content")
        mock_file.close.assert_called_once()

    def test_save_file_does_nothing_when_dialog_is_cancelled(self) -> None:
        mock_file: MagicMock = MagicMock()
        with patch("src.services.file_service.filedialog.asksaveasfile", return_value=None):
            FileService.save_file("some content")

        mock_file.write.assert_not_called()
