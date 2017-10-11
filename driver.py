import turtle 
import time
import align3 as game
import sys

disp =None

last_alpha_beta=[0,0,0,0,0]
last_minimax=[0,0,0,0,0]

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

#  board_init saves different polygons in the grid and constructs the game 
def board_init():
	global disp
	disp=turtle.Screen();
	disp.setup(700,700)
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


def printxy(x,y):
	print (x,y)

break_flag=0

#  to check the  coordinates belong to  which rectangle in the grid 
def rect_chek(x,y):
	flag=1
	for j,i in enumerate(square_limits) : 
		if x>= i[0][0] and x<=i[0][1] and y<=i[1][1] and y>=i[1][0]:
			return j	

play=game.grid_create()
play.perma_set(0,2,1)
posit= grid_to_id[(0,2)]

def wipeout():
	raph.clear()
	donney.clear()


 
# function to bind to onclick events in case alpha beta is to be used
def func1(x, y):
    
    # gotoresult = leo.goto(x, y)
    global play
    global last_alpha_beta
    global last_minimax
    marker = rect_chek(x,y)
    
    # print marker
    donney.pu()
    fill_square(squares[marker],donney)
    # print(leo.xcor(), leo.ycor())
    donney.pd()
    humanx= id_to_grid[marker][0]
    humany= id_to_grid[marker][1]

    play.perma_set(humanx,humany,2)
    
    st= time.time()
    play.recurse(game.x,game.y,1,1,1)
    en= time.time()
    diff= en - st 
    play.func_time = play.func_time + diff 


    ai_move = grid_to_id[(play.idx,play.idy)]
    fill_square(squares[ai_move],raph)

    play.sett(play.idx,play.idy,1)
    if play.terminate(play.idx,play.idy)==True:
    	
    	last_alpha_beta = play.analyze()
    	analy_ab = [0,None,0]
    	print"Computer wins\n"    	
    	wipeout()
    	play=game.grid_create()
    	play.perma_set(0,2,1)
    	posit= grid_to_id[(0,2)]
    	fill_square(squares[posit],raph)
    	# --------------------------------
    	analy_ab[0]= last_alpha_beta[0]
    	if last_minimax[0]!= 0:
    		analy_ab[1]= (last_minimax[0]-analy_ab[0])/(float)(last_minimax[0])
    	analy_ab[2]= last_alpha_beta[3]
    	# -----------------------------------	  
    	print(analy_ab)
    	print_options()
    else:
    	play.perma_set(play.idx,play.idy,1)

    # return gotoresult

# function to bind to onclick events in minimax is to be used
def func2(x, y):
    # gotoresult = leo.goto(x, y)
    global play
    global last_alpha_beta
    global last_minimax
    marker = rect_chek(x,y)
    # print marker
    donney.pu()
    fill_square(squares[marker],donney)
    # print(leo.xcor(), leo.ycor())
    donney.pd()
    humanx= id_to_grid[marker][0]
    humany= id_to_grid[marker][1]

    play.perma_set(humanx,humany,2)
    
    st= time.time()
    play.recurse(game.x,game.y,1,1,0)
    en= time.time()
    
    diff= en - st 
    play.func_time =play.func_time + diff 


    ai_move = grid_to_id[(play.idx,play.idy)]
    fill_square(squares[ai_move],raph)

    play.sett(play.idx,play.idy,1)
    if play.terminate(play.idx,play.idy)==True:
    	wipeout()
    	last_minimax= play.analyze()
    	print"Computer wins\n"    	
    	play=game.grid_create()
    	play.perma_set(0,2,1)
    	posit= grid_to_id[(0,2)]
    	fill_square(squares[posit],raph)
    	print(last_minimax)
    	print_options()
    else:
    	play.perma_set(play.idx,play.idy,1)
    # return gotoresult

def print_options():
	print "1. Play with minimax"
	print "2. Play with alpha beta"
	print "3. Analyze"
	print "4. End"
	chosen = sys.stdin.readline()

	if int(chosen)==1:
		disp.onscreenclick(func2)
	elif int(chosen)==2:
		disp.onscreenclick(func1)
	elif int(chosen)==4:
		turtle.bye()
	else:
		print "analyzing"
		print last_minimax
		print last_alpha_beta
        # print_options()
# print "\n"

print "The game has been initialized \n clicking on the X in window exits the game."
board_init()
fill_square(squares[posit],raph)

disp.listen()
print_options()
turtle.mainloop()
