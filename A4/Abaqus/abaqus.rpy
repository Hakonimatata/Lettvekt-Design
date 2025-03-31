# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Mon Mar 31 14:47:04 2025
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
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#* TypeError: boxpro() takes exactly 9 arguments (8 given)
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 111, in <module>
#*     boxpro(modelname='BP-1', L=300, b=60, h=30, t=1, esize=5, loadcase=1, 
#* value=1)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=515.191, 
    farPlane=849.183, width=356.578, height=141.165, cameraPosition=(34.4774, 
    380.349, 715.486), cameraUpVector=(-0.607211, 0.428702, -0.668961), 
    cameraTarget=(-3.83035, -9.33953, 163.17))
session.viewports['Viewport: 1'].view.setValues(nearPlane=504.315, 
    farPlane=866.143, width=349.052, height=138.185, cameraPosition=(134.775, 
    226.965, 782.536), cameraUpVector=(-0.352379, 0.741661, -0.570761), 
    cameraTarget=(-3.07295, -10.4978, 163.676))
session.viewports['Viewport: 1'].view.setValues(nearPlane=506.732, 
    farPlane=873.784, width=350.725, height=138.847, cameraPosition=(54.7765, 
    23.2487, 837.844), cameraUpVector=(-0.12278, 0.919367, -0.373751), 
    cameraTarget=(-4.02947, -12.9336, 164.337))
session.viewports['Viewport: 1'].view.setValues(nearPlane=522.19, 
    farPlane=848.659, width=361.424, height=143.083, cameraPosition=(463.219, 
    96.1515, 646.166), cameraUpVector=(-0.334689, 0.877757, -0.34282), 
    cameraTarget=(3.79372, -11.5372, 160.666))
session.viewports['Viewport: 1'].view.setValues(nearPlane=514.964, 
    farPlane=854.456, width=356.423, height=141.103, cameraPosition=(408.851, 
    153.549, 677.524), cameraUpVector=(-0.378816, 0.832472, -0.404338), 
    cameraTarget=(3.12839, -10.8348, 161.05))
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=503.164, 
    farPlane=872.36, width=348.256, height=137.87, cameraPosition=(221.742, 
    60.0889, 798.396), cameraUpVector=(-0.278525, 0.890812, -0.358996), 
    cameraTarget=(1.03149, -11.8822, 162.405))
session.viewports['Viewport: 1'].view.setValues(nearPlane=515.475, 
    farPlane=856.633, width=356.777, height=141.243, cameraPosition=(409.777, 
    95.6702, 692.013), cameraUpVector=(-0.423396, 0.86313, -0.275213), 
    cameraTarget=(3.96403, -11.3273, 160.746))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=527.387, 
    farPlane=827.761, width=389.58, height=154.23, cameraPosition=(554.338, 
    383.247, 386.007), cameraUpVector=(-0.532155, 0.575645, -0.620841), 
    cameraTarget=(163.141, -7.95029, -5.19083))
session.viewports['Viewport: 1'].view.setValues(nearPlane=595.517, 
    farPlane=746.939, width=439.909, height=174.154, cameraPosition=(231.391, 
    235.155, 623.576), cameraUpVector=(-0.0199634, 0.759183, -0.650571), 
    cameraTarget=(163.141, -7.9503, -5.1908))
session.viewports['Viewport: 1'].view.setValues(nearPlane=523.33, 
    farPlane=834.297, width=386.584, height=153.044, cameraPosition=(593.998, 
    199.915, 473.13), cameraUpVector=(-0.510779, 0.785177, -0.350145), 
    cameraTarget=(159.713, -7.61715, -3.76852))
session.viewports['Viewport: 1'].view.setValues(nearPlane=497.849, 
    farPlane=868.027, width=367.762, height=145.592, cameraPosition=(772.893, 
    237.363, 149.05), cameraUpVector=(-0.639628, 0.758078, -0.127253), 
    cameraTarget=(160.04, -7.54874, -4.36051))
session.viewports['Viewport: 1'].view.setValues(nearPlane=499.833, 
    farPlane=872.88, width=369.227, height=146.172, cameraPosition=(815.087, 
    149.481, -80.844), cameraUpVector=(-0.550344, 0.834022, -0.0390917), 
    cameraTarget=(160.371, -8.23914, -6.16655))
session.viewports['Viewport: 1'].view.setValues(nearPlane=500.584, 
    farPlane=868.543, width=369.781, height=146.392, cameraPosition=(795.236, 
    129.005, 189.178), cameraUpVector=(-0.498202, 0.855502, -0.141105), 
    cameraTarget=(160.117, -8.50116, -2.71124))
session.viewports['Viewport: 1'].view.setValues(nearPlane=511.815, 
    farPlane=855.685, width=378.079, height=149.676, cameraPosition=(732.175, 
    87.393, 347.966), cameraUpVector=(-0.384626, 0.885593, -0.260361), 
    cameraTarget=(159.473, -8.92606, -1.08985))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=554.389, 
    farPlane=797.303, width=409.527, height=162.126, cameraPosition=(439.985, 
    222.06, 568.881), cameraUpVector=(-0.445078, 0.755124, -0.481346), 
    cameraTarget=(163.141, -7.95029, -5.19084))
session.viewports['Viewport: 1'].view.setValues(nearPlane=523.37, 
    farPlane=832.951, width=386.613, height=153.055, cameraPosition=(578.506, 
    367.797, 375.85), cameraUpVector=(-0.477408, 0.5879, -0.653035), 
    cameraTarget=(162.787, -8.32283, -4.6974))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
#: Warning: The output database 'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=566.468, 
    farPlane=801.041, width=389.398, height=161.199, cameraPosition=(369.518, 
    254.129, 581.493), cameraUpVector=(-0.506568, 0.691192, -0.515405), 
    cameraTarget=(160.933, -9.39685, -2.89848))
session.viewports['Viewport: 1'].view.setValues(nearPlane=622.743, 
    farPlane=772.231, width=428.082, height=177.213, cameraPosition=(177.274, 
    -675.945, 155.673), cameraUpVector=(0.089014, 0.554783, 0.82722), 
    cameraTarget=(158.23, -22.4734, -8.88538))
session.viewports['Viewport: 1'].view.setValues(nearPlane=607.96, 
    farPlane=788.094, width=417.92, height=173.006, cameraPosition=(228.053, 
    -662.219, 192.249), cameraUpVector=(0.0633149, 0.60547, 0.793346), 
    cameraTarget=(159.93, -22.014, -7.66117))
session.viewports['Viewport: 1'].view.setValues(nearPlane=549.788, 
    farPlane=853.243, width=377.932, height=156.452, cameraPosition=(540.944, 
    -561.171, 141.975), cameraUpVector=(-0.193486, 0.515017, 0.835058), 
    cameraTarget=(170.636, -18.5564, -9.38144))
session.viewports['Viewport: 1'].view.setValues(nearPlane=533.107, 
    farPlane=872.954, width=366.465, height=151.706, cameraPosition=(663.887, 
    -461.812, 115.906), cameraUpVector=(-0.299406, 0.417796, 0.857789), 
    cameraTarget=(175.433, -14.6794, -10.3987))
session.viewports['Viewport: 1'].view.setValues(nearPlane=613.14, 
    farPlane=782.642, width=421.482, height=174.481, cameraPosition=(85.0231, 
    -661.884, 197.221), cameraUpVector=(0.271787, 0.570989, 0.774663), 
    cameraTarget=(151.647, -22.9006, -7.05739))
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    coordSystemDisplay=ON)
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    bcDisplay=ON, coordSystemDisplay=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=595.476, 
    farPlane=802.957, width=409.34, height=169.454, cameraPosition=(319.385, 
    -677.557, 19.5546), cameraUpVector=(0.0665754, 0.405314, 0.91175), 
    cameraTarget=(159.622, -23.4339, -13.1032))
session.viewports['Viewport: 1'].view.setValues(nearPlane=541.869, 
    farPlane=859.862, width=372.49, height=154.199, cameraPosition=(560.362, 
    -380.103, 408.001), cameraUpVector=(-0.472143, 0.700685, 0.534904), 
    cameraTarget=(168.263, -12.7673, 0.826389))
session.viewports['Viewport: 1'].view.setValues(nearPlane=618.361, 
    farPlane=782.715, width=425.072, height=175.967, cameraPosition=(113.09, 
    -386.317, -597.562), cameraUpVector=(-0.421152, -0.495109, 0.759933), 
    cameraTarget=(151.209, -13.0042, -37.5147))
session.viewports['Viewport: 1'].view.setValues(nearPlane=598.735, 
    farPlane=805.401, width=411.581, height=170.382, cameraPosition=(31.9634, 
    601.735, -356.217), cameraUpVector=(-0.261875, -0.771164, -0.580283), 
    cameraTarget=(148.152, 24.224, -28.4212))
session.viewports['Viewport: 1'].view.setValues(nearPlane=626.581, 
    farPlane=776.854, width=430.723, height=178.306, cameraPosition=(173.8, 
    147.978, 671.202), cameraUpVector=(-0.551412, 0.687603, -0.472384), 
    cameraTarget=(153.794, 6.1755, 12.4451))
session.viewports['Viewport: 1'].view.setValues(nearPlane=585.373, 
    farPlane=818.99, width=402.396, height=166.58, cameraPosition=(355.241, 
    -650.103, 153.945), cameraUpVector=(-0.619339, 0.349114, 0.703235), 
    cameraTarget=(160.924, -25.1853, -7.8807))
session.viewports['Viewport: 1'].view.setValues(nearPlane=614.421, 
    farPlane=787.813, width=422.365, height=174.846, cameraPosition=(74.2277, 
    -688.581, -122.43), cameraUpVector=(-0.367115, 0.240867, 0.898448), 
    cameraTarget=(149.703, -26.7217, -18.9165))
session.viewports['Viewport: 1'].view.setValues(nearPlane=605.855, 
    farPlane=797.536, width=416.477, height=172.409, cameraPosition=(263.701, 
    -680.353, 114.433), cameraUpVector=(-0.0994546, 0.491738, 0.865045), 
    cameraTarget=(156.993, -26.4051, -9.8036))
session.viewports['Viewport: 1'].view.setValues(nearPlane=592.627, 
    farPlane=811.207, width=407.384, height=168.645, cameraPosition=(326.01, 
    -661.939, 139.155), cameraUpVector=(-0.140484, 0.513319, 0.846621), 
    cameraTarget=(159.44, -25.6821, -8.83287))
session.viewports['Viewport: 1'].view.setValues(nearPlane=583.435, 
    farPlane=820.749, width=401.066, height=166.029, cameraPosition=(373.393, 
    -644.432, 152.255), cameraUpVector=(-0.207195, 0.508477, 0.835776), 
    cameraTarget=(161.315, -24.9894, -8.31451))
session.viewports['Viewport: 1'].view.setValues(nearPlane=620.362, 
    farPlane=781.899, width=426.451, height=176.538, cameraPosition=(96.8674, 
    -693.966, 70.3887), cameraUpVector=(-0.083319, 0.452666, 0.887779), 
    cameraTarget=(150.307, -26.9612, -11.5734))
session.viewports['Viewport: 1'].view.setValues(nearPlane=611.882, 
    farPlane=790.134, width=420.622, height=174.125, cameraPosition=(79.1737, 
    -678.868, 145.477), cameraUpVector=(-0.145252, 0.553791, 0.819889), 
    cameraTarget=(149.626, -26.38, -8.68311))
session.viewports['Viewport: 1'].view.setValues(nearPlane=616.097, 
    farPlane=787.024, width=423.52, height=175.324, cameraPosition=(221.9, 
    -692.669, 70.7365), cameraUpVector=(-0.338869, 0.408289, 0.847625), 
    cameraTarget=(155.096, -26.9089, -11.5474))
session.viewports['Viewport: 1'].view.setValues(nearPlane=604.547, 
    farPlane=799.152, width=415.58, height=172.038, cameraPosition=(289.768, 
    -687.695, -2.36335), cameraUpVector=(-0.342821, 0.287788, 0.894233), 
    cameraTarget=(157.748, -26.7145, -14.4042))
session.viewports['Viewport: 1'].view.setValues(nearPlane=591.518, 
    farPlane=812.718, width=406.625, height=168.33, cameraPosition=(342.541, 
    -669.022, -105.541), cameraUpVector=(-0.246897, 0.149674, 0.957413), 
    cameraTarget=(159.831, -25.9774, -18.4772))
session.viewports['Viewport: 1'].view.setValues(nearPlane=583.204, 
    farPlane=821.358, width=400.91, height=165.965, cameraPosition=(385.122, 
    -653.11, -120.995), cameraUpVector=(-0.20566, 0.127199, 0.970322), 
    cameraTarget=(161.528, -25.3434, -19.0929))
session.viewports['Viewport: 1'].view.setValues(nearPlane=603.275, 
    farPlane=800.562, width=414.708, height=171.677, cameraPosition=(306.675, 
    -684.198, -9.12655), cameraUpVector=(-0.247296, 0.293649, 0.923372), 
    cameraTarget=(158.385, -26.589, -14.6107))
session.viewports['Viewport: 1'].view.setValues(nearPlane=619.935, 
    farPlane=783.062, width=426.161, height=176.418, cameraPosition=(201.841, 
    -690.228, 99.7105), cameraUpVector=(-0.221428, 0.46499, 0.857178), 
    cameraTarget=(154.237, -26.8276, -10.3039))
session.viewports['Viewport: 1'].view.setValues(nearPlane=616.126, 
    farPlane=786.996, width=423.543, height=175.334, cameraPosition=(217.837, 
    -691.467, 82.9719), cameraUpVector=(-0.219037, 0.44042, 0.870662), 
    cameraTarget=(154.861, -26.8759, -10.9566))
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=0)
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=1)
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=617.349, 
    farPlane=781.783, width=424.384, height=175.682, cameraPosition=(217.837, 
    -691.467, 82.9719), cameraUpVector=(-0.0403775, 0.459682, 0.887165), 
    cameraTarget=(154.861, -26.8759, -10.9566))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Stat')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Stat')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
#* TypeError: ur2; found FIXED, expecting float
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 99, in <module>
#*     boxpro(modelname='BP-1', L=300, b=60, h=30, t=1, n_supports=0, esize=5, 
#* loadcase=1, value=1)
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 82, in boxpro
#*     u1=FREED, ur2=FIXED, buckleCase=PERTURBATION_AND_BUCKLING)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-2', model='BP-1', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=609.339, 
    farPlane=765.686, width=418.868, height=173.399, cameraPosition=(234.12, 
    -13.9372, 668.343), cameraUpVector=(0.0477975, 0.939412, -0.339443), 
    cameraTarget=(159.019, -12.9838, -1.60155))
session.viewports['Viewport: 1'].view.setValues(nearPlane=588.316, 
    farPlane=817.031, width=404.417, height=167.416, cameraPosition=(372.339, 
    -665.551, -40.602), cameraUpVector=(0.15063, 0.364549, 0.918921), 
    cameraTarget=(161.707, -25.6564, -15.3891))
session.viewports['Viewport: 1'].view.setValues(nearPlane=587.838, 
    farPlane=816.995, width=404.089, height=167.281, cameraPosition=(347.215, 
    -635.947, 208.626), cameraUpVector=(0.0615859, 0.650934, 0.756632), 
    cameraTarget=(160.687, -24.4543, -5.26915))
session.viewports['Viewport: 1'].view.setValues(nearPlane=608.527, 
    farPlane=794.849, width=418.312, height=173.168, cameraPosition=(232.152, 
    -608.63, 325.198), cameraUpVector=(-0.1246, 0.737316, 0.663958), 
    cameraTarget=(156.055, -23.3547, -0.576645))
session.viewports['Viewport: 1'].view.setValues(nearPlane=589.843, 
    farPlane=815.084, width=405.468, height=167.852, cameraPosition=(360.573, 
    -668.527, 25.843), cameraUpVector=(-0.186715, 0.346228, 0.919382), 
    cameraTarget=(161.096, -25.7061, -12.3285))
