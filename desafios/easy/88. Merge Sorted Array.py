nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

i = j = 0
arr_clone = []

while i < m and j < n:
    if nums1[i] < nums2[j]:
        arr_clone.append(nums1[i])
        i += 1
    else:
        arr_clone.append(nums2[j])
        j += 1

while i < m:
    arr_clone.append(nums1[i])
    i += 1

while j < n:
    arr_clone.append(nums2[j])
    j += 1

nums1[:len(arr_clone)] = arr_clone
print(nums1)
