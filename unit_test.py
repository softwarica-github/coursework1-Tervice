import unittest
from unittest.mock import patch
from web_enumeration import *


class TestReadDirectoryList(unittest.TestCase):
    def test_read_directory_list_existing_file(self):
        directories = read_directory_list('test_directory.txt')
        expected_directories = ['dir1', 'dir2', 'dir3']
        self.assertEqual(directories, expected_directories)

    def test_read_directory_list_nonexistent_file(self):
        directories = read_directory_list('nonexistent_file.txt')
        self.assertEqual(directories, [])

class TestScanDirectories(unittest.TestCase):
    @patch('requests.get')
    def test_scan_directories_exists(self, mock_get):
        mock_get.return_value.status_code = 200
        url = 'http://example.com'
        directories = ['dir1', 'dir2']
        
        with patch('builtins.print') as mock_print:
            scan_directories(url, directories)
            mock_print.assert_called_with(f'{url}/dir1 exists')

    @patch('requests.get')
    def test_scan_directories_not_exists(self, mock_get):
        mock_get.return_value.status_code = 404
        url = 'http://example.com'
        directories = ['dir1', 'dir2']
        
        with patch('builtins.print') as mock_print:
            scan_directories(url, directories)
            mock_print.assert_called_with(f'{url}/dir1 doesn\'t exist.')

class TestHighlightSearchText(unittest.TestCase):
    def setUp(self):
        self.text_widget = MagicMock()
        self.search_text = 'search_text'

    def test_highlight_search_text_found(self):
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            highlight_search_text(self.text_widget, self.search_text)
            mock_showinfo.assert_not_called()

    def test_highlight_search_text_not_found(self):
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            highlight_search_text(self.text_widget, 'nonexistent_text')
            mock_showinfo.assert_called_with(
                "Search Result", "No results found", parent=self.text_widget)
