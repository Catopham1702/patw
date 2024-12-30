import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from index import get_data_by_config_value

class TestGetDataByConfigValue(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_get_data_by_config_value(self, mock_connect):
        # Mock the connection and cursor methods
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Define the expected result
        expected_result = [(1, 'admin', 'password')]

        # Configure the mock cursor to return the expected result when fetchall is called
        mock_cursor.fetchall.return_value = expected_result

        # Call the function with a test value
        result = get_data_by_config_value("admin")

        # Assert that the connection and cursor methods were called correctly
        mock_connect.assert_called_once_with('database.db')
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROMusersWhereusername")
        mock_cursor.fetchall.assert_called_once()

        # Assert that the result is as expected
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
