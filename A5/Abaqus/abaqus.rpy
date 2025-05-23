# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Wed Apr 30 10:05:59 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=223.052093505859, 
    height=199.851852416992)
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
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Scripts/script.py', 
    __main__.__dict__)
#: The model "A4" has been created.
#: The interaction property "Contact-properties" has been created.
#: The interaction "ContactBolt-1" has been created.
p = mdb.models['A4'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1994.71, 
    farPlane=2854.83, width=1178.2, height=483.944, cameraPosition=(1894.6, 
    384.793, 1955.99), cameraUpVector=(-0.768185, 0.640226, -0.00154388), 
    cameraTarget=(547.7, 23.7128, -21.4124))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2026.83, 
    farPlane=2888.46, width=1197.18, height=491.738, cameraPosition=(1800.64, 
    -1792.35, 977.974), cameraUpVector=(-0.379838, 0.580613, 0.720147), 
    cameraTarget=(547.501, 19.106, -23.4819))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2092.86, 
    farPlane=2822.43, width=337.107, height=138.466, viewOffsetX=-252.498, 
    viewOffsetY=95.1998)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2282.41, 
    farPlane=2771.87, width=367.639, height=151.007, cameraPosition=(1275.49, 
    -2074.3, 1129.67), cameraUpVector=(-0.29992, 0.671457, 0.677639), 
    cameraTarget=(569.59, -52.2109, 3.8384), viewOffsetX=-275.367, 
    viewOffsetY=103.822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2191.17, 
    farPlane=2863.11, width=1388.15, height=570.181, viewOffsetX=74.9896, 
    viewOffsetY=99.9708)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2197.52, 
    farPlane=2856.76, width=1392.18, height=571.835, cameraPosition=(1273.62, 
    -2074.37, 1130.72), cameraUpVector=(-0.286841, 0.676424, 0.67836), 
    cameraTarget=(567.723, -52.2795, 4.88573), viewOffsetX=75.2071, 
    viewOffsetY=100.261)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2179.07, 
    farPlane=2897.43, width=1380.49, height=567.033, cameraPosition=(1443.33, 
    -1960.07, 1232.57), cameraUpVector=(-0.468102, 0.621206, 0.628477), 
    cameraTarget=(600.192, -53.8308, 3.74164), viewOffsetX=74.5755, 
    viewOffsetY=99.419)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2037.25, 
    farPlane=3113.52, width=1290.64, height=530.13, cameraPosition=(2327.42, 
    -1531.14, 892.703), cameraUpVector=(-0.416896, 0.517153, 0.747496), 
    cameraTarget=(636.053, -47.6795, 2.05861), viewOffsetX=69.722, 
    viewOffsetY=92.9486)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2092.1, 
    farPlane=3028.05, width=1325.39, height=544.403, cameraPosition=(1998.48, 
    -1762.05, 1014.43), cameraUpVector=(-0.415719, 0.559441, 0.71708), 
    cameraTarget=(612.975, -54.9266, 4.12466), viewOffsetX=71.5992, 
    viewOffsetY=95.4511)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1998.96, 
    farPlane=3149.85, width=1266.39, height=520.165, cameraPosition=(2557.38, 
    -1448.23, 397.072), cameraUpVector=(-0.456926, 0.224654, 0.860668), 
    cameraTarget=(656.805, -18.4336, -48.0294), viewOffsetX=68.4115, 
    viewOffsetY=91.2014)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2046.36, 
    farPlane=3119.83, width=1296.42, height=532.502, cameraPosition=(2379.98, 
    -1413.69, 999.932), cameraUpVector=(-0.493635, 0.486024, 0.721183), 
    cameraTarget=(648.144, -44.2505, 9.98885), viewOffsetX=70.0337, 
    viewOffsetY=93.364)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2039.66, 
    farPlane=3123.02, width=1292.18, height=530.758, cameraPosition=(2392.53, 
    -1436.4, 936.307), cameraUpVector=(-0.485586, 0.465974, 0.739645), 
    cameraTarget=(647.923, -43.1604, 3.66141), viewOffsetX=69.8044, 
    viewOffsetY=93.0583)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2039.88, 
    farPlane=3122.8, width=1292.32, height=530.817, cameraPosition=(2371.45, 
    -1448.07, 958.309), cameraUpVector=(-0.346194, 0.617935, 0.705908), 
    cameraTarget=(626.843, -54.8291, 25.6631), viewOffsetX=69.8118, 
    viewOffsetY=93.0682)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2172.91, 
    farPlane=2925.77, width=1376.6, height=565.434, cameraPosition=(1509.12, 
    -1911.56, 1278.29), cameraUpVector=(-0.198078, 0.754001, 0.626297), 
    cameraTarget=(548.964, -66.8104, 41.5153), viewOffsetX=74.3644, 
    viewOffsetY=99.1375)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2227.96, 
    farPlane=2874.95, width=1411.48, height=579.761, cameraPosition=(1227.22, 
    -1819.68, 1576.75), cameraUpVector=(-0.161935, 0.840905, 0.516388), 
    cameraTarget=(531.345, -64.9848, 63.0141), viewOffsetX=76.2485, 
    viewOffsetY=101.649)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2229.77, 
    farPlane=2888.63, width=1412.62, height=580.232, cameraPosition=(1249.93, 
    -1691.97, 1718.55), cameraUpVector=(-0.174301, 0.874805, 0.452034), 
    cameraTarget=(533.919, -64.6006, 77.3329), viewOffsetX=76.3103, 
    viewOffsetY=101.731)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2184.85, 
    farPlane=2863.4, width=1384.16, height=568.542, cameraPosition=(1276.65, 
    -2205.02, 827.521), cameraUpVector=(-0.173398, 0.614122, 0.769927), 
    cameraTarget=(535.104, -57.4977, -4.862), viewOffsetX=74.7729, 
    viewOffsetY=99.6814)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2230.39, 
    farPlane=2842.75, width=1413.01, height=580.393, cameraPosition=(1133.86, 
    -2012.94, 1333.54), cameraUpVector=(-0.162895, 0.773872, 0.612035), 
    cameraTarget=(528.867, -66.6857, 29.4374), viewOffsetX=76.3315, 
    viewOffsetY=101.759)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2332.42, 
    farPlane=2700.57, width=1477.66, height=606.944, cameraPosition=(535.164, 
    -2099.94, 1307.88), cameraUpVector=(0.0185746, 0.78286, 0.62192), 
    cameraTarget=(486.097, -49.1533, 24.7252), viewOffsetX=79.8235, 
    viewOffsetY=106.414)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2327.01, 
    farPlane=2712.86, width=1474.23, height=605.537, cameraPosition=(413.422, 
    -1980.67, 1490.05), cameraUpVector=(0.0154317, 0.833695, 0.55201), 
    cameraTarget=(483.693, -49.9851, 33.301), viewOffsetX=79.6382, 
    viewOffsetY=106.167)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2281.81, 
    farPlane=2741.82, width=1445.59, height=593.774, cameraPosition=(241.972, 
    -2020.34, 1399.13), cameraUpVector=(0.0635407, 0.807374, 0.586609), 
    cameraTarget=(474.241, -41.8214, 25.7774), viewOffsetX=78.0912, 
    viewOffsetY=104.105)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2248.83, 
    farPlane=2757.63, width=1424.7, height=585.193, cameraPosition=(122.199, 
    -2084.34, 1252.71), cameraUpVector=(0.0806495, 0.765328, 0.638567), 
    cameraTarget=(470.191, -34.5211, 15.0864), viewOffsetX=76.9626, 
    viewOffsetY=102.6)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].view.setValues(nearPlane=1984.28, 
    farPlane=2441.83, width=2692.17, height=1105.8, viewOffsetX=473.225, 
    viewOffsetY=69.8543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1973.74, 
    farPlane=2452.37, width=2677.87, height=1099.93, cameraPosition=(532.93, 
    -71.4543, 2213.06), cameraUpVector=(-0.234227, 0.972182, 0), cameraTarget=(
    532.93, -71.4543, 0), viewOffsetX=470.711, viewOffsetY=69.4832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1425.59, 
    farPlane=2426.86, width=1934.17, height=794.457, cameraPosition=(-350.008, 
    -1613.89, 500.093), cameraUpVector=(-0.211708, 0.459805, 0.862415), 
    cameraTarget=(578.394, 244.515, -262.825), viewOffsetX=339.985, 
    viewOffsetY=50.1863)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1539.09, 
    farPlane=2313.37, width=1196.51, height=491.462, viewOffsetX=49.4859, 
    viewOffsetY=141.813)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=1544.41, 
    farPlane=2308.04, width=1200.64, height=493.162, viewOffsetX=120.614, 
    viewOffsetY=167.283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1803.84, 
    farPlane=2154.38, width=1402.33, height=576.005, cameraPosition=(339.873, 
    -1233.31, 1510.88), cameraUpVector=(-0.179544, 0.811403, 0.556228), 
    cameraTarget=(450.712, 33.0591, -300.662), viewOffsetX=140.875, 
    viewOffsetY=195.384)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2118.69, 
    farPlane=2307.42, width=820.411, height=336.982, viewOffsetX=707.924, 
    viewOffsetY=18.243)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.91, 
    farPlane=2303.2, width=822.046, height=337.654, cameraPosition=(457.668, 
    50, 2213.06), cameraTarget=(457.668, 50, 0), viewOffsetX=709.335, 
    viewOffsetY=18.2794)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(405.719, 50, 
    2213.06), cameraTarget=(405.719, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(353.77, 50, 
    2213.06), cameraTarget=(353.77, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(312.403, 50, 
    2213.06), cameraTarget=(312.403, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(276.327, 50, 
    2213.06), cameraTarget=(276.327, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(237.846, 50, 
    2213.06), cameraTarget=(237.846, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(205.137, 50, 
    2213.06), cameraTarget=(205.137, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(170.023, 50, 
    2213.06), cameraTarget=(170.023, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(149.34, 50, 
    2213.06), cameraTarget=(149.34, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(103.163, 50, 
    2213.06), cameraTarget=(103.163, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(52.1757, 50, 
    2213.06), cameraTarget=(52.1757, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-0.73568, 
    50, 2213.06), cameraTarget=(-0.73568, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-48.8369, 
    50, 2213.06), cameraTarget=(-48.8369, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-102.229, 
    50, 2213.06), cameraTarget=(-102.229, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-153.697, 
    50, 2213.06), cameraTarget=(-153.697, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-206.127, 
    50, 2213.06), cameraTarget=(-206.127, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-253.747, 
    50, 2213.06), cameraTarget=(-253.747, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-300.886, 
    50, 2213.06), cameraTarget=(-300.886, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-346.582, 
    50, 2213.06), cameraTarget=(-346.582, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2122.92, 
    farPlane=2303.2, width=822.05, height=337.655, cameraPosition=(-361.012, 
    50, 2213.06), cameraTarget=(-361.012, 50, 0), viewOffsetX=709.338, 
    viewOffsetY=18.2795)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2116.84, 
    farPlane=2309.28, width=845.519, height=347.295, viewOffsetX=1147.07, 
    viewOffsetY=40.4092)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2102.05, 
    farPlane=2324.07, width=1019.16, height=418.616, viewOffsetX=488.693, 
    viewOffsetY=-41.3456)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=2169.02, 
    farPlane=2257.1, width=223.902, height=96.2473, viewOffsetX=434.87, 
    viewOffsetY=-8.40454)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].view.setValues(nearPlane=2079.97, 
    farPlane=2346.15, width=1374.09, height=590.674, viewOffsetX=862.509, 
    viewOffsetY=-175.812)
p = mdb.models['A4'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Scripts/script.py', 
    __main__.__dict__)
#: The model "A4" has been created.
#: The interaction property "Contact-properties" has been created.
#: The interaction "ContactBolt-1" has been created.
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='single_bolt', model='A4', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['single_bolt'].submit(consistencyChecking=OFF)
#: The job input file "single_bolt.inp" has been submitted for analysis.
p = mdb.models['A4'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Scripts/script.py', 
    __main__.__dict__)
#: The model "A4" has been created.
#: The interaction property "Contact-properties" has been created.
#: The interaction "ContactBolt-1" has been created.
#: The interaction property "Contact-properties" has been created.
#: The interaction "ContactBolt-2" has been created.
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='two_bolts', model='A4', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['two_bolts'].submit(consistencyChecking=OFF)
#: The job input file "two_bolts.inp" has been submitted for analysis.
#: Job single_bolt completed successfully. 
p = mdb.models['A4'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Scripts/script.py', 
    __main__.__dict__)
#: The model "A4" has been created.
#: The interaction property "Contact-properties" has been created.
#: The interaction "ContactBolt-1" has been created.
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#: Job two_bolts completed successfully. 
mdb.Job(name='reduced_width', model='A4', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['reduced_width'].submit(consistencyChecking=OFF)
#: The job input file "reduced_width.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/two_bolts.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/two_bolts.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       9
#: Number of Node Sets:          11
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1978.47, 
    farPlane=2364.46, width=1113.73, height=478.752, cameraPosition=(172.357, 
    108.793, 2146.28), cameraUpVector=(0.0126448, 0.928291, -0.371639), 
    cameraTarget=(543.327, 26.2497, -19.5775))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1820.19, 
    farPlane=2520.59, width=1024.63, height=440.452, cameraPosition=(-412.633, 
    -928.647, 1709.39), cameraUpVector=(0.119066, 0.974777, 0.188769), 
    cameraTarget=(550.731, 39.3804, -14.0478))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1768.95, 
    farPlane=2547.73, width=995.785, height=428.052, cameraPosition=(-680.744, 
    -214.555, 1787.79), cameraUpVector=(0.416568, 0.909102, 0.00210251), 
    cameraTarget=(554.259, 29.9836, -15.0795))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1746.25, 
    farPlane=2574.05, width=983.005, height=422.558, cameraPosition=(-765.533, 
    -603.848, 1624.52), cameraUpVector=(0.358878, 0.911894, 0.199141), 
    cameraTarget=(555.854, 37.3085, -12.0074))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1777.4, 
    farPlane=2551.7, width=1000.54, height=430.096, cameraPosition=(-633.322, 
    -818.862, 1627.22), cameraUpVector=(0.287099, 0.925677, 0.246365), 
    cameraTarget=(553.479, 41.1705, -12.0558))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1651.05, 
    farPlane=2738.3, width=929.416, height=399.523, cameraPosition=(-1163.49, 
    -791.971, 1079.53), cameraUpVector=(0.268089, 0.869526, 0.414793), 
    cameraTarget=(555.047, 41.091, -10.4361))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1695.47, 
    farPlane=2690.15, width=954.42, height=410.271, cameraPosition=(-1005.41, 
    -638.237, 1381.9), cameraUpVector=(0.632601, 0.60858, 0.479006), 
    cameraTarget=(554.739, 40.7916, -11.0249))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1656.79, 
    farPlane=2738.46, width=932.644, height=400.91, cameraPosition=(-1143.52, 
    -1160.58, 700.243), cameraUpVector=(0.363595, 0.542507, 0.757288), 
    cameraTarget=(555.126, 42.2555, -9.1145))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TSAIW', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    sectionResults=USE_ENVELOPE)
