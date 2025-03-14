# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Tue Mar 11 17:27:03 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=209.19792175293, 
    height=229.125915527344)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Ror_25mm.cae')
#: The model database "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A2 Abaqus\Ror_25mm.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
odb = session.mdbData['Pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#: Warning: Boundary conditions are shown in the local co-ordinate system, in which they were defined.
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.7839, 
    farPlane=67.5581, width=45.2978, height=22.8281, cameraPosition=(53.7776, 
    22.6772, 11.4028), cameraUpVector=(-0.561344, 0.607164, -0.562356), 
    cameraTarget=(0.561258, 0.464658, 6.22201))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.1497, 
    farPlane=69.1693, width=43.7487, height=22.0474, cameraPosition=(47.9035, 
    18.6968, -21.5993), cameraUpVector=(-0.791684, 0.52954, -0.30467), 
    cameraTarget=(0.584411, 0.480347, 6.35209))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.4554, 
    farPlane=68.8082, width=44.0385, height=22.1935, cameraPosition=(31.1296, 
    8.75344, -42.0984), cameraUpVector=(-0.654369, 0.747601, 0.113552), 
    cameraTarget=(0.653884, 0.521529, 6.43699))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.mdbData['Pipe'])
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.654, 
    farPlane=67.0752, width=47.0706, height=23.7215, cameraPosition=(55.6804, 
    18.5446, 10.2982), cameraUpVector=(-0.549526, 0.700752, -0.454938), 
    cameraTarget=(0.968139, 0.176773, 5.67145))
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.2996, 
    farPlane=69.4315, width=44.8387, height=22.5968, cameraPosition=(26.9876, 
    9.41658, -45.5338), cameraUpVector=(-0.0980815, 0.866999, 0.488562), 
    cameraTarget=(0.738904, 0.103847, 5.22539))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3136, 
    farPlane=68.4186, width=45.8001, height=23.0812, cameraPosition=(8.56152, 
    3.29568, -52.0825), cameraUpVector=(-0.0825545, 0.922207, 0.377783), 
    cameraTarget=(0.591394, 0.0548459, 5.17296))
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0092, 
    farPlane=68.723, width=51.507, height=25.9573, viewOffsetX=0.632437, 
    viewOffsetY=-0.183505)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.1939, 
    farPlane=68.7705, width=52.7779, height=26.5978, cameraPosition=(-24.9412, 
    0.351862, -47.3607), cameraUpVector=(0.111161, 0.940147, 0.322129), 
    cameraTarget=(0.254818, 0.0399736, 4.76677), viewOffsetX=0.648043, 
    viewOffsetY=-0.188033)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    interactions=ON, constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.0554, 
    farPlane=72.7699, width=43.0544, height=20.9593, viewOffsetX=-0.0109773, 
    viewOffsetY=0.0790772)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.5512, 
    farPlane=72.9375, width=43.5502, height=21.2007, cameraPosition=(-5.62976, 
    25.5963, -45.6495), cameraUpVector=(-0.686866, 0.361526, 0.630488), 
    cameraTarget=(0.591037, 0.466964, 6.15483), viewOffsetX=-0.0111037, 
    viewOffsetY=0.0799878)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.9748, 
    farPlane=69.9266, width=45.9737, height=22.3805, cameraPosition=(17.9006, 
    10.3371, -48.2112), cameraUpVector=(-0.981021, 0.177543, 0.0779492), 
    cameraTarget=(0.749571, 0.407303, 6.20488), viewOffsetX=-0.0117216, 
    viewOffsetY=0.084439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.1106, 
    farPlane=67.0436, width=48.1095, height=23.4202, cameraPosition=(52.2649, 
    -8.59751, -18.5133), cameraUpVector=(-0.471086, 0.74592, -0.470831), 
    cameraTarget=(0.688953, 0.347348, 6.26125), viewOffsetX=-0.0122661, 
    viewOffsetY=0.0883618)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.4513, 
    farPlane=69.0913, width=46.4502, height=22.6125, cameraPosition=(29.8291, 
    6.64568, -43.3717), cameraUpVector=(-0.385429, 0.880236, 0.27682), 
    cameraTarget=(0.818492, 0.240124, 6.33963), viewOffsetX=-0.011843, 
    viewOffsetY=0.0853142)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.2701, 
    farPlane=67.1525, width=48.2691, height=23.4979, cameraPosition=(40.2229, 
    1.12876, -36.0698), cameraUpVector=(-0.26669, 0.936775, 0.226561), 
    cameraTarget=(0.774416, 0.2532, 6.3202), viewOffsetX=-0.0123067, 
    viewOffsetY=0.0886547)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3461, 
    farPlane=67.0638, width=48.3451, height=23.5349, cameraPosition=(41.4805, 
    0.632115, -34.8702), cameraUpVector=(-0.260632, 0.940111, 0.219686), 
    cameraTarget=(0.768827, 0.255035, 6.31569), viewOffsetX=-0.0123261, 
    viewOffsetY=0.0887943)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3096, 
    farPlane=67.1003, width=51.3921, height=25.0182, viewOffsetX=1.09667, 
    viewOffsetY=-0.243816)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.3506, 
    farPlane=67.0594, width=51.4357, height=25.0394, viewOffsetX=1.0976, 
    viewOffsetY=-0.247803)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.6199, 
    farPlane=68.2805, width=50.6584, height=24.661, cameraPosition=(33.986, 
    -0.997849, -41.3866), cameraUpVector=(-0.216148, 0.948818, 0.23027), 
    cameraTarget=(0.94065, 0.281733, 6.15531), viewOffsetX=1.08102, 
    viewOffsetY=-0.244058)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.7296, 
    farPlane=68.8344, width=49.7113, height=24.2, cameraPosition=(38.8279, 
    6.67782, -36.9156), cameraUpVector=(-0.278986, 0.899559, 0.336097), 
    cameraTarget=(0.842728, 0.204068, 6.31728), viewOffsetX=1.06081, 
    viewOffsetY=-0.239495)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.0775, 
    farPlane=69.1459, width=49.0176, height=23.8623, cameraPosition=(43.0829, 
    11.5291, -31.3703), cameraUpVector=(-0.370624, 0.859089, 0.352994), 
    cameraTarget=(0.701803, 0.183302, 6.43159), viewOffsetX=1.04601, 
    viewOffsetY=-0.236153)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.3265, 
    farPlane=68.6996, width=49.2825, height=23.9912, cameraPosition=(45.6416, 
    11.542, -28.1264), cameraUpVector=(-0.397068, 0.859042, 0.323085), 
    cameraTarget=(0.610541, 0.186596, 6.47312), viewOffsetX=1.05166, 
    viewOffsetY=-0.237429)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.5304, 
    farPlane=68.3553, width=49.4994, height=24.0968, cameraPosition=(47.3706, 
    11.22, -25.7445), cameraUpVector=(-0.411692, 0.862056, 0.295583), 
    cameraTarget=(0.540808, 0.194975, 6.49352), viewOffsetX=1.05629, 
    viewOffsetY=-0.238474)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.8324, 
    farPlane=69.0306, width=48.7569, height=23.7354, cameraPosition=(46.9564, 
    14.7877, -24.8598), cameraUpVector=(-0.469598, 0.828279, 0.305665), 
    cameraTarget=(0.510544, 0.188132, 6.50109), viewOffsetX=1.04045, 
    viewOffsetY=-0.234897)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p1 = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
