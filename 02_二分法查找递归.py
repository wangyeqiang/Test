def binary_search(alist,item):
	n = len(alist)
	mid = n//2
	if n > 0:
		if item == alist[mid]:
			return True
		if item < alist[mid]:
			return binary_search(alist[:mid],item)
		elif item > alist[mid]:
			return binary_search(alist[mid+1:],item)
		#注意要打上return,因为每一层都要有返回值，如果不返回，那么
		#就都返回最后的False
	return False
A = [11,22,33,44,57,68,79,88,91]
print(binary_search(A,11))
print(binary_search(A,157))