#: Job reduced_width completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=1658.45, 
    farPlane=2736.8, width=933.581, height=401.313, cameraPosition=(-1143.52, 
    -1160.58, 700.243), cameraUpVector=(0.514222, 0.345998, 0.784768), 
    cameraTarget=(555.126, 42.2555, -9.11449))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1654.88, 
    farPlane=2735.97, width=931.57, height=400.449, cameraPosition=(-1167.05, 
    -880.232, 1000.05), cameraUpVector=(0.645572, 0.338468, 0.6846), 
    cameraTarget=(555.14, 42.0862, -9.29554))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1633.95, 
    farPlane=2756.9, width=1253.28, height=538.74, viewOffsetX=94.3863, 
    viewOffsetY=-46.6972)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1698.58, 
    farPlane=2771.47, width=1302.86, height=560.052, cameraPosition=(-1039.68, 
    -1356.94, 695.564), cameraUpVector=(0.493119, 0.368935, 0.787858), 
    cameraTarget=(523.6, 24.5435, 0.535828), viewOffsetX=98.1202, 
    viewOffsetY=-48.5446)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1574.33, 
    farPlane=2770.66, width=1207.56, height=519.085, cameraPosition=(-1306.09, 
    -478.865, 994.009), cameraUpVector=(0.641469, 0.38756, 0.662053), 
    cameraTarget=(562.034, 67.9164, -28.9907), viewOffsetX=90.9428, 
    viewOffsetY=-44.9936)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1662.8, 
    farPlane=2748.85, width=1275.42, height=548.258, cameraPosition=(-1098.89, 
    -1050.9, 964.784), cameraUpVector=(0.49652, 0.540755, 0.679008), 
    cameraTarget=(519.802, 60.8475, -24.7814), viewOffsetX=96.0535, 
    viewOffsetY=-47.5221)
