import numpy as np

def laminateThickness(layup):
    return sum([layer['thi'] for layer in layup])

def S2D(m):
    return np.array([[        1/m['E1'], -m['v12']/m['E1'],          0],
                     [-m['v12']/m['E1'],         1/m['E2'],          0],
                     [                0,                 0, 1/m['G12']]], float)

def T2Ds(rot):
    c,s = np.cos(np.radians(rot)), np.sin(np.radians(rot))
    return np.array([[ c*c ,  s*s ,   2*c*s],
                     [ s*s ,  c*c ,  -2*c*s],
                     [-c*s,   c*s , c*c-s*s]], float)

def T2De(rot):
    c,s = np.cos(np.radians(rot)), np.sin(np.radians(rot))
    return np.array([[   c*c,   s*s,     c*s ],
                     [   s*s,   c*c,    -c*s ],
                     [-2*c*s, 2*c*s, c*c-s*s ]], float)

def Q2D(m,rot=0):
    S=S2D(m)
    Q=np.linalg.inv(S)
    if rot==0:
        return Q
    else:
        return np.dot(np.linalg.inv( T2Ds(rot) ) , np.dot(Q,T2De(rot)) )
    
def Q2Drotate(Q,rot):
    return np.dot(np.linalg.inv( T2Ds(rot) ) , np.dot(Q,T2De(rot)) )
        
def computeA(layup):
    A=np.zeros((3,3),float)
    hbot = -laminateThickness(layup)/2         # bottom of first layer
    for layer in layup:                        # loop, all layers
        htop = hbot + layer['thi']             # top of current layer
        Qt = Q2D( layer['mat'], layer['ori'])  # transformed stiffness matrix
        A = A + Qt*(htop-hbot)                 # adding the contribution
        hbot=htop                              # bottom for the next layer
    return A

def computeB(layup):
    B=np.zeros((3,3),float)
    hbot = -laminateThickness(layup)/2         # bottom of first layer
    for layer in layup:                        # loop, all layers
        htop = hbot + layer['thi']             # top of current layer
        Qt = Q2D( layer['mat'], layer['ori'])  # transformed stiffness matrix
        B = B + (Qt*(htop**2-hbot**2))/2       # adding the contribution
        hbot=htop                              # bottom for the next layer
    return B

def computeD(layup):
    D=np.zeros((3,3),float)
    hbot = -laminateThickness(layup)/2         # bottom of first layer
    for layer in layup:                        # loop, all layers
        htop = hbot + layer['thi']             # top of current layer
        Qt = Q2D( layer['mat'], layer['ori'])  # transformed stiffness matrix
        D = D + (Qt*(htop**3-hbot**3))/3       # adding the contribution
        hbot=htop                              # bottom for the next layer
    return D

def laminateStiffnessMatrix(layup):
    ABD=np.zeros((6,6),float)
    hbot = -laminateThickness(layup)/2    
    for layer in layup:
        htop = hbot + layer['thi'] 
        Qt = Q2D( layer['mat'], layer['ori'])
        ABD[0:3,0:3] = ABD[0:3,0:3] +       Qt*(htop   -hbot   )
        ABD[0:3,3:6] = ABD[0:3,3:6] + (1/2)*Qt*(htop**2-hbot**2)
        ABD[3:6,0:3] = ABD[3:6,0:3] + (1/2)*Qt*(htop**2-hbot**2)
        ABD[3:6,3:6] = ABD[3:6,3:6] + (1/3)*Qt*(htop**3-hbot**3)
        hbot=htop   
    return ABD

def solveLaminateLoadCase(ABD,**kwargs):
    # ABD: the laminate stiffness matrix
    # kwargs: prescribed loads or deformations
    loads=np.zeros((6))
    defor=np.zeros((6))
    loadKeys=('Nx','Ny','Nxy','Mx','My','Mxy')   # valid load keys
    defoKeys=('ex','ey','exy','Kx','Ky','Kxy')   # valid deformation keys
    knownKeys=['Nx','Ny','Nxy','Mx','My','Mxy']  # initially assume known loads
    knownVals=np.array([0,0,0,0,0,0],float)      
    for key in kwargs:
        if key in loadKeys:
            i=loadKeys.index(key)
            knownKeys[i]=key
            knownVals[i]=kwargs[key]
        if key in defoKeys:
            i=defoKeys.index(key)
            knownKeys[i]=key
            knownVals[i]=kwargs[key]
    M1=-np.copy(ABD)
    M2= np.copy(ABD)
    ID= np.identity(6)
    for k in range(0,6):
        if knownKeys[k] in loadKeys:
            M2[:,k]=-ID[:,k]
        else:
            M1[:,k]=ID[:,k]
    sol=np.dot(  np.linalg.inv(M1),   np.dot(M2,knownVals))
    for i in range(0,6):
        if knownKeys[i] == loadKeys[i]:
            loads[i]=knownVals[i]
            defor[i]=sol[i]
        if knownKeys[i] == defoKeys[i]:
            defor[i]=knownVals[i]
            loads[i]=sol[i]
    return loads,defor

