import turtle 
import time
import align3 as game
# object counter 
oc = 0
res= False
# -----------------------
# ------------------------
play   = None # will be initialised later 

def init_turtles (tlist):
# 	TNMT FTW
	tlist[0].shape("turtle")
	tlist[0].color("blue")

	tlist[1].shape("turtle")
	tlist[1].color("red")
	
	tlist[2].shape("turtle")
	tlist[2].color("green")

	tlist[3].shape("turtle")
	tlist[3].color("yellow")

	tlist[2].speed(100)

squares=[]
square_limits=[]



def construct_square(turt):
	turt.fd(70) ;turt.lt(90)
	turt.fd(70) ;turt.lt(90)
	turt.fd(70) ;turt.lt(90)
	turt.fd(70)

def board_init(leo,sensei):
	for j in range(4):
		for i in range(4):
			leo.pu()
			xxx=20+ (i*70) ; yyy= 20+ (j*70)
			leo.setx(xxx); leo.sety(yyy)
			leo.setheading(0)
			leo.begin_poly()
			leo.pd()
			construct_square(leo)
			leo.end_poly()
			p=leo.get_poly()
			# print p
			squares.append(p)
			square_limits.append([[xxx,xxx+70],[yyy,yyy+70]])
	sensei.pu()
	sensei.goto(-300,300)
	sensei.pd()
	sensei.write("1. Do not click on already clicked moves . ", font=("Arial",10, "normal"))
	sensei.pu()
	sensei.goto(-300,260)
	sensei.pd()	
	sensei.write("2. Do not click outside the game box ", font=("Arial",10, "normal"))
	sensei.pu()
	sensei.goto(-300,220)
	sensei.pd()	
	sensei.write("until you want to exit. ", font=("Arial",10, "normal"))



def draw_baseline(mikey):
	mikey.pensize(4)
	mikey.pu()
	mikey.fd(20)
	mikey.pd()
	mikey.fd(280)
	mikey.pu()
	mikey.goto(200,-250)
	mikey.pd()
	mikey.fd(30);mikey.lt(90)
	mikey.fd(30);mikey.lt(90)
	mikey.fd(30);mikey.lt(90)
	mikey.fd(30)

def fill_square(i, turt):
	turt.pu()
	turt.begin_fill()
	for tx,ty in i :
		# print tx,ty	
		turt.pu()
		turt.goto(tx,ty)

	turt.end_fill()
	# turt.done()
def board_wipe(raph):
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
		# print i
		# print "-------------"
		if x>= i[0][0] and x<=i[0][1] and y<=i[1][1] and y>=i[1][0]:
			return j
		# raph.end_fill()	

def gotoandprint(x,y):
    if x<0:
    	break_flag =1
    # leo.pu()

    # print squares
    marker = rect_chek(x,y)
    leo=turtle.Turtle();leo.shape(None);leo.color("green")
    leo.pu()
    gotoresult = leo.goto(x, y)
    raph=turtle.Turtle();raph.shape(None);raph.color("blue")
    # print marker
    fill_square(squares[marker],leo)
    fx,fy=id_to_grid[marker]
    play.perma_set(fx,fy,2)

    play.recurse(game.x,game.y,1,1,1)
    ai_marker = grid_to_id[(play.idx,play.idy)]
    fill_square(squares[ai_marker],raph)

# terminal check needed
    play.sett(play.idx,play.idy,1)
    if play.terminate(play.idx,play.idy)== True:
    	# print "1 won"
    	sensei = turtle.Turtle()
    	sensei.pu()
    	sensei.goto(-300,100)
    	sensei.pd()
    	sensei.write("computer wins", font=("Arial",10, "normal"))
    	global res
    	res= True
    	time.sleep(5)
    	# disp.bye() #check
    	turtle.bye() 

    play.perma_set(play.idx,play.idy,1)
    # print (play.idx,play.idy)
    
    # donney.pu()
    # donney.goto(x+50,y+60)
    # print(leo.xcor(), leo.ycor())

    # leo.pd()
    return gotoresult

def play_game(opt):
	global oc
	square_limits[:]=[]
	squares[:]=[]
# -----------------------------------
	disp = turtle.Screen()
	disp.setup (width=700, height=700)
# --------------------------------------
	
# 	raph=None;mikey=None;leo=None;donney=None;sensei=None
	tlist=[]
	for i in range(5):
		# print oc 
		locals()['turt_{0}'.format(oc)]=turtle.Turtle()
		tlist.append(locals()['turt_'+str(oc)])
		oc=oc+1
	# ----------------------------------------
	init_turtles(tlist)
# --------------------------------------
	
	global play
	global res
	play = game.grid_create()
	board_init(tlist[2],tlist[4])
	play.perma_set(0,2,1)
	draw_baseline(tlist[1])
	fill_square(squares[2],tlist[0])
	
	# if res== True:
	# 	res=False
		# disp.bye()

	disp.onscreenclick(gotoandprint)

	turtle.getscreen()._root.mainloop()
	for i in tlist :
		del i
# 	# print z
	
	# time.sleep(5)
	print "move"
	# disp.bye()