session.Viewport(name='Viewport: 2', origin=(6.65000009536743, 
    5.34814786911011), width=404.818756103516, height=187.748138427734)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].maximize()
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 2'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0.0, 5.34815979003906), 
    width=226.100006103516, height=194.503692626953)
session.viewports['Viewport: 2'].setValues(origin=(226.100006103516, 
    5.34815979003906), width=226.100006103516, height=194.503692626953)
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 2'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/two_bolts.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/two_bolts.odb')
session.viewports['Viewport: 2'].setValues(displayedObject=o3)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/two_bolts.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/single_bolt.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/single_bolt.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1912.59, 
    farPlane=2419.27, width=681.136, height=566.607, cameraPosition=(93.2769, 
    419.591, 2082.81), cameraUpVector=(-0.44192, 0.692091, -0.570716), 
    cameraTarget=(565.922, 37.7629, -30.5204))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1517.24, 
    farPlane=2806.48, width=540.341, height=449.486, cameraPosition=(-1452.76, 
    629.844, 549.806), cameraUpVector=(0.190935, 0.298608, -0.935082), 
    cameraTarget=(589.489, 34.5579, -7.15189))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1715.58, 
    farPlane=2610.82, width=610.978, height=508.246, cameraPosition=(-674.503, 
    -975.79, 1458.49), cameraUpVector=(-0.311749, 0.945335, -0.0956749), 
    cameraTarget=(576.141, 62.0963, -22.7368))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1524.69, 
    farPlane=2799.69, width=542.996, height=451.695, cameraPosition=(-1468.51, 
    798.595, 119.572), cameraUpVector=(0.621504, 0.642543, 0.448186), 
    cameraTarget=(589.26, 32.7799, -0.615128))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1534.26, 
    farPlane=2790.34, width=546.405, height=454.531, cameraPosition=(-1516.56, 
    275.849, 576.921), cameraUpVector=(0.527472, 0.781354, 0.333555), 
    cameraTarget=(590.077, 41.6654, -8.38902))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1610.26, 
    farPlane=2786.6, width=846.735, height=704.362, cameraPosition=(-994.271, 
    -62.9137, 1556.51), cameraUpVector=(-0.0319057, 0.99879, 0.0374173))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1707.82, 
    farPlane=2689.05, width=898.034, height=747.035, cameraPosition=(-731.427, 
    293.071, 1765.74), cameraUpVector=(0.237232, 0.970774, 0.0363157), 
    cameraTarget=(554.523, 44.8723, 3.8147e-05))
