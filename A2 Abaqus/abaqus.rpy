# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Fri Mar  7 09:08:08 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=354.666687011719, 
    height=221.244445800781)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
mdb.Model(name='Pipe', modelType=STANDARD_EXPLICIT)
#: The model "Pipe" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Pipe'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.ConstructionLine(point1=(-25.0, 0.0), point2=(30.0, 0.0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.rectangle(point1=(0.0, 15.0), point2=(10.0, 20.0))
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s.DistanceDimension(entity1=g[7], entity2=g[3], textPoint=(-14.7357177734375, 
    6.7618408203125), value=7.65466)
s.undo()
s.FixedConstraint(entity=g[3])
s.DistanceDimension(entity1=g[7], entity2=g[3], textPoint=(-15.8241500854492, 
    6.67678833007812), value=7.65466)
s.DistanceDimension(entity1=g[5], entity2=g[3], textPoint=(-31.0622253417969, 
    4.89064407348633), value=12.5)
session.viewports['Viewport: 1'].view.setValues(nearPlane=177.74, 
    farPlane=199.384, width=125.914, height=61.852, cameraPosition=(1.54958, 
    0.670848, 188.562), cameraTarget=(1.54958, 0.670848, 0))
s.DistanceDimension(entity1=g[6], entity2=g[4], textPoint=(0.365898132324219, 
    20.6243209838867), value=2.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=179.537, 
    farPlane=197.587, width=118.843, height=58.3787, cameraPosition=(5.9958, 
    3.62438, 188.562), cameraTarget=(5.9958, 3.62438, 0))
