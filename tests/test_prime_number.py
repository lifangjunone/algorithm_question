from alg_python.prime_number import PrimeNumber
from tests.common.base_test import BaseTest


class TestPrimeNumber(BaseTest):
    """
        测试素数
    """

    @staticmethod
    def generate_primes(n):
        """
            生成 n 以内的素数
        :return:
        """
        primes = []
        sieve = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
        return primes

    def setUp(self):
        self.prime_list = self.generate_primes(100)
        self.prime_size = len(self.prime_list)

    def test_imp01(self):
        res = 0
        obj = PrimeNumber()
        for ele in self.prime_list:
            if obj.imp01(ele):
                res += 1
            else:
                print(ele)
        self.assertEqual(self.prime_size, res)
