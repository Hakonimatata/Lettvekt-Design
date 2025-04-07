# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Tue Mar 25 11:40:38 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=137.516662597656, 
    height=129.691665649414)
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
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A3/3-point-test-shell.py', 
    __main__.__dict__)
#: The model "3-point-test-shell" has been created.
a = mdb.models['3-point-test-shell'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='Job-1', model='3-point-test-shell', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/Job-1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=531.598, 
    farPlane=812.314, width=380.331, height=171.259, cameraPosition=(365.063, 
    425.912, 365.524), cameraUpVector=(-0.611315, 0.495536, -0.61704), 
    cameraTarget=(6.23304, -12.6567, 6.40076))
session.viewports['Viewport: 1'].view.setValues(nearPlane=527.508, 
    farPlane=843.925, width=377.405, height=169.942, cameraPosition=(536.728, 
    -179.888, 382.325), cameraUpVector=(-0.452794, 0.798403, 0.3969), 
    cameraTarget=(6.50977, -13.6333, 6.42784))
session.viewports['Viewport: 1'].view.setValues(nearPlane=545.517, 
    farPlane=835.571, width=390.29, height=175.744, cameraPosition=(423.958, 
    -517.002, 168.159), cameraUpVector=(-0.203669, 0.550026, 0.809932), 
    cameraTarget=(4.06867, -20.9307, 1.79185))
session.viewports['Viewport: 1'].view.setValues(nearPlane=530.116, 
    farPlane=845.642, width=379.272, height=170.782, cameraPosition=(504.05, 
    -430.676, -188.52), cameraUpVector=(-0.175381, -0.097406, 0.97967), 
    cameraTarget=(6.35017, -18.4716, -8.36857))
session.viewports['Viewport: 1'].view.setValues(nearPlane=523.299, 
    farPlane=849.386, width=374.395, height=168.586, cameraPosition=(557.01, 
    -343.395, -212.186), cameraUpVector=(-0.215899, -0.263162, 0.940284), 
    cameraTarget=(7.65939, -16.314, -8.95361))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=538.987, 
    farPlane=836.123, width=385.619, height=173.64, cameraPosition=(459.644, 
    -390.859, -334.683), cameraUpVector=(-0.03694, -0.276573, 0.960283), 
    cameraTarget=(5.465, -17.3837, -11.7144))
session.viewports['Viewport: 1'].view.setValues(nearPlane=517.572, 
    farPlane=848.017, width=370.298, height=166.741, cameraPosition=(596.849, 
    -84.1482, -325.752), cameraUpVector=(-0.0349328, -0.611342, 0.790595), 
    cameraTarget=(8.7938, -9.94241, -11.4977))
session.viewports['Viewport: 1'].view.setValues(nearPlane=520.386, 
    farPlane=839.006, width=372.312, height=167.648, cameraPosition=(557.272, 
    172.253, -353.897), cameraUpVector=(0.188923, -0.828788, 0.526706), 
    cameraTarget=(8.10281, -5.46582, -11.9891))
session.viewports['Viewport: 1'].view.setValues(nearPlane=530.499, 
    farPlane=834.873, width=379.547, height=170.906, cameraPosition=(525.897, 
    -64.0388, -435.492), cameraUpVector=(-0.275154, -0.909589, 0.31135), 
    cameraTarget=(7.69555, -8.53292, -13.0482))
#: Length of path computed = 30, Number of iterations = 15
session.viewports['Viewport: 1'].view.setValues(nearPlane=587.229, 
    farPlane=778.143, width=35.5039, height=15.9871, viewOffsetX=63.6481, 
    viewOffsetY=-0.328104)
session.Path(name='Path-1', type=EDGE_LIST, expression=(('SPECIMEN', ((1601, 1, 
    1, 1), (1602, 1, 1, 1), (1603, 1, 1, 1), (1604, 1, 1, 1), (1605, 1, 1, 1), 
    (1606, 1, 1, 1), (1607, 1, 1, 1), (1608, 1, 1, 1), (1681, 1, 1, 1), (1682, 
    1, 1, 1), (1683, 1, 1, 1), (1684, 1, 1, 1), (1685, 1, 1, 1), (1686, 1, 1, 
    1), (1687, 1, 1, 1), (1688, 1, 1, 1), )), ))
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['_temp_1']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
execfile('C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A3/4-point-test.py', 
    __main__.__dict__)