s.sketchOptions.setValues(constructionGeometry=ON)
s.assignCenterline(line=g[3])
p = mdb.models['Pipe'].Part(name='pipe', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Pipe'].parts['pipe']
p.BaseSolidRevolve(sketch=s, angle=180.0, flipRevolveDirection=OFF)
s.unsetPrimaryObject()
p = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Pipe'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(width=47.7566, height=23.4592, 
    viewOffsetX=0.493279, viewOffsetY=0.088079)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.8053, 
    farPlane=72.9951, width=44.5524, height=21.8852, cameraPosition=(34.0086, 
    33.8622, 39.6652), cameraTarget=(0.572723, 0.426329, 6.22937), 
    viewOffsetX=0.460182, viewOffsetY=0.0821692)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.7845, 
    farPlane=73.0157, width=44.5308, height=21.8746, viewOffsetX=2.02979, 
    viewOffsetY=0.533975)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.2254, 
    farPlane=69.2775, width=52.2754, height=25.679, cameraPosition=(56.8609, 
    18.913, -3.45964), cameraUpVector=(-0.637571, 0.676525, -0.368533), 
    cameraTarget=(2.49317, 1.76048, 6.7294), viewOffsetX=2.3828, 
    viewOffsetY=0.626842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.7045, 
    farPlane=71.4938, width=52.7742, height=25.924, cameraPosition=(37.6138, 
    1.90661, -42.6433), cameraUpVector=(-0.227603, 0.930057, 0.288429), 
    cameraTarget=(3.87996, -0.17688, 4.38394), viewOffsetX=2.40553, 
    viewOffsetY=0.632822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.8109, 
    farPlane=73.9988, width=52.8851, height=25.9784, cameraPosition=(-13.3795, 
    5.8155, -54.2312), cameraUpVector=(-0.255957, 0.835652, 0.485975), 
    cameraTarget=(1.68424, 1.12491, 1.49088), viewOffsetX=2.41058, 
    viewOffsetY=0.63415)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.2643, 
    farPlane=75.2982, width=50.2346, height=24.6764, cameraPosition=(27.2013, 
    16.1528, -47.3617), cameraUpVector=(-0.32418, 0.817707, 0.47567), 
    cameraTarget=(4.49715, 1.04071, 3.72658), viewOffsetX=2.28976, 
    viewOffsetY=0.602367)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4874, 
    farPlane=73.2127, width=52.5485, height=25.8131, cameraPosition=(16.9393, 
    4.26031, -53.3962), cameraUpVector=(-0.0585899, 0.914325, 0.400721), 
    cameraTarget=(3.90636, -0.117575, 2.86078), viewOffsetX=2.39523, 
    viewOffsetY=0.630113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.784, 
    farPlane=73.5883, width=52.8573, height=25.9648, cameraPosition=(-13.1869, 
    -3.54828, -54.2383), cameraUpVector=(-0.203246, 0.919022, 0.337772), 
    cameraTarget=(2.05883, 0.344286, 1.49573), viewOffsetX=2.4093, 
    viewOffsetY=0.633815)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.6607, 
    farPlane=73.2364, width=52.729, height=25.9017, cameraPosition=(10.9085, 
    3.29715, -54.8543), cameraUpVector=(-0.113895, 0.920914, 0.372754), 
    cameraTarget=(3.75431, 0.147736, 2.52828), viewOffsetX=2.40345, 
    viewOffsetY=0.632276)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.5638, 
    farPlane=75.5324, width=51.5873, height=25.3409, cameraPosition=(-34.8593, 
    15.215, -42.7471), cameraUpVector=(0.539725, 0.791294, 0.287317), 
    cameraTarget=(-0.294548, 0.0825481, 1.18637), viewOffsetX=2.35141, 
    viewOffsetY=0.618586)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.7332, 
    farPlane=75.6645, width=50.7228, height=24.9163, cameraPosition=(-16.4056, 
    -17.2949, -50.9598), cameraUpVector=(0.317838, 0.948096, -0.00964317), 
    cameraTarget=(1.73661, -2.47731, 2.00394), viewOffsetX=2.31201, 
    viewOffsetY=0.60822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=52.0214, 
    farPlane=71.6173, width=54.1453, height=26.5975, cameraPosition=(59.136, 
    20.4309, 0.302468), cameraUpVector=(-0.592239, 0.457756, -0.663108), 
    cameraTarget=(4.39493, 3.27632, 8.23956), viewOffsetX=2.46801, 
    viewOffsetY=0.649258)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.4446, 
    farPlane=74.3018, width=51.4633, height=25.28, cameraPosition=(47.1679, 
    17.7005, 43.5728), cameraUpVector=(-0.460568, 0.804673, -0.374671), 
    cameraTarget=(2.33496, 0.866646, 11.0076), viewOffsetX=2.34576, 
    viewOffsetY=0.617098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=53.8245, 
    farPlane=69.6619, width=56.022, height=27.5194, cameraPosition=(60.4238, 
    2.91218, -10.5233), cameraUpVector=(-0.383064, 0.922206, 0.0529033), 
    cameraTarget=(5.57564, 0.00874978, 7.83744), viewOffsetX=2.55355, 
    viewOffsetY=0.671762)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.8441, 
    farPlane=73.5974, width=51.8792, height=25.4843, cameraPosition=(19.3225, 
    -4.85168, -52.566), cameraUpVector=(-0.290166, 0.9382, 0.188636), 
    cameraTarget=(4.86412, 0.0196791, 3.30071), viewOffsetX=2.36471, 
    viewOffsetY=0.622084)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.143, 
    farPlane=72.3699, width=53.2311, height=26.1484, cameraPosition=(-18.7953, 
    -0.962094, -52.3154), cameraUpVector=(0.0759742, 0.945419, 0.316878), 
    cameraTarget=(2.35172, -0.311871, 1.59422), viewOffsetX=2.42633, 
    viewOffsetY=0.638295)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4436, 
    farPlane=73.1166, width=52.5032, height=25.7908, cameraPosition=(-11.2566, 
    3.29397, -54.286), cameraUpVector=(0.0186511, 0.919419, 0.392836), 
    cameraTarget=(2.93727, 0.0526707, 1.76662), viewOffsetX=2.39315, 
    viewOffsetY=0.629566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.7972, 
    farPlane=72.7587, width=52.8712, height=25.9716, cameraPosition=(-22.5537, 
    2.20093, -50.8941), cameraUpVector=(0.221248, 0.92411, 0.311559), 
    cameraTarget=(1.94146, -0.44416, 1.51642), viewOffsetX=2.40993, 
    viewOffsetY=0.633979)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4819, 
    farPlane=73.0824, width=52.543, height=25.8104, cameraPosition=(-16.573, 
    3.30145, -52.9619), cameraUpVector=(0.120907, 0.921205, 0.369814), 
    cameraTarget=(2.48424, -0.1546, 1.61602), viewOffsetX=2.39497, 
    viewOffsetY=0.630043)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.5301, 
    farPlane=73.046, width=52.5932, height=25.835, cameraPosition=(-24.1439, 
    4.13187, -50.1168), cameraUpVector=(0.162987, 0.915954, 0.366692), 
    cameraTarget=(1.86866, -0.0674029, 1.45439), viewOffsetX=2.39726, 
    viewOffsetY=0.630644)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.9378, 
    farPlane=76.3231, width=48.8542, height=23.9984, cameraPosition=(-0.479786, 
    -22.6349, -51.1323), cameraUpVector=(-0.0824774, 0.996267, -0.0254946), 
    cameraTarget=(3.71298, -1.53543, 2.63667), viewOffsetX=2.22683, 
    viewOffsetY=0.58581)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.6891, 
    farPlane=76.5341, width=48.5954, height=23.8712, cameraPosition=(-8.30086, 
    -25.9242, -48.9426), cameraUpVector=(0.0192707, 0.995648, -0.0911819), 
    cameraTarget=(3.16233, -2.04141, 2.5557), viewOffsetX=2.21503, 
    viewOffsetY=0.582706)
