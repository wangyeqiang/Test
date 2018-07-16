def merge_sort(alist):
	n = len(alist)
	if n <=1:
		return alist
	mid = n//2
	left_alist = merge_sort(alist[:mid]) 
	right_alist = merge_sort(alist[mid:])

	left_pointer = 0
	right_pointer =0

	result = []
	while left_pointer < len(left_alist) and right_pointer < len(right_alist):
		if left_alist[left_pointer]<= right_alist[right_pointer]:
			result.append(left_alist[left_pointer])
			left_pointer += 1
		else:
			result.append(right_alist[right_pointer])
			right_pointer += 1
	result += left_alist[left_pointer:]
	result += right_alist[right_pointer:]  #必须得加冒号，否则超出范围
	return result
print(merge_sort([1,3,57,2,1,2,3,4]))
