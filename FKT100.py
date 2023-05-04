import math
from IKT100 import IKT100

class FKT100:

    IK = IKT100()

    #LINK LENGTHS IN m
    A1,A2,A3,A4,A5,A6 = IK.getLinkLengths()
    
    #JOINT OFFSET IN m
    ex,D1,D6 = IK.getJointOffset()


    def SetT1(self, t1=0):
        self.T1 = (t1/180.0)*math.pi
        
    def SetT2(self, t2=0):
        self.T2 = (t2/180.0)*math.pi
        
    def SetT3(self, t3=0):
        self.T3 = (t3/180.0)*math.pi
        
    def SetT4(self, t4=0):
        self.T4 = (t4/180.0)*math.pi
        
    def SetT5(self, t5=0):
        self.T5 = (t5/180.0)*math.pi
        
    def SetT6(self, t6=0):
        self.T6 = (t6/180.0)*math.pi  
        


    def H0_3(self):  
        T1 = self.T1
        T2 = self.T2
        T3 = self.T3
        sa = math.cos(T1)*math.cos(T2)*math.cos(T3) + (-math.cos(T1)*math.sin(T2)*math.sin(T3))
        sb = math.sin(T1)
        sc = math.cos(T1)*math.cos(T2)*math.sin(T3) + (math.cos(T1)*math.sin(T2)*math.cos(T3))
        
        sd = self.A3*math.cos(T1)*math.cos(T2)*math.cos(T3) + (- self.A3*math.cos(T1)*math.sin(T2)*math.sin(T3)) + self.A2*math.cos(T1)*math.cos(T2) + self.A1*math.cos(T1)

        se = math.sin(T1)*math.cos(T2)*math.cos(T3) + (-math.sin(T1)*math.sin(T2)*math.sin(T3))
        sf = -math.cos(T1)
        sg = math.sin(T1)*math.cos(T2)*math.sin(T3) + math.sin(T1)*math.sin(T2)*math.cos(T3)
        
        sh = self.A3*math.sin(T1)*math.cos(T2)*math.cos(T3) + (-self.A3*math.sin(T1)*math.sin(T2)*math.sin(T3)) + self.A2*math.sin(T1)*math.cos(T2) + self.A1*math.sin(T1)

        si = math.sin(T2)*math.cos(T3) + math.cos(T2)*math.sin(T3)
        sj = 0
        sk = math.sin(T2)*math.sin(T3) + (-math.cos(T2)*math.cos(T3))
        
        sl = self.A3*math.sin(T2)*math.cos(T3) + self.A3*math.cos(T2)*math.sin(T3) + self.A2*math.sin(T2) + self.D1

        H0_3A = ([sa,sb,sc,sd],
                 [se,sf,sg,sh],
                 [si,sj,sk,sl],
                 [0,  0, 0, 1])
        return H0_3A

#The homogeneous transformation matrix [H3_6] spherical wrist section
    def H3_6(self):
        T4 = self.T4
        T5 = self.T5
        T6 = self.T6
        la = math.cos(T4)*math.cos(T5)*math.cos(T6) - math.sin(T4)*math.sin(T6)
        lb = -math.cos(T4)*math.cos(T5)*math.sin(T6) - math.sin(T4)*math.cos(T6)
        lc = math.cos(T4)*math.sin(T5)
        
        ld = math.cos(T4)*math.sin(T5)*self.D6

        le = math.sin(T4)*math.cos(T5)*math.cos(T6) + math.cos(T4)*math.sin(T6)
        lf = -math.sin(T4)*math.cos(T5)*math.sin(T6) + math.cos(T4)*math.cos(T6)
        lg = math.sin(T4)*math.sin(T5)
        
        lh = math.sin(T4)*math.sin(T5)*self.D6

        li = -math.sin(T5)*math.cos(T6)
        lj = math.sin(T5)*math.sin(T6)
        lk = math.cos(T5)
        
        ll = math.cos(T5)*self.D6

        H3_6A =    ([la,lb,lc,ld],
                    [le,lf,lg,lh],
                    [li,lj,lk,ll],
                    [0,0,0, 1])
        return H3_6A