p = mdb.models['Pipe'].parts['pipe']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[0], 
    sketchPlaneSide=SIDE1, origin=(1.0, -10.07733, 0.0))
s1 = mdb.models['Pipe'].ConstrainedSketch(name='__profile__', sheetSize=25.31, 
    gridSpacing=0.63, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Pipe'].parts['pipe']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=9.58998, 
    farPlane=23.8776, width=11.7693, height=5.78137, cameraPosition=(1.11921, 
    -9.97638, -10.4838), cameraTarget=(1.11921, -9.97638, 1.23412e-15))
s1.Line(point1=(-1.0, 0.0), point2=(1.0, 0.0))
s1.HorizontalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[11], addUndoState=False)
s1.CoincidentConstraint(entity1=v[8], entity2=g[4], addUndoState=False)
s1.EqualDistanceConstraint(entity1=v[2], entity2=v[3], midpoint=v[8], 
    addUndoState=False)
s1.CoincidentConstraint(entity1=v[9], entity2=g[2], addUndoState=False)
s1.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[9], 
    addUndoState=False)
s1.DistanceDimension(entity1=g[11], entity2=g[5], textPoint=(-2.53945779800415, 
    2.14866197784424), value=2.42267)
s1.undo()
p = mdb.models['Pipe'].parts['pipe']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[0], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Pipe'].sketches['__profile__']
p = mdb.models['Pipe'].parts['pipe']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
pickedEdges =(e[0], )
p.PartitionCellBySweepEdge(sweepPath=e[7], cells=pickedCells, 
    edges=pickedEdges)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3221, 
    farPlane=74.8383, width=50.295, height=24.7061, cameraPosition=(-41.0275, 
    -25.1468, -31.1949), cameraUpVector=(0.180072, 0.943967, -0.276586), 
    cameraTarget=(0.427814, -2.74111, 2.4697), viewOffsetX=2.2925, 
    viewOffsetY=0.603086)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.0277, 
    farPlane=72.2943, width=53.111, height=26.0894, cameraPosition=(-43.6936, 
    -8.8872, -35.4013), cameraUpVector=(0.187295, 0.977747, 0.0945103), 
    cameraTarget=(0.148207, -1.12173, 1.63183), viewOffsetX=2.42086, 
    viewOffsetY=0.636853)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Pipe'].Material(name='Carbon/Epoxy(a)')
mdb.models['Pipe'].materials['Carbon/Epoxy(a)'].Elastic(
    type=ENGINEERING_CONSTANTS, table=((130000.0, 10000.0, 10000.0, 0.28, 0.28, 
    0.5, 4500.0, 4500.0, 3500.0), ))
mdb.models['Pipe'].HomogeneousSolidSection(name='Section-1', 
    material='Carbon/Epoxy(a)', thickness=None)
mdb.models['Pipe'].HomogeneousSolidSection(name='Section-2', 
    material='Carbon/Epoxy(a)', thickness=None)
