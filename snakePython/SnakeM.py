import random
class serpiente:
    #nuestra serviente esta formada por 3 valores x,y,d una matriz de 10*10
    bl=True;    
    queue=[];
    posiblesPuntos=[]
    pi=[]
    pf=[]
    vivo=True
    def __init__(self) :
        
        for i in range(15):
            for j in range(15):
                if not(i==4 and j==4):
                    self.posiblesPuntos.append([i,j])
                
        #cabeza
        self.queue.append([4,4,1]); #uno
        #self.queue.append([3,4,1])
        #self.queue.append([2,4,1])
        self.pi=[2,2]
        self.pf=[2,2]
        
    def getCola(self):
        return self.queue;
    def mover(self,pos):
        self.situacionCab()
        bl=False
        cab=[]
        cols=self.queue[-1]
        vl=0;
        #izq =3: der=1:arib=4:abajo=1
        cola=self.queue[-1];
        if(cola[0]==self.pf[0] and cola[1]==self.pf[1]): bl=True
        extraerCAbeza=True;
        self.posiblesPuntos.append([cols[0],cols[1]]);    
        for x in self.queue:
            if(pos==8 or abs(pos-x[2])==2):
                pos=x[2]
            cabAc=[x[0],x[1]]
            if(pos==1):
                if(x[0]>13):
                    x[0]=0; 
                else:
                    x[0]=x[0]+1;
            elif pos==3:
                if(x[0]==0):
                    x[0]=14; 
                else:
                    x[0]=x[0]-1;
            elif pos==2:
                if(x[1]>13):
                    x[1]=0; 
                else:
                    x[1]=x[1]+1;
            elif pos==4:
                if(x[1]==0):
                    x[1]=14; 
                else:
                    x[1]=x[1]-1;
            vl=x[2]
            x[2]=pos;
            pos=vl;
            if(extraerCAbeza): 
                cab=[x[0],x[1]]
                
                extraerCAbeza=False
                
            else: 
                self.vivo=not(cab[0]==x[0] and cab[1]==x[1])
                if(not(self.vivo) ):
                    break
        if(bl):
            self.situacionCol()
        if(self.vivo):self.posiblesPuntos.remove(cab)
        
        
       
        #    print(x)
    
    def situacionCab(self):
        #verificar creacion
        if(self.pi[0]==self.queue[0][0] and self.pi[1]==self.queue[0][1]):
            self.pi=self.crearPos()
    def situacionCol(self):
        #if(self.pf[0]==self.queue[-1][0] and self.pf[1]==self.queue[-1][1]):
            self.queue.append([self.pf[0],self.pf[1],8])
            self.pf=self.pi;
    
    def crearPos(self):
        
        return random.choice(self.posiblesPuntos)
    def reiniciar(self):
        self.queue=[]
        self.posiblesPuntos=[]
        self.vivo=True;
        self.bl=True
        for i in range(15):
            for j in range(15):
                if not(i==4 and j==4):
                    self.posiblesPuntos.append([i,j])
                
        #cabeza
        
        self.queue.append([4,4,1]); #uno
        #self.queue.append([3,4,1])
        #self.queue.append([2,4,1])
        self.pi=[2,2]
        self.pf=[2,2]
            
            
#sl=serpiente();
#sl.mover(1);
#sl.mover(2)
#sl.mover(3)