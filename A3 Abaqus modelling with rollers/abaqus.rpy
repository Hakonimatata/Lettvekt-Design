# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Mon Mar 24 08:11:23 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=185.368759155273, 
    height=177.896286010742)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('sandwitch.cae')
#: The model database "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A3 Abaqus modelling\sandwitch.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['roller']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=599.478, 
    farPlane=780.744, width=441.435, height=174.758, cameraPosition=(717.416, 
    174.845, 159.69), cameraUpVector=(-0.559284, 0.788751, -0.255093), 
    cameraTarget=(46.4157, -6.19276, 162.902))
session.viewports['Viewport: 1'].view.setValues(nearPlane=506.005, 
    farPlane=864.612, width=372.605, height=147.509, cameraPosition=(542.411, 
    -147.165, -300.445), cameraUpVector=(-0.100562, 0.991247, 0.08554), 
    cameraTarget=(47.6557, -3.91118, 166.162))
session.viewports['Viewport: 1'].view.setValues(nearPlane=512.777, 
    farPlane=856.053, width=377.592, height=149.484, cameraPosition=(567.245, 
    -66.1672, -291.085), cameraUpVector=(-0.160969, 0.967635, 0.19435), 
    cameraTarget=(47.3045, -5.05673, 166.03))
session.viewports['Viewport: 1'].view.setValues(nearPlane=514.574, 
    farPlane=854.256, width=336.18, height=133.089, viewOffsetX=28.4133, 
    viewOffsetY=13.1068)
session.viewports['Viewport: 1'].view.setValues(nearPlane=574.17, 
    farPlane=770.492, width=375.115, height=148.503, cameraPosition=(703.146, 
    149.878, 98.3244), cameraUpVector=(-0.530795, 0.840549, 0.108324), 
    cameraTarget=(29.9571, -8.5067, 167.301), viewOffsetX=31.704, 
    viewOffsetY=14.6248)
session.viewports['Viewport: 1'].view.setValues(nearPlane=478.011, 
    farPlane=838.556, width=312.292, height=123.632, cameraPosition=(387.34, 
    238.287, 664.425), cameraUpVector=(-0.490762, 0.748471, -0.446031), 
    cameraTarget=(8.49271, -13.679, 139.054), viewOffsetX=26.3944, 
    viewOffsetY=12.1755)
session.viewports['Viewport: 1'].view.setValues(nearPlane=546.855, 
    farPlane=784.748, width=357.269, height=141.438, cameraPosition=(585.708, 
    341.353, 354.864), cameraUpVector=(-0.765944, 0.629471, -0.130753), 
    cameraTarget=(20.8422, -17.073, 166.49), viewOffsetX=30.1958, 
    viewOffsetY=13.929)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A3 Abaqus modelling\sandwitch.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
del mdb.jobs['Job-2']
del mdb.jobs['Job-3']
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
session.viewports['Viewport: 1'].view.setValues(nearPlane=488.494, 
    farPlane=868.225, width=319.141, height=132.115, cameraPosition=(-99.8386, 
    37.0836, -512.473), cameraUpVector=(-0.28329, 0.84396, 0.455499), 
    cameraTarget=(91.9233, 15.596, 155.205), viewOffsetX=26.9733, 
    viewOffsetY=12.4425)
session.viewports['Viewport: 1'].view.setValues(nearPlane=532.753, 
    farPlane=833.057, width=348.057, height=144.085, cameraPosition=(555.888, 
    336.005, -167.479), cameraUpVector=(-0.74535, 0.63326, 0.208413), 
    cameraTarget=(62.1094, 2.82114, 190.572), viewOffsetX=29.4172, 
    viewOffsetY=13.5698)
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.877, 
    farPlane=785.396, width=373.617, height=154.666, cameraPosition=(724.013, 
    21.7523, 75.3852), cameraUpVector=(-0.361591, 0.929495, 0.0727364), 
    cameraTarget=(39.2986, -4.46813, 191.611), viewOffsetX=31.5775, 
    viewOffsetY=14.5663)