p = mdb.models['Pipe'].parts['pipe']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Pipe'].parts['pipe']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Pipe'].parts['pipe']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-2')
p = mdb.models['Pipe'].parts['pipe']
p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4598, 
    farPlane=72.8621, width=23.4956, height=25.3522, viewOffsetX=2.67441, 
    viewOffsetY=-0.197716)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.5413, 
    farPlane=76.6952, width=21.671, height=23.3835, cameraPosition=(-35.7099, 
    26.7089, 48.0504), cameraUpVector=(0.285053, 0.67295, -0.682557), 
    cameraTarget=(-3.8627, 0.603256, 7.33047), viewOffsetX=2.46672, 
    viewOffsetY=-0.182362)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.3872, 
    farPlane=73.1678, width=23.4618, height=25.3158, cameraPosition=(-48.3776, 
    13.6259, 40.9085), cameraUpVector=(0.58051, 0.808586, -0.0959002), 
    cameraTarget=(-3.67228, 1.29042, 6.22227), viewOffsetX=2.67056, 
    viewOffsetY=-0.197431)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.6483, 
    farPlane=71.4979, width=52.826, height=25.9494, cameraPosition=(-56.2825, 
    14.3194, -11.4741), cameraUpVector=(0.5145, 0.83556, 0.192687), 
    cameraTarget=(-1.75212, 0.639903, 2.42482), viewOffsetX=2.7374, 
    viewOffsetY=-0.202373)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.9695, 
    farPlane=72.1224, width=52.1318, height=25.6084, cameraPosition=(-52.9369, 
    13.548, -20.2903), cameraUpVector=(0.482727, 0.843014, 0.237281), 
    cameraTarget=(-1.12539, 0.491242, 2.04706), viewOffsetX=2.70142, 
    viewOffsetY=-0.199713)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.9289, 
    farPlane=72.1629, width=21.9052, height=23.6682, viewOffsetX=1.35771, 
    viewOffsetY=1.21948)
p = mdb.models['Pipe'].parts['pipe']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#2 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Pipe'].parts['pipe']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#40 ]', ), )
normalAxisRegion = p.Surface(side1Faces=side1Faces, name='Surf-1')
p = mdb.models['Pipe'].parts['pipe']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#4000 ]', ), )
primaryAxisRegion = p.Set(edges=edges, name='Set-3')
mdb.models['Pipe'].parts['pipe'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_1, normalAxisDefinition=SURFACE, 
    normalAxisRegion=normalAxisRegion, flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=EDGE, 
    primaryAxisRegion=primaryAxisRegion, primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)
#: Specified material orientation has been assigned to the selected regions.
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.8116, 
    farPlane=72.5086, width=20.9945, height=22.6842, cameraPosition=(-49.355, 
    17.5963, 35.2399), cameraUpVector=(0.589823, 0.791359, -0.160812), 
    cameraTarget=(-2.47281, 1.0155, 5.55807), viewOffsetX=1.30127, 
    viewOffsetY=1.16878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.3036, 
    farPlane=78.6045, width=42.8601, height=21.0539, cameraPosition=(-22.6478, 
    41.238, -33.5511), cameraUpVector=(0.275997, 0.453009, 0.847708), 
    cameraTarget=(1.13159, 2.40445, 2.23112), viewOffsetX=1.20775, 
    viewOffsetY=1.08478)
p = mdb.models['Pipe'].parts['pipe']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models['Pipe'].parts['pipe']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#40 ]', ), )
normalAxisRegion = p.Surface(side1Faces=side1Faces, name='Surf-2')
p = mdb.models['Pipe'].parts['pipe']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#20000 ]', ), )
primaryAxisRegion = p.Set(edges=edges, name='Set-5')
mdb.models['Pipe'].parts['pipe'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_1, normalAxisDefinition=SURFACE, 
    normalAxisRegion=normalAxisRegion, flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=EDGE, 
    primaryAxisRegion=primaryAxisRegion, primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)
