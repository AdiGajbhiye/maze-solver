import sys
m = 6
n = 6
a = [[0 for i in range(n+2)] for i in range(m+2)]
puzz = open("prob.txt","r")
for i in range(1,m+1):
	s = puzz.read(n+1)
	for j in range(1,n+1):
		a[i][j] = s[j-1]
puzz.close()
a[0] = ["#" for i in range(n+2)]
a[m+1] = a[0]
for i in range(1,m+1):
	a[i][0] = '#'
	a[i][n+1] = '#'
def disp():
	for i in range(m+2):
		for j in range(n+2):
			print a[i][j],
		print
	print "\n\n"
st_x = 0
while 'S' not in a[st_x]:
	st_x += 1
st_y = a[st_x].index('S')
def sol(i,j,direc,l):
	if a[i][j] == 'G':
		disp()
		sys.exit(0)
	if l > 36:
		return False
	if a[i][j] == '#':
		return False
	a[i][j] = '@'
	if direc == 'R':
		ans = sol(i,j+1,'R',l+1) or sol(i-1,j,'U',l+1) or sol(i+1,j,'D',l+1)
		if not(ans):
			a[i][j] = '.'
		return ans
	if direc == 'L':
		ans = sol(i,j-1,'L',l+1) or sol(i-1,j,'U',l+1) or sol(i+1,j,'D',l+1)
		if not(ans):
			a[i][j] = '.'
		return ans
	if direc == 'U':
		ans = sol(i-1,j,'U',l+1) or sol(i,j+1,'R',l+1) or sol(i,j-1,'L',l+1)
		if not(ans):
			a[i][j] = '.'
		return ans
	if direc == 'D':
		ans = sol(i+1,j,'D',l+1) or sol(i,j+1,'R',l+1) or sol(i,j-1,'L',l+1)
		if not(ans):
			a[i][j] = '.'
		return ans

disp()
x = sol(st_x,st_y,'R',0)
if not(x):
	print "CAN'T BE SOLVED"