session.viewports['Viewport: 1'].view.setValues(nearPlane=606.026, 
    farPlane=797.846, width=416.594, height=172.457, cameraPosition=(275.419, 
    -684.809, -101.414), cameraUpVector=(-0.0848505, 0.20169, 0.975767), 
    cameraTarget=(157.663, -26.3625, -17.4591))
session.viewports['Viewport: 1'].view.setValues(nearPlane=592.88, 
    farPlane=811.685, width=407.558, height=168.717, cameraPosition=(335.259, 
    -670.116, 82.532), cameraUpVector=(-0.151915, 0.435129, 0.88746), 
    cameraTarget=(160.033, -25.7807, -10.1753))
session.viewports['Viewport: 1'].view.setValues(nearPlane=609.976, 
    farPlane=793.659, width=419.311, height=173.582, cameraPosition=(261.066, 
    -690.755, 38.6358), cameraUpVector=(-0.102495, 0.391914, 0.914274), 
    cameraTarget=(157.06, -26.6077, -11.9343))
session.viewports['Viewport: 1'].view.setValues(nearPlane=609.052, 
    farPlane=794.583, width=418.676, height=173.319, cameraPosition=(261.066, 
    -690.755, 38.6358), cameraUpVector=(-0.114403, 0.390004, 0.913679), 
    cameraTarget=(157.06, -26.6077, -11.9343))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=601.667, 
    farPlane=801.848, width=637.807, height=264.033, viewOffsetX=-27.3867, 
    viewOffsetY=-9.09092)
session.viewports['Viewport: 1'].view.setValues(nearPlane=532.779, 
    farPlane=848.062, width=564.781, height=233.802, cameraPosition=(488.105, 
    -596.22, 63.9613), cameraUpVector=(-0.0244949, 0.493866, 0.869193), 
    cameraTarget=(163.032, -11.4733, -18.9151), viewOffsetX=-24.2511, 
    viewOffsetY=-8.05005)
session.viewports['Viewport: 1'].view.setValues(nearPlane=535.293, 
    farPlane=842.258, width=567.446, height=234.905, cameraPosition=(473.558, 
    -570.894, 192.733), cameraUpVector=(-0.162901, 0.598635, 0.784283), 
    cameraTarget=(161.814, -9.92928, -13.6755), viewOffsetX=-24.3655, 
    viewOffsetY=-8.08803)
session.viewports['Viewport: 1'].view.setValues(nearPlane=553.84, 
    farPlane=831.193, width=587.107, height=243.045, cameraPosition=(409.991, 
    -622.388, 140.216), cameraUpVector=(-0.153544, 0.517027, 0.842085), 
    cameraTarget=(161.529, -14.3573, -11.5551), viewOffsetX=-25.2097, 
    viewOffsetY=-8.36827)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=470.598, 
    farPlane=879.032, width=498.866, height=206.515, cameraPosition=(765.057, 
    -255.626, 87.9352), cameraUpVector=(-0.335384, 0.415463, 0.845523), 
    cameraTarget=(155.462, 11.4922, -19.3502), viewOffsetX=-21.4207, 
    viewOffsetY=-7.11052)
session.viewports['Viewport: 1'].view.setValues(nearPlane=512.108, 
    farPlane=850.72, width=542.869, height=224.732, cameraPosition=(587.108, 
    -476.916, 197.348), cameraUpVector=(-0.313859, 0.537636, 0.782585), 
    cameraTarget=(165.144, 3.99059, -15.1228), viewOffsetX=-23.3102, 
    viewOffsetY=-7.73772)
session.viewports['Viewport: 1'].view.setValues(nearPlane=534.322, 
    farPlane=828.506, width=238.192, height=98.6045, viewOffsetX=-6.06604, 
    viewOffsetY=-7.27406)
session.viewports['Viewport: 1'].view.setValues(nearPlane=517.099, 
    farPlane=858.062, width=230.514, height=95.426, cameraPosition=(762.034, 
    -306.009, -72.9778), cameraUpVector=(-0.221551, 0.123139, 0.967343), 
    cameraTarget=(166.372, 4.60788, -16.643), viewOffsetX=-5.8705, 
    viewOffsetY=-7.03958)
session.viewports['Viewport: 1'].view.setValues(nearPlane=510.767, 
    farPlane=864.394, width=330.05, height=136.631, viewOffsetX=-0.232405, 
    viewOffsetY=-10.6604)
session.viewports['Viewport: 1'].view.setValues(nearPlane=504.13, 
    farPlane=864.23, width=325.762, height=134.855, cameraPosition=(758.652, 
    -290.213, 95.6195), cameraUpVector=(-0.445438, 0.185463, 0.875893), 
    cameraTarget=(162.958, 5.95649, -13.4797), viewOffsetX=-0.229385, 
    viewOffsetY=-10.5218)
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=513.347, 
    farPlane=896.78, width=352.89, height=146.086, cameraPosition=(849.822, 
    -39.8384, -80.2761), cameraUpVector=(-0.23113, 0.302365, 0.924746), 
    cameraTarget=(179.729, -1.23474, -17.3803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.097, 
    farPlane=892.227, width=356.156, height=147.438, cameraPosition=(806.122, 
    -156.101, 187.407), cameraUpVector=(-0.479206, 0.456401, 0.749707), 
    cameraTarget=(177.813, -6.33321, -5.64154))
session.viewports['Viewport: 1'].view.setValues(nearPlane=522.425, 
    farPlane=887.483, width=359.132, height=148.67, cameraPosition=(786.233, 
    -295.75, 42.629), cameraUpVector=(-0.29049, 0.340913, 0.894088), 
    cameraTarget=(176.938, -12.4759, -12.0099))
session.viewports['Viewport: 1'].view.setValues(nearPlane=545.223, 
    farPlane=864.527, width=374.805, height=155.158, cameraPosition=(612.696, 
    -493.533, 180.407), cameraUpVector=(-0.255387, 0.549795, 0.7953), 
    cameraTarget=(169.354, -21.12, -5.98831))
session.viewports['Viewport: 1'].view.setValues(nearPlane=599.304, 
    farPlane=809.99, width=411.982, height=170.548, cameraPosition=(-13.7223, 
    -630.701, 253.872), cameraUpVector=(-0.309921, 0.717513, 0.623798), 
    cameraTarget=(142.043, -27.1003, -2.78534))
session.viewports['Viewport: 1'].view.setValues(nearPlane=512.455, 
    farPlane=896.724, width=352.279, height=145.833, cameraPosition=(-531.373, 
    -87.9499, 145.988), cameraUpVector=(0.432175, 0.58188, 0.688942), 
    cameraTarget=(119.635, -3.60535, -7.4555))
session.viewports['Viewport: 1'].view.setValues(nearPlane=558.428, 
    farPlane=850.529, width=383.883, height=158.916, cameraPosition=(-249.661, 
    -564.417, 122.331), cameraUpVector=(0.184908, 0.491466, 0.851041), 
    cameraTarget=(131.808, -24.1937, -8.47772))
session.viewports['Viewport: 1'].view.setValues(nearPlane=622.649, 
    farPlane=786.183, width=428.031, height=177.192, cameraPosition=(227.913, 
    -698.188, 34.9587), cameraUpVector=(0.0315576, 0.404408, 0.914034), 
    cameraTarget=(152.372, -29.9538, -12.2399))
session.viewports['Viewport: 1'].view.setValues(nearPlane=521.13, 
    farPlane=887.749, width=358.243, height=148.302, cameraPosition=(760.765, 
    -349.076, -19.9677), cameraUpVector=(-0.368005, 0.0127486, 0.929737), 
    cameraTarget=(175.271, -14.9511, -14.6003))
session.viewports['Viewport: 1'].view.setValues(nearPlane=536.152, 
    farPlane=873.062, width=368.57, height=152.577, cameraPosition=(662.332, 
    -441.851, 179.02), cameraUpVector=(-0.438463, 0.378667, 0.815084), 
    cameraTarget=(171.038, -18.941, -6.04267))
session.viewports['Viewport: 1'].view.setValues(nearPlane=519.09, 
    farPlane=889.99, width=356.841, height=147.722, cameraPosition=(794.588, 
    -269.28, 68.5088), cameraUpVector=(-0.343796, 0.31946, 0.883034), 
    cameraTarget=(176.756, -11.4803, -10.8204))
session.viewports['Viewport: 1'].view.setValues(nearPlane=527.634, 
    farPlane=881.378, width=362.716, height=150.153, cameraPosition=(741.115, 
    -375.485, 53.1332), cameraUpVector=(-0.289407, 0.330438, 0.898362), 
    cameraTarget=(174.449, -16.0622, -11.4837))
session.viewports['Viewport: 1'].view.setValues(nearPlane=542.75, 
    farPlane=866.316, width=373.108, height=154.455, cameraPosition=(633.908, 
    -495.114, 111.546), cameraUpVector=(-0.281229, 0.418402, 0.863626), 
    cameraTarget=(169.829, -21.2178, -8.96632))
session.viewports['Viewport: 1'].view.setValues(nearPlane=546.824, 
    farPlane=862.095, width=375.909, height=155.615, cameraPosition=(621.179, 
    -520.688, 31.0044), cameraUpVector=(-0.181734, 0.365686, 0.912823), 
    cameraTarget=(169.28, -22.3209, -12.4404))
session.viewports['Viewport: 1'].view.setValues(nearPlane=516.54, 
    farPlane=892.623, width=355.09, height=146.997, cameraPosition=(802.04, 
    -229.08, 116.862), cameraUpVector=(-0.426029, 0.299515, 0.853692), 
    cameraTarget=(177.063, -9.77192, -8.74561))
session.viewports['Viewport: 1'].view.setValues(nearPlane=556.499, 
    farPlane=852.873, width=382.561, height=158.369, cameraPosition=(537.987, 
    -511.374, 274.317), cameraUpVector=(-0.378759, 0.578701, 0.722251), 
    cameraTarget=(165.656, -21.9668, -1.94368))
session.viewports['Viewport: 1'].view.setValues(nearPlane=539.871, 
    farPlane=869.619, width=371.131, height=153.637, cameraPosition=(617.184, 
    -399.743, 327.926), cameraUpVector=(-0.465968, 0.599047, 0.651166), 
    cameraTarget=(169.089, -17.1285, 0.379849))
session.viewports['Viewport: 1'].view.setValues(nearPlane=532.047, 
    farPlane=877.444, width=498.365, height=206.308, viewOffsetX=-6.97242, 
    viewOffsetY=13.4996)
session.viewports['Viewport: 1'].view.setValues(nearPlane=590.187, 
    farPlane=818.36, width=552.825, height=228.853, cameraPosition=(310.564, 
    -669.034, 134.449), cameraUpVector=(0.190055, 0.580551, 0.791732), 
    cameraTarget=(148.441, -30.9712, -10.6761), viewOffsetX=-7.73434, 
    viewOffsetY=14.9748)
session.viewports['Viewport: 1'].view.setValues(nearPlane=581.31, 
    farPlane=814.591, width=544.51, height=225.411, cameraPosition=(308.322, 
    -670.857, -123.282), cameraUpVector=(0.189838, 0.244887, 0.950785), 
    cameraTarget=(148.38, -23.8983, -21.6318), viewOffsetX=-7.61801, 
    viewOffsetY=14.7496)
session.viewports['Viewport: 1'].view.setValues(nearPlane=597.606, 
    farPlane=798.296, width=341.221, height=141.255, viewOffsetX=24.1125, 
    viewOffsetY=16.4617)
session.viewports['Viewport: 1'].view.setValues(nearPlane=601.988, 
    farPlane=798.45, width=343.724, height=142.291, cameraPosition=(315.436, 
    -676.183, 59.259), cameraUpVector=(-0.149295, 0.423928, 0.893306), 
    cameraTarget=(154.214, -26.9474, -24.2318), viewOffsetX=24.2893, 
    viewOffsetY=16.5825)
session.viewports['Viewport: 1'].view.setValues(nearPlane=559.493, 
    farPlane=863.709, width=319.46, height=132.247, cameraPosition=(592.974, 
    -548.156, 79.0239), cameraUpVector=(-0.199443, 0.438375, 0.876385), 
    cameraTarget=(168.186, -33.8459, -18.4965), viewOffsetX=22.5747, 
    viewOffsetY=15.4119)
session.viewports['Viewport: 1'].view.setValues(nearPlane=567.805, 
    farPlane=854.406, width=324.207, height=134.212, cameraPosition=(535.761, 
    -555.637, 202.747), cameraUpVector=(-0.261243, 0.567154, 0.781082), 
    cameraTarget=(165.424, -34.7239, -11.6598), viewOffsetX=22.9101, 
    viewOffsetY=15.6409)
session.viewports['Viewport: 1'].view.setValues(nearPlane=547.816, 
    farPlane=886.372, width=312.794, height=129.487, cameraPosition=(729.482, 
    -421.053, -8.28222), cameraUpVector=(-0.25318, 0.259147, 0.932064), 
    cameraTarget=(180.436, -30.2342, -24.9872), viewOffsetX=22.1036, 
    viewOffsetY=15.0903)
session.viewports['Viewport: 1'].view.setValues(nearPlane=543.147, 
    farPlane=900.119, width=310.128, height=128.384, cameraPosition=(781.495, 
    -327.669, 100.731), cameraUpVector=(-0.390185, 0.318005, 0.864077), 
    cameraTarget=(188.936, -28.4874, -16.8877), viewOffsetX=21.9152, 
    viewOffsetY=14.9617)
session.viewports['Viewport: 1'].view.setValues(nearPlane=566.567, 
    farPlane=854.911, width=323.502, height=133.92, cameraPosition=(573.102, 
    -569.396, 19.8945), cameraUpVector=(-0.187663, 0.35192, 0.917025), 
    cameraTarget=(164.067, -35.3016, -23.7271), viewOffsetX=22.8602, 
    viewOffsetY=15.6068)
session.viewports['Viewport: 1'].view.setValues(nearPlane=564.842, 
    farPlane=857.625, width=322.517, height=133.512, cameraPosition=(568.742, 
    -566.263, 80.8059), cameraUpVector=(-0.273003, 0.386615, 0.880908), 
    cameraTarget=(165.503, -35.8579, -21.8505), viewOffsetX=22.7906, 
    viewOffsetY=15.5593)
session.viewports['Viewport: 1'].view.setValues(nearPlane=539.332, 
    farPlane=905.994, width=307.951, height=127.482, cameraPosition=(817.956, 
    -248.154, 100.788), cameraUpVector=(-0.47399, 0.155859, 0.866627), 
    cameraTarget=(192.975, -26.9946, -21.5108), viewOffsetX=21.7613, 
    viewOffsetY=14.8566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=544.437, 
    farPlane=893.381, width=310.866, height=128.689, cameraPosition=(768.155, 
    -364.655, 12.9711), cameraUpVector=(-0.363353, 0.151932, 0.91918), 
    cameraTarget=(183.492, -31.6367, -28.7163), viewOffsetX=21.9673, 
    viewOffsetY=14.9972)
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=0)
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=1)
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=1)
session.viewports['Viewport: 1'].odbDisplay.setDeformedVariable(
    variableLabel='UR', )
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports['Viewport: 1'].odbDisplay.setDeformedVariable(
    variableLabel='U', )
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=533.937, 
    farPlane=898.34, width=417.108, height=172.67, viewOffsetX=16.146, 
    viewOffsetY=20.458)
session.viewports['Viewport: 1'].view.setValues(nearPlane=589.753, 
    farPlane=815.928, width=460.712, height=190.721, cameraPosition=(313.842, 
    -620.997, 303.618), cameraUpVector=(-0.385171, 0.645517, 0.659509), 
    cameraTarget=(154.564, -46.4531, -11.0243), viewOffsetX=17.8339, 
    viewOffsetY=22.5966)