#: The model "SW1" has been created.
odb = session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=522.264, 
    farPlane=849.218, width=46.1464, height=20.7793, viewOffsetX=59.6339, 
    viewOffsetY=-1.92608)
a = mdb.models['3-point-test-shell'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/Job-1.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/SW1.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/SW1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       14
#: Number of Node Sets:          18
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=382.046, 
    farPlane=616.018, width=217.016, height=97.7201, cameraPosition=(289.337, 
    -66.4447, 396.029), cameraUpVector=(-0.32176, 0.945693, -0.0462027), 
    cameraTarget=(9.55299, -9.39461, 2.10776))
session.viewports['Viewport: 1'].view.setValues(nearPlane=383.031, 
    farPlane=625.292, width=217.575, height=97.972, cameraPosition=(302.87, 
    -326.536, 231.181), cameraUpVector=(-0.0543288, 0.856368, 0.5135), 
    cameraTarget=(9.89213, -15.9124, -2.02327))
session.viewports['Viewport: 1'].view.setValues(nearPlane=390.905, 
    farPlane=625.185, width=222.048, height=99.986, cameraPosition=(301.745, 
    -403.342, -71.5935), cameraUpVector=(0.0600285, 0.322229, 0.944757), 
    cameraTarget=(9.85279, -18.599, -12.614))
session.viewports['Viewport: 1'].view.setValues(nearPlane=368.911, 
    farPlane=643.731, width=209.554, height=94.3603, cameraPosition=(415.008, 
    -290.036, 1.13474), cameraUpVector=(-0.20436, 0.326541, 0.922826), 
    cameraTarget=(14.6502, -13.7998, -9.53349))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=353.425, 
    farPlane=659.217, width=330.691, height=148.907, viewOffsetX=10.6149, 
    viewOffsetY=-15.9497)
session.viewports['Viewport: 1'].view.setValues(nearPlane=368.081, 
    farPlane=684.776, width=344.404, height=155.082, cameraPosition=(436.851, 
    -41.5438, -296.73), cameraUpVector=(0.129673, -0.484547, 0.865101), 
    cameraTarget=(27.0244, -19.4529, -35.4634), viewOffsetX=11.0551, 
    viewOffsetY=-16.6112)
session.viewports['Viewport: 1'].view.setValues(nearPlane=365.668, 
    farPlane=674.898, width=342.147, height=154.066, cameraPosition=(371.537, 
    -304.863, -205.726), cameraUpVector=(-0.118841, -0.217125, 0.968883), 
    cameraTarget=(10.556, -35.208, -22.1911), viewOffsetX=10.9826, 
    viewOffsetY=-16.5023)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417.579, 
    farPlane=648.188, width=390.72, height=175.937, cameraPosition=(-197.74, 
    -370.034, -334.687), cameraUpVector=(-0.138715, -0.301231, 0.943408), 
    cameraTarget=(-38.8146, -26.0106, -29.5694), viewOffsetX=12.5417, 
    viewOffsetY=-18.845)
session.viewports['Viewport: 1'].view.setValues(nearPlane=400.663, 
    farPlane=676.91, width=374.892, height=168.81, cameraPosition=(242.718, 
    -166.512, -457.424), cameraUpVector=(-0.420584, -0.791441, 0.443543), 
    cameraTarget=(0.562407, -20.7971, -61.401), viewOffsetX=12.0336, 
    viewOffsetY=-18.0816)
#: Length of path computed = 30, Number of iterations = 15
session.viewports['Viewport: 1'].view.setValues(nearPlane=453.486, 
    farPlane=624.087, width=75.9608, height=34.2044, viewOffsetX=103.911, 
    viewOffsetY=-34.707)
