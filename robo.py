#5 2 south RW2LW4R
#3 -2 east
import math
#x, y = 0
pos = [0,0]
D = ['east','west','south','north']
s = raw_input()
ln = len(D)-1
E = D[0]
W = D[1]
S = D[2]
N = D[3]
#print s

movement = s.split(" ")
x = int(movement[0])      #movement on x axis
y = int(movement[1])     #movement on y axis)
D = movement[2]      #facing
s = movement[3]		 #walk string

pos[0] += x
pos[1] += y


i = 0
for i in xrange(len(s)-1):
	#print s[i-1]

	move  = s[i]
	if move == "R":
		i += 1
		path = s[i]
		if path == "W":
			i += 1
			num = int(s[i])
			if D == S:
				D = W
				x = x - num
			elif D == N:
				D = E
				x = x + num
			elif D == E:
				D = S
				y = y - num
			elif D == W:
				D = N
				y = y + num
			else:
				pass
	else:
		pass
	
	if move == "L":
		#print "hello"
		i += 1
		if s[i] == "W":
			i += 1
			num = int(s[i])
			if D == S:
				D = E
				x = x + num
			elif D == N:
				D = W
				x = x - num
			elif D == E:
				D = N
				y = y + num
			elif D == W:
				D = S
				y = y - num
			else:
				pass
	else:
		pass


Dir = D
print D

if s[-1] == "R":
	if Dir == S :
		D = E
	elif Dir ==N:
		D = W
	elif Dir == E:
		D = S
	else:
		D = N
else: 
	pass

if s[-1] == "L":
	if Dir == S :
		D = W
	elif Dir ==N:
		D = E
	elif Dir == E:
		D = N
	else:
		D = S
else: 
	pass




print x, y , D




			