session.viewports['Viewport: 1'].view.setValues(nearPlane=502.427, 
    farPlane=880.733, width=392.493, height=162.48, cameraPosition=(-440.819, 
    -231.255, 293.324), cameraUpVector=(0.187517, 0.952963, 0.238115), 
    cameraTarget=(125.694, -30.6083, -12.0833), viewOffsetX=15.1932, 
    viewOffsetY=19.2507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=557.844, 
    farPlane=810.462, width=435.784, height=180.402, cameraPosition=(442.729, 
    2.26862, 634.362), cameraUpVector=(-0.784722, 0.617857, -0.049642), 
    cameraTarget=(161.811, -39.9336, 22.9918), viewOffsetX=16.869, 
    viewOffsetY=21.374)
session.viewports['Viewport: 1'].view.setValues(nearPlane=502.264, 
    farPlane=874.775, width=392.367, height=162.428, cameraPosition=(715.306, 
    -289.166, 283.771), cameraUpVector=(-0.583761, 0.404154, 0.704189), 
    cameraTarget=(159.351, -37.3364, -2.52409), viewOffsetX=15.1883, 
    viewOffsetY=19.2444)
session.viewports['Viewport: 1'].view.setValues(nearPlane=529.568, 
    farPlane=853.681, width=413.697, height=171.258, cameraPosition=(612.533, 
    -515.379, -1.28186), cameraUpVector=(-0.346816, 0.158375, 0.924465), 
    cameraTarget=(146.813, -28.1976, -16.3821), viewOffsetX=16.014, 
    viewOffsetY=20.2906)
session.viewports['Viewport: 1'].view.setValues(nearPlane=517.496, 
    farPlane=863.11, width=404.266, height=167.354, cameraPosition=(626.839, 
    -433.27, 265.454), cameraUpVector=(-0.427175, 0.542638, 0.723232), 
    cameraTarget=(149.945, -38.6479, -1.5931), viewOffsetX=15.6489, 
    viewOffsetY=19.8281)
session.viewports['Viewport: 1'].view.setValues(nearPlane=501.112, 
    farPlane=877.318, width=391.467, height=162.056, cameraPosition=(752.872, 
    -300.291, 165.798), cameraUpVector=(-0.478014, 0.308202, 0.822505), 
    cameraTarget=(157.774, -34.4757, -6.44762), viewOffsetX=15.1535, 
    viewOffsetY=19.2003)
session.viewports['Viewport: 1'].view.setValues(nearPlane=504.075, 
    farPlane=875.008, width=393.783, height=163.014, cameraPosition=(742.548, 
    -334.111, 133.744), cameraUpVector=(-0.431898, 0.304395, 0.849004), 
    cameraTarget=(155.564, -34.253, -7.68746), viewOffsetX=15.2431, 
    viewOffsetY=19.3138)
session.viewports['Viewport: 1'].view.setValues(nearPlane=498.961, 
    farPlane=877.495, width=389.788, height=161.361, cameraPosition=(824.911, 
    -139.222, 28.1018), cameraUpVector=(-0.403587, -0.0360343, 0.914231), 
    cameraTarget=(161.847, -25.1393, -14.3125), viewOffsetX=15.0885, 
    viewOffsetY=19.1179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=497.624, 
    farPlane=875.625, width=388.745, height=160.929, cameraPosition=(825.544, 
    107.393, -55.8998), cameraUpVector=(-0.259876, -0.108321, 0.959547), 
    cameraTarget=(165.076, -21.3964, -15.1244), viewOffsetX=15.0481, 
    viewOffsetY=19.0667)
session.viewports['Viewport: 1'].view.setValues(nearPlane=498.402, 
    farPlane=874.948, width=389.354, height=161.181, cameraPosition=(833.594, 
    75.0987, 18.2334), cameraUpVector=(-0.374932, -0.0307568, 0.926542), 
    cameraTarget=(167.447, -23.8787, -12.0812), viewOffsetX=15.0716, 
    viewOffsetY=19.0965)
session.viewports['Viewport: 1'].view.setValues(nearPlane=502.224, 
    farPlane=875.871, width=392.34, height=162.417, cameraPosition=(774.259, 
    -291.709, 51.975), cameraUpVector=(-0.387892, 0.164166, 0.906967), 
    cameraTarget=(156.442, -29.6291, -11.9247), viewOffsetX=15.1872, 
    viewOffsetY=19.243)
session.viewports['Viewport: 1'].view.setValues(nearPlane=543.092, 
    farPlane=838.092, width=424.266, height=175.633, cameraPosition=(493.348, 
    -558.436, 235.04), cameraUpVector=(-0.380584, 0.526691, 0.7601), 
    cameraTarget=(144.914, -34.4634, -6.85449), viewOffsetX=16.423, 
    viewOffsetY=20.8089)
session.viewports['Viewport: 1'].view.setValues(nearPlane=566.703, 
    farPlane=814.501, width=442.711, height=183.269, cameraPosition=(343.471, 
    -556.352, 377.095), cameraUpVector=(-0.29899, 0.746412, 0.594537), 
    cameraTarget=(138.971, -36.562, -0.349863), viewOffsetX=17.137, 
    viewOffsetY=21.7136)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_UNDEF, SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=534.535, 
    farPlane=846.581, width=417.581, height=172.866, cameraPosition=(516.051, 
    -551.729, 214.335), cameraUpVector=(-0.286293, 0.55868, 0.778404), 
    cameraTarget=(142.567, -35.1725, -5.08801), viewOffsetX=16.1642, 
    viewOffsetY=20.4811)
session.viewports['Viewport: 1'].view.setValues(nearPlane=519.253, 
    farPlane=861.16, width=405.643, height=167.924, cameraPosition=(623.466, 
    -486.139, 146.127), cameraUpVector=(-0.319399, 0.444676, 0.836808), 
    cameraTarget=(147.151, -34.3832, -7.19786), viewOffsetX=15.7021, 
    viewOffsetY=19.8956)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=513.494, 
    farPlane=865.968, width=401.144, height=166.062, cameraPosition=(660.148, 
    -428.461, 197.102), cameraUpVector=(-0.456187, 0.395821, 0.797006), 
    cameraTarget=(152.972, -34.0776, -7.1074), viewOffsetX=15.528, 
    viewOffsetY=19.6749)
session.viewports['Viewport: 1'].view.setValues(nearPlane=513.754, 
    farPlane=865.161, width=401.348, height=166.146, cameraPosition=(655.809, 
    -402.765, 256.883), cameraUpVector=(-0.508559, 0.443059, 0.738286), 
    cameraTarget=(154.65, -35.3334, -4.46143), viewOffsetX=15.5359, 
    viewOffsetY=19.6849)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=537.017, 
    farPlane=859.354, width=419.521, height=173.669, cameraPosition=(577.856, 
    -529.055, 140.553), cameraUpVector=(-0.375299, 0.386704, 0.842384), 
    cameraTarget=(146.028, -34.4092, -12.1444), viewOffsetX=16.2394, 
    viewOffsetY=20.5762)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=600.456, 
    farPlane=782.102, width=469.079, height=194.185, cameraPosition=(84.6599, 
    -520.094, 467.113), cameraUpVector=(-0.286065, 0.874993, 0.390582), 
    cameraTarget=(134.295, -37.9112, -1.39735), viewOffsetX=18.1578, 
    viewOffsetY=23.0069)
session.viewports['Viewport: 1'].view.setValues(nearPlane=515.94, 
    farPlane=860.665, width=403.056, height=166.853, cameraPosition=(598.307, 
    -364.044, 391.255), cameraUpVector=(-0.553544, 0.612302, 0.564514), 
    cameraTarget=(153.336, -40.2856, 1.83616), viewOffsetX=15.602, 
    viewOffsetY=19.7686)
session.viewports['Viewport: 1'].view.setValues(nearPlane=503.873, 
    farPlane=872.184, width=393.629, height=162.951, cameraPosition=(714.63, 
    -300.187, 271.628), cameraUpVector=(-0.557306, 0.422537, 0.714754), 
    cameraTarget=(158.078, -37.3008, -3.3379), viewOffsetX=15.2371, 
    viewOffsetY=19.3062)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=520.345, 
    farPlane=865.174, width=406.498, height=168.278, cameraPosition=(673.763, 
    -441.309, 108.971), cameraUpVector=(-0.376181, 0.32671, 0.867034), 
    cameraTarget=(149.572, -35.1385, -12.3328), viewOffsetX=15.7352, 
    viewOffsetY=19.9373)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=498.207, 
    farPlane=877.98, width=389.204, height=161.119, cameraPosition=(811.12, 
    -194.774, 23.7823), cameraUpVector=(-0.437521, -0.124733, 0.890515), 
    cameraTarget=(160.567, -23.3874, -19.4926), viewOffsetX=15.0658, 
    viewOffsetY=19.0891)
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.515, 
    farPlane=861.612, width=405.069, height=167.687, cameraPosition=(646.892, 
    -465.048, 135.785), cameraUpVector=(-0.455518, 0.28974, 0.841757), 
    cameraTarget=(151.499, -33.0681, -14.0287), viewOffsetX=15.6799, 
    viewOffsetY=19.8672)
session.viewports['Viewport: 1'].view.setValues(nearPlane=527.838, 
    farPlane=852.491, width=412.354, height=170.702, cameraPosition=(574.865, 
    -510.143, 207.599), cameraUpVector=(-0.468402, 0.41364, 0.780706), 
    cameraTarget=(149.396, -35.3031, -11.4179), viewOffsetX=15.9618, 
    viewOffsetY=20.2244)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=538.734, 
    farPlane=840.383, width=420.866, height=174.226, cameraPosition=(515.11, 
    -568.41, -152.546), cameraUpVector=(-0.170201, 0.0671412, 0.983119), 
    cameraTarget=(137.54, -24.3359, -26.4954), viewOffsetX=16.2913, 
    viewOffsetY=20.6419)
session.viewports['Viewport: 1'].view.setValues(nearPlane=529.117, 
    farPlane=854.971, width=413.353, height=171.116, cameraPosition=(606.919, 
    -519.16, -34.4518), cameraUpVector=(-0.228165, 0.220039, 0.948432), 
    cameraTarget=(142.118, -31.0161, -22.5864), viewOffsetX=16.0005, 
    viewOffsetY=20.2734)
session.viewports['Viewport: 1'].view.setValues(nearPlane=526.198, 
    farPlane=859.198, width=411.074, height=170.172, cameraPosition=(630.204, 
    -498.777, -1.87575), cameraUpVector=(-0.262829, 0.247032, 0.932682), 
    cameraTarget=(144.032, -32.1772, -21.5284), viewOffsetX=15.9122, 
    viewOffsetY=20.1616)
session.viewports['Viewport: 1'].view.setValues(nearPlane=601.953, 
    farPlane=792.984, width=470.255, height=194.671, cameraPosition=(253.518, 
    -687.524, 44.0108), cameraUpVector=(-0.146782, 0.40303, 0.903339), 
    cameraTarget=(129.832, -28.078, -21.5414), viewOffsetX=18.203, 
    viewOffsetY=23.0642)
session.viewports['Viewport: 1'].view.setValues(nearPlane=494.387, 
    farPlane=887.282, width=386.223, height=159.885, cameraPosition=(823.007, 
    -140.12, -75.4516), cameraUpVector=(-0.275965, -0.0446814, 0.960129), 
    cameraTarget=(161.342, -20.8674, -26.0335), viewOffsetX=14.9502, 
    viewOffsetY=18.9427)
session.viewports['Viewport: 1'].view.setValues(nearPlane=510.754, 
    farPlane=871.87, width=399.01, height=165.178, cameraPosition=(733.806, 
    -366.749, -56.5721), cameraUpVector=(-0.296843, 0.0676189, 0.952529), 
    cameraTarget=(154.205, -23.8657, -25.623), viewOffsetX=15.4451, 
    viewOffsetY=19.5698)
session.viewports['Viewport: 1'].view.setValues(nearPlane=514.235, 
    farPlane=878.069, width=401.73, height=166.304, cameraPosition=(716.279, 
    -377.442, 129.351), cameraUpVector=(-0.401593, 0.355432, 0.844033), 
    cameraTarget=(156.289, -31.6018, -16.4902), viewOffsetX=15.5504, 
    viewOffsetY=19.7032)
session.viewports['Viewport: 1'].view.setValues(nearPlane=526.464, 
    farPlane=866.311, width=411.283, height=170.259, cameraPosition=(634.641, 
    -475.241, 139.19), cameraUpVector=(-0.340932, 0.42864, 0.83668), 
    cameraTarget=(150.09, -33.0591, -16.21), viewOffsetX=15.9202, 
    viewOffsetY=20.1717)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=497.49, 
    farPlane=877.983, width=388.648, height=160.889, cameraPosition=(784.743, 
    -228.063, 156.142), cameraUpVector=(-0.609988, -0.0526761, 0.790658), 
    cameraTarget=(167.944, -22.2408, -21.7895), viewOffsetX=15.044, 
    viewOffsetY=19.0615)
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.06, 
    farPlane=856.756, width=404.719, height=167.541, cameraPosition=(630.102, 
    -452.194, 213.292), cameraUpVector=(-0.589628, 0.288858, 0.754254), 
    cameraTarget=(158.848, -29.7643, -18.9519), viewOffsetX=15.666, 
    viewOffsetY=19.8496)
session.viewports['Viewport: 1'].view.setValues(nearPlane=510.901, 
    farPlane=859.064, width=399.126, height=165.226, cameraPosition=(651.582, 
    -329.353, 347.766), cameraUpVector=(-0.652317, 0.43396, 0.621419), 
    cameraTarget=(162.249, -34.5463, -10.1538), viewOffsetX=15.4495, 
    viewOffsetY=19.5753)
session.viewports['Viewport: 1'].view.setValues(nearPlane=500.531, 
    farPlane=876.654, width=391.024, height=161.872, cameraPosition=(777.336, 
    239.896, -143.14), cameraUpVector=(-0.271043, 0.225739, 0.935723), 
    cameraTarget=(172.034, -27.2447, -13.8735), viewOffsetX=15.1359, 
    viewOffsetY=19.178)
session.viewports['Viewport: 1'].view.setValues(nearPlane=528.513, 
    farPlane=846.03, width=412.884, height=170.922, cameraPosition=(558.181, 
    -409.805, 388.32), cameraUpVector=(-0.603682, 0.558362, 0.569034), 
    cameraTarget=(156.52, -39.2874, -6.45785), viewOffsetX=15.9821, 
    viewOffsetY=20.2501)
session.viewports['Viewport: 1'].view.setValues(nearPlane=522.209, 
    farPlane=852.334, width=491.173, height=203.331, viewOffsetX=41.7631, 
    viewOffsetY=18.262)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
