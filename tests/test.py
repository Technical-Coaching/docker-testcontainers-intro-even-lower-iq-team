import unittest

from testcontainers.mysql import MySqlContainer


class MyTestCase(unittest.TestCase):

    def test_etl(self):
        self.mysql_container = (MySqlContainer('mysql:5.7')
                                .with_bind_ports(3306, 3306)
                                .with_env('MYSQL_USER', "root")
                                .with_env('MYSQL_PASSWORD', "root")
                                )

        self.mysql_container.start()

        print("created and started container")
        self.assertTrue(True, True)


if __name__ == '__main__':
    unittest.main()