session.Viewport(name='Viewport: 3', origin=(13.3000001907349, 
    5.34814786911011), width=404.818756103516, height=180.992584228516)
session.viewports['Viewport: 3'].makeCurrent()
session.viewports['Viewport: 1'].setValues(origin=(0.0, 5.34815979003906), 
    width=150.733337402344)
session.viewports['Viewport: 2'].setValues(origin=(150.733337402344, 
    5.34815979003906), width=150.733337402344)
session.viewports['Viewport: 3'].setValues(origin=(301.466674804688, 
    5.34815979003906), width=150.733337402344, height=194.503692626953)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 3'].makeCurrent()
a = mdb.models['A4'].rootAssembly
session.viewports['Viewport: 3'].setValues(displayedObject=a)
session.viewports['Viewport: 3'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/two_bolts.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/reduced_width.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A5/Abaqus/reduced_width.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 3'].setValues(displayedObject=o3)
session.viewports['Viewport: 3'].makeCurrent()
session.viewports['Viewport: 3'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 3'].odbDisplay.setPrimaryVariable(
    variableLabel='TSAIW', outputPosition=INTEGRATION_POINT, )
session. linkedViewportCommands.setValues(linkViewports=True)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 3'].makeCurrent()
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 3'].makeCurrent()
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].odbDisplay.setPrimaryVariable(
    variableLabel='TSAIW', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(width=1003.2, height=1259.6, 
    viewOffsetX=-15.349, viewOffsetY=-1.82727)
session.viewports['Viewport: 2'].view.setValues(width=1007.36, height=1264.81, 
    viewOffsetX=-15.4126, viewOffsetY=-1.83483)
session.viewports['Viewport: 3'].view.setValues(width=1006.59, height=1263.85, 
    viewOffsetX=-15.4009, viewOffsetY=-1.83344)
session.viewports['Viewport: 1'].view.setValues(width=892.141, height=1120.15, 
    viewOffsetX=-28.704, viewOffsetY=-3.57033)
session.viewports['Viewport: 2'].view.setValues(width=895.762, height=1124.69, 
    viewOffsetX=-28.8205, viewOffsetY=-3.58482)
session.viewports['Viewport: 3'].view.setValues(width=894.918, height=1123.63, 
    viewOffsetX=-28.7934, viewOffsetY=-3.58145)
session.viewports['Viewport: 1'].view.setValues(width=851.103, height=1068.62, 
    viewOffsetX=-42.6621, viewOffsetY=-5.38043)
session.viewports['Viewport: 2'].view.setValues(width=854.586, height=1073, 
    viewOffsetX=-42.8367, viewOffsetY=-5.40245)
session.viewports['Viewport: 3'].view.setValues(width=853.847, height=1072.07, 
    viewOffsetX=-42.7996, viewOffsetY=-5.39778)
session.viewports['Viewport: 1'].view.setValues(width=804.375, height=1009.95, 
    viewOffsetX=-56.1619, viewOffsetY=-7.07008)
session.viewports['Viewport: 2'].view.setValues(width=807.67, height=1014.09, 
    viewOffsetX=-56.392, viewOffsetY=-7.09904)
session.viewports['Viewport: 3'].view.setValues(width=806.98, height=1013.22, 
    viewOffsetX=-56.3438, viewOffsetY=-7.09297)
session.viewports['Viewport: 1'].view.setValues(width=760.756, height=955.185, 
    viewOffsetX=-69.6013, viewOffsetY=-8.68392)
session.viewports['Viewport: 2'].view.setValues(width=763.88, height=959.107, 
    viewOffsetX=-69.8871, viewOffsetY=-8.71957)
session.viewports['Viewport: 3'].view.setValues(width=763.242, height=958.307, 
    viewOffsetX=-69.8288, viewOffsetY=-8.71229)
session.viewports['Viewport: 1'].view.setValues(width=719.185, height=902.99, 
    viewOffsetX=-82.3769, viewOffsetY=-10.1307)
session.viewports['Viewport: 2'].view.setValues(width=722.144, height=906.704, 
    viewOffsetX=-82.7158, viewOffsetY=-10.1723)
session.viewports['Viewport: 3'].view.setValues(width=721.555, height=905.965, 
    viewOffsetX=-82.6483, viewOffsetY=-10.164)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-82.8217)
session.viewports['Viewport: 2'].view.setValues(viewOffsetY=-10.2273)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1629.05, 
    farPlane=2900.09, width=590.954, height=741.986, cameraPosition=(-1166.14, 
    753.822, 1291.6), cameraUpVector=(0.378987, 0.924949, -0.028965), 
    cameraTarget=(515.037, 26.9058, 75.7339), viewOffsetX=-67.689, 
    viewOffsetY=-8.32436)
session.viewports['Viewport: 2'].view.setValues(nearPlane=1635.18, 
    farPlane=2906.25, width=594.1, height=745.937, cameraPosition=(-1173.11, 
    760.146, 1295.17), cameraUpVector=(0.378987, 0.924949, -0.028965), 
    cameraTarget=(512.549, 31.2904, 76.0541), viewOffsetX=-68.0495, 
    viewOffsetY=-8.36869)
session.viewports['Viewport: 3'].view.setValues(nearPlane=1634.59, 
    farPlane=2888.99, width=596.021, height=748.347, cameraPosition=(-1166.02, 
    728.281, 1290.22), cameraUpVector=(0.378987, 0.924949, -0.028965), 
    cameraTarget=(512.839, 2.36469, 76.0193), viewOffsetX=-68.2694, 
    viewOffsetY=-8.39573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1670.32, 
    farPlane=2875.02, width=605.926, height=760.784, cameraPosition=(-1226.24, 
    96.1846, 1413.05), cameraUpVector=(0.315027, 0.888509, 0.333631), 
    cameraTarget=(512.86, -17.2374, 72.9848), viewOffsetX=-69.4039, 
    viewOffsetY=-8.53526)
session.viewports['Viewport: 2'].view.setValues(nearPlane=1674.25, 
    farPlane=2883.45, width=608.296, height=763.76, cameraPosition=(-1233.37, 
    100.683, 1416.93), cameraUpVector=(0.315028, 0.888508, 0.333632), 
    cameraTarget=(510.363, -13.0407, 73.2931), viewOffsetX=-69.6755, 
    viewOffsetY=-8.56865)