#: Warning: The output database 'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=311.431, 
    farPlane=973.195, width=1556.94, height=644.526, viewOffsetX=388.873, 
    viewOffsetY=11.0921)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1761.01, 
    farPlane=3522.01, width=2304.7, height=954.076, cameraPosition=(2195.16, 
    -1717.82, 1612.35), cameraUpVector=(-0.544154, 0.626061, 0.558519), 
    cameraTarget=(424.731, -569.075, 136.691), viewOffsetX=575.64, 
    viewOffsetY=16.4194)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1690.93, 
    farPlane=3577.43, width=2222.04, height=919.858, viewOffsetX=665.105, 
    viewOffsetY=-13.0307)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1656.05, 
    farPlane=3577.99, width=2176.2, height=900.88, cameraPosition=(2309.62, 
    -2095.49, 941.688), cameraUpVector=(-0.291499, 0.568226, 0.769511), 
    cameraTarget=(405.739, -535.675, 184.17), viewOffsetX=651.384, 
    viewOffsetY=-12.7619)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1667.25, 
    farPlane=3549.04, width=2190.91, height=906.972, cameraPosition=(2267.96, 
    -2225.2, 663.184), cameraUpVector=(-0.271869, 0.483989, 0.83177), 
    cameraTarget=(392.372, -550.363, 107.585), viewOffsetX=655.788, 
    viewOffsetY=-12.8482)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1737.03, 
    farPlane=3479.24, width=1307.93, height=541.442, viewOffsetX=732.383, 
    viewOffsetY=-41.6799)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1745.49, 
    farPlane=3465.04, width=1314.29, height=544.077, cameraPosition=(2245.42, 
    -2238.82, 653.504), cameraUpVector=(-0.265874, 0.483919, 0.833746), 
    cameraTarget=(385.287, -544.123, 106.248), viewOffsetX=735.948, 
    viewOffsetY=-41.8828)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1655.74, 
    farPlane=3554.78, width=2472.48, height=1023.53, viewOffsetX=767.056, 
    viewOffsetY=8.58562)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1639.89, 
    farPlane=3698.33, width=2448.82, height=1013.74, cameraPosition=(2619.15, 
    -2063.09, 617.518), cameraUpVector=(-0.331324, 0.428436, 0.840635), 
    cameraTarget=(524.633, -658.182, 97.091), viewOffsetX=759.716, 
    viewOffsetY=8.50346)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1661.03, 
    farPlane=3414.39, width=2480.4, height=1026.81, cameraPosition=(1865.59, 
    -2423.72, 411.092), cameraUpVector=(-0.310663, 0.409022, 0.858015), 
    cameraTarget=(263.695, -472.848, -98.4681), viewOffsetX=769.511, 
    viewOffsetY=8.61309)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1742.42, 
    farPlane=3142.96, width=2601.94, height=1077.13, cameraPosition=(1144.22, 
    -2458.45, 619.821), cameraUpVector=(-0.285101, 0.535637, 0.794865), 
    cameraTarget=(122.142, -230.098, -168.481), viewOffsetX=807.219, 
    viewOffsetY=9.03515)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1584.85, 
    farPlane=3585.45, width=2366.65, height=979.724, cameraPosition=(2379.34, 
    -2266.13, 139.402), cameraUpVector=(-0.429364, 0.210093, 0.878355), 
    cameraTarget=(401.442, -659.949, -234.363), viewOffsetX=734.221, 
    viewOffsetY=8.21809)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1609.48, 
    farPlane=3799.02, width=2403.44, height=994.952, cameraPosition=(3068.02, 
    -1660.41, 668.456), cameraUpVector=(-0.54456, 0.220531, 0.80921), 
    cameraTarget=(735.372, -849.55, -61.5143), viewOffsetX=745.633, 
    viewOffsetY=8.34582)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1608.86, 
    farPlane=3799.64, width=2402.51, height=994.567, cameraPosition=(3063.12, 
    -1658.15, 686.626), cameraUpVector=(-0.539732, 0.233942, 0.808678), 
    cameraTarget=(730.471, -847.291, -43.3439), viewOffsetX=745.345, 
    viewOffsetY=8.34259)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1537.4, 
    farPlane=3787.03, width=2452.34, height=1015.19, viewOffsetX=684.703, 
    viewOffsetY=-0.35959)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1567.26, 
    farPlane=3470.76, width=2499.97, height=1034.91, cameraPosition=(2163.4, 
    -2014.84, 1270.22), cameraUpVector=(-0.744487, 0.364156, 0.55958), 
    cameraTarget=(498.447, -750.676, -233.584), viewOffsetX=698.001, 
    viewOffsetY=-0.366574)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1626.38, 
    farPlane=3593.63, width=2594.28, height=1073.95, cameraPosition=(2344.23, 
    -519.879, 2323.69), cameraUpVector=(-0.678654, 0.70579, 0.203197), 
    cameraTarget=(494.608, -566.488, 532.5), viewOffsetX=724.332, 
    viewOffsetY=-0.380403)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1531.5, 
    farPlane=3684.23, width=2442.93, height=1011.3, cameraPosition=(2628.88, 
    -1313.43, 1728.43), cameraUpVector=(-0.552063, 0.650197, 0.521987), 
    cameraTarget=(524.452, -696.332, 378.544), viewOffsetX=682.074, 
    viewOffsetY=-0.35821)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1584.86, 
    farPlane=3630.85, width=1862.94, height=771.201, viewOffsetX=657.505, 
    viewOffsetY=-28.5936)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1586.81, 
    farPlane=3711.29, width=1865.23, height=772.147, cameraPosition=(2985.95, 
    -1471.03, 1183.66), cameraUpVector=(-0.522059, 0.473125, 0.709652), 
    cameraTarget=(668.065, -831.485, 261.699), viewOffsetX=658.312, 
    viewOffsetY=-28.6287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1592.73, 
    farPlane=3707.64, width=1872.19, height=775.03, cameraPosition=(2959.96, 
    -1720.89, 859.671), cameraUpVector=(-0.510002, 0.347254, 0.786964), 
    cameraTarget=(651.216, -883.702, 84.7982), viewOffsetX=660.768, 
    viewOffsetY=-28.7355)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=10)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1657.24, 
    farPlane=3778.44, width=1948.02, height=806.42, cameraPosition=(3444.11, 
    -1134.88, 705.338), cameraUpVector=(-0.51665, 0.230612, 0.824555), 
    cameraTarget=(943.824, -932.151, 123.035), viewOffsetX=687.53, 
    viewOffsetY=-29.8993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1770.49, 
    farPlane=3665.19, width=603.751, height=249.935, viewOffsetX=851.274, 
    viewOffsetY=-3.57909)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1706.15, 
    farPlane=3544.87, width=581.81, height=240.852, cameraPosition=(2960.98, 
    -1714.72, 761.313), cameraUpVector=(-0.437018, 0.381471, 0.814552), 
    cameraTarget=(604.375, -871.297, 155.785), viewOffsetX=820.337, 
    viewOffsetY=-3.44902)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1697.96, 
    farPlane=3553.06, width=741.617, height=307.007, viewOffsetX=842.337, 
    viewOffsetY=3.44085)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=HIDDEN)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=SHADED)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1648.75, 
    farPlane=3602.27, width=1336.99, height=553.474, viewOffsetX=927.341, 
    viewOffsetY=20.8378)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1686.09, 
    farPlane=3670.93, width=1367.27, height=566.01, cameraPosition=(3152.11, 
    -1448.58, 939.625), cameraUpVector=(-0.501399, 0.377666, 0.778439), 
    cameraTarget=(740.717, -898.728, 222.362), viewOffsetX=948.346, 
    viewOffsetY=21.3098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1629.54, 
    farPlane=3583.53, width=1321.41, height=547.025, cameraPosition=(2910.15, 
    -1793.16, 668.147), cameraUpVector=(-0.479925, 0.314337, 0.819063), 
    cameraTarget=(586.979, -897.201, 11.061), viewOffsetX=916.537, 
    viewOffsetY=20.595)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1609.53, 
    farPlane=3603.55, width=1678.55, height=694.868, viewOffsetX=903.171, 
    viewOffsetY=45.0574)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1720.89, 
    farPlane=3808.46, width=1794.68, height=742.945, cameraPosition=(3549.49, 
    -1150.26, 511.782), cameraUpVector=(-0.482822, 0.180382, 0.856939), 
    cameraTarget=(1020.48, -987.61, 54.3214), viewOffsetX=965.66, 
    viewOffsetY=48.1748)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=EXTERIOR)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1646.86, 
    farPlane=3882.49, width=2659.31, height=1100.87, viewOffsetX=1091.34, 
    viewOffsetY=32.1849)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1556.18, 
    farPlane=3699.55, width=2512.89, height=1040.26, cameraPosition=(2965.62, 
    -1296.86, 1389.55), cameraUpVector=(-0.614444, 0.398836, 0.680726), 
    cameraTarget=(654.353, -893.465, 327.969), viewOffsetX=1031.25, 
    viewOffsetY=30.4129)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1637.78, 
    farPlane=3617.97, width=1612.1, height=667.359, viewOffsetX=964.346, 
    viewOffsetY=-27.785)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1518.93, 
    farPlane=3443, width=1495.11, height=618.932, cameraPosition=(2483.53, 
    -2100.2, 506.026), cameraUpVector=(-0.383241, 0.331258, 0.862203), 
    cameraTarget=(301.636, -814.935, 37.9714), viewOffsetX=894.367, 
    viewOffsetY=-25.7688)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1475.3, 
    farPlane=3486.63, width=2239.35, height=927.024, viewOffsetX=906.934, 
    viewOffsetY=-24.6877)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1628.92, 
    farPlane=3818.55, width=2472.53, height=1023.55, cameraPosition=(3540.22, 
    -1159.31, 501.556), cameraUpVector=(-0.450542, 0.174955, 0.875444), 
    cameraTarget=(990.693, -1065.42, 151.21), viewOffsetX=1001.37, 
    viewOffsetY=-27.2584)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1842.57, 
    farPlane=4051.67, width=2796.83, height=1157.8, cameraPosition=(4044.07, 
    -214.704, -94.722), cameraUpVector=(-0.307857, 0.00556404, 0.951417), 
    cameraTarget=(1582.55, -963.338, 15.386), viewOffsetX=1132.71, 
    viewOffsetY=-30.8337)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1651.57, 
    farPlane=3914.6, width=2506.91, height=1037.78, cameraPosition=(3710.53, 
    -769.65, 733.656), cameraUpVector=(-0.5485, 0.0432243, 0.835032), 
    cameraTarget=(1224.41, -1093.27, 145.341), viewOffsetX=1015.29, 
    viewOffsetY=-27.6374)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1430.81, 
    farPlane=3546.87, width=2171.82, height=899.068, cameraPosition=(2580.14, 
    -2037.8, 822.034), cameraUpVector=(-0.546079, 0.274012, 0.791653), 
    cameraTarget=(334.13, -1065.81, 20.6067), viewOffsetX=879.579, 
    viewOffsetY=-23.9432)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1339.07, 
    farPlane=3638.6, width=3773.69, height=1562.19, viewOffsetX=846.4, 
    viewOffsetY=-47.0619)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1357.45, 
    farPlane=3715.91, width=3825.51, height=1583.64, cameraPosition=(2853.94, 
    -1746.56, 1015.67), cameraUpVector=(-0.600339, 0.250543, 0.759487), 
    cameraTarget=(522.678, -1142.19, 103.757), viewOffsetX=858.022, 
    viewOffsetY=-47.7081)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=20)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=30)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1421.38, 
    farPlane=3645.08, width=2763.39, height=1143.96, viewOffsetX=1079.93, 
    viewOffsetY=-21.7489)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1408.42, 
    farPlane=3644.47, width=2738.21, height=1133.53, cameraPosition=(2885.36, 
    -1818, 783.006), cameraUpVector=(-0.531918, 0.232671, 0.814203), 
    cameraTarget=(501.775, -1137.11, 85.4944), viewOffsetX=1070.08, 
    viewOffsetY=-21.5507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1503.35, 
    farPlane=3730.52, width=2922.77, height=1209.94, cameraPosition=(3106.2, 
    -1481.86, 1132.81), cameraUpVector=(-0.584947, 0.269828, 0.764873), 
    cameraTarget=(692.365, -1159.74, 295.412), viewOffsetX=1142.2, 
    viewOffsetY=-23.0032)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1351.94, 
    farPlane=3558.43, width=2628.41, height=1088.08, cameraPosition=(2649.74, 
    -1971.5, 786.919), cameraUpVector=(-0.563824, 0.242867, 0.789378), 
    cameraTarget=(361.264, -1113.34, -24.2727), viewOffsetX=1027.16, 
    viewOffsetY=-20.6864)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=50)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1430.79, 
    farPlane=3497.35, width=2781.71, height=1151.54, cameraPosition=(2504.97, 
    -1761.54, 1401.56), cameraUpVector=(-0.691502, 0.337832, 0.638509), 
    cameraTarget=(379.201, -1113.18, 100.668), viewOffsetX=1087.07, 
    viewOffsetY=-21.8929)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1469.73, 
    farPlane=3458.4, width=2097.08, height=868.126, viewOffsetX=1110.76, 
    viewOffsetY=-47.6403)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1459.97, 
    farPlane=3498.29, width=2083.14, height=862.356, cameraPosition=(2635.51, 
    -1805.89, 1198.3), cameraUpVector=(-0.631632, 0.314824, 0.708468), 
    cameraTarget=(401.93, -1121.71, 114.52), viewOffsetX=1103.38, 
    viewOffsetY=-47.3236)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1480.43, 
    farPlane=3477.82, width=1985.6, height=821.977, viewOffsetX=1115.39, 
    viewOffsetY=-46.0046)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1385.77, 
    farPlane=3391.58, width=1858.64, height=769.42, cameraPosition=(2329.42, 
    -2163.26, 731.702), cameraUpVector=(-0.451094, 0.33811, 0.825952), 
    cameraTarget=(134.251, -980.715, 87.9786), viewOffsetX=1044.07, 
    viewOffsetY=-43.0631)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1463.6, 
    farPlane=3547.87, width=1963.03, height=812.636, cameraPosition=(2815.28, 
    -1757.96, 1054.3), cameraUpVector=(-0.488106, 0.374415, 0.788395), 
    cameraTarget=(426.171, -1101.6, 352.225), viewOffsetX=1102.71, 
    viewOffsetY=-45.4818)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1411.53, 
    farPlane=3460.48, width=1893.2, height=783.726, cameraPosition=(2540.33, 
    -1958.23, 1003.87), cameraUpVector=(-0.48903, 0.380058, 0.785115), 
    cameraTarget=(255.059, -1053.25, 235.663), viewOffsetX=1063.48, 
    viewOffsetY=-43.8638)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1385.19, 
    farPlane=3486.83, width=2379.6, height=985.083, viewOffsetX=1081.61, 
    viewOffsetY=-13.3533)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1332.2, 
    farPlane=2705.99, width=2288.56, height=947.396, cameraPosition=(514.467, 
    -2420.92, 148.185), cameraUpVector=(-0.0241036, 0.338273, 0.940739), 
    cameraTarget=(-589.598, -94.9073, 195.955), viewOffsetX=1040.23, 
    viewOffsetY=-12.8424)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1364.88, 
    farPlane=2686.41, width=2344.7, height=970.637, cameraPosition=(414.273, 
    -2380.89, -378.698), cameraUpVector=(-0.0308689, 0.137983, 0.989954), 
    cameraTarget=(-599.591, -70.0292, 134.682), viewOffsetX=1065.75, 
    viewOffsetY=-13.1574)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1204.36, 
    farPlane=2908.91, width=2068.94, height=856.48, cameraPosition=(1112.74, 
    -2484.49, -121.108), cameraUpVector=(-0.340445, 0.219246, 0.914346), 
    cameraTarget=(-500.945, -482.641, -263.165), viewOffsetX=940.407, 
    viewOffsetY=-11.61)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1216.35, 
    farPlane=2886.31, width=2089.54, height=865.008, cameraPosition=(1115.37, 
    -2479.49, 143.542), cameraUpVector=(-0.375688, 0.308709, 0.873818), 
    cameraTarget=(-491.124, -507.994, -261.327), viewOffsetX=949.771, 
    viewOffsetY=-11.7256)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1237.34, 
    farPlane=2889.28, width=2125.59, height=879.932, cameraPosition=(1086.17, 
    -2486.22, -46.5126), cameraUpVector=(-0.0969723, 0.250983, 0.963122), 
    cameraTarget=(-507.965, -474.343, 159.945), viewOffsetX=966.157, 
    viewOffsetY=-11.9279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1277.74, 
    farPlane=2794.65, width=2195, height=908.665, cameraPosition=(815.737, 
    -2466.83, 171.259), cameraUpVector=(-0.120979, 0.343366, 0.931378), 
    cameraTarget=(-570.397, -297.319, 113.011), viewOffsetX=997.705, 
    viewOffsetY=-12.3174)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1364.84, 
    farPlane=2647.53, width=2344.62, height=970.603, cameraPosition=(397.357, 
    -2400.46, -89.2061), cameraUpVector=(-0.206963, 0.298255, 0.931778), 
    cameraTarget=(-614.945, -33.3934, -150.511), viewOffsetX=1065.71, 
    viewOffsetY=-13.157)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1160.17, 
    farPlane=2952.97, width=1993.03, height=825.056, cameraPosition=(1284.01, 
    -2473.59, -48.0335), cameraUpVector=(-0.356336, 0.218412, 0.908472), 
    cameraTarget=(-471.302, -599.382, -242.268), viewOffsetX=905.901, 
    viewOffsetY=-11.184)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1208.04, 
    farPlane=2893.14, width=2075.27, height=859.099, cameraPosition=(1165.34, 
    -2477.23, -193.67), cameraUpVector=(-0.339516, 0.183459, 0.922535), 
    cameraTarget=(-504.136, -517.905, -267.265), viewOffsetX=943.279, 
    viewOffsetY=-11.6455)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1494.19, 
    farPlane=2409.42, width=2566.84, height=1062.59, cameraPosition=(-159.209, 
    -2128.77, 503.761), cameraUpVector=(-0.0346554, 0.5195, 0.853768), 
    cameraTarget=(-629.36, 348.878, -17.5228), viewOffsetX=1166.71, 
    viewOffsetY=-14.404)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1285.88, 
    farPlane=2675.16, width=2208.99, height=914.456, cameraPosition=(426.154, 
    -2404.4, -54.2172), cameraUpVector=(-0.0918625, 0.265505, 0.959723), 
    cameraTarget=(-659.807, -73.9539, 91.5244), viewOffsetX=1004.06, 
    viewOffsetY=-12.3959)
