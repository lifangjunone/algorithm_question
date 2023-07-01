

class PrimeNumber:
    """
    素数： 素数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数，也称之为质数
    判断一个数是否是素数
    """

    @staticmethod
    def method_one(num: int) -> bool:
        """
        暴力实现素数
        :param num:
        :return:
        """
        if num <= 1:
            return False
        square_root = num ** 1/2 + 1
        for i in range(2, square_root):
            if num % i == 0:
                return False
        return True


class TestPrimeNumber:
    pass