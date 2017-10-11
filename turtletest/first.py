import turtle 
from time import time
import align3 as game


def init_turtles (raph,donney,mikey,leo):
# 	TNMT FTW
	raph.shape("turtle")
	raph.color("blue")
	
	# mikey  = turtle.Turtle()
	mikey.shape("turtle")
	mikey.color("red")
	
	# leo    = turtle.Turtle()
	leo.shape("turtle")
	leo.color("green")

	# donney = turtle.Turtle()
	donney.shape("turtle")
	donney.color("yellow")


raph   = turtle.Turtle() 
mikey  = turtle.Turtle()
leo    = turtle.Turtle()
donney = turtle.Turtle()

init_turtles(raph,donney,mikey,leo)
leo.speed(10)
squares=[]
square_limits=[]

def construct_square():
	leo.fd(70) ;leo.lt(90)
	leo.fd(70) ;leo.lt(90)
	leo.fd(70) ;leo.lt(90)
	leo.fd(70)

def board_init():

	for j in range(4):
		for i in range(4):
			leo.pu()
			xxx=20+ (i*70) ; yyy= 20+ (j*70)
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

id_to_grid=[]
grid_to_id={}

for i in range(4):
    for j in range(4):
        id_to_grid.append([i,j])

for i in range(16):
    grid_to_id[tuple(id_to_grid[i])]=i


def fill_square(i, turt):
	turt.begin_fill()
	for tx,ty in i :
		# print tx,ty	
		turt.pu()
		turt.goto(tx,ty)

	turt.end_fill()

def board_wipe():
	for i in squares : 
		raph.begin_fill()
		for tx,ty in i:
			# for tx,ty in j:
			raph.pu()
			raph.goto(tx,ty)
		raph.end_fill()		

def printxy(x,y):
	print (x,y)

break_flag=0

def rect_chek(x,y):
	flag=1
	for j,i in enumerate(square_limits) : 
		if x>= i[0][0] and x<=i[0][1] and y<=i[1][1] and y>=i[1][0]:
			return j	



# z = turtle.getscreen()._root.mainloop()

# print z
# print "move"
# time.sleep(10)
# quit()
play=game.grid_create()
play.perma_set(0,2)
posit= grid_to_id[(0,2)]
fill_square(square[posit],raph)

def func1(x, y):
    gotoresult = leo.goto(x, y)
    marker = rect_chek(x,y)
    # print marker
    fill_square(squares[marker],leo)
   	
    # print(leo.xcor(), leo.ycor())
    # leo.pd()
    
    play.recurse(game.x,game.y,1,1,1)
    
    ai_move = grid_to_id[(play.idx,play.idy)]
    fill_square(square[ai_move],raph)
    return gotoresult


def print_options():
	print "1. Play with minimax"
	print "2. Play with alpha beta"
	print "3. Analyze"
	print "4. End"
	chosen = sys.stdin.readline()

	if int(chosen)==1:
		disp.onscreenclick(func1)
	elif int(chosen)==2:
		disp.onscreenclick(func2)
	elif int(chosen)==4:
		turtle.bye()
	else:
		print "analyzing"
# print "\n"

print "The game has been initialized"
board_init()

disp.listen()

print_options()
turtle.mainloop()
