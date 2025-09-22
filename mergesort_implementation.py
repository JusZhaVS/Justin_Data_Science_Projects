from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr: List[int], L: int, M: int, R: int):
            left, right = arr[L:M+1], arr[M+1: R+1]
            i = L #for the main array
            j,k = 0,0 #for the left and right subarrays

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                i += 1
                k += 1


        def mergeSort(arr: List[int], l: int, r: int) -> None:
            if l == r:
                return
            
            m = l + (r-l) // 2
            mergeSort(arr, l, m) #sort left
            mergeSort(arr, m+1, r) #sort right
            merge(arr, l, m, r) #now combine

            return
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums