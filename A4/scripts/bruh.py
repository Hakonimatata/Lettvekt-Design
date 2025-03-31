from abaqus import *
from abaqusConstants import *

def iprofile(modelname, L, bb, bt, h, tf, tw, offs, esize, F):

    mod = mdb.Model(name=modelname, modelType=STANDARD_EXPLICIT)
    
    # Part
    ske = mod.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    ske.Line(point1=(-bb/2.0, -h/2.0), point2=(bb/2.0, -h/2.0))
    ske.Line(point2=(-bt/2.0,  h/2.0), point1=(bt/2.0,  h/2.0))
    ske.Line(point1=(0.0, -h/2.0), point2=(0.0, h/2.0))
    prt = mod.Part(name='IProfile', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    prt.BaseShellExtrude(sketch=ske, depth=L)
    del mod.sketches['__profile__']
    
    # Partition
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0).id
    prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)

    # Material and section 
    mat = mod.Material(name='Alu')
    mat.Elastic(table=((70000.0, 0.33), ))
    mod.HomogeneousShellSection(name='Sec-fla', 
        preIntegrate=OFF, material='Alu', thicknessType=UNIFORM, thickness=tf, 
        thicknessField='', nodalThicknessField='', 
        idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
        thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
        integrationRule=SIMPSON, numIntPts=5)
    mod.HomogeneousShellSection(name='Sec-web', 
        preIntegrate=OFF, material='Alu', thicknessType=UNIFORM, thickness=tw, 
        thicknessField='', nodalThicknessField='', 
        idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
        thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
        integrationRule=SIMPSON, numIntPts=5)
    
    # Sets
    setall = prt.Set(faces=prt.faces, name='faces-all')
    setbot = prt.Set(faces=prt.faces.getByBoundingBox(yMax=-h/2.0), name='faces-bottm-flange')
    settop = prt.Set(faces=prt.faces.getByBoundingBox(yMin= h/2.0), name='faces-top-flange')
    setfla = prt.SetByBoolean(sets=(setbot,settop), name='faces-flanges')
    setweb = prt.SetByBoolean(sets=(setall, setfla), operation=DIFFERENCE, name='faces-web')

    # Section assignments
    prt.SectionAssignment(region=setfla, sectionName='Sec-fla', offset=0.0, 
        offsetType=offs, offsetField='', thicknessAssignment=FROM_SECTION)
    prt.SectionAssignment(region=setweb, sectionName='Sec-web', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
   
    # Mesh
    prt.setMeshControls(regions=prt.faces, elemShape=QUAD, technique=STRUCTURED)
    prt.seedPart(size=esize, deviationFactor=0.1, minSizeFactor=0.1)
    prt.generateMesh()

    # Assembly and constraints 
    ass = mod.rootAssembly
    ass.DatumCsysByDefault(CARTESIAN)
    ins = ass.Instance(name='IProfile', part=prt, dependent=ON)
    ass.rotate(instanceList=('IProfile', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 1.0, 0.0), angle=90.0)
    ass.rotate(instanceList=('IProfile', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)

    # Set of center node at end 2
    v = ins.vertices.findAt(((L, 0.0, 0.0), ))
    ass.Set(vertices=v, name='MONITORPOINT')    

    # Fix one end
    edges=ins.edges.getByBoundingBox(xMax=0.0)
    region = ass.Set(edges=edges, name = 'EDGES1')   
    bc1 = mod.DisplacementBC(name='FIXEDEND', createStepName='Initial', 
        region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)    

    # Step and loading
    mod.StaticStep(name='Step-Stat', previous='Initial') 
    v = ins.vertices.findAt(((L, 0.0, -h/2.0), ))
    region = ass.Set(vertices=v, name='POINLOAD')
    mod.ConcentratedForce(name='PointForce', createStepName='Step-Stat', 
        region=region, cf3=F, distributionType=UNIFORM, field='', localCsys=None)

    # Job
    job = mdb.Job(name=modelname, model=modelname)
    job.submit(consistencyChecking=OFF)
    job.waitForCompletion()
    
    # Result
    odb = session.openOdb(name=modelname+'.odb')
    region = odb.rootAssembly.nodeSets['MONITORPOINT']
    uz = odb.steps['Step-Stat'].frames[-1].fieldOutputs['U'].getSubset(region=region).values[0].data[2]
    print 'Model: {}, uz = {}'.format(modelname, uz)