session.viewports['Viewport: 3'].view.setValues(nearPlane=1666.34, 
    farPlane=2873.51, width=607.598, height=762.883, cameraPosition=(-1226.05, 
    71.3167, 1411.48), cameraUpVector=(0.315029, 0.888508, 0.333632), 
    cameraTarget=(510.654, -41.9489, 73.2588), viewOffsetX=-69.5954, 
    viewOffsetY=-8.5588)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1771.84, 
    farPlane=2738.47, width=642.754, height=807.025, cameraPosition=(-702.804, 
    63.09, 1874.3), cameraUpVector=(0.591864, 0.719395, 0.363549), 
    cameraTarget=(537.745, -41.8686, 62.3621), viewOffsetX=-73.6223, 
    viewOffsetY=-9.05403)
session.viewports['Viewport: 2'].view.setValues(nearPlane=1776.37, 
    farPlane=2746.14, width=645.397, height=810.344, cameraPosition=(-708.5, 
    67.4593, 1879.39), cameraUpVector=(0.591865, 0.719394, 0.36355), 
    cameraTarget=(535.353, -37.7772, 62.6243), viewOffsetX=-73.9252, 
    viewOffsetY=-9.09127)
session.viewports['Viewport: 3'].view.setValues(nearPlane=1768.88, 
    farPlane=2735.8, width=644.986, height=809.827, cameraPosition=(-703.205, 
    38.1353, 1872.04), cameraUpVector=(0.591866, 0.719393, 0.36355), 
    cameraTarget=(535.633, -66.6771, 62.5913), viewOffsetX=-73.8779, 
    viewOffsetY=-9.08546)
session.viewports['Viewport: 1'].view.setValues(width=680.096, height=853.911, 
    viewOffsetX=-85.2228, viewOffsetY=-19.4074)
session.viewports['Viewport: 2'].view.setValues(width=682.88, height=857.406, 
    viewOffsetX=-85.5717, viewOffsetY=-19.4869)
session.viewports['Viewport: 3'].view.setValues(width=682.425, height=856.835, 
    viewOffsetX=-85.5145, viewOffsetY=-19.4739)
session.viewports['Viewport: 1'].view.setValues(width=719.559, height=903.459, 
    viewOffsetX=-97.7745, viewOffsetY=-30.4716)
session.viewports['Viewport: 2'].view.setValues(width=722.499, height=907.151, 
    viewOffsetX=-98.1742, viewOffsetY=-30.5961)
session.viewports['Viewport: 3'].view.setValues(width=722.006, height=906.531, 
    viewOffsetX=-98.1069, viewOffsetY=-30.5752)
session.viewports['Viewport: 1'].view.setValues(width=761.05, height=955.554, 
    viewOffsetX=-111.231, viewOffsetY=-42.109)
session.viewports['Viewport: 2'].view.setValues(width=764.154, height=959.451, 
    viewOffsetX=-111.685, viewOffsetY=-42.2807)
session.viewports['Viewport: 3'].view.setValues(width=763.617, height=958.777, 
    viewOffsetX=-111.607, viewOffsetY=-42.251)
session.viewports['Viewport: 1'].view.setValues(width=804.664, height=1010.31, 
    viewOffsetX=-125.377, viewOffsetY=-54.342)
session.viewports['Viewport: 2'].view.setValues(width=807.938, height=1014.43, 
    viewOffsetX=-125.887, viewOffsetY=-54.5631)
session.viewports['Viewport: 3'].view.setValues(width=807.354, height=1013.69, 
    viewOffsetX=-125.796, viewOffsetY=-54.5237)
session.viewports['Viewport: 1'].view.setValues(width=850.474, height=1067.83, 
    viewOffsetX=-142.816, viewOffsetY=-70.5896)
session.viewports['Viewport: 2'].view.setValues(width=853.927, height=1072.17, 
    viewOffsetX=-143.396, viewOffsetY=-70.8761)
session.viewports['Viewport: 3'].view.setValues(width=853.292, height=1071.37, 
    viewOffsetX=-143.289, viewOffsetY=-70.8234)
session.viewports['Viewport: 1'].view.setValues(width=898.557, height=1128.2, 
    viewOffsetX=-160.918, viewOffsetY=-87.2338)
session.viewports['Viewport: 2'].view.setValues(width=902.196, height=1132.77, 
    viewOffsetX=-161.57, viewOffsetY=-87.5871)
session.viewports['Viewport: 3'].view.setValues(width=901.505, height=1131.91, 
    viewOffsetX=-161.446, viewOffsetY=-87.52)
session.viewports['Viewport: 1'].view.setValues(width=948.986, height=1191.52, 
    viewOffsetX=-178.945, viewOffsetY=-104.258)
session.viewports['Viewport: 2'].view.setValues(width=952.82, height=1196.33, 
    viewOffsetX=-179.668, viewOffsetY=-104.679)
session.viewports['Viewport: 3'].view.setValues(width=952.068, height=1195.39, 
    viewOffsetX=-179.526, viewOffsetY=-104.596)
session.viewports['Viewport: 1'].view.setValues(width=1001.83, height=1257.87, 
    viewOffsetX=-196.824, viewOffsetY=-121.985)
session.viewports['Viewport: 2'].view.setValues(width=1005.87, height=1262.94, 
    viewOffsetX=-197.617, viewOffsetY=-122.476)
session.viewports['Viewport: 3'].view.setValues(width=1005.05, height=1261.91, 
    viewOffsetX=-197.457, viewOffsetY=-122.377)
session.viewports['Viewport: 1'].view.setValues(width=1057.16, height=1327.35, 
    viewOffsetX=-214.238, viewOffsetY=-139.823)
session.viewports['Viewport: 2'].view.setValues(width=1061.41, height=1332.68, 
    viewOffsetX=-215.099, viewOffsetY=-140.385)
session.viewports['Viewport: 3'].view.setValues(width=1060.52, height=1331.56, 
    viewOffsetX=-214.919, viewOffsetY=-140.267)
session.viewports['Viewport: 1'].view.setValues(width=985.255, height=1237.06, 
    viewOffsetX=-193.803, viewOffsetY=-120.206)
session.viewports['Viewport: 2'].view.setValues(width=989.202, height=1242.02, 
    viewOffsetX=-194.58, viewOffsetY=-120.687)
session.viewports['Viewport: 3'].view.setValues(width=988.345, height=1240.94, 
    viewOffsetX=-194.411, viewOffsetY=-120.583)
