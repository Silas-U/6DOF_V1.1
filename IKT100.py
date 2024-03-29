'''-----------------------------------------------------------------------------------------------------#
#                                                                                                       #
# Program : kinematics for a 6DOF robot arm                                                             #
# Author  : Udofia, Silas Silas                                                                         #
# Project : ROBOT ARM                                                                                   #
# Model   : T100                                                                                        #
# Ser_Nom : RB346A6DOFUSSOCT92022                                                                       #
# Date    : October 9, 2022                                                                             #
#                                                                                                       #   
# (inverse kinematics) Given the desired end effector position vector and orientation, solves           #
# for the joint variables th1, th2, th3, th4, th5, th6                                                  #
#                                                                                                       #
-----------------------------------------------------------------------------------------------------'''
'''DH TABLE FOR T100 ROBOT ARM'''
'''---------+-------------+--------------+---------------+--------------+
|    Link   |    Theta    |  Link Twist  |  Link Length  | Joint Offset |
------------+-------------+--------------+---------------+--------------+
|     1     |     Th1     |      90      |       A1      |    D1 + ex   |
|     2     |     Th2     |      0       |       A2      |       0      |
|     3     |     Th3     |      90      |       A3      |       0      |
|     4     |     Th4     |     -90      |       0       |       0      |
|     5     |     Th5     |      90      |       0       |       0      |
|     6     |     Th6     |      0       |       0       |       D6     |
+-----------+-------------+--------------+---------------+------------'''
import math
class IKT100:
    
    #JOINT OFFSET IN m
    #JOINT OFFSET IN m
    ex = 0.0
    D1 = 0.085 + ex #Z
    D6 = 0.065 #End effector length

    #LINK LENGTHS IN m
    A1 = 0.045
    A2 = 0.12
    A3 = 0.17
    A4 = 0 #not used but inclusive
    A5 = 0 #not used but inclusive
    A6 = 0 #not used but inclusive
 
    
    def __init__(self, t1=0, t2=0, t3=0):
        self.T1 = (t1/180.0)*math.pi
        self.T2 = (t2/180.0)*math.pi
        self.T3 = (t3/180.0)*math.pi

    def getLinkLengths(self):
        return self.A1, self.A2, self.A3, self.A4, self.A5, self.A6    

    def getJointOffset(self):
        return self.ex, self.D1, self.D6     
    
    def setPosition(self, px, py, pz):
        if (px > self.A1 + self.A2 + self.A3 + self.D6 or py > self.A1 + self.A2 + self.A3 + self.D6 or pz > self.A1 + self.A2 + self.A3 + self.D1 + self.D6 ):
            raise ValueError("Invalide position: Position out of range: Target locked")
        self.PX = px 
        self.PY = py 
        self.PZ = pz 
        
    def setRPY(self,t6=0, t5=0, t4=0):
        self.T4 = (t4/180)*math.pi
        self.T5 = (t5/180)*math.pi
        self.T6 = (t6/180)*math.pi

    def getMatrix(self, arr= 0,r= 4,c= 4):
        matrix = []
        a = []
        for i in range(r):
            for j in range(c):
                a.append(arr)
                matrix.append(a)    
        for i in range(r):
            for j in range(c):
                return (matrix[i][j])
            
            
    def setT1(self, t1=0):
        self.T1 = (t1/180)*math.pi
        
    def setT2(self, t2=0):
        self.T2 = (t2/180)*math.pi
        
    def setT3(self, t3=0):
        self.T3 = (t3/180)*math.pi
        
    def setT4(self, t4=0):
        self.T4 = (t4/180)*math.pi
        
    def setT5(self, t5=0):
        self.T5 = (t5/180)*math.pi
        
    def setT6(self, t6=0):
        self.T6 = (t6/180)*math.pi  
        
    def getT1(self):
        return self.T1
    
    def getT2(self):
        return self.T2
    
    def getT3(self):
        return self.T3
    
    def getT4(self):
        return (self.T4)/math.pi * 180
    
    def getT5(self):
        return (self.T5)/math.pi * 180
    
    def getT6(self):
        return (self.T6)/math.pi * 180

    #The homogeneous transformation matrix [H0_3] articulated robot section      
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

    def H3_6stringf(self):
        T4 = self.T4
        T5 = self.T5
        T6 = self.T6
        la = math.cos(T4)*math.cos(T5)*math.cos(T6) - math.sin(T4)*math.sin(T6)
        lai = f"{la:.6f}"
        lb = -math.cos(T4)*math.cos(T5)*math.sin(T6) - math.sin(T4)*math.cos(T6)
        lbi = f"{lb:.6f}"
        lc = math.cos(T4)*math.sin(T5)
        lci = f"{lc:.6f}"
        ld = math.cos(T4)*math.sin(T5)*self.D6
        ldi = f"{ld:.6f}"

        le = math.sin(T4)*math.cos(T5)*math.cos(T6) + math.cos(T4)*math.sin(T6)
        lei = f"{le:.6f}"
        lf = -math.sin(T4)*math.cos(T5)*math.sin(T6) + math.cos(T4)*math.cos(T6)
        lfi = f"{lf:.6f}"
        lg = math.sin(T4)*math.sin(T5)
        lgi = f"{lg:.6f}"
        lh = math.sin(T4)*math.sin(T5)*self.D6
        lhi = f"{lh:.6f}"

        li = -math.sin(T5)*math.cos(T6)
        lii = f"{li:.6f}"
        lj = math.sin(T5)*math.sin(T6)
        lji = f"{lj:.6f}"
        lk = math.cos(T5)
        lki = f"{lk:.6f}"
        ll = math.cos(T5)*self.D6
        lli = f"{ll:.6f}"

        H3_6A =    ([lai,lbi,lci,ldi],
                    [lei,lfi,lgi,lhi],
                    [lii,lji,lki,lli],
                    [0,0,0, 1])
        return H3_6A


    #The homogeneous transformation matrix  row.col entries are given by the formulars below

    #[a,b,c,d]
    #[e,f,g,h]
    #[i,j,k,l]
    #[0,0,0,1]

    #FIRST ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
    def H0_6(self):
        H0_3A = self.H0_3()
        H3_4A = self.H3_6()
        
        A = H0_3A[0][0] * H3_4A[0][0] + H0_3A[0][1] * H3_4A[1][0] + H0_3A[0][2] * H3_4A[2][0] + H0_3A[0][3] * H3_4A[3][0]
        B = H0_3A[0][0] * H3_4A[0][1] + H0_3A[0][1] * H3_4A[1][1] + H0_3A[0][2] * H3_4A[2][1] + H0_3A[0][3] * H3_4A[3][1]
        C = H0_3A[0][0] * H3_4A[0][2] + H0_3A[0][1] * H3_4A[1][2] + H0_3A[0][2] * H3_4A[2][2] + H0_3A[0][3] * H3_4A[3][2]
        D = self.PX
        #SECOND ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        E = H0_3A[1][0] * H3_4A[0][0] + H0_3A[1][1] * H3_4A[1][0] + H0_3A[1][2] * H3_4A[2][0] + H0_3A[1][3] * H3_4A[3][0]
        F = H0_3A[1][0] * H3_4A[0][1] + H0_3A[1][1] * H3_4A[1][1] + H0_3A[1][2] * H3_4A[2][1] + H0_3A[1][3] * H3_4A[3][1]
        G = H0_3A[1][0] * H3_4A[0][2] + H0_3A[1][1] * H3_4A[1][2] + H0_3A[1][2] * H3_4A[2][2] + H0_3A[1][3] * H3_4A[3][2]
        H = self.PY
        #THIRD ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        I = H0_3A[2][0] * H3_4A[0][0] + H0_3A[2][1] * H3_4A[1][0] + H0_3A[2][2] * H3_4A[2][0] + H0_3A[2][3] * H3_4A[3][0]
        J = H0_3A[2][0] * H3_4A[0][1] + H0_3A[2][1] * H3_4A[1][1] + H0_3A[2][2] * H3_4A[2][1] + H0_3A[2][3] * H3_4A[3][1]
        K = H0_3A[2][0] * H3_4A[0][2] + H0_3A[2][1] * H3_4A[1][2] + H0_3A[2][2] * H3_4A[2][2] + H0_3A[2][3] * H3_4A[3][2]
        L = self.PZ
        
        #THE HOMOGENOUS TRANSFORMATION MATRIX FROM FRAME 0 TO FRAME 6
        H0_6 = ([A, B, C, D],
                [E, F, G, H],
                [I, J, K, L],
                [0, 0, 0, 1])
        return H0_6

        


    def getH0_6(self):
        return self.H0_6()
    
    
    def H0_6stringf(self):
        H0_3A = self.H0_3()
        H3_4A = self.H3_6()
       
        #FIRST ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6  
        A = H0_3A[0][0] * H3_4A[0][0] + H0_3A[0][1] * H3_4A[1][0] + H0_3A[0][2] * H3_4A[2][0] + H0_3A[0][3] * H3_4A[3][0]
        Ai = f"{A:.6f}"
        B = H0_3A[0][0] * H3_4A[0][1] + H0_3A[0][1] * H3_4A[1][1] + H0_3A[0][2] * H3_4A[2][1] + H0_3A[0][3] * H3_4A[3][1]
        Bi = f"{B:.6f}"
        C = H0_3A[0][0] * H3_4A[0][2] + H0_3A[0][1] * H3_4A[1][2] + H0_3A[0][2] * H3_4A[2][2] + H0_3A[0][3] * H3_4A[3][2]
        Ci = f"{C:.6f}"
        D = self.PX
        Di = f"{D:.6f}"
        #SECOND ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        E = H0_3A[1][0] * H3_4A[0][0] + H0_3A[1][1] * H3_4A[1][0] + H0_3A[1][2] * H3_4A[2][0] + H0_3A[1][3] * H3_4A[3][0]
        Ei = f"{E:.6f}"
        F = H0_3A[1][0] * H3_4A[0][1] + H0_3A[1][1] * H3_4A[1][1] + H0_3A[1][2] * H3_4A[2][1] + H0_3A[1][3] * H3_4A[3][1]
        Fi = f"{F:.6f}"
        G = H0_3A[1][0] * H3_4A[0][2] + H0_3A[1][1] * H3_4A[1][2] + H0_3A[1][2] * H3_4A[2][2] + H0_3A[1][3] * H3_4A[3][2]
        Gi = f"{G:.6f}"
        H = self.PY
        Hi = f"{H:.6f}"
        #THIRD ROW OF THE HOMOGENEOUS TRANSFORMATION MATRIX H0_6
        I = H0_3A[2][0] * H3_4A[0][0] + H0_3A[2][1] * H3_4A[1][0] + H0_3A[2][2] * H3_4A[2][0] + H0_3A[2][3] * H3_4A[3][0]
        Ii = f"{I:.6f}"
        J = H0_3A[2][0] * H3_4A[0][1] + H0_3A[2][1] * H3_4A[1][1] + H0_3A[2][2] * H3_4A[2][1] + H0_3A[2][3] * H3_4A[3][1]
        Ji = f"{J:.6f}"
        K = H0_3A[2][0] * H3_4A[0][2] + H0_3A[2][1] * H3_4A[1][2] + H0_3A[2][2] * H3_4A[2][2] + H0_3A[2][3] * H3_4A[3][2]
        Ki = f"{K:.6f}"
        L = self.PZ
        Li = f"{L:.6f}"
        #THE HOMOGENOUS TRANSFORMATION MATRIX FROM FRAME 0 TO FRAME 6
        H0_6 = ([Ai, Bi, Ci, Di],
                [Ei, Fi, Gi, Hi],
                [Ii, Ji, Ki, Li],
                [0, 0, 0, 1])
        return H0_6

    
    
    def DX(self):
        D = self.H0_6()
        DX = D[0][3]
        return DX
    
    def DY(self):
        H = self.H0_6()
        DY = H[1][3]
        return DY
    
    def DZ(self):
        L = self.H0_6()
        DZ = L[2][3]
        return DZ
 #---------------------------------   
    def nc(self):
        nc = self.H0_6()[0][2]
        return nc
    
    def ng(self):
        ng = self.H0_6()[1][2]
        return ng
    
    def nk(self):
        nk = self.H0_6()[2][2]
        return nk

    #CALCULATE FOR THE WRIST CENTER
   
    def UX(self):
        UX = self.DX() -(self.nc()*self.D6)
        return UX
    
    def VY(self):
        VY = self.DY() -(self.ng()*self.D6)
        return VY
    
    def WZ(self):
        WZ = self.DZ() -(self.nk()*self.D6)
        return WZ

    #WRIST CENTER VECTOR
    def getWristCenter(self):
        Ux = self.UX()
        Vy = self.VY()
        Wz = self.WZ()
        O0_C = [Ux,Vy,Wz]
        return O0_C
    
    
    #Calculate for Theta_1
    def GET_TH1_DEG(self):
        Ux = self.UX()
        Vy = self.VY()
        #self.calcWristCenter(self.DX,self.DY,self.DZ)
        Th_1 = math.atan2(Vy,Ux) #in radians
        theta1_deg = Th_1 / math.pi * 180
        #th1 = f"{theta1_deg:.6f}"
        return theta1_deg

    def GET_TH1_RAD(self):
        Ux = self.UX()
        Vy = self.VY()
        Th_1 = math.atan2(Vy,Ux) #in radians
        return Th_1

    #Calculation for Theta_2
    # Theta_2 = phy1 + phy2
    #---------------------This robot arm uses an elbow up configuration----------------------------
    def M(self):
        Ux = self.UX()
        Vy = self.VY()
        M = math.sqrt(math.pow(Ux,2) + math.pow(Vy,2))
        return M
        
    def r1(self):
        m = self.M()
        r1 = m - self.A1
        return r1
        
    def r2(self):    
        r2 = self.WZ() - self.D1
        return r2
    
    def r3(self):
        r3 = math.sqrt(math.pow(self.r1(),2) + math.pow(self.r2(),2))
        return r3
    
    def phy1(self):
        phy1 = math.acos((math.pow(self.A3,2) - math.pow(self.A2,2)- math.pow(self.r3(),2))/(-2*self.A2*self.r3()))
        return phy1
    
    def phy2(self):
        phy2 = math.atan2(self.r2(),self.r1())
        return phy2
    
    def phy3(self):
        phy3 = math.acos((math.pow(self.r3(),2)-math.pow(self.A2,2)-math.pow(self.A3,2))/(-2*self.A2*self.A3))
        return phy3
    
    #Theta 2
    def GET_TH2_DEG(self):
        Th_2 = (self.phy2() + self.phy1()) #in radians
        theta2_deg = Th_2 /math.pi * 180
        #th2 = f"{theta2_deg:.6f}"
        return theta2_deg

    def GET_TH2_RAD(self):
        Th_2 = (self.phy2() + self.phy1()) #in radians
        return Th_2  

    #Theta 3
    def GET_TH3_DEG(self):
        Th_3 = - math.pi + self.phy3() #in radians
        theta3_deg = Th_3 /math.pi * 180
        #th3 = f"{theta3_deg:.6f}"
        return theta3_deg

    def GET_TH3_RAD(self):
        Th_3 = - math.pi + self.phy3() #in radians
        return Th_3


    def R0_3(self):

        T1R  = self.T1
        T2R  = self.T2
        T3R  = self.T3

        RA = math.cos(T1R)*math.cos(T2R)*math.cos(T3R) + (-math.cos(T1R)*math.sin(T2R)*math.sin(T3R))
        RB = math.sin(T1R)
        RC = math.cos(T1R)*math.cos(T2R)*math.sin(T3R) + (math.cos(T1R)*math.sin(T2R)*math.cos(T3R))
        RD = math.sin(T1R)*math.cos(T2R)*math.cos(T3R) + (-math.sin(T1R)*math.sin(T2R)*math.sin(T3R))
        RE = -math.cos(T1R)
        RF = math.sin(T1R)*math.cos(T2R)*math.sin(T3R) + math.sin(T1R)*math.sin(T2R)*math.cos(T3R)
        RG = math.sin(T2R)*math.cos(T3R) + math.cos(T2R)*math.sin(T3R)
        RH = 0
        RR = math.sin(T2R)*math.sin(T3R) + (-math.cos(T2R)*math.cos(T3R))
        R0_3A = ([RA, RB, RC],[RD, RE, RF],[RG, RH, RR])
        
        return R0_3A

    #R0_3 MATRIX
    def GET_R0_3(self):
        R0_3A = self.R0_3()
        return R0_3A


    #................DETERMINANT CALCULATION.........................

    def isSquare (self,m):
        return all (len (row) == len (m) for row in m)
        

    def DET_Matrix(self, m):
        if self.isSquare(m):
            DET = (m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])) - (m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])) + (m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]))
        else:
            print('Error non square matrix inputed')
        return DET
          
    def GET_mat_transpose(self, m):
        Mm = m[1][1]*m[2][2] - m[1][2]*m[2][1]
        Nm = m[1][0]*m[2][2] - m[1][2]*m[2][0]
        Om = m[1][0]*m[2][1] - m[1][1]*m[2][0]
        Pm = m[0][1]*m[2][2] - m[0][2]*m[2][1]
        Qm = m[0][0]*m[2][2] - m[0][2]*m[2][0]
        Rm = m[0][0]*m[2][1] - m[0][1]*m[2][0]
        Sm = m[0][1]*m[1][2] - m[0][2]*m[1][1]
        Tm = m[0][0]*m[1][2] - m[0][2]*m[1][0]
        Um = m[0][0]*m[1][1] - m[0][1]*m[1][0]
        
        MAT_transpose = ([Mm,-Pm,Sm], [-Nm,Qm,-Tm], [Om,-Rm,Um])
        return MAT_transpose



    def MAT_inverse(self, m):
        MD = self.DET_Matrix(m)
        MT = self.GET_mat_transpose(m)
        Ad = 1/MD * MT[0][0]
        Bd = 1/MD * MT[0][1]
        Cd = 1/MD * MT[0][2]
        Dd = 1/MD * MT[1][0]
        Ed = 1/MD * MT[1][1]
        Fd = 1/MD * MT[1][2]
        Gd = 1/MD * MT[2][0]
        Hd = 1/MD * MT[2][1]
        Id = 1/MD * MT[2][2]
        
        Inverse = ([Ad,Bd,Cd],
                   [Dd,Ed,Fd],
                   [Gd,Hd,Id])
        return Inverse


    def GET_R0_6_IK(self):
        R0_6_IKA = self.H0_6()
        return R0_6_IKA


    #R3_6 CALCULATION
    def R3_6(self):
        R0_3 = self.GET_R0_3()
        R0_6_IK = self.GET_R0_6_IK()

        R0_3_INV = self.MAT_inverse(R0_3)        
        RA = R0_3_INV[0][0]*R0_6_IK[0][0] + R0_3_INV[0][1]*R0_6_IK[1][0] + R0_3_INV[0][2]*R0_6_IK[2][0]
        RB = R0_3_INV[0][0]*R0_6_IK[0][1] + R0_3_INV[0][1]*R0_6_IK[1][1] + R0_3_INV[0][2]*R0_6_IK[2][1]
        RC = R0_3_INV[0][0]*R0_6_IK[0][2] + R0_3_INV[0][1]*R0_6_IK[1][2] + R0_3_INV[0][2]*R0_6_IK[2][2]

        RD = R0_3_INV[1][0]*R0_6_IK[0][0] + R0_3_INV[1][1]*R0_6_IK[1][0] + R0_3_INV[1][2]*R0_6_IK[2][0]
        RE = R0_3_INV[1][0]*R0_6_IK[0][1] + R0_3_INV[1][1]*R0_6_IK[1][1] + R0_3_INV[1][2]*R0_6_IK[2][1]
        RF = R0_3_INV[1][0]*R0_6_IK[0][2] + R0_3_INV[1][1]*R0_6_IK[1][2] + R0_3_INV[1][2]*R0_6_IK[2][2]

        RG = R0_3_INV[2][0]*R0_6_IK[0][0] + R0_3_INV[2][1]*R0_6_IK[1][0] + R0_3_INV[2][2]*R0_6_IK[2][0]
        RH = R0_3_INV[2][0]*R0_6_IK[0][1] + R0_3_INV[2][1]*R0_6_IK[1][1] + R0_3_INV[2][2]*R0_6_IK[2][1]
        RI = R0_3_INV[2][0]*R0_6_IK[0][2] + R0_3_INV[2][1]*R0_6_IK[1][2] + R0_3_INV[2][2]*R0_6_IK[2][2]
        
        R3_6 = ([RA,RB,RC],  #mathematically   #[11, 12, 13]   #incode   #[00, 01, 02]
                [RD,RE,RF],                    #[21, 22, 23]                #[10, 11, 12]
                [RG,RH,RI])                    #[31, 32, 33]                #[20, 21, 22]
        return R3_6
        
    def GET_R3_6(self):
        R3_6 = self.R3_6()
        return R3_6



    #Theta_4 CALCULATION
    def GET_TH4_DEG(self):
        R3_6 = self.GET_R3_6()
        Th_4 =  math.atan(-R3_6[1][2] / -R3_6[0][2])/math.pi * 180
        #th4 = f"{Th_4:.6f}"
        return Th_4

    def getTh4(self):
        R3_6 = self.GET_R3_6()
        Th_4 =  math.atan(R3_6[1][2] / R3_6[0][2])/math.pi * 180
        th4 = f"{Th_4:.6f}"
        return th4
        
    def GET_TH4_RAD(self):
        R3_6 = self.GET_R3_6()
        Th_4 =  math.atan(-R3_6[1][2] / -R3_6[0][2])
        return Th_4    

    #Theta_5 CALCULATION
    def GET_TH5_DEG(self):
        R3_6 = self.GET_R3_6()
        Th_5 = math.atan2( math.sqrt(math.pow(R3_6[0][2],2) + math.pow(R3_6[1][2],2)), R3_6[2][2])/math.pi * 180
        return Th_5


    def GET_TH5_RAD(self):
        R3_6 = self.GET_R3_6()
        Th_5 = math.atan2( math.sqrt(math.pow(R3_6[0][2],2) + math.pow(R3_6[1][2],2)) , R3_6[2][2])
        return Th_5   

    #Theta_6 CALCULATION
    def GET_TH6_DEG(self):
        R3_6 = self.GET_R3_6()
        Th_6 = math.atan(-R3_6[2][1] / -R3_6[2][0])/math.pi * 180
        #Th_6 = (math.pi - math.atan(R3_6[2][1] / R3_6[2][0]))/math.pi * 180
        #th6 = f"{Th_6:.6f}"
        return Th_6


    def GET_TH6_RAD(self):
        R3_6 = self.GET_R3_6()
        Th_6 = math.atan(-R3_6[2][1] / -R3_6[2][0])
        #Th_6 = math.pi - math.atan2(R3_6[2][1] , R3_6[2][0])
        return Th_6    

#-----------------------------------------THE END----------------------------------------------------------------------
   




