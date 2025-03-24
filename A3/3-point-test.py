from abaqus import *
from abaqusConstants import *
from part import EdgeArray


mcore={'name':'H100','rho':100E-12,
       'E1':100, 'E2':100, 'E3':100,
       'v12':0.3, 'v13':0.3, 'v23':0.3, 
       'G12': 38.5, 'G13': 38.5, 'G23': 38.5 }

# mcfrp={'name':'Woven Carbon/epoxy','rho':1580E-12, 
#        'E1': 59000, 'E2': 59000, 'E3': 9200,
#        'v12': 0.045, 'v13' :0.462, 'v23': 0.462, 
#        'G12': 2750, 'G13': 2700, 'G23': 2700 }

mcfrp = {
    "name": "Carbon/Epoxy(a)", 
    "units": "MPa-mm-Mg", "type": "UD", "fiber": "Carbon",
    "Vf": 0.55, 
    "rho": 1600, # kg/m^3
    "description": "Typical low modulus carbon/Epoxy from TMM4175",  
    "E1": 130000, 
    "E2": 10000, 
    "E3": 10000, 
    "v12": 0.28, "v13": 0.28, "v23": 0.5, 
    "G12": 4500, "G13": 4500, "G23": 3500, 
    "a1": -0.5e-06, "a2": 3.0e-05, "a3": 3.0e-05, 
    "XT": 1800, "YT": 40, "ZT": 40,
    "XC": 1200, "YC": 180, "ZC": 180,
    "S12": 70, "S13": 70, "S23": 40,
    "f12":-0.5, "f13":-0.5, "f23":-0.5
}