def thermalLoad(layup,dT):
    NTMT=np.zeros(6,float) #thermal loads
    hbot = -laminateThickness(layup)/2
    for layer in layup:
        htop = hbot + layer['thi'] 
        Qt = Q2D( layer['mat'], layer['ori'])
        a123=[layer['mat']['a1'],  layer['mat']['a2'], 0]
        aXYZ=np.dot( T2De(-layer['ori']) , a123 )
        NTMT[0:3] = NTMT[0:3] +     dT*(  np.dot(Qt,aXYZ)    )*(htop   -hbot   )
        NTMT[3:6] = NTMT[3:6] + 0.5*dT*(  np.dot(Qt,aXYZ)    )*(htop**2-hbot**2)
        hbot=htop   
    return NTMT    
    

from copy import deepcopy

def symmetricLayup(layup):
    for layer in reversed(layup):
        layup.append(deepcopy(layer))

def repeatLayers(layup,count):
    n=len(layup)
    for c in range(0,count):
        for k in range(0,n):
            layup.append(deepcopy(layup[k]))

def fE2DMS(s,m):
    s1,s2,s12=s[0],s[1],s[2]
    XT,YT,XC,YC,S12 = m['XT'], m['YT'], m['XC'], m['YC'], m['S12']
    f=max(s1/XT,-s1/XC,s2/YT,-s2/YC,abs(s12/S12))
    return f

def fE2DME(s,m):
    s1,s2,s12=s[0],s[1],s[2]
    XT,YT,XC,YC,S12 = m['XT'],m['YT'],m['XC'],m['YC'],m['S12']
    E1,E2,v12,G12=m['E1'],m['E2'],m['v12'],m['G12']
    e1=   (1/E1)*s1 + (-v12/E1)*s2
    e2=(-v12/E1)*s1 +    (1/E2)*s2
    e12 = s12/G12
    
    f=max( e1/(XT/E1),-e1/(XC/E1),e2/(YT/E2),-e2/(YC/E2),abs(e12/(S12/G12)) )
    return f

def fE2DTW(s,m):
    s1,s2,s12=s[0],s[1],s[2]
    XT,YT,XC,YC,S12,f12 = m['XT'], m['YT'], m['XC'], m['YC'], m['S12'], m['f12']
    F1,  F2  = (1/XT)-(1/XC) , (1/YT)-(1/YC)
    F11, F22 =  1/(XT*XC) , 1/(YT*YC)
    F66 = 1/(S12**2)
    F12 = f12*(F11*F22)**0.5
    a=F11*s1**2 + F22*s2**2 + 2*F12*s1*s2 + F66*s12**2
    b=F1*s1 + F2*s2
    c=-1
    if a==0:
        return 0.0
    R=(-b+(b**2-4*a*c)**0.5)/(2*a)
    fE=1/R
    return fE

