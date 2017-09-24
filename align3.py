x= -100000000007
y= -x

def valid(nx,ny):
    if nx>=4 or ny>=4 or nx<0 or ny<0:
        return False;
    return True;

mid_diag=[ [[1,1],[-1,-1]] , [[1,-1],[-1,1]] ]
end_diag=[ [[1,1],[2,2]] , [[-1,-1],[-2,-2]] , [[1,-1],[2,-2]] , [[-1,1],[-2,2]] ]
mid_updown=[ [[-1,0],[1,0]] ,  [[0,-1],[0,1]] ]
end_updown=[ [[-1,0],[-2,0]] , [[1,0],[2,0]] , [[0,-1],[0,-2]] ,[[0,1],[0,2]] ]

options=[mid_diag,mid_updown,end_diag,end_updown]

class grid_create :
    
    def __init__(self):
        
        self.gs= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.gc=0
        self.cnt=0
#         one for each column 
        self.colm = [0,0,0,0]
#         self.child_utils =[0,0,0,0]
        self.idx = -1
        self.idy = -1
        
    def perma_set(self,a,b,minmax):
        self.gs[a][b]= minmax*10 + minmax
        self.colm[b] = self.colm[b]+1

    def perma_reset(self,a,b):
        self.gs[a][b]=0
        self.colm[b] = a-1

    def show_grid(self):
        print self.gs
        
    def terminal(self,lx,ly,term):
        
        state= self.gs[lx][ly]
    
        for i in term:
            flag=0
            for j in i:
#                 next x;
                nx=j[0]+lx 
#                 next y;
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
    
    def sett(self,a,b,minmax):
        
        if   minmax==1:
            self.gs[a][b]=1;
        elif minmax==2 :
            self.gs[a][b]=2;
            
#         self.gc=self.gc+1;
        
    def terminate(self,lx,ly):
        check = False
        for i in options :
            check= check or self.terminal(lx,ly,i)
        return check 
        
    
    def reset(self,a,b):
        self.gs[a][b]=0;
#         self.gc=self.gc-1;


#   the function should return utilities 
    
    def recurse(self,alpha,beta,minmax,depth):         
        
        ret_val = None
        
        if   minmax==0: # second player choosing moves
            ret_val= 1000000007
            
        elif minmax==1: # first player choosing moves
            ret_val= -1000000007
            
        if self.colm==[4,4,4,4]:
            return 0 # has to be a draw since it wasn't terminated before reaching this state
        
        
        for i,j in enumerate(self.colm):
#             print self.colm[i],i,depth
            # current position to chose 
            val1 = self.colm[i] 
            val2 = i
            
            if j==4:
                continue;
            
            if self.gs[val1][val2]==11 or self.gs[val1][val2]==22: # likely to be replaced bya boolean grid
                continue;
            
            flag1=False 
            
            if True :
                self.colm[i]=self.colm[i]+1
                self.sett(val1,val2,minmax);
                
                if self.terminate(val1,val2)== True: 
                    flag1=True
#                     print val1,val2,depth
#                     check if the state is a terminating one 
#                     return utility can be depth inverse  as of now go by the assignment
#                     print(val1,val2)
                    self.reset(val1,val2);
                    self.colm[i]=self.colm[i]-1

                    if   minmax== 0:
#                          print depth,(-1.0/depth)*10;
                          z=(-1.0/depth)*10;

                    elif minmax== 1:
#                         print depth,(1.0/depth)*10 ;
                          z=(1.0/depth)*10;
                else:
                    self.reset(val1,val2);
                    self.colm[i]=self.colm[i]-1

                        
            if flag1==False :     
                self.colm[i]=self.colm[i]+1
                self.sett(val1,val2,minmax);
                
                                        
                z=self.recurse(alpha,beta,abs(minmax-1),depth+1)
                
                                            
                self.reset(val1,val2);
                self.colm[i]=self.colm[i]-1
                
            if   minmax==0:
                ret_val= min(z,ret_val)

                if depth==1 :
                    if ret_val == z :
                        self.idx= val1
                        self.idy= val2

            elif minmax==1:
                ret_val= max(z,ret_val)

                if depth==1 :
                    if ret_val == z :
                        self.idx= val1
                        self.idy= val2
        return ret_val
