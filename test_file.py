import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from index import get_data_by_config_value, CONFIG

class TestGetDataByConfigValue(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_get_data_by_config_value(self, mock_connect):
        # Mock the connection and cursor methods
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Define the expected result
        expected_result = [("admin", "password")]

        # Configure the mock cursor to return the expected result
        mock_cursor.fetchall.return_value = expected_result

        # Call the function with a sample value
        result = get_data_by_config_value("admin")

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
