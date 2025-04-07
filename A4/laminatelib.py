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