def layerResults(layup,deformations):
    # An empty list that shall be populated with results from all layers:
    results=[]
    # The bottom coordinate of the laminate:
    bot = -laminateThickness(layup)/2
    for layer in layup:
        # the top of current layer is just the bottom + the thickness:
        top=bot+layer['thi']
        # creating a dictionary with the two coordinates:
        h={'bot':bot, 'top':top}
        # computing the strains in laminate coordinate system:
        strnXYZbot=deformations[0:3]+bot*deformations[3:6]
        strnXYZtop=deformations[0:3]+top*deformations[3:6]
        # put the strains into a dictionary:
        strnXYZ={'bot':strnXYZbot, 'top':strnXYZtop}
        # the transformation matrix for strains:
        Te=T2De(layer['ori'])
        # transforming the strains into the material coordinate system:
        strn123bot=np.dot(Te, strnXYZbot)
        strn123top=np.dot(Te, strnXYZtop)
        # the strains at top and bottom as a dictionary:
        strn123={'bot':strn123bot, 'top':strn123top}
        # all strains as a new dictionary:
        strn={'xyz':strnXYZ, '123':strn123}
        # stiffness matrix of the material:
        Q=Q2D(layer['mat'])
        # Hooke's law: finding the stresses in material system:
        strs123bot=np.dot(Q,strn123bot)
        strs123top=np.dot(Q,strn123top)
        # the material stresses as a dictionary having bottom and topp results:
        strs123={'bot':strs123bot, 'top':strs123top}
        # transformation matrix for stress, negativ rotation applies now,
        # since this is from material system to laminat system (reversed..)
        Ts=T2Ds(-layer['ori'])
        # transforming stresses into laminate system:
        strsXYZbot=np.dot(Ts,strs123bot)
        strsXYZtop=np.dot(Ts,strs123top)
        # organizing the stresses for the two location in a dictionary
        strsXYZ={'bot':strsXYZbot, 'top':strsXYZtop}
        # all stresses as a new nested dictionary:
        strs={'xyz':strsXYZ, '123':strs123}
        # Failure criteria...follows the same logic as above
        MSbot=fE2DMS(strs123bot,layer['mat'])
        MStop=fE2DMS(strs123top,layer['mat'])
        MS={'bot':MSbot, 'top':MStop}
        MEbot=fE2DME(strs123bot,layer['mat'])
        MEtop=fE2DME(strs123top,layer['mat'])
        ME={'bot':MEbot, 'top':MEtop}
        TWbot=fE2DTW(strs123bot,layer['mat'])
        TWtop=fE2DTW(strs123top,layer['mat'])
        TW={'bot':TWbot, 'top':TWtop}
        fail={'MS':MS, 'ME':ME, 'TW':TW}
        # and finally put everything into a top level dictionary,
        # and add that to the list
        results.append( {'h':h , 'strain':strn, 'stress':strs, 'fail':fail }  )
        bot=top
    return results


def plotLayerStresses(results):
    h=  []
    sx, sy, sxy = [], [], []
    s1, s2, s12 = [], [], []
    for layer in results:
        h.append(layer['h']['bot'])
        h.append(layer['h']['top'])
        sx.append(layer['stress']['xyz']['bot'][0])
        sx.append(layer['stress']['xyz']['top'][0])
        sy.append(layer['stress']['xyz']['bot'][1])
        sy.append(layer['stress']['xyz']['top'][1])
        sxy.append(layer['stress']['xyz']['bot'][2])
        sxy.append(layer['stress']['xyz']['top'][2])
        s1.append(layer['stress']['123']['bot'][0])
        s1.append(layer['stress']['123']['top'][0])
        s2.append(layer['stress']['123']['bot'][1])
        s2.append(layer['stress']['123']['top'][1])
        s12.append(layer['stress']['123']['bot'][2])
        s12.append(layer['stress']['123']['top'][2])
    import matplotlib.pyplot as plt
    fig,(ax1,ax2) = plt.subplots(ncols=2,nrows=1,figsize=(10,4))
    ax1.grid(True)
    ax1.plot(sx,h,'-', color='red',label='$\sigma_x$')
    ax1.plot(sy,h,'-',color='blue',label='$\sigma_y$')
    ax1.plot(sxy,h,'-',color='green',label=r'$\tau_{xy}$')
    ax1.set_xlabel('Stress',fontsize=12)
    ax1.set_ylabel('z', fontsize=14)
    ax1.legend(loc='best')
    ax2.grid(True)
    ax2.plot(s1,h,'--', color='red',label='$\sigma_1$')
    ax2.plot(s2,h,'--',color='blue',label='$\sigma_2$')
    ax2.plot(s12,h,'--',color='green',label=r'$\tau_{12}$')
    ax2.set_xlabel('Stress',fontsize=12)
    ax2.set_ylabel('z', fontsize=14)
    ax2.legend(loc='best')
    plt.tight_layout()
    plt.show()    
    

def plotLayerFailure(results, title=''):
    h=  []
    ms, me, tw = [], [], []
    for layer in results:
        h.append(layer['h']['bot'])
        h.append(layer['h']['top'])
        ms.append(layer['fail']['MS']['bot'])
        ms.append(layer['fail']['MS']['top'])
        me.append(layer['fail']['ME']['bot'])
        me.append(layer['fail']['ME']['top'])
        tw.append(layer['fail']['TW']['bot'])
        tw.append(layer['fail']['TW']['top'])
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots(ncols=1,nrows=1,figsize=(5,4))
    ax.grid(True)
    ax.plot(ms,h,'-', color='red',label='$f_E (MS)$')
    ax.plot(me,h,'-',color='blue',label='$f_E (ME)$')
    ax.plot(tw,h,'-',color='green',label='$f_E (TW)$')
    ax.set_xlabel('$f_E$',fontsize=12)
    ax.set_ylabel('z', fontsize=14)
    ax.legend(loc='best')
    plt.tight_layout()
    plt.title(title)
    plt.show()    