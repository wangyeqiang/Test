def quick_sort(li,start,last):
	#print('start:%d,last:%d'%(start,last))
	#print('*'*15)
	if last <= start:
		return
	low = start
	high = last 
	mid_index = li[low]
	while high > low:
		while high >low and mid_index <= li[high]:
			high -= 1
		li[low] = li[high]
		#print('上面的',li)
		while high > low and mid_index> li[low]:
			low += 1
		li[high] = li[low]
		#print('下面的',li)
	li[low] = mid_index
	#print('start:%d,last:%d'%(start,last))
	#print('一个循环结束')
	quick_sort(alist,low+1,last)
	quick_sort(alist,start,low-1)    
	#这个两个语句谁先在前就把谁先可劲执行完

	#print(li)
 	#这里的start和last浪费了我很多时间，他们应该是动态传入的，而不是我想象的固定的0和9，每进行一次递归，他们就重新传入值，start可能会变成low+1，last会变成low-1，而我要是一直用0，9，就不对了。
alist = [54,26,93,17,77,31,44,55]
quick_sort(alist,0,len(alist)-1)
print(alist)