#: Specified material orientation has been assigned to the selected regions.
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.4739, 
    farPlane=78.954, width=42.0751, height=45.4, cameraPosition=(-38.296, 
    26.2748, -33.4941), cameraUpVector=(0.249669, 0.645624, 0.721689), 
    cameraTarget=(0.0398228, 1.50403, 2.15198), viewOffsetX=1.18563, 
    viewOffsetY=1.06491)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0205, 
    farPlane=74.8383, width=45.4304, height=49.0204, cameraPosition=(-42.4914, 
    -3.2606, -37.0702), cameraUpVector=(0.0486227, 0.925097, 0.376605), 
    cameraTarget=(-0.0441297, -0.626955, 2.23826), viewOffsetX=1.28018, 
    viewOffsetY=1.14983)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4794, 
    farPlane=74.1758, width=45.8646, height=49.4889, cameraPosition=(-53.9899, 
    -5.36471, -20.4491), cameraUpVector=(0.25545, 0.963588, 0.0790203), 
    cameraTarget=(-1.28495, -1.24242, 3.19537), viewOffsetX=1.29241, 
    viewOffsetY=1.16082)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.2112, 
    farPlane=73.4441, width=38.6694, height=41.7252, viewOffsetX=1.16652, 
    viewOffsetY=1.34241)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Pipe'].parts['pipe']
p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Pipe'].parts['pipe']
p.generateMesh()
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Meshability']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Section']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Meshability']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.69697, 
    farPlane=5.30303, width=4.28084, height=2.10285, viewOffsetX=0.113209, 
    viewOffsetY=-0.12684)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.67454, 
    farPlane=5.32546, width=4.25487, height=2.09502, viewOffsetX=0.10339, 
    viewOffsetY=-0.122622)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Part']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Meshability']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.65208, 
    farPlane=5.34792, width=4.51719, height=2.22418, viewOffsetX=0.215032, 
    viewOffsetY=-0.202181)
p = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.5516, 
    farPlane=72.1037, width=72.3021, height=35.6002, viewOffsetX=2.24291, 
    viewOffsetY=1.69256)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    interactions=ON, constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Pipe'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Pipe'].parts['pipe']
a.Instance(name='pipe-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.8969, 
    farPlane=68.5365, width=45.8823, height=22.5385, cameraPosition=(37.4265, 
    8.24158, -37.7585), cameraUpVector=(-0.687151, 0.726469, -0.00813864), 
    cameraTarget=(0.572723, 0.447905, 6.22937))
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.5529, 
    farPlane=72.7393, width=41.6323, height=20.4508, cameraPosition=(0.261965, 
    -26.6036, -44.8882), cameraUpVector=(0.130783, 0.980793, -0.144713), 
    cameraTarget=(0.698902, 0.566211, 6.25358))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.4471, 
    farPlane=71.1774, width=43.4855, height=21.3612, cameraPosition=(-35.2868, 
    -22.8264, -32.5417), cameraUpVector=(0.0769205, 0.983016, -0.16662), 
    cameraTarget=(0.863264, 0.548747, 6.1965))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.5711, 
    farPlane=71.442, width=43.6068, height=47.0527, cameraPosition=(-25.6054, 
    0.0458696, -45.2979), cameraUpVector=(0.166927, 0.945225, 0.280511), 
    cameraTarget=(0.846459, 0.509046, 6.21864))
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.9364, 
    farPlane=73.1519, width=42.0075, height=45.327, cameraPosition=(-22.6503, 
    5.0859, -46.5154), cameraUpVector=(0.167857, 0.91357, 0.370424), 
    cameraTarget=(0.851245, 0.517209, 6.21667))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.2452, 
    farPlane=70.9483, width=44.2663, height=47.7643, cameraPosition=(-47.1924, 
    3.00541, -26.0603), cameraUpVector=(0.343986, 0.9256, 0.157921), 
    cameraTarget=(0.795636, 0.512495, 6.26302))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.5211, 
    farPlane=69.6723, width=33.4033, height=36.0429, viewOffsetX=-0.350819, 
    viewOffsetY=0.470917)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.9587, 
    farPlane=74.5986, width=30.8455, height=33.2829, cameraPosition=(33.0682, 
    19.6434, -38.9269), cameraUpVector=(-0.363064, 0.78041, 0.509062), 
    cameraTarget=(1.09136, 0.569232, 5.42984), viewOffsetX=-0.323955, 
    viewOffsetY=0.434856)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.5949, 
    farPlane=68.9624, width=3.12405, height=3.37092, viewOffsetX=2.96427, 
    viewOffsetY=-1.70716)