session.viewports['Viewport: 1'].view.setValues(nearPlane=539.529, 
    farPlane=825.582, width=352.484, height=145.918, cameraPosition=(622.047, 
    208.912, 460.927), cameraUpVector=(-0.644637, 0.761369, -0.0690043), 
    cameraTarget=(27.95, -15.4149, 178.515), viewOffsetX=29.7913, 
    viewOffsetY=13.7424)
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A3 Abaqus modelling/Job-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A3 Abaqus modelling/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     5
#: Number of Meshes:             6
#: Number of Element Sets:       4
#: Number of Node Sets:          12
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=610.533, 
    farPlane=712.175, width=379.222, height=156.986, cameraPosition=(665.815, 
    114.473, 145.834), cameraUpVector=(-0.495587, 0.823318, -0.276659), 
    cameraTarget=(11.636, -5.12061, 160.339))
session.viewports['Viewport: 1'].view.setValues(nearPlane=599.012, 
    farPlane=726.66, width=372.066, height=154.024, cameraPosition=(672.939, 
    -23.3224, 228.607), cameraUpVector=(-0.276599, 0.908475, -0.313316), 
    cameraTarget=(11.5948, -4.32362, 159.86))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=526.071, 
    farPlane=838.168, width=359.391, height=142.278, cameraPosition=(589.583, 
    164.222, 535.591), cameraUpVector=(-0.493337, 0.829372, -0.262222), 
    cameraTarget=(19.3824, -8.73261, 177.836), viewOffsetX=29.0482, 
    viewOffsetY=13.3996)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
mdb.models['Model-1'].interactions['Int-1'].move('Initial', 'Step-1')
mdb.models['Model-1'].interactions['Int-1'].move('Step-1', 'Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=517.635, 
    farPlane=838.751, width=353.628, height=139.997, cameraPosition=(562.023, 
    -181.295, 553.935), cameraUpVector=(-0.26294, 0.946342, 0.187882), 
    cameraTarget=(12.3132, -11.7937, 163.911), viewOffsetX=28.5824, 
    viewOffsetY=13.1847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=528.62, 
    farPlane=834.268, width=361.133, height=142.968, cameraPosition=(603.155, 
    147.858, 521.15), cameraUpVector=(-0.610644, 0.791299, -0.030977), 
    cameraTarget=(24.6604, -19.3792, 174.154), viewOffsetX=29.189, 
    viewOffsetY=13.4645)
session.viewports['Viewport: 1'].view.setValues(nearPlane=550.247, 
    farPlane=814.784, width=375.908, height=148.817, cameraPosition=(609.651, 
    290.735, 415.898), cameraUpVector=(-0.704854, 0.693086, -0.151039), 
    cameraTarget=(30.517, -14.7602, 182.858), viewOffsetX=30.3832, 
    viewOffsetY=14.0154)
session.viewports['Viewport: 1'].view.setValues(nearPlane=552.706, 
    farPlane=812.327, width=354.932, height=140.513, viewOffsetX=29.8533, 
    viewOffsetY=13.3669)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=568.291, 
    farPlane=791.448, width=364.941, height=144.475, cameraPosition=(713.109, 
    126.299, 64.041), cameraUpVector=(-0.529885, 0.833427, -0.15691), 
    cameraTarget=(41.649, 1.64293, 193.009), viewOffsetX=30.6951, 
    viewOffsetY=13.7439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=586.98, 
    farPlane=772.758, width=131.658, height=52.1219, viewOffsetX=62.7247, 
    viewOffsetY=23.3704)
session.viewports['Viewport: 1'].view.setValues(nearPlane=523.637, 
    farPlane=789.062, width=117.451, height=46.4973, cameraPosition=(582.235, 
    114.606, 519.554), cameraUpVector=(-0.214249, 0.811232, -0.544058), 
    cameraTarget=(-11.7358, 11.3993, 173.754), viewOffsetX=55.9559, 
    viewOffsetY=20.8484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=569.935, 
    farPlane=755.717, width=127.836, height=50.6085, cameraPosition=(684.87, 
    38.0131, 339.492), cameraUpVector=(-0.312091, 0.891452, -0.328502), 
    cameraTarget=(6.12297, 6.439, 193.42), viewOffsetX=60.9034, 
    viewOffsetY=22.6918)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A3 Abaqus modelling\sandwitch.cae".
