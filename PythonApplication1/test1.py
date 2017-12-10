import unittest
import koalaapi

class Test_test1(unittest.TestCase):
    # def test_A(self):
    #    self.fail("Not implemented")
    def test_login(self):
        base_addr = "n1871312c4.iask.in"
        port = 23230
        user_name = "469231573@qq.com"
        password = "123456"
        client = koalaapi.client(
            base_address = base_addr,
            port = port,
            user_name = user_name,
            password = password
            )
        result = client.login()
        self.assertEqual(0, result.get("code"))

if __name__ == '__main__':
    unittest.main()