a = mdb.models['Pipe'].rootAssembly
e11 = a.instances['pipe-1'].edges
a.ReferencePoint(point=a.instances['pipe-1'].InterestingPoint(edge=e11[3], 
    rule=CENTER))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.1429, 
    farPlane=69.4144, width=6.11298, height=6.59604, viewOffsetX=2.30941, 
    viewOffsetY=-1.1411)
a = mdb.models['Pipe'].rootAssembly
e21 = a.instances['pipe-1'].edges
a.ReferencePoint(point=a.instances['pipe-1'].InterestingPoint(edge=e21[1], 
    rule=CENTER))
a = mdb.models['Pipe'].rootAssembly
r1 = a.referencePoints
a.ReferencePoint(point=r1[4])
a = mdb.models['Pipe'].rootAssembly
r11 = a.referencePoints
a.ReferencePoint(point=r11[6])
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.8505, 
    farPlane=69.7068, width=7.78208, height=8.39704, viewOffsetX=2.14645, 
    viewOffsetY=-0.976766)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.0398, 
    farPlane=80.7115, width=58.6978, height=67.2436, cameraPosition=(48.2975, 
    14.1325, -29.5092), cameraUpVector=(-0.431498, 0.833049, 0.346177), 
    cameraTarget=(5.27946, 0.0165999, 6.60251), viewOffsetX=1.82089, 
    viewOffsetY=1.37409)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.8062, 
    farPlane=70.9451, width=10.6733, height=12.2272, viewOffsetX=6.41312, 
    viewOffsetY=-0.30637)
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.6003, 
    farPlane=72.6646, width=10.8401, height=12.4183, cameraPosition=(37.8532, 
    12.9539, -42.1782), cameraUpVector=(-0.351777, 0.845572, 0.401574), 
    cameraTarget=(6.06334, 0.360399, 4.56235), viewOffsetX=6.51336, 
    viewOffsetY=-0.311159)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Pipe'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
a.Set(referencePoints=refPoints1, name='set-rp')
#: The set 'set-rp' has been created (1 reference point).
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.2693, 
    farPlane=71.288, width=15.8113, height=18.1133, viewOffsetX=0.87612, 
    viewOffsetY=0.406809)
a = mdb.models['Pipe'].rootAssembly
f1 = a.instances['pipe-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#88 ]', ), )
a.Set(faces=faces1, name='set-x=L')
#: The set 'set-x=L' has been created (2 faces).
mdb.models['Pipe'].Equation(name='Constraint-1', terms=((1.0, 'set-x=L', 1), (
    -1.0, 'set-rp', 1)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.0524, 
    farPlane=72.5049, width=22.3165, height=25.5656, viewOffsetX=-0.628366, 
    viewOffsetY=2.13075)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Pipe'].rootAssembly
f1 = a.instances['pipe-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#612 ]', ), )
region = a.Set(faces=faces1, name='Set-3')
mdb.models['Pipe'].DisplacementBC(name='BC-1', createStepName='Initial', 
    region=region, u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.2789, 
    farPlane=71.0404, width=23.9147, height=27.3965, cameraPosition=(54.6361, 
    25.2542, -0.443703), cameraUpVector=(-0.665191, 0.700089, 0.259609), 
    cameraTarget=(2.44683, 0.934194, 5.77566), viewOffsetX=-0.673368, 
    viewOffsetY=2.28335)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.0214, 
    farPlane=74.7886, width=23.2919, height=26.6829, cameraPosition=(27.4678, 
    15.9701, 58.7277), cameraUpVector=(-0.536742, 0.766868, -0.351881), 
    cameraTarget=(2.53825, 0.748516, 8.72088), viewOffsetX=-0.655829, 
    viewOffsetY=2.22388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.2871, 
    farPlane=70.8142, width=24.4142, height=27.9687, cameraPosition=(40.3014, 
    2.94411, 51.56), cameraUpVector=(-0.475427, 0.875001, -0.091339), 
    cameraTarget=(2.70523, -0.00947988, 7.60932), viewOffsetX=-0.68743, 
    viewOffsetY=2.33104)