session.viewports['Viewport: 1'].view.setValues(nearPlane=969.218, 
    farPlane=3116.98, width=1665, height=689.261, cameraPosition=(2277.1, 
    -2102.56, 215.199), cameraUpVector=(-0.459987, 0.115074, 0.880437), 
    cameraTarget=(-100.81, -1192.71, -171.123), viewOffsetX=756.799, 
    viewOffsetY=-9.34327)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1081.18, 
    farPlane=3161.98, width=1857.34, height=768.884, cameraPosition=(3377.65, 
    -741.314, 292.42), cameraUpVector=(-0.4174, -0.0850291, 0.904736), 
    cameraTarget=(951.776, -1568.98, 44.2132), viewOffsetX=844.224, 
    viewOffsetY=-10.4226)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1187.67, 
    farPlane=3135.84, width=2040.28, height=844.615, cameraPosition=(3525.46, 
    -85.9368, 230.664), cameraUpVector=(-0.356865, -0.110152, 0.927639), 
    cameraTarget=(1364.96, -1485.42, 158.664), viewOffsetX=927.376, 
    viewOffsetY=-11.4492)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1193.75, 
    farPlane=3149.14, width=2050.72, height=848.938, cameraPosition=(3543.69, 
    -6.5257, -7.52264), cameraUpVector=(-0.270592, -0.105274, 0.956921), 
    cameraTarget=(1426.59, -1466.12, 130.259), viewOffsetX=932.123, 
    viewOffsetY=-11.5078)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1184.24, 
    farPlane=3148.6, width=2034.38, height=842.173, cameraPosition=(3539.18, 
    -31.7269, 97.6146), cameraUpVector=(-0.311004, -0.154835, 0.937711), 
    cameraTarget=(1408.75, -1478.06, 67.6046), viewOffsetX=924.695, 
    viewOffsetY=-11.4161)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.45, 
    farPlane=3169.96, width=1720.38, height=712.184, cameraPosition=(3178.68, 
    -1165.08, 377.311), cameraUpVector=(-0.442649, 0.0124381, 0.896609), 
    cameraTarget=(653.121, -1580.5, 93.5829), viewOffsetX=781.968, 
    viewOffsetY=-9.65403)
session.viewports['Viewport: 1'].view.setValues(nearPlane=979.488, 
    farPlane=3191.94, width=2172.85, height=899.493, viewOffsetX=1193.52, 
    viewOffsetY=-59.5697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=518.236, 
    farPlane=2663.91, width=1149.63, height=475.912, cameraPosition=(1794.93, 
    -2054.95, 488.954), cameraUpVector=(-0.416633, 0.246632, 0.87498), 
    cameraTarget=(-598.738, -1194.26, 87.5959), viewOffsetX=631.477, 
    viewOffsetY=-31.5177)
session.viewports['Viewport: 1'].view.setValues(nearPlane=519.77, 
    farPlane=2662.38, width=2296.05, height=950.496, viewOffsetX=845.765, 
    viewOffsetY=-64.9148)
session.viewports['Viewport: 1'].view.setValues(nearPlane=291.233, 
    farPlane=2117.54, width=1286.5, height=532.574, cameraPosition=(524.443, 
    -1996.54, 567.714), cameraUpVector=(-0.353337, 0.432804, 0.829357), 
    cameraTarget=(-1283.33, -275.403, -65.6618), viewOffsetX=473.891, 
    viewOffsetY=-36.3725)
session.viewports['Viewport: 1'].view.setValues(nearPlane=309.604, 
    farPlane=2099.18, width=2117.65, height=876.645, viewOffsetX=489.791, 
    viewOffsetY=-32.9122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=267.505, 
    farPlane=2337.67, width=1829.7, height=757.443, cameraPosition=(1688.82, 
    -1800.1, 975.533), cameraUpVector=(-0.648306, 0.278211, 0.70873), 
    cameraTarget=(-648.861, -1510.95, -65.2075), viewOffsetX=423.192, 
    viewOffsetY=-28.4369)
session.viewports['Viewport: 1'].view.setValues(nearPlane=512.031, 
    farPlane=2365.08, width=3502.23, height=1449.82, cameraPosition=(2272.1, 
    -911.769, 1617.9), cameraUpVector=(-0.843177, 0.0878426, 0.530411), 
    cameraTarget=(331.287, -2014.11, 333.536), viewOffsetX=810.031, 
    viewOffsetY=-54.431)
session.viewports['Viewport: 1'].view.setValues(nearPlane=929.53, 
    farPlane=1783.51, width=6357.88, height=2631.97, cameraPosition=(2794.51, 
    -363.881, 1445.01), cameraUpVector=(-0.561251, -0.824673, 0.0700834), 
    cameraTarget=(2503.19, -1405.1, -892.184), viewOffsetX=1470.51, 
    viewOffsetY=-98.8129)
session.viewports['Viewport: 1'].view.setValues(nearPlane=953.468, 
    farPlane=2888.12, width=6521.62, height=2699.75, cameraPosition=(1413.4, 
    -1420.9, 1291.58), cameraUpVector=(-0.903109, -0.280374, -0.325247), 
    cameraTarget=(1180.96, 311.685, 222.414))
session.viewports['Viewport: 1'].view.setValues(nearPlane=519.357, 
    farPlane=3324.3, width=3552.35, height=1470.57, cameraPosition=(2568.76, 
    -996.089, -315.141), cameraUpVector=(-0.61545, -0.757796, 0.216718), 
    cameraTarget=(1103.76, 283.298, 329.78))
session.viewports['Viewport: 1'].view.setValues(nearPlane=995.342, 
    farPlane=3070.71, width=6808.06, height=2818.33, cameraPosition=(2051.38, 
    -1228.02, 1243.41), cameraUpVector=(-0.619572, 0.184589, 0.762927), 
    cameraTarget=(1138.03, 298.662, 226.533))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1189.83, 
    farPlane=2876.24, width=3640.81, height=1507.18, viewOffsetX=-6.13169, 
    viewOffsetY=-153.605)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1131.33, 
    farPlane=3424.9, width=3461.81, height=1433.09, cameraPosition=(2912.52, 
    -536.716, 1021.32), cameraUpVector=(-0.440825, -0.012291, 0.897509), 
    cameraTarget=(1178.84, 247.344, 260.641), viewOffsetX=-5.83023, 
    viewOffsetY=-146.053)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1229.17, 
    farPlane=3327.07, width=2439.05, height=1009.69, viewOffsetX=-94.2646, 
    viewOffsetY=-133.701)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1364.95, 
    farPlane=3006.23, width=2708.5, height=1121.24, cameraPosition=(2410.26, 
    -1511.5, 632.416), cameraUpVector=(-0.216252, 0.13234, 0.967327), 
    cameraTarget=(1248.71, 126.251, 223.008), viewOffsetX=-104.678, 
    viewOffsetY=-148.471)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1399.85, 
    farPlane=2965.89, width=2454.43, height=1016.06, viewOffsetX=-12.8231, 
    viewOffsetY=-1.18115)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1403.84, 
    farPlane=2976.25, width=2461.43, height=1018.96, cameraPosition=(2388.27, 
    -1288.91, 1068.05), cameraUpVector=(-0.345451, 0.284175, 0.894376), 
    cameraTarget=(1419.98, -14.374, 134.318))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1506.13, 
    farPlane=2873.97, width=1342.49, height=555.752, viewOffsetX=-34.7052, 
    viewOffsetY=-45.6593)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1434.92, 
    farPlane=3170.26, width=1279.02, height=529.477, cameraPosition=(2873.33, 
    -860.433, 932.448), cameraUpVector=(-0.266108, 0.277239, 0.923215), 
    cameraTarget=(1490.53, 57.4557, 108.297), viewOffsetX=-33.0645, 
    viewOffsetY=-43.5006)
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3017.71, 
    farPlane=4752.56, width=1911.23, height=756.632, cameraPosition=(-1832.36, 
    670.195, 2679.73), cameraUpVector=(-0.11984, 0.620568, -0.774941), 
    cameraTarget=(978.221, -43.348, -34.8729))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3166.52, 
    farPlane=4582.43, width=2005.48, height=793.942, cameraPosition=(-1012.73, 
    2388.87, 2376.51), cameraUpVector=(0.30129, 0.496781, -0.8139), 
    cameraTarget=(959.874, -81.8198, -28.0855))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3096.95, 
    farPlane=4684.81, width=1961.42, height=776.501, cameraPosition=(-1612.81, 
    -77.6961, 2969.85), cameraUpVector=(-0.0797336, 0.867369, -0.491236), 
    cameraTarget=(974.995, -19.6671, -43.0365))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3562.6, 
    farPlane=4271.21, width=2256.34, height=893.254, cameraPosition=(603.266, 
    -2921.81, 2591.85), cameraUpVector=(-0.325836, 0.850021, 0.413879), 
    cameraTarget=(928.738, 39.6988, -35.1464))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3381.08, 
    farPlane=4468.79, width=2141.37, height=847.742, cameraPosition=(1949.18, 
    -3653.02, 979.94), cameraUpVector=(-0.635229, 0.362072, 0.682193), 
    cameraTarget=(909.771, 50.0031, -12.4313))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3448.12, 
    farPlane=4399.21, width=2183.83, height=864.552, cameraPosition=(1680.27, 
    -3406.17, 1784.61), cameraUpVector=(-0.442075, 0.622886, 0.645432), 
    cameraTarget=(913.003, 47.0368, -22.1008))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].view.setValues(nearPlane=2941.33, 
    farPlane=4866.67, width=1862.87, height=737.485, cameraPosition=(-2162.35, 
    -1627.89, 1792.57), cameraUpVector=(0.423367, 0.670304, 0.60947), 
    cameraTarget=(960.436, 25.0861, -22.1991))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3623.66, 
    farPlane=4199.94, width=2295.02, height=908.569, cameraPosition=(859.026, 
    -3151.95, 2316.43), cameraUpVector=(-0.163932, 0.818886, 0.550047), 
    cameraTarget=(907.735, 51.6693, -31.3364))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2965.06, 
    farPlane=4869.23, width=1877.9, height=743.437, cameraPosition=(3860.73, 
    -2065.14, 1520.98), cameraUpVector=(-0.545115, 0.394454, 0.739767), 
    cameraTarget=(861.472, 34.9191, -19.0767))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3146.33, 
    farPlane=4683.5, width=1992.71, height=788.887, cameraPosition=(3103.66, 
    -3028.65, 1139.21), cameraUpVector=(-0.447803, 0.404336, 0.797487), 
    cameraTarget=(872.092, 48.4353, -13.7211))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2973.52, 
    farPlane=4860.72, width=1883.26, height=745.559, cameraPosition=(3942.65, 
    -2007.15, 1434.41), cameraUpVector=(-0.564652, 0.33323, 0.755067), 
    cameraTarget=(859.838, 33.5149, -18.0329))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3156.49, 
    farPlane=4674.05, width=1999.15, height=791.437, cameraPosition=(3062.47, 
    -2950.63, 1395.31), cameraUpVector=(-0.407307, 0.503305, 0.762092), 
    cameraTarget=(872.193, 46.758, -17.4841))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2954.17, 
    farPlane=4881.09, width=1871.01, height=740.709, cameraPosition=(4062.26, 
    -1642.25, 1628.17), cameraUpVector=(-0.626594, 0.300507, 0.71908), 
    cameraTarget=(857.68, 27.765, -20.8644))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3118.77, 
    farPlane=4713.48, width=1975.26, height=781.979, cameraPosition=(3260.87, 
    -2613.14, 1712.85), cameraUpVector=(-0.479025, 0.526296, 0.70253), 
    cameraTarget=(868.824, 41.266, -22.042))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
#: Warning: The following boundary conditions are applied to empty
#: regions.  These regions may have been invalidated by
#: changes to your model.
#: 
#:     BC3
#: Error in job BP-1: Analysis Input File Processor exited with an error - Please see the  BP-1.dat file for possible error messages if the file exists.
#: Job BP-1 aborted due to errors.
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3323.61, 
    farPlane=5495.96, width=1954.08, height=773.596, cameraPosition=(78.9398, 
    1959.06, 4851.04), cameraUpVector=(-0.237607, 0.660313, -0.712412), 
    cameraTarget=(-34.3857, -51.6213, 986.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3291.44, 
    farPlane=5625.48, width=1935.17, height=766.109, cameraPosition=(-761.084, 
    -256.654, 5286.23), cameraUpVector=(-0.518338, 0.759489, -0.393069), 
    cameraTarget=(-44.2084, -77.5303, 991.096))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3585.96, 
    farPlane=5315.7, width=2108.33, height=834.661, cameraPosition=(-3273.36, 
    1331.71, 3606.97), cameraUpVector=(0.0745681, 0.621396, -0.77994), 
    cameraTarget=(-100.69, -41.8205, 953.343))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3573.15, 
    farPlane=5248.37, width=2100.8, height=831.679, cameraPosition=(-1705.08, 
    3112.04, 3520.55), cameraUpVector=(0.478735, 0.420563, -0.770675), 
    cameraTarget=(-68.0624, -4.78123, 951.545))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3267.79, 
    farPlane=5599.8, width=1921.26, height=760.604, cameraPosition=(-1004.23, 
    710.029, 5160.28), cameraUpVector=(0.191293, 0.868265, -0.457736), 
    cameraTarget=(-59.7156, -33.3879, 971.073))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3542.13, 
    farPlane=5320.62, width=2082.56, height=824.459, cameraPosition=(-2446.34, 
    2340.14, 3760.12), cameraUpVector=(0.585223, 0.610259, -0.533946), 
    cameraTarget=(-84.2926, -5.60684, 947.211))
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3504.74, 
    farPlane=5216.87, width=2178.62, height=862.487, cameraUpVector=(-0.285048, 
    0.515675, -0.807977))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3427.21, 
    farPlane=5401.59, width=2130.43, height=843.408, cameraPosition=(4255.63, 
    -1209.59, 2602.27), cameraUpVector=(-0.069858, 0.997243, -0.025012), 
    cameraTarget=(985.898, -47.254, -38.6443))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3799.56, 
    farPlane=5059.96, width=2361.89, height=935.042, cameraPosition=(2434.03, 
    -3802.09, 1679.78), cameraUpVector=(-0.203648, 0.650063, 0.732083), 
    cameraTarget=(963.781, -78.7315, -49.8449))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3435.17, 
    farPlane=5470.05, width=2135.38, height=845.368, cameraPosition=(4222.23, 
    -2776.07, 1043.74), cameraUpVector=(-0.255086, 0.554235, 0.79231), 
    cameraTarget=(991.617, -62.7599, -59.7459))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3423.42, 
    farPlane=5446.42, width=2128.07, height=842.476, cameraPosition=(4320.07, 
    -2024.55, 1969.75), cameraUpVector=(-0.459006, 0.614922, 0.641236), 
    cameraTarget=(993.634, -47.2651, -40.6534))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].view.setValues(nearPlane=3578.25, 
    farPlane=5227.11, width=2224.32, height=880.577, cameraPosition=(-1482.7, 
    -3478.96, 1268.57), cameraUpVector=(0.0912064, 0.65403, 0.750951), 
    cameraTarget=(896.662, -71.5703, -52.3711))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3588.11, 
    farPlane=5205.95, width=2230.45, height=883.007, cameraPosition=(-1373.24, 
    -3392.5, 1631.95), cameraUpVector=(0.1213, 0.70715, 0.696581), 
    cameraTarget=(897.703, -70.7479, -48.9145))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3763.8, 
    farPlane=5024.83, width=2339.67, height=926.243, cameraPosition=(2392.52, 
    -3165.63, 2658.43), cameraUpVector=(-0.504136, 0.687089, 0.523216), 
    cameraTarget=(928.734, -68.8785, -40.4559))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3359.52, 
    farPlane=5432.66, width=2088.36, height=826.754, cameraPosition=(4329.78, 
    -1801.3, 2079.34), cameraUpVector=(-0.633439, 0.406092, 0.658668), 
    cameraTarget=(943.511, -58.4715, -44.8732))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3339.33, 
    farPlane=5513.27, width=2075.81, height=821.785, cameraPosition=(4657.47, 
    -2308.38, 387.437), cameraUpVector=(-0.330508, 0.280011, 0.901309), 
    cameraTarget=(946.142, -62.5431, -58.4582))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3278.22, 
    farPlane=5512.72, width=2037.83, height=806.748, cameraPosition=(4953.04, 
    -484.535, 1631.71), cameraUpVector=(-0.672403, -0.000697278, 0.740185), 
    cameraTarget=(950.516, -35.5531, -40.045))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
