def countSmaller(nums):
    from bisect import bisect_left,insort
    ans = []
    sorted_arr = []
    for num in reversed(nums):
        idx = bisect_left(sorted_arr,num)
        ans.append(idx)
        insort(sorted_arr,num)
    return ans[::-1]

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    result = countSmaller(nums)
    print(*result)

"""
| Aspect               | Answer                                                                                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Approach Used**    | **Binary Search + Sorted List (using `bisect_left` and `insort`)**                                                                                                     |
| **Time Complexity**  | **O(n²)** – `bisect_left` takes **O(log n)**, but `insort` requires shifting elements in a Python list, taking **O(n)**. Repeated for `n` elements.                    |
| **Space Complexity** | **O(n)** – for the `sorted_arr` and the output list.                                                                                                                   |
| **Is it Optimal?**   | **No.** More optimized solutions use a **Fenwick Tree (Binary Indexed Tree)**, **Segment Tree**, or **Merge Sort** to achieve **O(n log n)** time with **O(n)** space. |

"""