def sb3p(modelname, L, dL, b, hc, ts1, ts2, ezL, ezT, ezs1, ezs2, ezc, U3, mcore, mcfrp):
    '''
    L:     support length
    dL:    added length at both ends
    b:     width
    hc:    thickness of core
    ts1:   thickness of bottom skin
    ts2:   thickness of top skin
    ezL:   element size in the longitudinal direction
    ezT:   element size in the transverse direction
    ezs1:  element size through the thickness of bottom skin
    ezs2:  element size through the thickness of top skin
    ezc:   element size through the thickness of the core
    U3:    imposed displacement (deflection)
    '''

    mod = mdb.Model(name=modelname, modelType=STANDARD_EXPLICIT)
    
    # Solid beam:
    ske = mod.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    ske.rectangle(point1=(-L/2.0-dL, -b/2.0), point2=(L/2.0+dL, b/2.0))
    prt = mod.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    prt.BaseSolidExtrude(sketch=ske, depth=hc+ts1+ts2)
    del mod.sketches['__profile__']
    
    # Partitions:
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=0.0).id
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[id], cells=prt.cells)
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=-L/2.0).id
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[id], cells=prt.cells)
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=L/2.0).id
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[id], cells=prt.cells)
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0).id
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[id], cells=prt.cells)
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=ts1).id
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[id], cells=prt.cells)
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=ts1+hc).id
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[id], cells=prt.cells)

    # Sets, cells:
    c = prt.cells.getByBoundingBox(zMax=ts1)
    prt.Set(name='CELLS-BOT', cells=c)
    c = prt.cells.getByBoundingBox(zMin=ts1, zMax=ts1+hc)
    prt.Set(name='CELLS-CORE', cells=c) 
    c = prt.cells.getByBoundingBox(zMin=ts1+hc)
    prt.Set(name='CELLS-TOP', cells=c)  

    # Sets, edges
    edgesLongitudinal = []
    edgesTransverse = []
    edgesThickness = []
    for e in prt.edges:
        vs = e.getVertices()
        x1 = prt.vertices[vs[0]].pointOn[0][0]
        x2 = prt.vertices[vs[1]].pointOn[0][0]
        y1 = prt.vertices[vs[0]].pointOn[0][1]
        y2 = prt.vertices[vs[1]].pointOn[0][1]
        z1 = prt.vertices[vs[0]].pointOn[0][2]
        z2 = prt.vertices[vs[1]].pointOn[0][2]
        if y1==y2 and z1==z2:
            edgesLongitudinal.append(e)
        if x1==x2 and z1==z2:
            edgesTransverse.append(e)
        if x1==x2 and y1==y2:
            edgesThickness.append(e)
    prt.Set(name='EDGES-LONG', edges=EdgeArray(edgesLongitudinal))
    prt.Set(name='EDGES-TRAN', edges=EdgeArray(edgesTransverse))
    prt.Set(name='EDGES-THIC', edges=EdgeArray(edgesThickness))
    edgesThickS1 = prt.sets['EDGES-THIC'].edges.getByBoundingBox(zMax=ts1)
    prt.Set(name='EDGES-THIC-S1', edges=edgesThickS1)    
    edgesThickCo = prt.sets['EDGES-THIC'].edges.getByBoundingBox(zMin=ts1,zMax=ts1+hc)
    prt.Set(name='EDGES-THIC-CORE', edges=edgesThickCo)
    edgesThickS2 = prt.sets['EDGES-THIC'].edges.getByBoundingBox(zMin=ts1+hc)
    prt.Set(name='EDGES-THIC-S2', edges=edgesThickS2) 
    edgesSupport1 = prt.sets['EDGES-TRAN'].edges.getByBoundingBox(xMin=-L/2.0, xMax=-L/2.0, zMax=0.0)
    prt.Set(name='EDGES-SUPPORT-1', edges=edgesSupport1)     
    edgesSupport2 = prt.sets['EDGES-TRAN'].edges.getByBoundingBox(xMin=L/2.0, xMax=L/2.0, zMax=0.0)
    prt.Set(name='EDGES-SUPPORT-2', edges=edgesSupport2)
    edgesLoading = prt.sets['EDGES-TRAN'].edges.getByBoundingBox(xMin=0.0, xMax=0.0, zMin=ts1+hc+ts2)
    prt.Set(name='EDGES-LOADING', edges=edgesLoading)
    vertsRBX = prt.vertices.findAt(((0.0, -b/2, 0.0), ), ((0.0, b/2, 0.0), ))
    prt.Set(name='VERTICES-RBX', vertices=vertsRBX)
    vertsRBY = prt.vertices.findAt(((0.0, 0.0, 0.0),))
    prt.Set(name='VERTICES-RBY', vertices=vertsRBY)

    # Materials
    mat1 = mod.Material(name='FiberComposite')
    mat1.Elastic(type=ENGINEERING_CONSTANTS, 
        table=((mcfrp['E1'], mcfrp['E2'], mcfrp['E3'], mcfrp['v12'], mcfrp['v13'], mcfrp['v23'], mcfrp['G12'], mcfrp['G13'], mcfrp['G23']), ))
    
    mat2 = mod.Material(name='Foam')
    mat2 = mod.Material(name='Foam')
    mat2.Elastic(type=ENGINEERING_CONSTANTS, 
        table=((mcore['E1'], mcore['E2'], mcore['E3'], mcore['v12'], mcore['v13'], mcore['v23'], mcore['G12'], mcore['G13'], mcore['G23']), ))


    mod.HomogeneousSolidSection(name='Section-Skin', material='FiberComposite', thickness=None)
    mod.HomogeneousSolidSection(name='Section-Foam', material='Foam', thickness=None)
    prt.SectionAssignment(region=prt.sets['CELLS-BOT'], sectionName='Section-Skin', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
    prt.SectionAssignment(region=prt.sets['CELLS-TOP'], sectionName='Section-Skin', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
    prt.SectionAssignment(region=prt.sets['CELLS-CORE'], sectionName='Section-Foam', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
    
    # Set material orientation
    orientation=None
  
    prt.MaterialOrientation(region=prt.sets['CELLS-BOT'], 
        orientationType=SYSTEM, axis=AXIS_1, localCsys=orientation, 
        fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, 
        additionalRotationField='', stackDirection=STACK_3)
    
    prt.MaterialOrientation(region=prt.sets['CELLS-TOP'], 
        orientationType=SYSTEM, axis=AXIS_1, localCsys=orientation, 
        fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, 
        additionalRotationField='', stackDirection=STACK_3)
    
    prt.MaterialOrientation(region=prt.sets['CELLS-CORE'], 
        orientationType=SYSTEM, axis=AXIS_1, localCsys=orientation, 
        fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, 
        additionalRotationField='', stackDirection=STACK_3)

    # Mesh
    prt.seedEdgeBySize(edges=prt.sets['EDGES-LONG'].edges, 
        size=ezL, deviationFactor=0.1, constraint=FINER)
    prt.seedEdgeBySize(edges=prt.sets['EDGES-TRAN'].edges, 
        size=ezT, deviationFactor=0.1, constraint=FINER)
    prt.seedEdgeBySize(edges=prt.sets['EDGES-THIC-S1'].edges, 
        size=ezs1, deviationFactor=0.1, constraint=FINER)        
    prt.seedEdgeBySize(edges=prt.sets['EDGES-THIC-S2'].edges, 
        size=ezs2, deviationFactor=0.1, constraint=FINER)   
    prt.seedEdgeBySize(edges=prt.sets['EDGES-THIC-CORE'].edges, 
        size=ezc, deviationFactor=0.1, constraint=FINER) 
    prt.generateMesh()

    # Assembly, steps, BC and loading
    ass = mod.rootAssembly
    ins = ass.Instance(name='Beam', part=prt, dependent=ON)
 
    edges = ins.sets['EDGES-SUPPORT-1']  
    mod.DisplacementBC(name='BC-SUPPORT-1', createStepName='Initial', region=edges, u3=SET)
    edges = ins.sets['EDGES-SUPPORT-2'] 
    mod.DisplacementBC(name='BC-SUPPORT-2', createStepName='Initial', region=edges, u3=SET)
    edges = ins.sets['EDGES-LOADING']
    mod.DisplacementBC(name='BC-LOADING', createStepName='Initial', region=edges, u3=SET)
    verts = ins.sets['VERTICES-RBX']
    mod.DisplacementBC(name='BC-RBX', createStepName='Initial', region=verts, u1=SET)
    verts = ins.sets['VERTICES-RBY']
    mod.DisplacementBC(name='BC-RBY', createStepName='Initial', region=verts, u2=SET)    

    mod.StaticStep(name='Step-1', previous='Initial')
    mod.boundaryConditions['BC-LOADING'].setValuesInStep(stepName='Step-1', u3=-U3)

    job = mdb.Job(name=modelname, model=modelname)
    job.submit(consistencyChecking=OFF)    

sb3p(modelname='SW1', L=200, dL=10, b=30, hc=8, ts1=1, ts2=1,
     ezL=2, ezT=2, ezs1=0.2, ezs2=0.2, ezc=2, U3=10, mcore=mcore, mcfrp=mcfrp)