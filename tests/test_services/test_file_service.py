from unittest.mock import MagicMock, mock_open, patch

from src.services.file_service import FileService


class TestFileServiceOpenFile:
    def test_returns_file_content_when_file_selected(self) -> None:
        fake_content: str = "hello world"
        with patch("src.services.file_service.filedialog.askopenfilename", return_value="/fake/path.txt"):
            with patch("builtins.open", mock_open(read_data=fake_content)):
                result: str | None = FileService.open_file()
        assert result == fake_content

    def test_returns_none_when_empty_string_returned(self) -> None:
        with patch("src.services.file_service.filedialog.askopenfilename", return_value=""):
            result: str | None = FileService.open_file()
        assert result is None

    def test_returns_none_when_dialog_cancelled(self) -> None:
        with patch("src.services.file_service.filedialog.askopenfilename", return_value=None):
            result: str | None = FileService.open_file()
        assert result is None

    def test_reads_file_with_utf8_encoding(self) -> None:
        mock_file = mock_open(read_data="contenido")
        with patch("src.services.file_service.filedialog.askopenfilename", return_value="/fake/path.txt"):
            with patch("builtins.open", mock_file) as patched_open:
                FileService.open_file()
        patched_open.assert_called_once_with("/fake/path.txt", "r", encoding="utf-8")


class TestFileServiceSaveFile:
    def test_writes_content_when_file_selected(self) -> None:
        fake_file: MagicMock = MagicMock()
        with patch("src.services.file_service.filedialog.asksaveasfile", return_value=fake_file):
            FileService.save_file("some content")
        fake_file.write.assert_called_once_with("some content")
        fake_file.close.assert_called_once()

    def test_does_nothing_when_dialog_cancelled(self) -> None:
        with patch("src.services.file_service.filedialog.asksaveasfile", return_value=None):
            FileService.save_file("some content")

    def test_write_receives_exact_content(self) -> None:
        fake_file: MagicMock = MagicMock()
        content: str = "line1\nline2\nline3"
        with patch("src.services.file_service.filedialog.asksaveasfile", return_value=fake_file):
            FileService.save_file(content)
        fake_file.write.assert_called_once_with(content)
