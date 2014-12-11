def memoize(proc):
	memos = {}
	def newproc(x):
		if x in memos:
			return memos[x]
		else:
			t = proc(x, newproc)
			memos[x] = t
			return t
	return newproc