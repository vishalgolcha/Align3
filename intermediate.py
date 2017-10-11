import turtle 
import time

leo=None
raph=None
mikey=None
squares=[]
square_limits=[]	
disp = None

id_to_grid=[]
grid_to_id={}

for i in range(4):
    for j in range(4):
        id_to_grid.append([i,j])

for i in range(16):
    grid_to_id[tuple(id_to_grid[i])]=i

cnt=0

def construct_square():
	global leo
	leo.fd(70) ;leo.lt(90)
	leo.fd(70) ;leo.lt(90)
	leo.fd(70) ;leo.lt(90)
	leo.fd(70)

def fill_square(i, turt):
	turt.begin_fill()
	for tx,ty in i :
		# print tx,ty	
		turt.pu()
		turt.goto(tx,ty)

	turt.end_fill()

def game_restart():
	# global mikey; global raph
	mikey.clear()
	raph.clear()

def rect_chek(x,y,square_limits):
	# global square_limits
	flag=1
	for j,i in enumerate(square_limits) : 
		if x>= i[0][0] and x<=i[0][1] and y<=i[1][1] and y>=i[1][0]:
			return j

def gotoandprint(x, y):
# 	print "boom"
# 	global raph;global disp
# 	global squares
# 	global cnt

# 	cnt= cnt+1 
	raph.pu()
	gotoresult = raph.goto(x, y)
	marker = rect_chek(x,y,square_limits)
	fill_square(squares[marker],raph)
		
	# if cnt==5:
	# 	return gotoresult	
	# else :
	# disp.onscreenclick(gotoandprint)
	gotoandprint(x,y)
	return gotoresult



def board_init():
	global disp;
	global mikey; global raph; global leo
	global squares; global square_limits


	disp = turtle.Screen()
	disp.setup (width=700, height=700)

	raph   = turtle.Turtle() 
	mikey  = turtle.Turtle()
	leo    = turtle.Turtle()
	leo.speed(10)

	mikey.shape("turtle")
	mikey.color("green")
	raph.shape("turtle")
	raph.color("blue")

	for j in range(4):
		for i in range(4):
			leo.pu()
			xxx=20+ (i*70) ; yyy= 20+ (j*70);
			leo.setx(xxx); leo.sety(yyy)
			leo.setheading(0)
			leo.begin_poly()
			leo.pd()
			construct_square()
			leo.end_poly()
			p=leo.get_poly()
			# print p
			squares.append(p)
			square_limits.append([[xxx,xxx+70],[yyy,yyy+70]])
	
def draw_board():
	board_init()



# def obj_pass(obj):
# 	obj.disp.onscreenclick(gotoandprint)

	
	

# player = tnmt()
draw_board()
# global disp
disp.onscreenclick(gotoandprint)

# time.sleep(3)
print "move"

# board_init()
# draw_baseline()