session.viewports['Viewport: 1'].view.setValues(nearPlane=3569.92, 
    farPlane=5266.53, width=2219.16, height=878.536, cameraPosition=(3470.54, 
    -3448.02, 1013.86), cameraUpVector=(-0.527104, 0.285229, 0.800503), 
    cameraTarget=(938.821, -58.931, -44.919))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3482.81, 
    farPlane=5266.61, width=2164.99, height=857.09, cameraPosition=(3777.57, 
    1202.24, 3069.73), cameraUpVector=(-0.400115, 0.807734, -0.432982), 
    cameraTarget=(985.898, -47.2543, -38.6443))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3479.54, 
    farPlane=5271.02, width=2162.96, height=856.287, cameraPosition=(3821.78, 
    1296.64, 2989.3), cameraUpVector=(-0.404311, 0.794128, -0.453755), 
    cameraTarget=(986.039, -46.9543, -38.8999))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].view.setValues(nearPlane=3601.28, 
    farPlane=5226.04, width=2238.64, height=886.248, cameraPosition=(3350.9, 
    -2438.91, 2744.93), cameraUpVector=(-0.0688198, 0.938467, 0.338442), 
    cameraTarget=(984.482, -59.3079, -39.7079))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3284.26, 
    farPlane=5662.49, width=2041.57, height=808.232, cameraPosition=(5302.29, 
    533.469, -593.468), cameraUpVector=(-0.290605, 0.422586, 0.858469), 
    cameraTarget=(1007.85, -23.7149, -79.6838))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3401.91, 
    farPlane=5499.4, width=2114.71, height=837.186, cameraPosition=(4587.09, 
    -1388.67, 2071.39), cameraUpVector=(-0.453665, 0.712289, 0.535568), 
    cameraTarget=(989.853, -72.0832, -12.6259))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3506.3, 
    farPlane=5444.14, width=2179.6, height=862.877, cameraPosition=(4071.08, 
    -2922.36, 1198.5), cameraUpVector=(-0.253902, 0.575856, 0.777125), 
    cameraTarget=(979.436, -103.045, -30.2477))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3322.81, 
    farPlane=5606.14, width=2065.54, height=817.722, cameraPosition=(5008.19, 
    -1288.64, 1182.51), cameraUpVector=(-0.439731, 0.492127, 0.751298), 
    cameraTarget=(1003.39, -61.2769, -30.6565))
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=382.971, 
    farPlane=876.037, width=711.413, height=294.504, viewOffsetX=192.214, 
    viewOffsetY=-8.70085)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=245.591, 
    farPlane=1014.75, width=2169.16, height=897.965, viewOffsetX=711.039, 
    viewOffsetY=40.028)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.7117, 
    farPlane=1950.71, width=182.933, height=75.7289, cameraPosition=(-88.131, 
    -207.423, 135.476), cameraUpVector=(0.361811, 0.059419, 0.930356), 
    cameraTarget=(499.426, -65.1917, 206.727))
session.viewports['Viewport: 1'].view.setValues(nearPlane=849.072, 
    farPlane=1245.15, width=7499.31, height=3104.49, cameraPosition=(640.409, 
    1008.94, 422.304), cameraUpVector=(0.555229, -0.542571, 0.630347), 
    cameraTarget=(635.859, 770.792, 227.206))
session.viewports['Viewport: 1'].view.setValues(nearPlane=542.047, 
    farPlane=1704.21, width=2743.25, height=1135.62, viewOffsetX=162.084, 
    viewOffsetY=-17.4822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199.658, 
    farPlane=1654.41, width=1010.45, height=418.295, cameraPosition=(1396.06, 
    786.049, 96.8263), cameraUpVector=(0.189405, -0.614077, 0.766183), 
    cameraTarget=(946.865, -147.979, -86.0743), viewOffsetX=59.7021, 
    viewOffsetY=-6.43939)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2011.93, 
    farPlane=4023.86, width=3282.11, height=1358.7, cameraPosition=(3405.8, 
    -1242.27, 1146.31), cameraUpVector=(-0.59517, 0.224475, 0.771611), 
    cameraTarget=(540.816, -153.902, 20.3944), viewOffsetX=193.923, 
    viewOffsetY=-20.9162)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2328.4, 
    farPlane=3714.59, width=3798.39, height=1572.42, cameraPosition=(1693.83, 
    -2479.55, 1558.65), cameraUpVector=(-0.484798, 0.601927, 0.634551), 
    cameraTarget=(527.958, 96.9965, -73.0708), viewOffsetX=224.427, 
    viewOffsetY=-24.2063)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2297.07, 
    farPlane=3774.58, width=4799.61, height=1986.89, cameraTarget=(919.849, 
    -99.7731, -33.3506), viewOffsetX=327.283, viewOffsetY=-82.7222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2244.55, 
    farPlane=3896.61, width=4689.87, height=1941.46, cameraPosition=(1936.83, 
    -2660.4, 1127.09), cameraUpVector=(-0.450012, 0.479424, 0.75342), 
    cameraTarget=(931.69, -121.381, -30.4569), viewOffsetX=319.8, 
    viewOffsetY=-80.8308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2225.3, 
    farPlane=3976.15, width=4649.65, height=1924.82, cameraPosition=(2138.59, 
    -2556.91, 1237.59), cameraUpVector=(-0.385779, 0.519171, 0.762651), 
    cameraTarget=(945.437, -127.042, 25.5829), viewOffsetX=317.058, 
    viewOffsetY=-80.1376)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2293.78, 
    farPlane=3776.54, width=4792.75, height=1984.05, cameraPosition=(1675.71, 
    -2848.41, 709.292), cameraUpVector=(0.0249778, 0.475326, 0.879455), 
    cameraTarget=(926.757, -39.8647, 119.389), viewOffsetX=326.815, 
    viewOffsetY=-82.6038)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2106.61, 
    farPlane=4671.72, width=4401.68, height=1822.16, cameraPosition=(4031.02, 
    -682.9, 1128.93), cameraUpVector=(-0.556878, 0.20413, 0.80512), 
    cameraTarget=(1268.41, -313.334, 114.918), viewOffsetX=300.148, 
    viewOffsetY=-75.8636)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2389.21, 
    farPlane=4389.11, width=1448.26, height=599.535, viewOffsetX=297.607, 
    viewOffsetY=-48.8538)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2383.15, 
    farPlane=4428.95, width=1444.58, height=598.013, cameraPosition=(4145.82, 
    -865.722, 613.531), cameraUpVector=(-0.409291, 0.217964, 0.885986), 
    cameraTarget=(1281.22, -333.112, 59.2666), viewOffsetX=296.852, 
    viewOffsetY=-48.7298)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2518.67, 
    farPlane=4061.28, width=1526.73, height=632.019, cameraPosition=(2726.26, 
    -2560.88, 1002.56), cameraUpVector=(-0.359049, 0.431554, 0.827554), 
    cameraTarget=(891.07, -430.475, 59.0216), viewOffsetX=313.732, 
    viewOffsetY=-51.5008)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2432.5, 
    farPlane=4147.45, width=2748.78, height=1137.91, viewOffsetX=349.104, 
    viewOffsetY=-55.5505)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=AUTO)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2311.97, 
    farPlane=4601.04, width=2612.57, height=1081.53, cameraPosition=(4377.98, 
    2.88867, 133.869), cameraUpVector=(-0.319628, -0.0863603, 0.943599), 
    cameraTarget=(1438.03, -343.867, -48.5774), viewOffsetX=331.806, 
    viewOffsetY=-52.798)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2323.29, 
    farPlane=4596, width=2625.38, height=1086.83, cameraPosition=(4383.89, 
    8.09089, 42.8011), cameraUpVector=(-0.29508, -0.104587, 0.949731), 
    cameraTarget=(1441.07, -343.766, -70.5845), viewOffsetX=333.431, 
    viewOffsetY=-53.0566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2300.91, 
    farPlane=4478.57, width=2600.1, height=1076.36, cameraPosition=(3803.03, 
    -1624.59, 760.695), cameraUpVector=(-0.417491, 0.244914, 0.875054), 
    cameraTarget=(1129.14, -530.317, 90.0572), viewOffsetX=330.22, 
    viewOffsetY=-52.5456)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2311.69, 
    farPlane=4580.27, width=2612.29, height=1081.41, cameraPosition=(4371.57, 
    -56.9714, 49.7644), cameraUpVector=(-0.290668, 0.00283276, 0.95682), 
    cameraTarget=(1423.35, -374.974, -11.4478), viewOffsetX=331.768, 
    viewOffsetY=-52.7919)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2927.31, 
    farPlane=3707.21, width=3307.96, height=1369.4, cameraPosition=(695.805, 
    -1470.16, 3002.97), cameraUpVector=(-0.0617938, 0.977158, 0.20333), 
    cameraTarget=(441.177, -122.879, 372.974), viewOffsetX=420.12, 
    viewOffsetY=-66.8508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2419.98, 
    farPlane=4200.77, width=2734.67, height=1132.07, cameraPosition=(2465.05, 
    -1774.74, 2361.64), cameraUpVector=(-0.435007, 0.745318, 0.505242), 
    cameraTarget=(714.406, -398.472, 402.553), viewOffsetX=347.309, 
    viewOffsetY=-55.2649)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2209.1, 
    farPlane=4403.02, width=2496.37, height=1033.42, cameraPosition=(3871.36, 
    387.017, 1473.89), cameraUpVector=(-0.652067, 0.343364, 0.675951), 
    cameraTarget=(1187.93, -302.973, 415.57), viewOffsetX=317.045, 
    viewOffsetY=-50.4492)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2179.83, 
    farPlane=4423.39, width=2463.29, height=1019.73, cameraPosition=(4198.96, 
    -457.535, 192.092), cameraUpVector=(-0.289913, 0.0782469, 0.953849), 
    cameraTarget=(1233.71, -463.992, 127.434), viewOffsetX=312.844, 
    viewOffsetY=-49.7807)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2206.31, 
    farPlane=4402.19, width=2493.22, height=1032.12, cameraPosition=(3996.37, 
    -832.709, 925.581), cameraUpVector=(-0.53614, -0.0879097, 0.839539), 
    cameraTarget=(1165.42, -511.662, 101.225), viewOffsetX=316.645, 
    viewOffsetY=-50.3855)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2365.54, 
    farPlane=4249.82, width=2673.16, height=1106.61, cameraPosition=(3154.48, 
    -1439.33, 1999.34), cameraUpVector=(-0.769736, 0.199364, 0.606433), 
    cameraTarget=(954.145, -539.513, 225.707), viewOffsetX=339.497, 
    viewOffsetY=-54.0218)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2361.86, 
    farPlane=4255.51, width=2669.01, height=1104.89, cameraPosition=(3244.69, 
    -875.173, 2211.94), cameraUpVector=(-0.818789, 0.139408, 0.556911), 
    cameraTarget=(1022.91, -499.518, 283.337), viewOffsetX=338.969, 
    viewOffsetY=-53.9378)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2316.79, 
    farPlane=4295.58, width=2618.08, height=1083.8, cameraPosition=(3179.54, 
    -1797.96, 1648.61), cameraUpVector=(-0.617393, 0.32474, 0.716498), 
    cameraTarget=(899.102, -542.216, 227.477), viewOffsetX=332.5, 
    viewOffsetY=-52.9085)
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=1)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2307.08, 
    farPlane=4277.16, width=2607.11, height=1079.26, cameraPosition=(3096.48, 
    -1773.58, 1782.85), cameraUpVector=(-0.43569, 0.59582, 0.674665), 
    cameraTarget=(848.243, -465.403, 357.707), viewOffsetX=331.107, 
    viewOffsetY=-52.6868)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2222.79, 
    farPlane=4360.48, width=2511.86, height=1039.83, cameraPosition=(3689.73, 
    -743.249, 1675.43), cameraUpVector=(-0.59379, 0.415363, 0.68912), 
    cameraTarget=(1044.32, -438.279, 369.394), viewOffsetX=319.01, 
    viewOffsetY=-50.7619)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2278.82, 
    farPlane=4306.05, width=2575.18, height=1066.05, cameraPosition=(3287.43, 
    -1600.27, 1698.9), cameraUpVector=(-0.464816, 0.54983, 0.693998), 
    cameraTarget=(897.192, -472.046, 353.253), viewOffsetX=327.051, 
    viewOffsetY=-52.0414)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2287.3, 
    farPlane=4317.07, width=2584.77, height=1070.02, cameraPosition=(3269.33, 
    -2337.36, 237.337), cameraUpVector=(-0.37746, 0.0580919, 0.924202), 
    cameraTarget=(885.354, -586.709, 16.5216), viewOffsetX=328.268, 
    viewOffsetY=-52.235)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2175.75, 
    farPlane=4428.2, width=2458.72, height=1017.83, cameraPosition=(4176.36, 
    -265.841, 568.757), cameraUpVector=(-0.412551, -0.0975189, 0.9057), 
    cameraTarget=(1254.3, -456.933, 97.6751), viewOffsetX=312.258, 
    viewOffsetY=-49.6875)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2179.53, 
    farPlane=4422.83, width=2462.99, height=1019.6, cameraPosition=(4215.7, 
    -270.159, 242.816), cameraUpVector=(-0.326311, -0.16854, 0.930116), 
    cameraTarget=(1263.38, -458.583, 30.3072), viewOffsetX=312.801, 
    viewOffsetY=-49.7739)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2191.78, 
    farPlane=4410.25, width=2476.83, height=1025.33, cameraPosition=(4193.4, 
    458.862, 259.488), cameraUpVector=(-0.285279, -0.243128, 0.927095), 
    cameraTarget=(1354.42, -368.196, 29.1901), viewOffsetX=314.559, 
    viewOffsetY=-50.0537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2177.42, 
    farPlane=4422.34, width=2460.6, height=1018.61, cameraPosition=(4230.21, 
    52.1503, -168.717), cameraUpVector=(-0.192187, -0.116984, 0.974361), 
    cameraTarget=(1307.94, -419.861, 16.6693), viewOffsetX=312.498, 
    viewOffsetY=-49.7257)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2179.36, 
    farPlane=4422.98, width=2462.8, height=1019.52, cameraPosition=(4222.79, 
    -66.3258, 283.246), cameraUpVector=(-0.326554, -0.153169, 0.932685), 
    cameraTarget=(1289.08, -435.127, 50.5512), viewOffsetX=312.777, 
    viewOffsetY=-49.7701)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2180.45, 
    farPlane=4421.52, width=2464.04, height=1020.04, cameraPosition=(4225.72, 
    105.516, 230.735), cameraUpVector=(-0.303259, -0.173798, 0.936925), 
    cameraTarget=(1311.8, -414.448, 42.2801), viewOffsetX=312.934, 
    viewOffsetY=-49.7951)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2185.11, 
    farPlane=4418.29, width=2469.31, height=1022.22, cameraPosition=(4193.65, 
    96.0373, 519.533), cameraUpVector=(-0.386266, -0.133098, 0.912734), 
    cameraTarget=(1302.98, -414.834, 95.4344), viewOffsetX=313.602, 
    viewOffsetY=-49.9015)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2178.83, 
    farPlane=4421.84, width=2462.21, height=1019.28, cameraPosition=(4234.6, 
    56.6968, 20.9993), cameraUpVector=(-0.248126, -0.0657933, 0.966491), 
    cameraTarget=(1307, -416.877, 62.2839), viewOffsetX=312.7, 
    viewOffsetY=-49.758)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2331.92, 
    farPlane=4268.75, width=675.505, height=279.639, viewOffsetX=347.132, 
    viewOffsetY=-60.7248)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2337.78, 
    farPlane=4263.88, width=677.202, height=280.341, cameraPosition=(4231.79, 
    156.264, 33.5415), cameraUpVector=(-0.249389, -0.0801272, 0.965083), 
    cameraTarget=(1319.55, -404.91, 60.7177), viewOffsetX=348.004, 
    viewOffsetY=-60.8774)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2325.47, 
    farPlane=4276.18, width=866.339, height=358.638, viewOffsetX=347.25, 
    viewOffsetY=-53.8988)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2321.34, 
    farPlane=4273.81, width=864.8, height=358.001, cameraPosition=(4196.59, 
    -470.886, 125.289), cameraUpVector=(-0.279475, 0.0174186, 0.959995), 
    cameraTarget=(1230.83, -473.325, 92.6447), viewOffsetX=346.634, 
    viewOffsetY=-53.8031)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2259.3, 
    farPlane=4335.86, width=1669.24, height=691.014, viewOffsetX=407.291, 
    viewOffsetY=-43.3822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2252.45, 
    farPlane=4349.47, width=1664.17, height=688.918, cameraPosition=(4212.65, 
    -376.421, 107.87), cameraUpVector=(-0.276321, -0.000758407, 0.961065), 
    cameraTarget=(1248.1, -464.282, 85.2292), viewOffsetX=406.056, 
    viewOffsetY=-43.2506)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3504.74, 
    farPlane=5216.87, width=2178.62, height=862.487, cameraPosition=(3503.61, 
    2470.46, 2479.07), cameraUpVector=(-0.197563, 0.476759, -0.856545), 
    cameraTarget=(985.898, -47.2544, -38.6443))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3253.21, 
    farPlane=5624.61, width=2022.26, height=800.587, cameraPosition=(5276.31, 
    707.249, -237.964), cameraUpVector=(-0.435182, 0.326388, -0.839099), 
    cameraTarget=(985.897, -47.2537, -38.6432))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3298.33, 
    farPlane=5602.82, width=2050.31, height=811.691, cameraPosition=(5186.47, 
    363.894, -1142.91), cameraUpVector=(-0.573191, 0.300996, -0.762137), 
    cameraTarget=(984.316, -53.2949, -54.5653))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3274.66, 
    farPlane=5599.51, width=2035.6, height=805.867, cameraPosition=(5172.48, 
    1045.66, -587.292), cameraUpVector=(-0.483414, 0.089863, -0.870767), 
    cameraTarget=(984.034, -39.5437, -43.3584))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3321.06, 
    farPlane=5586.68, width=2064.44, height=817.286, cameraPosition=(5093.71, 
    272.539, -1476.45), cameraUpVector=(-0.619262, -0.055935, -0.78319), 
    cameraTarget=(982.68, -52.8349, -58.6443))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3312.2, 
    farPlane=5554.54, width=2058.94, height=815.106, cameraPosition=(4901.44, 
    1605.94, -1033.55), cameraUpVector=(-0.486106, -0.230702, -0.842898), 
    cameraTarget=(978.662, -24.972, -49.3894))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3324.73, 
    farPlane=5562.36, width=2066.73, height=818.191, cameraPosition=(4931.3, 
    1066.8, -1536.07), cameraUpVector=(-0.55588, -0.342238, -0.757543), 
    cameraTarget=(979.151, -33.7971, -57.615))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3418.51, 
    farPlane=5424.74, width=2125.03, height=841.27, cameraPosition=(-2452.84, 
    2354.44, -1664.1), cameraUpVector=(0.569219, -0.331977, -0.752184), 
    cameraTarget=(841.661, -9.82178, -59.9989))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3393.46, 
    farPlane=5428.52, width=2109.46, height=835.106, cameraPosition=(-2492.61, 
    2704.08, -798.906), cameraUpVector=(0.408019, -0.27568, -0.870357), 
    cameraTarget=(841.114, -5.01245, -48.0981))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3385.8, 
    farPlane=5365.65, width=2104.7, height=833.222, cameraPosition=(4121.83, 
    2919.61, -494.641), cameraUpVector=(-0.211527, -0.402556, -0.890621), 
    cameraTarget=(916.367, -2.56036, -44.6365))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3208.24, 
    farPlane=5561.57, width=1994.33, height=789.528, cameraPosition=(5255.9, 
    157.582, -480.238), cameraUpVector=(-0.421156, -0.115185, -0.899644), 
    cameraTarget=(920.234, -11.9787, -44.5874))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3214.21, 
    farPlane=5552.43, width=1998.04, height=790.999, cameraPosition=(5268.77, 
    165.186, -319.372), cameraUpVector=(-0.387985, -0.106312, -0.915514), 
    cameraTarget=(920.305, -11.9369, -43.703))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3317.89, 
    farPlane=5445.09, width=2062.49, height=853.808, cameraPosition=(4546.95, 
    2311.56, -745.548), cameraUpVector=(-0.292631, -0.427913, -0.855136), 
    cameraTarget=(916.596, -0.906647, -45.8931))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3230.56, 
    farPlane=5533.95, width=2008.2, height=831.335, cameraPosition=(5025.55, 
    1365.27, -567.411), cameraUpVector=(-0.392124, -0.225524, -0.891839), 
    cameraTarget=(918.857, -5.3772, -45.0515))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3506.19, 
    farPlane=5287.85, width=2179.54, height=902.264, cameraPosition=(3695.92, 
    2443.12, -2355.73), cameraUpVector=(-0.484495, -0.622262, -0.614862), 
    cameraTarget=(912.344, -0.0977173, -53.8108))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3243.82, 
    farPlane=5522.42, width=2016.45, height=834.747, cameraPosition=(4891.98, 
    1726.35, -545.115), cameraUpVector=(-0.363486, -0.266949, -0.892533), 
    cameraTarget=(922.199, -6.00381, -38.8916))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3220.17, 
    farPlane=5551.82, width=2001.75, height=828.663, cameraPosition=(5156.43, 
    909.11, -543.003), cameraUpVector=(-0.418389, -0.146307, -0.896407), 
    cameraTarget=(923.547, -10.1688, -38.8808))
