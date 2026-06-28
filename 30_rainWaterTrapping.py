def totalRainwaterTrapped(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if left_max <= height[left]:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if right_max <= height[right]:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


hei = list(map(int, input().split()))
print(totalRainwaterTrapped(hei))

"""
| Metric               | Value                                         |
| -------------------- | --------------------------------------------- |
| **Approach**         | Two Pointers with Running Left/Right Maximums |
| **Time Complexity**  | **O(n)**                                      |
| **Space Complexity** | **O(1)**                                      |
| **Optimal?**         | **Yes**                                       |


"""