session.viewports['Viewport: 1'].view.setValues(nearPlane=50.4885, 
    farPlane=68.2714, width=25.0094, height=28.6505, cameraPosition=(59.0234, 
    11.014, 0.0423326), cameraUpVector=(-0.480705, 0.8442, 0.237169), 
    cameraTarget=(2.3913, 0.137364, 5.36742), viewOffsetX=-0.704187, 
    viewOffsetY=2.38786)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.1823, 
    farPlane=73.3054, width=22.381, height=25.6395, cameraPosition=(25.4365, 
    15.0029, -45.6036), cameraUpVector=(-0.19459, 0.823522, 0.532866), 
    cameraTarget=(0.638446, 0.119233, 4.5699), viewOffsetX=-0.63018, 
    viewOffsetY=2.1369)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.0613, 
    farPlane=71.8648, width=23.3118, height=26.7058, cameraPosition=(-35.1808, 
    10.6293, -39.7446), cameraUpVector=(0.247428, 0.862008, 0.442405), 
    cameraTarget=(-0.942214, -0.130674, 5.70636), viewOffsetX=-0.656388, 
    viewOffsetY=2.22577)
a = mdb.models['Pipe'].rootAssembly
f1 = a.instances['pipe-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#24 ]', ), )
region = a.Set(faces=faces1, name='Set-4')
mdb.models['Pipe'].DisplacementBC(name='BC-2', createStepName='Initial', 
    region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.saveAs(
    pathName='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A2 Abaqus/Ror_25mm')
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A2 Abaqus\Ror_25mm.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.0034, 
    farPlane=71.1524, width=23.2832, height=26.673, cameraPosition=(33.0348, 
    7.77213, -42.7852), cameraUpVector=(-0.166548, 0.882873, 0.439086), 
    cameraTarget=(0.907767, -0.0677034, 4.75675), viewOffsetX=-0.655581, 
    viewOffsetY=2.22303)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.7329, 
    farPlane=70.423, width=18.4605, height=21.1481, viewOffsetX=-1.10655, 
    viewOffsetY=-2.33544)
a = mdb.models['Pipe'].rootAssembly
e1 = a.instances['pipe-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2000 ]', ), )
region = a.Set(edges=edges1, name='Set-5')
mdb.models['Pipe'].DisplacementBC(name='BC-3', createStepName='Initial', 
    region=region, u1=UNSET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Pipe'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.9739, 
    farPlane=71.1819, width=24.7539, height=28.3578, viewOffsetX=-0.223752, 
    viewOffsetY=-2.43464)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.8296, 
    farPlane=72.8239, width=24.1508, height=27.667, cameraPosition=(0.528434, 
    11.5683, -51.9372), cameraUpVector=(0.240184, 0.827082, 0.50818), 
    cameraTarget=(0.927856, -0.0643778, 4.79347), viewOffsetX=-0.218302, 
    viewOffsetY=-2.37533)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.2748, 
    farPlane=70.8466, width=24.9125, height=28.5395, cameraPosition=(38.6336, 
    7.03342, -38.731), cameraUpVector=(-0.234394, 0.891578, 0.387489), 
    cameraTarget=(1.07792, -0.0954981, 4.77305), viewOffsetX=-0.225186, 
    viewOffsetY=-2.45023)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.2399, 
    farPlane=70.629, width=24.3672, height=27.9148, cameraPosition=(2.57624, 
    -5.14079, 64.4505), cameraUpVector=(-0.35672, 0.901731, -0.244198), 
    cameraTarget=(-0.183392, -0.438176, 6.79525), viewOffsetX=-0.220257, 
    viewOffsetY=-2.39659)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.9457, 
    farPlane=72.3517, width=24.2122, height=27.7372, cameraPosition=(34.7207, 
    -13.2506, -40.5058), cameraUpVector=(0.190107, 0.935852, 0.296714), 
    cameraTarget=(1.93937, -0.555607, 5.51676), viewOffsetX=-0.218856, 
    viewOffsetY=-2.38134)
