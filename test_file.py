import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from index import get_data_by_config_value

class TestGetDataByConfigValue(unittest.TestCase):

    @patch('sqlite3.connect')
    def test_get_data_by_config_value(self, mock_connect):
        # Mock the connection and cursor methods
        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        # Define the expected query and result
        expected_query = "SELECT * FROM users WHERE username"
        expected_result = [('admin', 'password123')]

        # Call the function with a test value
        result = get_data_by_config_value("admin")

        # Assert that the connection was made with the correct database name
        mock_connect.assert_called_once_with('database.db')

        # Assert that the cursor's execute method was called with the expected query
        mock_cursor.execute.assert_called_once_with(expected_query)

        # Assert that the fetchall method returned the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