session.viewports['Viewport: 1'].view.setValues(width=936.497, height=1175.84, 
    viewOffsetX=-207.165, viewOffsetY=-131.216)
session.viewports['Viewport: 2'].view.setValues(width=940.268, height=1180.57, 
    viewOffsetX=-207.999, viewOffsetY=-131.744)
session.viewports['Viewport: 3'].view.setValues(width=939.495, height=1179.6, 
    viewOffsetX=-207.828, viewOffsetY=-131.636)
session.viewports['Viewport: 1'].view.setValues(width=886.909, height=1113.58, 
    viewOffsetX=-219.744, viewOffsetY=-142.108)
session.viewports['Viewport: 2'].view.setValues(width=890.488, height=1118.07, 
    viewOffsetX=-220.63, viewOffsetY=-142.682)
session.viewports['Viewport: 3'].view.setValues(width=889.773, height=1117.18, 
    viewOffsetX=-220.453, viewOffsetY=-142.567)
session.viewports['Viewport: 1'].view.setValues(width=840.006, height=1054.69, 
    viewOffsetX=-232.452, viewOffsetY=-154.506)
session.viewports['Viewport: 2'].view.setValues(width=843.404, height=1058.96, 
    viewOffsetX=-233.392, viewOffsetY=-155.131)
session.viewports['Viewport: 3'].view.setValues(width=842.748, height=1058.13, 
    viewOffsetX=-233.211, viewOffsetY=-155.01)
session.viewports['Viewport: 1'].view.setValues(width=795.217, height=998.454, 
    viewOffsetX=-245.035, viewOffsetY=-166.902)
session.viewports['Viewport: 2'].view.setValues(width=798.442, height=1002.5, 
    viewOffsetX=-246.029, viewOffsetY=-167.579)
session.viewports['Viewport: 3'].view.setValues(width=797.838, height=1001.74, 
    viewOffsetX=-245.843, viewOffsetY=-167.452)
session.viewports['Viewport: 1'].view.setValues(width=851.677, height=1069.34, 
    viewOffsetX=-233.768, viewOffsetY=-154.903)
session.viewports['Viewport: 2'].view.setValues(width=855.138, height=1073.69, 
    viewOffsetX=-234.718, viewOffsetY=-155.532)
session.viewports['Viewport: 3'].view.setValues(width=854.51, height=1072.9, 
    viewOffsetX=-234.545, viewOffsetY=-155.418)
session.viewports['Viewport: 1'].view.setValues(width=793.821, height=996.701, 
    viewOffsetX=-245.364, viewOffsetY=-163.428)
session.viewports['Viewport: 2'].view.setValues(width=797.036, height=1000.74, 
    viewOffsetX=-246.358, viewOffsetY=-164.09)
session.viewports['Viewport: 3'].view.setValues(width=796.424, height=999.969, 
    viewOffsetX=-246.168, viewOffsetY=-163.964)
session.viewports['Viewport: 1'].view.setValues(width=851.854, height=1069.57, 
    viewOffsetX=-233.816, viewOffsetY=-156.199)
session.viewports['Viewport: 2'].view.setValues(width=855.317, height=1073.91, 
    viewOffsetX=-234.767, viewOffsetY=-156.834)
session.viewports['Viewport: 3'].view.setValues(width=854.691, height=1073.13, 
    viewOffsetX=-234.595, viewOffsetY=-156.719)
session.viewports['Viewport: 1'].view.setValues(width=793.8, height=996.674, 
    viewOffsetX=-245.357, viewOffsetY=-162.845)
session.viewports['Viewport: 2'].view.setValues(width=797.014, height=1000.71, 
    viewOffsetX=-246.351, viewOffsetY=-163.505)
session.viewports['Viewport: 3'].view.setValues(width=796.402, height=999.941, 
    viewOffsetX=-246.162, viewOffsetY=-163.379)
session.viewports['Viewport: 1'].view.setValues(width=752.701, height=945.071, 
    viewOffsetX=-260.37, viewOffsetY=-170.76)
session.viewports['Viewport: 2'].view.setValues(width=755.761, height=948.913, 
    viewOffsetX=-261.429, viewOffsetY=-171.454)
session.viewports['Viewport: 3'].view.setValues(width=755.207, height=948.218, 
    viewOffsetX=-261.237, viewOffsetY=-171.328)
session.viewports['Viewport: 1'].view.setValues(width=711.884, height=893.822, 
    viewOffsetX=-274.137, viewOffsetY=-176.822)
session.viewports['Viewport: 2'].view.setValues(width=714.783, height=897.462, 
    viewOffsetX=-275.254, viewOffsetY=-177.542)
session.viewports['Viewport: 3'].view.setValues(width=714.272, height=896.821, 
    viewOffsetX=-275.057, viewOffsetY=-177.415)
session.viewports['Viewport: 1'].view.setValues(width=673.227, height=845.285, 
    viewOffsetX=-283.846, viewOffsetY=-176.177)
session.viewports['Viewport: 2'].view.setValues(width=675.974, height=848.735, 
    viewOffsetX=-285.005, viewOffsetY=-176.896)
session.viewports['Viewport: 3'].view.setValues(width=675.505, height=848.146, 
    viewOffsetX=-284.806, viewOffsetY=-176.773)
session.viewports['Viewport: 1'].view.setValues(width=636.444, height=799.102, 
    viewOffsetX=-292.921, viewOffsetY=-175.559)
session.viewports['Viewport: 2'].view.setValues(width=639.047, height=802.37, 
    viewOffsetX=-294.119, viewOffsetY=-176.277)
session.viewports['Viewport: 3'].view.setValues(width=638.614, height=801.827, 
    viewOffsetX=-293.92, viewOffsetY=-176.158)
session.viewports['Viewport: 1'].view.setValues(width=601.487, height=755.211, 
    viewOffsetX=-301.261, viewOffsetY=-175.192)
session.viewports['Viewport: 2'].view.setValues(width=603.951, height=758.305, 
    viewOffsetX=-302.495, viewOffsetY=-175.91)
session.viewports['Viewport: 3'].view.setValues(width=603.553, height=757.805, 
    viewOffsetX=-302.295, viewOffsetY=-175.794)
session.viewports['Viewport: 1'].view.setValues(width=568.283, height=713.521, 
    viewOffsetX=-309.183, viewOffsetY=-174.844)
session.viewports['Viewport: 2'].view.setValues(width=570.615, height=716.45, 
    viewOffsetX=-310.452, viewOffsetY=-175.562)
session.viewports['Viewport: 3'].view.setValues(width=570.249, height=715.989, 
    viewOffsetX=-310.253, viewOffsetY=-175.449)
