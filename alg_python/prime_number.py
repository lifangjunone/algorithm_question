

class PrimeNumber:
    """
        素数
    """

    def __init__(self):
        self.square_toot = 0.5

    def imp01(self, num):
        if num == 2:
            return True
        elif num == 3:
            return True
        max_factor = num ** self.square_toot
        if max_factor < 2:
            return False
        for i in range(2, int(num ** self.square_toot) + 1):
            if num % i == 0:
                return False
        return True