#The homogeneous transformation matrix  row.col entries are given by the formulars below

#[a,b,c,d]
#[e,f,g,h]
#[i,j,k,l]
#[0,0,0,1]

#[00,01,02,03]
#[10,11,12,13]
#[20,21,22,23]
#[30,31,32,33]

#FIRST ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
    def H0_6_Default(self):
        H0_3A = self.H0_3()
        H3_4A = self.H3_6()
       
        #FIRST ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6  
        A = H0_3A[0][0] * H3_4A[0][0] + H0_3A[0][1] * H3_4A[1][0] + H0_3A[0][2] * H3_4A[2][0] + H0_3A[0][3] * H3_4A[3][0]
        B = H0_3A[0][0] * H3_4A[0][1] + H0_3A[0][1] * H3_4A[1][1] + H0_3A[0][2] * H3_4A[2][1] + H0_3A[0][3] * H3_4A[3][1]
        C = H0_3A[0][0] * H3_4A[0][2] + H0_3A[0][1] * H3_4A[1][2] + H0_3A[0][2] * H3_4A[2][2] + H0_3A[0][3] * H3_4A[3][2]
        D = H0_3A[0][0] * H3_4A[0][3] + H0_3A[0][1] * H3_4A[1][3] + H0_3A[0][2] * H3_4A[2][3] + H0_3A[0][3] * H3_4A[3][3]
        #SECOND ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        E = H0_3A[1][0] * H3_4A[0][0] + H0_3A[1][1] * H3_4A[1][0] + H0_3A[1][2] * H3_4A[2][0] + H0_3A[1][3] * H3_4A[3][0]
        F = H0_3A[1][0] * H3_4A[0][1] + H0_3A[1][1] * H3_4A[1][1] + H0_3A[1][2] * H3_4A[2][1] + H0_3A[1][3] * H3_4A[3][1]
        G = H0_3A[1][0] * H3_4A[0][2] + H0_3A[1][1] * H3_4A[1][2] + H0_3A[1][2] * H3_4A[2][2] + H0_3A[1][3] * H3_4A[3][2]
        H = H0_3A[1][0] * H3_4A[0][3] + H0_3A[1][1] * H3_4A[1][3] + H0_3A[1][2] * H3_4A[2][3] + H0_3A[1][3] * H3_4A[3][3]
        #THIRD ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        I = H0_3A[2][0] * H3_4A[0][0] + H0_3A[2][1] * H3_4A[1][0] + H0_3A[2][2] * H3_4A[2][0] + H0_3A[2][3] * H3_4A[3][0]
        J = H0_3A[2][0] * H3_4A[0][1] + H0_3A[2][1] * H3_4A[1][1] + H0_3A[2][2] * H3_4A[2][1] + H0_3A[2][3] * H3_4A[3][1]
        K = H0_3A[2][0] * H3_4A[0][2] + H0_3A[2][1] * H3_4A[1][2] + H0_3A[2][2] * H3_4A[2][2] + H0_3A[2][3] * H3_4A[3][2]
        L = H0_3A[2][0] * H3_4A[0][3] + H0_3A[2][1] * H3_4A[1][3] + H0_3A[2][2] * H3_4A[2][3] + H0_3A[2][3] * H3_4A[3][3]

        #THE HOMOGENOUS TRANSFORMATION MATRIX FROM FRAME 0 TO FRAME 6
        H0_6 = ([A, B, C, D],
                [E, F, G, H],
                [I, J, K, L],
                [0, 0, 0, 1])
        return H0_6


    def H0_6(self):
        H0_3A = self.H0_3()
        H3_4A = self.H3_6()
       
        #FIRST ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6  
        A = H0_3A[0][0] * H3_4A[0][0] + H0_3A[0][1] * H3_4A[1][0] + H0_3A[0][2] * H3_4A[2][0] + H0_3A[0][3] * H3_4A[3][0]
        An = f"{A:.6f}"
        B = H0_3A[0][0] * H3_4A[0][1] + H0_3A[0][1] * H3_4A[1][1] + H0_3A[0][2] * H3_4A[2][1] + H0_3A[0][3] * H3_4A[3][1]
        Bn = f"{B:.6f}"
        C = H0_3A[0][0] * H3_4A[0][2] + H0_3A[0][1] * H3_4A[1][2] + H0_3A[0][2] * H3_4A[2][2] + H0_3A[0][3] * H3_4A[3][2]
        Cn = f"{C:.6f}"
        D = H0_3A[0][0] * H3_4A[0][3] + H0_3A[0][1] * H3_4A[1][3] + H0_3A[0][2] * H3_4A[2][3] + H0_3A[0][3] * H3_4A[3][3]
        Dn = f"{D:.6f}"
        #SECOND ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        
        E = H0_3A[1][0] * H3_4A[0][0] + H0_3A[1][1] * H3_4A[1][0] + H0_3A[1][2] * H3_4A[2][0] + H0_3A[1][3] * H3_4A[3][0]
        En = f"{E:.6f}"
        F = H0_3A[1][0] * H3_4A[0][1] + H0_3A[1][1] * H3_4A[1][1] + H0_3A[1][2] * H3_4A[2][1] + H0_3A[1][3] * H3_4A[3][1]
        Fn = f"{F:.6f}"
        G = H0_3A[1][0] * H3_4A[0][2] + H0_3A[1][1] * H3_4A[1][2] + H0_3A[1][2] * H3_4A[2][2] + H0_3A[1][3] * H3_4A[3][2]
        Gn = f"{G:.6f}"
        H = H0_3A[1][0] * H3_4A[0][3] + H0_3A[1][1] * H3_4A[1][3] + H0_3A[1][2] * H3_4A[2][3] + H0_3A[1][3] * H3_4A[3][3]
        Hn = f"{H:.6f}"
        #THIRD ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        
        I = H0_3A[2][0] * H3_4A[0][0] + H0_3A[2][1] * H3_4A[1][0] + H0_3A[2][2] * H3_4A[2][0] + H0_3A[2][3] * H3_4A[3][0]
        In = f"{I:.6f}"
        J = H0_3A[2][0] * H3_4A[0][1] + H0_3A[2][1] * H3_4A[1][1] + H0_3A[2][2] * H3_4A[2][1] + H0_3A[2][3] * H3_4A[3][1]
        Jn = f"{J:.6f}"
        K = H0_3A[2][0] * H3_4A[0][2] + H0_3A[2][1] * H3_4A[1][2] + H0_3A[2][2] * H3_4A[2][2] + H0_3A[2][3] * H3_4A[3][2]
        Kn = f"{K:.6f}"
        L = H0_3A[2][0] * H3_4A[0][3] + H0_3A[2][1] * H3_4A[1][3] + H0_3A[2][2] * H3_4A[2][3] + H0_3A[2][3] * H3_4A[3][3]
        Ln = f"{L:.6f}"
        #THE HOMOGENOUS TRANSFORMATION MATRIX FROM FRAME 0 TO FRAME 6
        H0_6 = ([An, Bn, Cn, Dn],
                [En, Fn, Gn, Hn],
                [In, Jn, Kn, Ln],
                [0, 0, 0, 1])
        return H0_6


    def getH0_6(self):
        return self.H0_6()    

    def getPX(self):
        return self.H0_6_Default()[0][3]

    def getPY(self):
        return self.H0_6_Default()[1][3]

    def getPZ(self):
        return self.H0_6_Default()[2][3]    



