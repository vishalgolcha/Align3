x= -100000000007
y= -x

def valid(nx,ny):
    if nx>=4 or ny>=4 or nx<0 or ny<0:
        return False;
    return True;

#  terminating directions put into lists 
mid_diag=[ [[1,1],[-1,-1]] , [[1,-1],[-1,1]] ]
end_diag=[ [[1,1],[2,2]] , [[-1,-1],[-2,-2]] , [[1,-1],[2,-2]] , [[-1,1],[-2,2]] ]
mid_updown=[ [[-1,0],[1,0]] ,  [[0,-1],[0,1]] ]
end_updown=[ [[-1,0],[-2,0]] , [[1,0],[2,0]] , [[0,-1],[0,-2]] ,[[0,1],[0,2]] ]

options=[mid_diag,mid_updown,end_diag,end_updown]

# a class to create a game grid instance 
class grid_create :
    
    def __init__(self):
        
        self.gs= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.gc=0
        self.cnt=0 
        self.colm = [0,0,0,0]
        self.idx = -1
        self.idy = -1
        # useful for the analysis module 
        self.cnt_nodes= 0
        self.max_depth= 0
        self.func_time=0

    def analyze(self):
        return  [self.cnt_nodes ,self.cnt_nodes*8 ,self.max_depth ,self.func_time,self.cnt_nodes/self.func_time ]
    
#   permanently sets the grid pos to a particular value 

    def perma_set(self,a,b,minmax):
        self.gs[a][b]= minmax*10 + minmax
        self.colm[b] = self.colm[b]+1 

    def show_grid(self):
        print self.gs
          
#   helper function for terminate  function 
    def terminal(self,lx,ly,term):
        
        state= self.gs[lx][ly]
        for i in term:
            flag=0
            for j in i:
#               nx:  next x and ny: next y
                nx=j[0]+lx 
                ny=j[1]+ly 
                
                if valid(nx,ny)==True:
                    if self.gs[nx][ny]==0:
                        flag=1;
                        break;
                    elif self.gs[nx][ny] == state or self.gs[nx][ny] == (state*10) + state :
                        flag=2;
                    else :
                        flag=1;
                        break;
                else :
                    flag=1;
                    break;
                        
            if flag==2:
                return True ;
            else:
                continue ;
                
        return False

#   resets the grid[a][b] to 1/2 depending on given minimax value in the current state of backtracking   
    def sett(self,a,b,minmax):
        # problem here rectify 
        if   minmax==1:
            self.gs[a][b]=1;
        elif minmax==2 :
            self.gs[a][b]=2;
            
#         self.gc=self.gc+1;
    
#   checks if the state is in termination or not 
    def terminate(self,lx,ly):
        check = False
        for i in options :
            check= check or self.terminal(lx,ly,i)
        return check 
        
#   resets the grid[a][b] to 0 in the current state of backtracking   
    def reset(self,a,b):
        self.gs[a][b]=0;
    
#   the function should return utilities
#   utility defined based on depth to finish the game in shortest time
#   and to use minimalistic number of nodes
    def util(self,minmax,depth):
        z=None
        if   minmax== 0:
            z=(-1.0/depth)*10;
            
        elif minmax== 1:
            z=(1.0/depth)*10;            
        
        return z

#     isab   : translates to whether the method is running in alpha beta or nor 
#     palpha : parent's alpha 
#     pbeta  : parent's beta
#     minmax which player are you in the minmax state 
    def recurse(self,palpha,pbeta,minmax,depth,isab):         
        
        ret_val = None
        alpha   = palpha
        beta    = pbeta
        self.max_depth = max(self.max_depth,depth)

        if   minmax==0: # second player choosing moves
            ret_val= 1000000007
            
        elif minmax==1: # first player choosing moves
            ret_val= -1000000007
            
        if self.colm==[4,4,4,4]:
            return 0 # has to be a draw since it wasn't terminated before reaching this state
        
        #  self.colm and self.gs are grid states , self.colm is the alias of
        #  the succesor function here it tells us which column and row places to move to next
        # in the grid state
         
        for i,j in enumerate(self.colm):
            
#             current position to chose / mark 
            val1 = self.colm[i] 
            val2 = i
                        
            if j==4:
                continue;
            
            if self.gs[val1][val2]==11 or self.gs[val1][val2]==22: # likely to be replaced bya boolean grid
                continue;
            
            flag1=False 
            
            self.sett(val1,val2,minmax);
            if self.terminate(val1,val2)== True: 
                flag1=True
                z= self.util(minmax,depth)
            self.reset(val1,val2);
                
            if flag1==False:     
                self.colm[i]=self.colm[i]+1
                self.sett(val1,val2,minmax);
                z=self.recurse(alpha,beta,abs(minmax-1),depth+1,isab)
                self.reset(val1,val2);
                self.colm[i]=self.colm[i]-1
                
            if   minmax==0:
                ret_val= min(z,ret_val)
                beta   = min(beta,z)
                if depth==1 :
                    if ret_val == z :
                        self.idx= val1
                        self.idy= val2

            elif minmax==1:
                ret_val= max(z,ret_val)
                alpha  = max(alpha,z)
                if depth==1 :
                    if ret_val == z :
                        self.idx= val1
                        self.idy= val2
                        
#           this is where it gets pruned
            if isab==1:
                if alpha > beta :
                    break
        self.cnt_nodes=self.cnt_nodes + 1       
        return ret_val
    