session.viewports['Viewport: 1'].view.setValues(width=536.762, height=673.944, 
    viewOffsetX=-307.594, viewOffsetY=-173.667)
session.viewports['Viewport: 2'].view.setValues(width=538.969, height=676.715, 
    viewOffsetX=-308.859, viewOffsetY=-174.381)
session.viewports['Viewport: 3'].view.setValues(width=538.631, height=676.291, 
    viewOffsetX=-308.666, viewOffsetY=-174.271)
session.viewports['Viewport: 1'].view.setValues(width=506.855, height=636.394, 
    viewOffsetX=-303.786, viewOffsetY=-173.412)
session.viewports['Viewport: 2'].view.setValues(width=508.942, height=639.014, 
    viewOffsetX=-305.037, viewOffsetY=-174.126)
session.viewports['Viewport: 3'].view.setValues(width=508.631, height=638.624, 
    viewOffsetX=-304.85, viewOffsetY=-174.019)
session.viewports['Viewport: 1'].view.setValues(width=478.494, height=600.785, 
    viewOffsetX=-309.84, viewOffsetY=-175.611)
session.viewports['Viewport: 2'].view.setValues(width=480.467, height=603.262, 
    viewOffsetX=-311.118, viewOffsetY=-176.335)
session.viewports['Viewport: 3'].view.setValues(width=480.181, height=602.902, 
    viewOffsetX=-310.932, viewOffsetY=-176.229)
session.viewports['Viewport: 1'].view.setValues(width=511.105, height=641.73, 
    viewOffsetX=-305.184, viewOffsetY=-175.391)
session.viewports['Viewport: 2'].view.setValues(width=513.215, height=644.38, 
    viewOffsetX=-306.444, viewOffsetY=-176.115)
session.viewports['Viewport: 3'].view.setValues(width=512.916, height=644.003, 
    viewOffsetX=-306.265, viewOffsetY=-176.012)
session.viewports['Viewport: 1'].view.setValues(width=478.203, height=600.419, 
    viewOffsetX=-310.28, viewOffsetY=-174.981)
session.viewports['Viewport: 2'].view.setValues(width=480.174, height=602.894, 
    viewOffsetX=-311.559, viewOffsetY=-175.702)
session.viewports['Viewport: 3'].view.setValues(width=479.885, height=602.531, 
    viewOffsetX=-311.372, viewOffsetY=-175.597)
session.viewports['Viewport: 1'].view.setValues(width=451.631, height=567.056, 
    viewOffsetX=-318.114)
session.viewports['Viewport: 2'].view.setValues(width=453.496, height=569.398, 
    viewOffsetX=-319.428)
session.viewports['Viewport: 3'].view.setValues(width=453.232, height=569.066, 
    viewOffsetX=-319.241)
session.viewports['Viewport: 1'].view.setValues(width=426.143, height=535.054, 
    viewOffsetX=-325.433, viewOffsetY=-176.266)
session.viewports['Viewport: 2'].view.setValues(width=427.905, height=537.266, 
    viewOffsetX=-326.778, viewOffsetY=-176.995)
session.viewports['Viewport: 3'].view.setValues(width=427.661, height=536.959, 
    viewOffsetX=-326.592, viewOffsetY=-176.894)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1807.26, 
    farPlane=2687.77, width=425.143, height=533.798, cameraPosition=(-698.584, 
    -520.155, 1789.78), cameraUpVector=(0.661392, 0.50715, 0.552594), 
    cameraTarget=(524.148, -162.529, -1.90086), viewOffsetX=-324.669, 
    viewOffsetY=-175.852)
session.viewports['Viewport: 2'].view.setValues(nearPlane=1812.81, 
    farPlane=2694.34, width=427.113, height=536.271, cameraPosition=(-704.291, 
    -517.531, 1794.54), cameraUpVector=(0.661392, 0.507148, 0.552595), 
    cameraTarget=(521.698, -158.951, -1.91261), viewOffsetX=-326.173, 
    viewOffsetY=-176.667)
session.viewports['Viewport: 3'].view.setValues(nearPlane=1808.04, 
    farPlane=2681.29, width=427.52, height=536.782, cameraPosition=(-699.064, 
    -544.94, 1787.3), cameraUpVector=(0.661393, 0.507147, 0.552594), 
    cameraTarget=(521.983, -187.805, -1.92214), viewOffsetX=-326.484, 
    viewOffsetY=-176.835)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1812.91, 
    farPlane=2765.29, width=426.473, height=535.468, cameraPosition=(-762.831, 
    -1225.08, 1389.94), cameraUpVector=(0.503305, 0.408144, 0.761645), 
    cameraTarget=(538.768, -171.737, -34.6278), viewOffsetX=-325.685, 
    viewOffsetY=-176.402)
session.viewports['Viewport: 2'].view.setValues(nearPlane=1820.93, 
    farPlane=2769.75, width=429.027, height=538.674, cameraPosition=(-768.687, 
    -1224.35, 1393.58), cameraUpVector=(0.503305, 0.408141, 0.761646), 
    cameraTarget=(536.38, -168.198, -34.7784), viewOffsetX=-327.634, 
    viewOffsetY=-177.458)
session.viewports['Viewport: 3'].view.setValues(nearPlane=1823.64, 
    farPlane=2749.2, width=431.209, height=541.414, cameraPosition=(-763.148, 
    -1248.94, 1387.84), cameraUpVector=(0.503307, 0.40814, 0.761645), 
    cameraTarget=(536.66, -197.045, -34.7741), viewOffsetX=-329.301, 
    viewOffsetY=-178.361)
session.viewports['Viewport: 1'].view.setValues(width=453.619, height=569.552, 
    viewOffsetX=-325.478, viewOffsetY=-192.89)
session.viewports['Viewport: 2'].view.setValues(width=456.297, height=572.915, 
    viewOffsetX=-327.398, viewOffsetY=-194.028)
session.viewports['Viewport: 3'].view.setValues(width=458.501, height=575.681, 
    viewOffsetX=-328.98, viewOffsetY=-194.965)
session.viewports['Viewport: 1'].view.setValues(width=480.713, height=603.57, 
    viewOffsetX=-323.791, viewOffsetY=-208.552)
session.viewports['Viewport: 2'].view.setValues(width=483.55, height=607.133, 
    viewOffsetX=-325.701, viewOffsetY=-209.783)
session.viewports['Viewport: 3'].view.setValues(width=485.886, height=610.066, 
    viewOffsetX=-327.275, viewOffsetY=-210.796)
