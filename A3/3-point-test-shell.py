from abaqus import *
from abaqusConstants import *
import regionToolset

mcore={'name':'H100','rho':100E-12,
       'E1':100, 'E2':100, 'E3':100,
       'v12':0.3, 'v13':0.3, 'v23':0.3,
       'G12': 38.5, 'G13': 38.5, 'G23': 38.5 }

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

def matlib(modelname):
    mod = mdb.models[modelname]
    
    # Definerer Carbon/Epoxy(a)
    mat = mod.Material('Carbon/Epoxy(a)')
    mat.Density(table=((1600E-12, ), ))
    mat.Elastic(type=ENGINEERING_CONSTANTS, 
                table=((mcfrp['E1'], mcfrp['E2'], mcfrp['E3'], 
                        mcfrp['v12'], mcfrp['v13'], mcfrp['v23'], 
                        mcfrp['G12'], mcfrp['G13'], mcfrp['G23']), ))

    
    # Definerer H100 som core, med egenskaper fra mcore
    m = mod.Material('H100')
    m.Density(table=((mcore['rho'], ), ))
    m.Elastic(type=ENGINEERING_CONSTANTS, 
              table=((mcore['E1'], mcore['E2'], mcore['E3'], 
                      mcore['v12'], mcore['v13'], mcore['v23'], 
                      mcore['G12'], mcore['G13'], mcore['G23']), ))

lam1 = [{'mat':'Carbon/Epoxy(a)', 'ori':   0, 'thi': 1.0},
        {'mat':'H100', 'ori':  0, 'thi': 4.0},
        {'mat':'H100', 'ori':  0, 'thi': 4.0},
        {'mat':'Carbon/Epoxy(a)', 'ori':   0, 'thi': 1.0}]

def flex3pShell(modelname, L, b, dL, laminate, esize, U3, nonlin, dts):
    
    t = sum([layer['thi'] for layer in laminate])

    # new model:
    mod = mdb.Model(name=modelname)

    # materials and sections:
    matlib(modelname)
    for matname in mod.materials.keys():
        mod.HomogeneousSolidSection(name=matname, material=matname, thickness=None)
     
    # planar shell:   
    ske = mod.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    ske.rectangle(point1=(0.0, 0.0), point2=(L+2*dL, b))
    prt = mod.Part(name='Specimen', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    prt.BaseShell(sketch=ske)
    del mod.sketches['__profile__']
    session.viewports['Viewport: 1'].setValues(displayedObject=prt)

    # Partitions:
    id=prt.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=b/2.0).id
    prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)    
    for xpos in [dL, dL+L/2.0, dL+L]:
        id=prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=xpos).id
        prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)

    # layup:
    id = prt.DatumCsysByDefault(coordSysType=CARTESIAN).id
    layupOrientation = prt.datums[id]
    region = regionToolset.Region(faces=prt.faces)
    compositeLayup = prt.CompositeLayup(name='Layup1', elementType=SHELL, offsetType=MIDDLE_SURFACE)
    compositeLayup.Section()
    compositeLayup.ReferenceOrientation(orientationType=SYSTEM, localCsys=layupOrientation, axis=AXIS_3)
    count = 1
    for layer in laminate:
        compositeLayup.CompositePly(suppressed=False, plyName='Ply-'+str(count), region=region, 
            material=layer['mat'], thicknessType=SPECIFY_THICKNESS, thickness=layer['thi'], 
            orientationType=SPECIFY_ORIENT, orientationValue=layer['ori'] )
        count = count + 1

    # Mesh:
    prt.seedPart(size=esize, deviationFactor=0.1, minSizeFactor=0.1)
    prt.generateMesh()

    # Assembly:
    ass = mod.rootAssembly
    ass.DatumCsysByDefault(CARTESIAN)
    ins = ass.Instance(name='Specimen', part=prt, dependent=ON)
    ass.translate(instanceList=('Specimen', ), vector=(-L/2.0-dL, -b/2.0, 0.0))

    # Boundary conditions:
    edges = ins.edges.findAt(((-L/2.0, -b/4.0, 0.0), ), ((-L/2.0, b/4.0, 0.0), ), 
        ((L/2.0, -b/4.0, 0.0), ), ((L/2.0, b/4.0, 0.0), ))
    region = ass.Set(edges=edges, name='EDGES-SUPPORT')
    mod.DisplacementBC(name='BC-SUPPORT', createStepName='Initial', region=region, u3=SET)
    edges = ins.edges.findAt(((0.0, -b/4.0, 0.0), ), ((0.0, b/4.0, 0.0), ))
    region = ass.Set(edges=edges, name='EDGES-LOADING')
    mod.DisplacementBC(name='BC-LOADING', createStepName='Initial', region=region, u3=SET )
    
    verts = ins.vertices.findAt(((0.0, -b/2.0, 0.0), ), ((0.0, b/2, 0.0), ))
    region = ass.Set(vertices=verts, name='VERTICES-RB1')
    mod.DisplacementBC(name='BC-RB1', createStepName='Initial', region=region, u1=SET)
    verts = ins.vertices.findAt(((0.0, 0.0, 0.0), ))
    region = ass.Set(vertices=verts, name='VERTICES-RB2')
    mod.DisplacementBC(name='BC-RB2', createStepName='Initial', region=region, u2=SET)
    
    # Step and loading
    if nonlin:
        mod.StaticStep(name='Step-1', previous='Initial', initialInc=dts, maxInc=dts, nlgeom=ON)
    else:
        mod.StaticStep(name='Step-1', previous='Initial')
    mod.boundaryConditions['BC-LOADING'].setValuesInStep(stepName='Step-1', u3=-U3)

    '''
    # Job and results
    job=mdb.Job(name=modelname, model=modelname)
    job.submit(consistencyChecking=OFF)
    job.waitForCompletion()
    odb = session.openOdb(name=modelname+'.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].makeCurrent()

    # displacement and sum of reaction force
    uz = []
    fz = []
    region = odb.rootAssembly.nodeSets['EDGES-LOADING']
    for frame in odb.steps['Step-1'].frames:
        rfs = frame.fieldOutputs['RF'].getSubset(region = region).values
        us = frame.fieldOutputs['U'].getSubset(region = region).values
        rfsum = sum([rf.data[2] for rf in rfs])
        u = us[0].data[2]
        uz.append(-u)         # reversed sign
        fz.append(-rfsum)     # reversed sign

    print 'uz=', uz
    print 'fz=', fz
    '''

flex3pShell(modelname="3-point-test-shell", L=200, b=30, dL=10, laminate=lam1, esize=2, U3=10, nonlin=True, dts=0.1)