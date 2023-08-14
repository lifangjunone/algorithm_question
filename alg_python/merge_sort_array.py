import heapq


class PrimeNumber:
    """
        合并两个有序数组
    """

    def merge(self, nums1, nums2):
        nums1 = heapq.merge(nums1, nums2)
        return nums1

    def merge2(self, nums1, nums2):
        m = len(nums2)
        n = len(nums1) - m
        i = n - 1
        j = m - 1
        max = n + m - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[max] = nums1[i]
                i -= 1
            else:
                nums1[max] = nums2[j]
                j -= 1
            max -= 1
        while i >= 0:
            nums1[max] = nums1[i]
            i -= 1
            max -= 1
        while j >= 0:
            nums1[max] = nums2[j]
            j -= 1
            max -= 1
        print(nums1)

    def merge3(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        _max = n + m - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[_max] = nums1[i]
                i -= 1
            else:
                nums1[_max] = nums2[j]
                j -= 1
            _max -= 1
        while j >= 0:
            nums1[_max] = nums2[j]
            j -= 1
            _max -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 7, 9, 20, 0, 0, 0]
    nums2 = [2, 5, 6]
    PrimeNumber().merge2(nums1, nums2)