#: Job BP-1 completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=3214.8, 
    farPlane=5555.73, width=1998.41, height=827.282, cameraPosition=(5276.27, 
    230.747, -164.646), cameraUpVector=(-0.358853, -0.0454452, -0.932287), 
    cameraTarget=(924.236, -14.0675, -36.7063))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3227.11, 
    farPlane=5538.51, width=2006.06, height=830.45, cameraPosition=(5096.38, 
    1230.73, -293.718), cameraUpVector=(-0.345981, -0.19757, -0.917204), 
    cameraTarget=(923.232, -8.48636, -37.4267))
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/BP-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=351.909, 
    farPlane=907.1, width=1085.63, height=449.418, viewOffsetX=161.419, 
    viewOffsetY=1.42178)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1983.59, 
    farPlane=3967.18, width=1199.55, height=496.577, cameraPosition=(3605.47, 
    -1188.7, 557.65), cameraUpVector=(-0.484899, 0.0790625, 0.87099), 
    cameraTarget=(332.257, -311.206, -28.1317), viewOffsetX=178.357, 
    viewOffsetY=1.57098)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1890.21, 
    farPlane=4065.64, width=2411.66, height=998.355, viewOffsetX=323.532, 
    viewOffsetY=-13.8934)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2341.62, 
    farPlane=3977.33, width=2987.59, height=1236.77, cameraPosition=(2535.93, 
    -2612.7, 737.762), cameraUpVector=(-0.343665, 0.416548, 0.841654), 
    cameraTarget=(1051.87, -612.639, 78.3881))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2365.31, 
    farPlane=3959.72, width=2677.45, height=1108.38, viewOffsetX=445.185, 
    viewOffsetY=-19.238)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2310.01, 
    farPlane=4329.27, width=2614.85, height=1082.47, cameraPosition=(3463.45, 
    -1952.2, 830.009), cameraUpVector=(-0.410021, 0.36403, 0.83628), 
    cameraTarget=(1147.39, -381.551, -20.4125), viewOffsetX=434.776, 
    viewOffsetY=-18.7882)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2317.7, 
    farPlane=4309.02, width=2623.55, height=1086.07, cameraPosition=(3361.32, 
    -1800.04, 1276.74), cameraUpVector=(-0.425869, 0.507548, 0.74902), 
    cameraTarget=(1120.44, -338.995, 94.3111), viewOffsetX=436.223, 
    viewOffsetY=-18.8507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2384.55, 
    farPlane=4242.18, width=1750.38, height=724.606, viewOffsetX=393.428, 
    viewOffsetY=-18.4592)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=ALL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2388.01, 
    farPlane=4273.34, width=1752.92, height=725.657, cameraPosition=(3476.93, 
    -1952.18, 795.742), cameraUpVector=(-0.406363, 0.350692, 0.843733), 
    cameraTarget=(1148.83, -380.22, -18.6379), viewOffsetX=393.999, 
    viewOffsetY=-18.486)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2397.84, 
    farPlane=4424.63, width=1760.14, height=728.643, cameraPosition=(3913.97, 
    -1307.52, 908.669), cameraUpVector=(-0.454198, 0.342961, 0.822242), 
    cameraTarget=(1291.43, -344.11, 43.5293), viewOffsetX=395.62, 
    viewOffsetY=-18.5621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2379.18, 
    farPlane=4443.29, width=1857.92, height=769.122, viewOffsetX=325.015, 
    viewOffsetY=3.14227)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2412.57, 
    farPlane=4319.91, width=1883.99, height=779.917, cameraPosition=(3555.65, 
    -1373.52, 1528.96), cameraUpVector=(-0.567555, 0.437327, 0.697586), 
    cameraTarget=(1205.91, -337.428, 129.114), viewOffsetX=329.577, 
    viewOffsetY=3.18638)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2430.46, 
    farPlane=4172.31, width=1897.96, height=785.7, cameraPosition=(3069.38, 
    -2310.57, 917.659), cameraUpVector=(-0.401037, 0.400834, 0.823712), 
    cameraTarget=(1055.19, -402.493, -7.88322), viewOffsetX=332.021, 
    viewOffsetY=3.21001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2413.96, 
    farPlane=4218.32, width=1885.08, height=780.367, cameraPosition=(3215.21, 
    -2137.77, 1023.85), cameraUpVector=(-0.433023, 0.404974, 0.805287), 
    cameraTarget=(1090.94, -399.614, 13.5797), viewOffsetX=329.767, 
    viewOffsetY=3.18822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2385.61, 
    farPlane=4338.86, width=1862.94, height=771.201, cameraPosition=(3600.8, 
    -1846.99, 772.963), cameraUpVector=(-0.418504, 0.319131, 0.8503), 
    cameraTarget=(1182.9, -398.418, -7.90752), viewOffsetX=325.894, 
    viewOffsetY=3.15077)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2456.12, 
    farPlane=4266.52, width=1918, height=793.995, cameraPosition=(3561.29, 
    -484.122, 2037.94), cameraUpVector=(-0.782743, 0.283009, 0.554274), 
    cameraTarget=(1299.11, -271.206, 196.324), viewOffsetX=335.526, 
    viewOffsetY=3.2439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2397.91, 
    farPlane=4196.23, width=1872.54, height=775.176, cameraPosition=(3228.41, 
    -1605.31, 1732.78), cameraUpVector=(-0.54431, 0.537395, 0.644153), 
    cameraTarget=(1110.29, -350.403, 153.822), viewOffsetX=327.574, 
    viewOffsetY=3.16702)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2384.05, 
    farPlane=4511.24, width=1861.72, height=770.696, cameraPosition=(4281.02, 
    -640.404, 459.138), cameraUpVector=(-0.488356, -0.17519, 0.854878), 
    cameraTarget=(1439.24, -310.376, -148.88), viewOffsetX=325.681, 
    viewOffsetY=3.14872)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2707.85, 
    farPlane=4392.48, width=2114.58, height=875.372, cameraPosition=(3532.19, 
    2088.27, 1250.54), cameraUpVector=(-0.456051, -0.453077, 0.765989), 
    cameraTarget=(1632.09, 207.508, 64.5246), viewOffsetX=369.915, 
    viewOffsetY=3.57638)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2379.11, 
    farPlane=4481.23, width=1857.86, height=769.1, cameraPosition=(3947.28, 
    -1466.27, 733.447), cameraUpVector=(-0.5172, 0.112553, 0.848431), 
    cameraTarget=(1296.45, -513.673, -53.9221), viewOffsetX=325.006, 
    viewOffsetY=3.1422)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2420.29, 
    farPlane=4377.82, width=1890.02, height=782.413, cameraPosition=(3795.06, 
    -957.185, 1577.02), cameraUpVector=(-0.68898, 0.209459, 0.693854), 
    cameraTarget=(1308.87, -449.291, 122.651), viewOffsetX=330.632, 
    viewOffsetY=3.19659)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2428.64, 
    farPlane=4330.43, width=1896.55, height=785.113, cameraPosition=(3512.45, 
    -1678.35, 1415), cameraUpVector=(-0.635487, 0.271742, 0.722712), 
    cameraTarget=(1191.67, -523.002, 60.9566), viewOffsetX=331.773, 
    viewOffsetY=3.20762)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2417.1, 
    farPlane=4398.53, width=1887.54, height=781.385, cameraPosition=(3882.98, 
    -746.123, 1545.27), cameraUpVector=(-0.679488, 0.212989, 0.702091), 
    cameraTarget=(1338.19, -426.666, 139.47), viewOffsetX=330.197, 
    viewOffsetY=3.19238)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2459.64, 
    farPlane=4461.76, width=1920.76, height=795.136, cameraPosition=(4090.75, 
    796.082, 1192.36), cameraUpVector=(-0.617046, -0.114828, 0.778504), 
    cameraTarget=(1569.38, -193.314, 88.6908), viewOffsetX=336.008, 
    viewOffsetY=3.24856)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2417.65, 
    farPlane=4497.35, width=1887.97, height=781.561, cameraPosition=(4246.62, 
    127.338, 1002.77), cameraUpVector=(-0.576032, -0.131675, 0.806752), 
    cameraTarget=(1535.16, -313.912, -1.00347), viewOffsetX=330.271, 
    viewOffsetY=3.1931)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2405.08, 
    farPlane=4428.48, width=1878.15, height=777.498, cameraPosition=(3896.19, 
    -1309.26, 1118.43), cameraUpVector=(-0.638266, 0.0510078, 0.768124), 
    cameraTarget=(1318.4, -527.207, -20.729), viewOffsetX=328.553, 
    viewOffsetY=3.17649)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2445.77, 
    farPlane=4329.63, width=1909.93, height=790.653, cameraPosition=(3687.23, 
    -740.065, 1852.69), cameraUpVector=(-0.758714, 0.191017, 0.622788), 
    cameraTarget=(1311.44, -452.854, 171.191), viewOffsetX=334.112, 
    viewOffsetY=3.23024)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2410.93, 
    farPlane=4417.12, width=1882.72, height=779.391, cameraPosition=(3923.64, 
    -791.356, 1460.15), cameraUpVector=(-0.655001, 0.222185, 0.722224), 
    cameraTarget=(1338.15, -457.176, 134.298), viewOffsetX=329.353, 
    viewOffsetY=3.18423)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2410.12, 
    farPlane=4542.2, width=1882.09, height=779.128, cameraPosition=(4336.29, 
    -529.578, 451.805), cameraUpVector=(-0.426777, 0.0983549, 0.898993), 
    cameraTarget=(1452.76, -427.907, -26.9929), viewOffsetX=329.242, 
    viewOffsetY=3.18316)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2427.02, 
    farPlane=4572.31, width=1895.29, height=784.591, cameraPosition=(4419.95, 
    79.9239, 223.423), cameraUpVector=(-0.377419, 0.0538029, 0.924478), 
    cameraTarget=(1536.94, -327.43, -53.4856), viewOffsetX=331.551, 
    viewOffsetY=3.20548)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2453.14, 
    farPlane=4601.24, width=1915.69, height=793.037, cameraPosition=(4435.33, 
    62.3058, -345.234), cameraUpVector=(-0.223789, 0.0159101, 0.974508), 
    cameraTarget=(1542.4, -331.67, -171.759), viewOffsetX=335.119, 
    viewOffsetY=3.23998)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2406.37, 
    farPlane=4466.89, width=1879.17, height=777.919, cameraPosition=(4084.77, 
    -698.351, 1196.35), cameraUpVector=(-0.610152, 0.112491, 0.784258), 
    cameraTarget=(1385.32, -462.925, 95.4782), viewOffsetX=328.73, 
    viewOffsetY=3.17821)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2433.04, 
    farPlane=4387.29, width=1900, height=786.542, cameraPosition=(3773.91, 
    -940.38, 1657.42), cameraUpVector=(-0.690019, 0.236079, 0.684208), 
    cameraTarget=(1289.85, -489.4, 180.792), viewOffsetX=332.374, 
    viewOffsetY=3.21344)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2409.46, 
    farPlane=4460.96, width=1881.59, height=778.921, cameraPosition=(4079.06, 
    -646.935, 1236.24), cameraUpVector=(-0.617236, 0.120551, 0.777488), 
    cameraTarget=(1386.08, -457.192, 110.975), viewOffsetX=329.153, 
    viewOffsetY=3.1823)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2457.46, 
    farPlane=4348.01, width=1919.08, height=794.439, cameraPosition=(3438.43, 
    -1849.12, 1404.08), cameraUpVector=(-0.604178, 0.305677, 0.735888), 
    cameraTarget=(1142.98, -592.057, 98.2869), viewOffsetX=335.71, 
    viewOffsetY=3.2457)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2455.12, 
    farPlane=4350.35, width=1802.22, height=746.065, viewOffsetX=591.528, 
    viewOffsetY=-52.4051)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2542.83, 
    farPlane=4624.57, width=1866.6, height=772.718, cameraPosition=(4282.85, 
    -804.301, 1011.76), cameraUpVector=(-0.541326, 0.148579, 0.827581), 
    cameraTarget=(1509.46, -523.821, 126.305), viewOffsetX=612.66, 
    viewOffsetY=-54.2773)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2507.01, 
    farPlane=4501.79, width=1840.31, height=761.833, cameraPosition=(3926.37, 
    -1108.72, 1482.09), cameraUpVector=(-0.658044, 0.172669, 0.732914), 
    cameraTarget=(1370.38, -570.998, 165.966), viewOffsetX=604.03, 
    viewOffsetY=-53.5127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2587, 
    farPlane=4587.44, width=1899.03, height=786.139, cameraPosition=(4143.48, 
    -340.725, 1588.74), cameraUpVector=(-0.667443, 0.193667, 0.719036), 
    cameraTarget=(1517.48, -440.145, 304.729), viewOffsetX=623.302, 
    viewOffsetY=-55.22)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2581.73, 
    farPlane=4592.71, width=2016.13, height=834.616, viewOffsetX=410.618, 
    viewOffsetY=-58.2501)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2551.96, 
    farPlane=4587.52, width=1992.88, height=824.992, cameraPosition=(3947.19, 
    -1176.96, 1530.78), cameraUpVector=(-0.583136, 0.352045, 0.732132), 
    cameraTarget=(1369.73, -565.961, 290.694), viewOffsetX=405.883, 
    viewOffsetY=-57.5784)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2550.22, 
    farPlane=4605.79, width=1991.52, height=824.431, cameraPosition=(3954.06, 
    -1477.51, 1247.34), cameraUpVector=(-0.520962, 0.319562, 0.791504), 
    cameraTarget=(1354.93, -621.606, 214.669), viewOffsetX=405.607, 
    viewOffsetY=-57.5392)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2548.44, 
    farPlane=4647.51, width=1990.13, height=823.856, cameraPosition=(4210.35, 
    -974.445, 1148.51), cameraUpVector=(-0.557899, 0.181136, 0.8099), 
    cameraTarget=(1482.4, -562.187, 177.533), viewOffsetX=405.324, 
    viewOffsetY=-57.499)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2538.25, 
    farPlane=4657.7, width=1990.29, height=823.92, viewOffsetX=555.782, 
    viewOffsetY=-48.2413)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2613.32, 
    farPlane=4652.08, width=2049.15, height=848.286, cameraPosition=(4244.58, 
    -274.784, 1501.51), cameraUpVector=(-0.664864, 0.0700557, 0.743672), 
    cameraTarget=(1607.03, -444.367, 248.9), viewOffsetX=572.218, 
    viewOffsetY=-49.668)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2556.87, 
    farPlane=4637.01, width=2004.88, height=829.961, cameraPosition=(4181.18, 
    -837.972, 1329.86), cameraUpVector=(-0.60767, 0.165353, 0.776786), 
    cameraTarget=(1495.42, -544.939, 209.465), viewOffsetX=559.857, 
    viewOffsetY=-48.5951)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2515.15, 
    farPlane=4565.63, width=1972.17, height=816.418, cameraPosition=(3901.05, 
    -1500.12, 1249.68), cameraUpVector=(-0.546784, 0.274125, 0.791127), 
    cameraTarget=(1317.47, -633.054, 187.721), viewOffsetX=550.722, 
    viewOffsetY=-47.8022)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2529.89, 
    farPlane=4467.47, width=1983.73, height=821.203, cameraPosition=(3464.56, 
    -2208.82, 972.245), cameraUpVector=(-0.443166, 0.324946, 0.835472), 
    cameraTarget=(1114.99, -696.742, 107.595), viewOffsetX=553.949, 
    viewOffsetY=-48.0823)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2526.46, 
    farPlane=4556.14, width=1981.04, height=820.09, cameraPosition=(3797.26, 
    -1723.92, 1152.12), cameraUpVector=(-0.502968, 0.306042, 0.808308), 
    cameraTarget=(1255, -661.975, 170.474), viewOffsetX=553.197, 
    viewOffsetY=-48.017)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2515.08, 
    farPlane=4603.97, width=1972.12, height=816.398, cameraPosition=(4038.22, 
    -1463.04, 983.169), cameraUpVector=(-0.491404, 0.240941, 0.836941), 
    cameraTarget=(1359.1, -644.448, 142.536), viewOffsetX=550.706, 
    viewOffsetY=-47.8008)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3504.74, 
    farPlane=5216.87, width=2178.62, height=862.487, cameraPosition=(3503.61, 
    2470.46, 2479.07), cameraUpVector=(-0.375754, 0.546692, -0.748289), 
    cameraTarget=(985.898, -47.2544, -38.6443))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3261.72, 
    farPlane=5635.23, width=2027.55, height=802.682, cameraPosition=(5334.8, 
    -340.65, 94.0789), cameraUpVector=(-0.269651, 0.626756, -0.731071), 
    cameraTarget=(985.897, -47.2534, -38.6434))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3275.16, 
    farPlane=5607.16, width=2035.91, height=805.989, cameraPosition=(5207.22, 
    988.733, -444.444), cameraUpVector=(-0.474958, 0.213034, -0.853833), 
    cameraTarget=(983.383, -21.0553, -49.2561))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3294.68, 
    farPlane=5616.2, width=2048.04, height=810.793, cameraPosition=(5267.66, 
    -152.448, -868.527), cameraUpVector=(-0.494148, 0.205194, -0.844815), 
    cameraTarget=(984.477, -41.7022, -56.9288))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3385.24, 
    farPlane=5525.62, width=941.406, height=372.69, viewOffsetX=-46.1542, 
    viewOffsetY=-116.037)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3388.93, 
    farPlane=5534.01, width=942.433, height=373.097, cameraPosition=(5305.91, 
    -240.791, -661.389), cameraUpVector=(-0.445562, 0.254953, -0.85818), 
    cameraTarget=(992.346, -36.141, -54.8303), viewOffsetX=-46.2045, 
    viewOffsetY=-116.163)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3402.27, 
    farPlane=5557.21, width=946.144, height=374.566, cameraPosition=(5375.85, 
    190.457, 51.5968), cameraUpVector=(-0.321331, 0.123742, -0.938847), 
    cameraTarget=(1022.21, -43.1561, -37.3938), viewOffsetX=-46.3864, 
    viewOffsetY=-116.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3379.25, 
    farPlane=5580.24, width=1280.47, height=506.922, viewOffsetX=1.29814, 
    viewOffsetY=-101.859)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3359.43, 
    farPlane=5575.75, width=1272.96, height=503.948, cameraPosition=(5335.43, 
    403.922, -358.684), cameraUpVector=(-0.40324, 0.0172285, -0.914932), 
    cameraTarget=(1009.35, -49.9814, -49.3424), viewOffsetX=1.29053, 
    viewOffsetY=-101.262)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3409.99, 
    farPlane=5525.19, width=656.874, height=260.048, viewOffsetX=64.2705, 
    viewOffsetY=-114.39)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3436.22, 
    farPlane=5534.75, width=661.927, height=262.048, cameraPosition=(5341.49, 
    -262.57, -573.871), cameraUpVector=(-0.440709, 0.0579554, -0.895777), 
    cameraTarget=(1015.97, -66.8923, -55.8497), viewOffsetX=64.7648, 
    viewOffsetY=-115.27)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
