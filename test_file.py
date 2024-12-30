import unittest
from patw.index import get_data_by_config_value

class TestGetDataByConfigValue(unittest.TestCase):
    def test_get_data_by_config_value(self):
        # Mocking the database connection and cursor to avoid actual database operations
        class MockCursor:
            def execute(self, query):
                pass
            
            def fetchall(self):
                return [("admin", "password123"), ("user1", "pass1")]

        class MockConnection:
            def __init__(self, *args, **kwargs):
                pass

            def cursor(self):
                return MockCursor()

            def close(self):
                pass
        
        # Patching the sqlite3.connect to return a mock connection
        with unittest.mock.patch('sqlite3.connect', return_value=MockConnection()):
            result = get_data_by_config_value("admin")
        
        expected_result = [("admin", "password123"), ("user1", "pass1")]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
