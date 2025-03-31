from abaqus import *
from abaqusConstants import *

def boxpro(modelname, L, b, h, t, n_spars, esize, disp):

    # length from edge to point load
    load_pos = (2.0 / 3.0) * L

    
    mod = mdb.Model(name=modelname, modelType=STANDARD_EXPLICIT)
    
    # Part
    # Correct h and b (due to offsetType = MIDDLE_SURFACE)
    b -= t
    h -= t

    ske = mod.ConstrainedSketch(name='__profile__', sheetSize=200.0)
    ske.rectangle(point1=(-b/2.0, -h/2.0), point2=(b/2.0, h/2.0))

    # create spars
    if n_spars > 0:
        spacing = b / (n_spars + 1)
        x_pos = -b/2.0 + spacing
        for _ in range(n_spars):
            ske.Line(point1=(x_pos, h/2.0), point2=(x_pos, -h/2.0))
            x_pos += spacing

    prt = mod.Part(name='Box', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    prt.BaseShellExtrude(sketch=ske, depth=L)
    del mod.sketches['__profile__']
    
    # Partition
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=load_pos).id
    prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)


    wheel_width = 0.2 * b + 0.1 # added small value
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=(wheel_width/2.0)).id
    prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)
    id = prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=(-wheel_width/2.0)).id
    prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)


    # Material and section 
    mat = mod.Material(name='Alu')
    mat.Elastic(table=((70000.0, 0.33), ))
    mod.HomogeneousShellSection(name='Section-shell', 
        preIntegrate=OFF, material='Alu', thicknessType=UNIFORM, thickness=t, 
        thicknessField='', nodalThicknessField='', 
        idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
        thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
        integrationRule=SIMPSON, numIntPts=5)
    region = prt.Set(faces=prt.faces, name='faces-all')
    prt.SectionAssignment(region=region, sectionName='Section-shell', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
   
    # Mesh
    prt.setMeshControls(regions=prt.faces, elemShape=QUAD, technique=STRUCTURED)
    prt.seedPart(size=esize, deviationFactor=0.1, minSizeFactor=0.1)
    prt.generateMesh()


    # Assembly and constraints 
    ass = mod.rootAssembly
    ass.DatumCsysByDefault(CARTESIAN)
    ins = ass.Instance(name='Box', part=prt, dependent=ON)
    ass.rotate(instanceList=('Box', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 1.0, 0.0), angle=90.0)
    ass.rotate(instanceList=('Box', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
    rf1id = ass.ReferencePoint(point=(0.0, 0.0, 0.0)).id
    rf2id = ass.ReferencePoint(point=(L, 0.0, 0.0)).id
    regionRF1=ass.Set(referencePoints=(ass.referencePoints[rf1id],), name='RF1')
    regionRF2=ass.Set(referencePoints=(ass.referencePoints[rf2id],), name='RF2')
    edges1=ins.edges.getByBoundingBox(xMax=0.0)
    region1 = ass.Set(edges=edges1, name = 'EDGES1')   
    edges2=ins.edges.getByBoundingBox(xMin=L)
    region2 = ass.Set(edges=edges2, name = 'EDGES2')   
    mod.MultipointConstraint(name='Constraint-1', 
        controlPoint=regionRF1, surface=region1, mpcType=BEAM_MPC, 
        userMode=DOF_MODE_MPC, userType=0, csys=None)
    mod.MultipointConstraint(name='Constraint-2', 
        controlPoint=regionRF2, surface=region2, mpcType=BEAM_MPC, 
        userMode=DOF_MODE_MPC, userType=0, csys=None)

    # Steps, BC and loading
    bc1 = mod.DisplacementBC(name='BC1', createStepName='Initial', 
        region=regionRF1, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)
    bc2 = mod.DisplacementBC(name='BC2', createStepName='Initial', 
        region=regionRF2, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET)

    mod.BuckleStep(name='Step-Buck', previous='Initial', numEigen=2, vectors=4, maxIterations=500)
    mod.StaticStep(name='Step-Stat', previous='Step-Buck') 

    
    bc1.setValuesInStep(stepName='Step-Buck', 
        ur2=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
    bc1.setValuesInStep(stepName='Step-Stat', 
        ur2=FREED)
    bc2.setValuesInStep(stepName='Step-Buck', 
        u1=FREED, u3=FREED, buckleCase=PERTURBATION_AND_BUCKLING)
    bc2.setValuesInStep(stepName='Step-Stat', 
        u1=FREED, u3=FREED)
    

    edges = ins.edges.getByBoundingBox(xMin=load_pos, xMax=load_pos, zMin=h/2.0, yMax=(wheel_width/2.0), yMin=(-wheel_width/2.0)) # added yMax=(wheel_width/2.0), yMin=(-wheel_width/2.0)
    region3 = ass.Set(name='CONTACT-POINT', edges=edges)

    bc3 = mod.DisplacementBC(name='BC3', createStepName='Initial', region=region3, 
        u1=UNSET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
    bc3.setValuesInStep(stepName='Step-Buck', u3=-disp, buckleCase=PERTURBATION_AND_BUCKLING)
    bc3.setValuesInStep(stepName='Step-Stat', u3=-disp)  

    # Job:
    # job = mdb.Job(name=modelname, model=modelname)
    # job.submit()
    
boxpro(modelname='BP-1', L=1800, b=200, h=75, t=0.5, n_spars=4, esize=20, disp=1)