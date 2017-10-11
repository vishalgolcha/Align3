import turtle
cnt=0
tlist=[]
for i in range(5): 
	locals()['turt_{0}'.format(cnt)]=turtle.Turtle()
	z='turt_'+str(cnt)
	cnt=cnt+1
print tlist
print type(turt_0)