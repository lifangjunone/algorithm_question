from unittest import TestCase, main


class BaseTest(TestCase):

    def setUp(self):
        print("测试用例执行前执行")

    def tearDown(self):
        print("测试用例执行后执行")


if __name__ == '__main__':
    main()