session.Path(name='rf path', type=EDGE_LIST, expression=(('BEAM', ((17673, 5, 
    4, -1), (17674, 5, 4, -1), (17675, 5, 4, -1), (17676, 5, 4, -1), (17677, 5, 
    4, -1), (17678, 5, 4, -1), (17679, 5, 4, -1), (17680, 5, 4, -1), (23261, 4, 
    2, -1), (23426, 4, 2, -1), (23591, 4, 2, -1), (23756, 4, 2, -1), (23921, 4, 
    2, -1), (24086, 4, 2, -1), (24251, 4, 2, -1), (24416, 4, 2, -1), )), ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['rf path']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A3/3-point-test-shell.py', 
    __main__.__dict__)
#: The model "3-point-test-shell" has been created.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['3-point-test-shell'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Job-3', model='3-point-test-shell', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/Job-3.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/Testing/Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=535.674, 
    farPlane=840.131, width=383.247, height=172.572, cameraPosition=(465.405, 
    -227.259, 448.013), cameraUpVector=(-0.390454, 0.865201, 0.3146), 
    cameraTarget=(6.65022, -15.3724, 6.74372))
session.viewports['Viewport: 1'].view.setValues(nearPlane=568.282, 
    farPlane=819.41, width=406.577, height=183.077, cameraPosition=(283.551, 
    -551.035, 307.353), cameraUpVector=(-0.210443, 0.70306, 0.67928), 
    cameraTarget=(2.14829, -23.3877, 3.26157))
session.viewports['Viewport: 1'].view.setValues(nearPlane=564.995, 
    farPlane=824.867, width=404.225, height=182.019, cameraPosition=(291.851, 
    -619.791, 112.193), cameraUpVector=(-0.191926, 0.452079, 0.871085), 
    cameraTarget=(2.42312, -25.6642, -3.20017))
session.viewports['Viewport: 1'].view.setValues(nearPlane=563.417, 
    farPlane=823.19, width=403.097, height=181.511, cameraPosition=(294.874, 
    -508.701, 362.611), cameraUpVector=(-0.479644, 0.623891, 0.61701), 
    cameraTarget=(2.52776, -21.8184, 5.46898))
session.viewports['Viewport: 1'].view.setValues(nearPlane=556.676, 
    farPlane=827.481, width=398.275, height=179.339, cameraPosition=(339.045, 
    -429.616, 418.865), cameraUpVector=(-0.485876, 0.688373, 0.538579), 
    cameraTarget=(3.95682, -19.2598, 7.28896))
session.viewports['Viewport: 1'].view.setValues(nearPlane=574.192, 
    farPlane=809.965, width=283.403, height=127.614, viewOffsetX=-0.714298, 
    viewOffsetY=-5.31545)
session.viewports['Viewport: 1'].view.setValues(nearPlane=584.705, 
    farPlane=807.379, width=288.592, height=129.95, cameraPosition=(303.673, 
    -577.673, 237.271), cameraUpVector=(-0.288368, 0.573834, 0.766524), 
    cameraTarget=(4.12874, -25.1258, 2.67195), viewOffsetX=-0.727376, 
    viewOffsetY=-5.41277)
session.viewports['Viewport: 1'].view.setValues(nearPlane=574.853, 
    farPlane=810.437, width=283.729, height=127.761, cameraPosition=(351.06, 
    -445.606, 392.649), cameraUpVector=(-0.365056, 0.739228, 0.565929), 
    cameraTarget=(5.4459, -18.7979, 7.34727), viewOffsetX=-0.71512, 
    viewOffsetY=-5.32157)
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.573, 
    farPlane=813.204, width=282.111, height=127.032, cameraPosition=(376.893, 
    -433.925, 381.307), cameraUpVector=(-0.3589, 0.735649, 0.574466), 
    cameraTarget=(6.36375, -18.403, 6.97972), viewOffsetX=-0.711039, 
    viewOffsetY=-5.2912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=565.848, 
    farPlane=819.746, width=279.286, height=125.76, cameraPosition=(418.728, 
    -450.307, 314.396), cameraUpVector=(-0.361627, 0.652101, 0.666326), 
    cameraTarget=(7.74458, -19.4618, 5.30702), viewOffsetX=-0.703917, 
    viewOffsetY=-5.2382)
session.viewports['Viewport: 1'].view.setValues(width=262.764, height=118.32, 
    viewOffsetX=-1.64827, viewOffsetY=-5.11268)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
