def binary_search(alist,item):
	'非递归实现'
	n = len(alist)
	first = 0
	last = n-1
	
	while first <= last:
		mid = (first+last)//2
		if item == alist[mid]:
			return True
		
		if item < alist[mid]:
			last = mid-1
		elif item > alist[mid]:
			first = mid+1
	return False
A= [11,22,33,44,55,67,79,81,87,99,100,111,121,131,141]
print(binary_search(A,121))
print(binary_search(A,139))