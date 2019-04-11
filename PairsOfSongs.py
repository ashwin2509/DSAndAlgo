def solution(time):
	res = []
	for i in times:
		res.append(i % 60)

	count = collections.Counter(res)

	for key in count:
		if count == 0:
			_sum += count[key] * (count[key]-1) / 2 
		elif 0 < key < 30:
			if 60 - key in count:
				_sum += count[key] * count[60 - key]
		elif count == 30:
			_sum += count[key] * (count[key]-1) / 2 
	return _sum 