a = mdb.models['Pipe'].rootAssembly
s1 = a.instances['pipe-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
mdb.models['Pipe'].Pressure(name='Load-1', createStepName='Step-1', 
    region=region, distributionType=UNIFORM, field='', magnitude=100.0, 
    amplitude=UNSET)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.7916, 
    farPlane=71.3175, width=24.6579, height=28.2479, cameraPosition=(45.8974, 
    -13.1865, -29.7756), cameraUpVector=(0.0322007, 0.971168, 0.23621), 
    cameraTarget=(1.91522, -0.477184, 5.69115), viewOffsetX=-0.222885, 
    viewOffsetY=-2.42518)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.7175, 
    farPlane=70.3915, width=18.4546, height=21.1415, viewOffsetX=0.279884, 
    viewOffsetY=-2.4851)
a = mdb.models['Pipe'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
region = a.Set(referencePoints=refPoints1, name='Set-6')
mdb.models['Pipe'].ConcentratedForce(name='Load-2', createStepName='Step-1', 
    region=region, cf1=-24543.6926061703, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.6842, 
    farPlane=70.4247, width=20.8712, height=24.7616, viewOffsetX=0.0442383, 
    viewOffsetY=-2.07591)
mdb.Job(name='Job-1', model='Pipe', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A2 Abaqus/Job-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A2 Abaqus/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       9
#: Number of Node Sets:          11
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.863, 
    farPlane=69.1617, width=44.4248, height=22.3882, cameraPosition=(41.6336, 
    -15.9177, -33.0682), cameraUpVector=(-0.282476, 0.942277, -0.17978), 
    cameraTarget=(0.704656, -0.469653, 4.85801))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.2994, 
    farPlane=70.7166, width=43.8906, height=22.119, cameraPosition=(-9.90477, 
    -16.0403, -49.9416), cameraUpVector=(0.727207, 0.686188, 0.0177778), 
    cameraTarget=(0.603332, -0.469896, 4.82484))
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.9779, 
    farPlane=70.1749, width=45.4819, height=22.9209, cameraPosition=(-39.4273, 
    15.2524, -34.2193), cameraUpVector=(0.437394, 0.819264, 0.370802), 
    cameraTarget=(0.295703, -0.143821, 4.98867))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A2 Abaqus\Ror_25mm.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0247, 
    farPlane=70.0498, width=45.5263, height=22.9433, cameraPosition=(3.14864, 
    8.26865, -52.6063), cameraUpVector=(0.24304, 0.847241, 0.472351), 
    cameraTarget=(1.1447, -0.283083, 4.62202))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0121, 
    farPlane=70.0624, width=45.5144, height=22.9373)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.4281, 
    farPlane=68.4726, width=46.8568, height=23.6138, cameraPosition=(-44.0605, 
    7.27028, -31.479), cameraUpVector=(0.381854, 0.889797, 0.249899), 
    cameraTarget=(0.234046, -0.302341, 5.02956))
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.0353, 
    farPlane=66.8653, width=27.7218, height=13.9706, viewOffsetX=-1.88492, 
    viewOffsetY=2.89205)
session.Path(name='Path-1', type=EDGE_LIST, expression=(('PIPE-1', ((245, 2, 4, 
    1), (184, 2, 4, 1), (123, 2, 4, 1), (62, 2, 4, 1), (1, 2, 4, 1), (1281, 2, 
    2, 1), (1342, 2, 2, 1), (1403, 2, 2, 1), (1464, 2, 2, 1), (1525, 2, 2, 1), 
    )), ))
pth = session.paths['Path-1']
session.XYDataFromPath(name='S11', path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S13'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S23'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
pth = session.paths['Path-1']
session.XYDataFromPath(name='S22', path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'))
pth = session.paths['Path-1']
session.XYDataFromPath(name='S33', path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['S11']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['S22']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['S11']
c1 = session.Curve(xyData=xy1)
xy2 = session.xyDataObjects['S22']
c2 = session.Curve(xyData=xy2)
xy3 = session.xyDataObjects['S33']
c3 = session.Curve(xyData=xy3)
chart.setValues(curvesToPlot=(c1, c2, c3, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['S11']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['S11']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xQuantity = visualization.QuantityType(type=PATH)
yQuantity = visualization.QuantityType(type=STRESS)
session.xyDataObjects['S11'].setValues(axis1QuantityType=xQuantity, 
    axis2QuantityType=yQuantity, )
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A2 Abaqus\Ror_25mm.cae".
