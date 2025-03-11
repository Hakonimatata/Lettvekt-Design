# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Tue Mar 11 09:20:26 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=155.194442749023, 
    height=167.039581298828)
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
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.4532, 
    farPlane=75.222, width=33.8131, height=19.3259, cameraPosition=(34.2558, 
    33.8923, 39.2775), cameraTarget=(0.828182, 0.464657, 5.84984))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.5519, 
    farPlane=71.2077, width=38.9107, height=22.2395, cameraPosition=(51.1261, 
    29.5469, 3.77108), cameraUpVector=(-0.720597, 0.55294, -0.418325), 
    cameraTarget=(1.12756, 0.387543, 5.21974))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.9169, 
    farPlane=71.8757, width=38.38, height=21.9362, cameraPosition=(42.9038, 
    13.3054, -33.0983), cameraUpVector=(-0.784654, 0.601518, -0.149982), 
    cameraTarget=(0.990507, 0.116821, 4.60518))
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.5388, 
    farPlane=74.3473, width=36.3923, height=20.8001, cameraPosition=(-9.8851, 
    -21.2866, -48.7566), cameraUpVector=(0.562704, 0.824068, -0.0653889), 
    cameraTarget=(0.096055, -0.469306, 4.33987))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.6965, 
    farPlane=74.3913, width=38.1958, height=21.8309, cameraPosition=(-38.4217, 
    22.4293, -33.0357), cameraUpVector=(0.505645, 0.742933, 0.438605), 
    cameraTarget=(-0.409719, 0.305503, 4.6185))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.3333, 
    farPlane=74.4485, width=37.8922, height=21.6574, cameraPosition=(-38.6735, 
    21.5964, -33.0357), cameraTarget=(-0.661493, -0.5274, 4.6185))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.5617, 
    farPlane=73.6492, width=37.2473, height=21.2888, cameraPosition=(-38.6735, 
    19.5409, -33.0357), cameraTarget=(-0.661493, -2.58289, 4.6185))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.5868, 
    farPlane=72.2168, width=38.9401, height=22.2563, cameraPosition=(-23.4382, 
    4.6204, -48.2546), cameraUpVector=(0.236676, 0.889745, 0.390305), 
    cameraTarget=(-0.350331, -2.88762, 4.30767))
session.viewports['Viewport: 1'].view.setValues(nearPlane=46.579, 
    farPlane=72.3016, width=38.9336, height=22.2526, cameraPosition=(-24.5261, 
    3.80414, -47.8748), cameraUpVector=(0.207612, 0.897477, 0.389143), 
    cameraTarget=(-0.377867, -2.90828, 4.31728))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.897, 
    farPlane=72.9834, width=46.1887, height=26.3993, viewOffsetX=3.32297, 
    viewOffsetY=-1.98677)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.5823, 
    farPlane=74.4822, width=49.8974, height=28.519, cameraPosition=(-44.2506, 
    -6.29622, -36.5695), cameraUpVector=(0.131875, 0.95706, 0.258156), 
    cameraTarget=(-2.31213, -2.63138, 3.17894), viewOffsetX=3.58978, 
    viewOffsetY=-2.14629)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4532, 
    farPlane=74.8077, width=48.7612, height=27.8696, cameraPosition=(-46.4256, 
    3.67294, -33.4983), cameraUpVector=(0.277745, 0.902158, 0.330105), 
    cameraTarget=(-2.24502, -2.06663, 3.47924), viewOffsetX=3.50803, 
    viewOffsetY=-2.09741)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.5156, 
    farPlane=74.7454, width=48.824, height=27.9055, cameraPosition=(-46.3272, 
    3.39311, -33.6593), cameraUpVector=(0.317204, 0.905021, 0.283404), 
    cameraTarget=(-2.14662, -2.34646, 3.31824), viewOffsetX=3.51255, 
    viewOffsetY=-2.10011)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.4963, 
    farPlane=75.4788, width=45.7856, height=26.1688, cameraPosition=(-39.5406, 
    11.6961, -37.4305), cameraUpVector=(0.413937, 0.833923, 0.365005), 
    cameraTarget=(-1.07216, -2.19313, 3.55083), viewOffsetX=3.29395, 
    viewOffsetY=-1.96941)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.4567, 
    farPlane=75.5183, width=51.772, height=29.5904, viewOffsetX=3.71044, 
    viewOffsetY=-2.79501)
session.viewports['Viewport: 1'].view.setValues(nearPlane=47.9352, 
    farPlane=75.0353, width=54.5949, height=31.2038, cameraPosition=(-42.5696, 
    2.09821, -37.6924), cameraUpVector=(0.282119, 0.915214, 0.287736), 
    cameraTarget=(-1.80006, -2.23466, 3.18889), viewOffsetX=3.91275, 
    viewOffsetY=-2.94741)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.8004, 
    farPlane=74.1703, width=43.3942, height=24.8021, viewOffsetX=3.99887, 
    viewOffsetY=-1.18972)
session.viewports['Viewport: 1'].view.setValues(nearPlane=49.0561, 
    farPlane=74.0289, width=43.6217, height=24.932, cameraPosition=(-43.443, 
    3.27792, -36.7679), cameraUpVector=(0.287642, 0.907677, 0.305588), 
    cameraTarget=(-1.91285, -2.082, 3.21623), viewOffsetX=4.01983, 
    viewOffsetY=-1.19596)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=ALL)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=EXTERIOR)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxAutoCompute=OFF, maxValue=1, minValue=-440.439)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    maxAutoCompute=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.4389, 
    farPlane=74.2397, width=43.0729, height=24.6184, cameraPosition=(-42.2483, 
    5.14159, -37.4669), cameraUpVector=(0.32748, 0.89319, 0.308169), 
    cameraTarget=(-1.71595, -2.15276, 3.2287), viewOffsetX=3.96926, 
    viewOffsetY=-1.18091)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    averagingThreshold=25)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    averagingThreshold=75)
session.viewports['Viewport: 1'].view.setValues(nearPlane=48.0491, 
    farPlane=74.6295, width=42.9011, height=24.5202, viewOffsetX=3.93015, 
    viewOffsetY=-1.16922)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
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
    'S13'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S13'), )
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Pipe'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
p = mdb.models['Pipe'].parts['pipe']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