#* Feature creation failed.
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 116, in <module>
#*     boxpro(modelname='BP-1', L=1800, b=200, h=75, t=0.5, n_spars=4, 
#* esize=20, disp=1)
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 39, in boxpro
#*     prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3253.25, 
    farPlane=5611.38, width=1912.71, height=757.218, cameraPosition=(439.618, 
    530.305, 5279.12), cameraUpVector=(-0.278031, 0.861688, -0.424492), 
    cameraTarget=(-34.3858, -51.6212, 986.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3371.3, 
    farPlane=5493.33, width=736.504, height=291.572, viewOffsetX=28.1598, 
    viewOffsetY=-44.7834)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3375.9, 
    farPlane=5488.86, width=737.51, height=291.97, cameraPosition=(257.194, 
    516.651, 5295.29), cameraUpVector=(-0.251363, 0.865219, -0.433836), 
    cameraTarget=(-36.9089, -51.3757, 984.255), viewOffsetX=28.1982, 
    viewOffsetY=-44.8446)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
#* Feature creation failed.
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 116, in <module>
#*     boxpro(modelname='BP-1', L=1800, b=200, h=75, t=0.5, n_spars=4, 
#* esize=20, disp=1)
#* File "C:/Users/hakon/Skrivebord/Skole/Lettvekt 
#* Design/A4/scripts/script1.py", line 39, in boxpro
#*     prt.PartitionFaceByDatumPlane(datumPlane=prt.datums[id], faces=prt.faces)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-1" has been created.
p = mdb.models['BP-1'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3331.39, 
    farPlane=5463.35, width=1958.65, height=775.406, cameraPosition=(1019.25, 
    2053.05, 4654.02), cameraUpVector=(-0.575013, 0.588373, -0.568487), 
    cameraTarget=(-34.3858, -51.6213, 986.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3291.29, 
    farPlane=5549.24, width=1935.08, height=766.072, cameraPosition=(413.158, 
    1334.01, 5094.96), cameraUpVector=(-0.441716, 0.71154, -0.546441), 
    cameraTarget=(-39.7811, -58.022, 989.932))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3364.4, 
    farPlane=5476.14, width=1065.41, height=421.784, viewOffsetX=-74.6895, 
    viewOffsetY=-68.3331)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3374.18, 
    farPlane=5524.77, width=1068.51, height=423.01, cameraPosition=(224.52, 
    825.095, 5267.56), cameraUpVector=(-0.303544, 0.814601, -0.494254), 
    cameraTarget=(-25.5233, -68.4107, 1009.24), viewOffsetX=-74.9067, 
    viewOffsetY=-68.5318)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3507.63, 
    farPlane=5441.29, width=1110.77, height=439.74, cameraPosition=(-2224.57, 
    1294.75, 4561.18), cameraUpVector=(-0.115796, 0.670845, -0.732501), 
    cameraTarget=(-88.0236, -50.0244, 1008.58), viewOffsetX=-77.8692, 
    viewOffsetY=-71.2422)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3423.15, 
    farPlane=5525.77, width=2158.63, height=854.572, viewOffsetX=75.3712, 
    viewOffsetY=-117.456)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3412.93, 
    farPlane=5535.99, width=2152.18, height=852.02, cameraPosition=(-2161.1, 
    1360.41, 4574.5), cameraUpVector=(0.2982, 0.793795, -0.530063), 
    cameraTarget=(-24.5532, 15.6309, 1021.9), viewOffsetX=75.1461, 
    viewOffsetY=-117.105)
a = mdb.models['BP-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3518.61, 
    farPlane=5223.02, width=2187.24, height=865.9, cameraPosition=(3606.37, 
    1101.08, 3252.42), cameraUpVector=(-0.549922, 0.787396, -0.278555), 
    cameraTarget=(985.898, -47.2543, -38.6444))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3399.3, 
    farPlane=5449.23, width=2113.08, height=836.54, cameraPosition=(4412.25, 
    -1405.42, 2295.91), cameraUpVector=(-0.668287, 0.430662, 0.606566), 
    cameraTarget=(987.743, -52.9935, -40.8345))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3554.5, 
    farPlane=5276.23, width=2209.55, height=874.733, cameraPosition=(3606.25, 
    -2152.88, 2746.79), cameraUpVector=(-0.557151, 0.661917, 0.501446), 
    cameraTarget=(976.182, -63.7144, -34.3676))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3528.99, 
    farPlane=5276.17, width=2193.69, height=868.455, cameraPosition=(3711.11, 
    -1263.24, 3145.24), cameraUpVector=(-0.51192, 0.808207, 0.291101), 
    cameraTarget=(977.478, -52.7228, -29.4448))