session.viewports['Viewport: 1'].view.setValues(width=509.42, height=639.615, 
    viewOffsetX=-321.91, viewOffsetY=-224.55)
session.viewports['Viewport: 2'].view.setValues(width=512.425, height=643.387, 
    viewOffsetX=-323.807, viewOffsetY=-225.874)
session.viewports['Viewport: 3'].view.setValues(width=514.893, height=646.485, 
    viewOffsetX=-325.367, viewOffsetY=-226.963)
session.viewports['Viewport: 1'].view.setValues(width=476.887, height=598.767, 
    viewOffsetX=-322.525, viewOffsetY=-206.197)
session.viewports['Viewport: 2'].view.setValues(width=479.697, height=602.294, 
    viewOffsetX=-324.424, viewOffsetY=-207.412)
session.viewports['Viewport: 3'].view.setValues(width=482, height=605.187, 
    viewOffsetX=-325.982, viewOffsetY=-208.408)
session.viewports['Viewport: 1'].view.setValues(width=450.37, height=565.473, 
    viewOffsetX=-326.833, viewOffsetY=-190.373)
session.viewports['Viewport: 2'].view.setValues(width=453.027, height=568.809, 
    viewOffsetX=-328.759, viewOffsetY=-191.495)
session.viewports['Viewport: 3'].view.setValues(width=455.211, height=571.551, 
    viewOffsetX=-330.345, viewOffsetY=-192.419)
session.viewports['Viewport: 1'].view.setValues(width=424.954, height=533.561, 
    viewOffsetX=-330.816, viewOffsetY=-175.253)
session.viewports['Viewport: 2'].view.setValues(width=427.464, height=536.712, 
    viewOffsetX=-332.768, viewOffsetY=-176.288)
session.viewports['Viewport: 3'].view.setValues(width=429.529, height=539.306, 
    viewOffsetX=-334.376, viewOffsetY=-177.14)
session.viewports['Viewport: 1'].view.setValues(width=400.904, height=503.365, 
    viewOffsetX=-334.842, viewOffsetY=-160.797)
session.viewports['Viewport: 2'].view.setValues(width=403.274, height=506.34, 
    viewOffsetX=-336.819, viewOffsetY=-161.747)
session.viewports['Viewport: 3'].view.setValues(width=405.227, height=508.793, 
    viewOffsetX=-338.451, viewOffsetY=-162.531)
session.viewports['Viewport: 1'].view.setValues(width=378.137, height=474.779, 
    viewOffsetX=-344.392, viewOffsetY=-148.352)
session.viewports['Viewport: 2'].view.setValues(width=380.374, height=477.587, 
    viewOffsetX=-346.428, viewOffsetY=-149.229)
session.viewports['Viewport: 3'].view.setValues(width=382.221, height=479.907, 
    viewOffsetX=-348.111, viewOffsetY=-149.954)
session.viewports['Viewport: 1'].view.setValues(width=356.595, height=447.731, 
    viewOffsetX=-353.473, viewOffsetY=-136.576)
session.viewports['Viewport: 2'].view.setValues(width=358.705, height=450.381, 
    viewOffsetX=-355.564, viewOffsetY=-137.384)
session.viewports['Viewport: 3'].view.setValues(width=360.451, height=452.573, 
    viewOffsetX=-357.295, viewOffsetY=-138.053)
session.viewports['Viewport: 1'].view.setValues(width=336.218, height=422.146, 
    viewOffsetX=-362.063, viewOffsetY=-125.437)
session.viewports['Viewport: 2'].view.setValues(width=338.21, height=424.647, 
    viewOffsetX=-364.206, viewOffsetY=-126.18)
session.viewports['Viewport: 3'].view.setValues(width=339.859, height=426.718, 
    viewOffsetX=-365.983, viewOffsetY=-126.795)
session.viewports['Viewport: 1'].view.setValues(width=316.95, height=397.955, 
    viewOffsetX=-370.185, viewOffsetY=-114.905)
session.viewports['Viewport: 2'].view.setValues(width=318.83, height=400.314, 
    viewOffsetX=-372.378, viewOffsetY=-115.585)
session.viewports['Viewport: 3'].view.setValues(width=320.388, height=402.27, 
    viewOffsetX=-374.199, viewOffsetY=-116.151)
session.viewports['Viewport: 1'].view.setValues(width=298.739, height=375.088, 
    viewOffsetX=-378.006, viewOffsetY=-104.731)
session.viewports['Viewport: 2'].view.setValues(width=300.511, height=377.313, 
    viewOffsetX=-380.247, viewOffsetY=-105.352)
session.viewports['Viewport: 3'].view.setValues(width=301.982, height=379.161, 
    viewOffsetX=-382.109, viewOffsetY=-105.869)
session.viewports['Viewport: 1'].view.setValues(width=281.53, height=353.481, 
    viewOffsetX=-385.127, viewOffsetY=-95.939)
session.viewports['Viewport: 2'].view.setValues(width=283.201, height=355.579, 
    viewOffsetX=-387.412, viewOffsetY=-96.5081)
session.viewports['Viewport: 3'].view.setValues(width=284.59, height=357.324, 
    viewOffsetX=-389.313, viewOffsetY=-96.982)
session.viewports['Viewport: 1'].view.setValues(width=265.273, height=333.07, 
    viewOffsetX=-391.823, viewOffsetY=-87.6655)
session.viewports['Viewport: 2'].view.setValues(width=266.849, height=335.048, 
    viewOffsetX=-394.148, viewOffsetY=-88.1858)
session.viewports['Viewport: 3'].view.setValues(width=268.16, height=336.695, 
    viewOffsetX=-396.086, viewOffsetY=-88.6196)
session.viewports['Viewport: 1'].view.setValues(width=249.921, height=313.794, 
    viewOffsetX=-398.146, viewOffsetY=-79.9735)
session.viewports['Viewport: 2'].view.setValues(width=251.407, height=315.659, 
    viewOffsetX=-400.511, viewOffsetY=-80.4483)
session.viewports['Viewport: 3'].view.setValues(width=252.644, height=317.213, 
    viewOffsetX=-402.483, viewOffsetY=-80.8447)
session.viewports['Viewport: 1'].view.setValues(width=235.427, height=295.596, 
    viewOffsetX=-404.736, viewOffsetY=-72.8827)
session.viewports['Viewport: 2'].view.setValues(width=236.827, height=297.353, 
    viewOffsetX=-407.141, viewOffsetY=-73.3157)
