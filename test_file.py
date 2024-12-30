import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from index import get_data_by_config_value, CONFIG

class TestIndex(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_get_data_by_config_value(self, mock_connect):
        # Arrange
        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [("admin", "password123")]
        mock_connect.return_value = mock_connection

        expected_result = [("admin", "password123")]

        # Act
        result = get_data_by_config_value("admin")

        # Assert
        self.assertEqual(result, expected_result)
        mock_cursor.execute.assert_called_once_with("SELECT * FROMusersWhereusername")
        mock_connect.assert_called_once_with("database.db")

if __name__ == '__main__':
    unittest.main()
