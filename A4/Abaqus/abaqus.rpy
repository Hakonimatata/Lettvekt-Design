# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Tue Apr  8 21:18:03 2025
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
openMdb('Composite_beam_hakon.cae')
#: The model database "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['BP-2'].steps['Step-Buck'].setValues(numEigen=100, vectors=108)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
del mdb.jobs['Job-4']
mdb.Job(name='Job-4', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-4'].submit(consistencyChecking=OFF)
#: The job input file "Job-4.inp" has been submitted for analysis.
#: Job Job-4 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-4.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       11
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3184.48, 
    farPlane=4714.22, width=1907.92, height=783.674, cameraPosition=(2852.64, 
    -1555.02, 3100.1), cameraUpVector=(0.0267494, 0.998353, 0.0507576), 
    cameraTarget=(980.419, -21.582, -39.8911))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3407.96, 
    farPlane=4566.21, width=2041.81, height=838.671, cameraPosition=(2216.48, 
    -3667.21, 887.825), cameraUpVector=(0.153285, 0.609205, 0.778057), 
    cameraTarget=(982.837, -13.5521, -31.4807))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3003.13, 
    farPlane=5017.61, width=1799.27, height=739.046, cameraPosition=(4150.35, 
    -1555.5, 1800.71), cameraUpVector=(-0.5691, 0.479625, 0.667896), 
    cameraTarget=(993.857, -1.51917, -26.2789))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3054.98, 
    farPlane=4958.6, width=1830.34, height=751.807, cameraPosition=(3942, 
    -1967.3, 1752.15), cameraUpVector=(-0.541783, 0.482827, 0.688004), 
    cameraTarget=(991.467, -6.243, -26.8359))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2999.87, 
    farPlane=5022.84, width=1797.32, height=738.247, cameraPosition=(4281.61, 
    -1032.89, 1934.79), cameraUpVector=(-0.659681, 0.393625, 0.640219), 
    cameraTarget=(995.063, 3.65094, -24.9021))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=10)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=20)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3021.26, 
    farPlane=5065.64, width=1810.14, height=743.511, cameraPosition=(4695.4, 
    -816.323, 1143.04), cameraUpVector=(-0.435392, 0.605824, 0.665891), 
    cameraTarget=(1001.3, 6.91706, -36.843))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3058.42, 
    farPlane=5026.38, width=1832.41, height=752.657, cameraPosition=(4449.56, 
    -1772.46, 788.434), cameraUpVector=(-0.257437, 0.602663, 0.75533), 
    cameraTarget=(996.492, -11.7822, -43.7781))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3017.38, 
    farPlane=5080.63, width=1807.82, height=742.559, cameraPosition=(4806.62, 
    -301.846, 1033.43), cameraUpVector=(-0.530183, 0.376392, 0.75976), 
    cameraTarget=(1003.38, 16.6069, -39.0487))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3067.67, 
    farPlane=5001.49, width=1837.95, height=754.935, cameraPosition=(4362.26, 
    -1644.02, 1272.24), cameraUpVector=(-0.547785, 0.303198, 0.779745), 
    cameraTarget=(994.092, -11.447, -34.0572))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3096.94, 
    farPlane=4972.23, width=1361.75, height=559.336, viewOffsetX=59.0581, 
    viewOffsetY=-24.4001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3089.54, 
    farPlane=5001.26, width=1358.5, height=558.001, cameraPosition=(4503.2, 
    -1526.59, 1038.27), cameraUpVector=(-0.513256, 0.265164, 0.816245), 
    cameraTarget=(1001.04, -11.7245, -37.0732), viewOffsetX=58.9172, 
    viewOffsetY=-24.3418)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3121.86, 
    farPlane=4929.03, width=1372.71, height=563.839, cameraPosition=(4205.23, 
    -1871.27, 1345.04), cameraUpVector=(-0.486382, 0.428728, 0.761331), 
    cameraTarget=(985.381, -8.26054, -25.3892), viewOffsetX=59.5336, 
    viewOffsetY=-24.5965)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=45)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=45)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=24)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3070.68, 
    farPlane=5095.31, width=1350.21, height=554.596, cameraPosition=(4889.9, 
    -791.688, 367.277), cameraUpVector=(-0.347687, 0.391932, 0.851765), 
    cameraTarget=(1025.92, 3.61197, -24.5071), viewOffsetX=58.5577, 
    viewOffsetY=-24.1933)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3075.66, 
    farPlane=5073.44, width=1352.4, height=555.495, cameraPosition=(4836.42, 
    -504.903, 934.504), cameraUpVector=(-0.5142, 0.266725, 0.815142), 
    cameraTarget=(1021.97, 5.12349, -17.4457), viewOffsetX=58.6526, 
    viewOffsetY=-24.2325)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3107.07, 
    farPlane=4971.06, width=1366.21, height=561.168, cameraPosition=(4403.43, 
    -1154.53, 1656.11), cameraUpVector=(-0.631001, 0.308673, 0.711729), 
    cameraTarget=(991.956, -10.3739, -7.95708), viewOffsetX=59.2515, 
    viewOffsetY=-24.4799)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3148.38, 
    farPlane=4891.73, width=1384.38, height=568.63, cameraPosition=(4018.42, 
    -2134.76, 1381.78), cameraUpVector=(-0.532631, 0.363752, 0.764192), 
    cameraTarget=(970.968, -21.2187, -19.0687), viewOffsetX=60.0393, 
    viewOffsetY=-24.8054)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendNumberFormat=FIXED)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3032.66, 
    farPlane=5418.61, width=2980.78, height=1224.35, viewOffsetX=499.877, 
    viewOffsetY=-208.426)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2897.81, 
    farPlane=5194.1, width=2848.24, height=1169.91, cameraPosition=(3802.52, 
    -2543.34, -1729.79), cameraUpVector=(-0.277082, -0.258547, 0.925407), 
    cameraTarget=(945.92, -98.1093, -473.966), viewOffsetX=477.65, 
    viewOffsetY=-199.158)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2932.02, 
    farPlane=4359.94, width=2881.87, height=1183.72, cameraPosition=(1526.9, 
    -3424.27, -1651.48), cameraUpVector=(0.0343908, -0.0307692, 0.998935), 
    cameraTarget=(754.562, 179.473, -191.022), viewOffsetX=483.289, 
    viewOffsetY=-201.509)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2846.33, 
    farPlane=4754.96, width=2797.65, height=1149.13, cameraPosition=(2761.32, 
    -3215.49, -1414.05), cameraUpVector=(0.158778, 0.107667, 0.981426), 
    cameraTarget=(823.584, -14.123, -105.301), viewOffsetX=469.165, 
    viewOffsetY=-195.62)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2881.87, 
    farPlane=5009.33, width=2832.58, height=1163.48, cameraPosition=(3707.04, 
    -2755.01, -912.919), cameraUpVector=(-0.131084, 0.106762, 0.985606), 
    cameraTarget=(808.226, -135.394, -241.468), viewOffsetX=475.023, 
    viewOffsetY=-198.062)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2835.46, 
    farPlane=5048.87, width=2786.97, height=1144.74, cameraPosition=(3654.86, 
    -2714.6, -1326.02), cameraUpVector=(-0.0755632, 0.0189811, 0.99696), 
    cameraTarget=(819.332, -155.566, -264.174), viewOffsetX=467.374, 
    viewOffsetY=-194.873)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2911.59, 
    farPlane=4831.04, width=2861.79, height=1175.48, cameraPosition=(3210.41, 
    -3102.92, -804.741), cameraUpVector=(-0.128433, 0.14762, 0.98067), 
    cameraTarget=(733.201, -59.7968, -239.747), viewOffsetX=479.922, 
    viewOffsetY=-200.105)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2753.28, 
    farPlane=4989.35, width=5024.36, height=2063.75, viewOffsetX=715.835, 
    viewOffsetY=-104.73)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2725.96, 
    farPlane=4103.02, width=4974.51, height=2043.27, cameraPosition=(1122.06, 
    -3457.57, -472.037), cameraUpVector=(0.30371, 0.23749, 0.922691), 
    cameraTarget=(671.706, 438.577, 105.553), viewOffsetX=708.732, 
    viewOffsetY=-103.691)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2698.02, 
    farPlane=4653.34, width=4923.52, height=2022.33, cameraPosition=(2452.6, 
    -3350.01, -477.931), cameraUpVector=(-0.179435, 0.227309, 0.957149), 
    cameraTarget=(462.97, 73.4191, -283.322), viewOffsetX=701.467, 
    viewOffsetY=-102.628)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2685.68, 
    farPlane=5017.05, width=4901.01, height=2013.08, cameraPosition=(3437.13, 
    -2917.09, -531.532), cameraUpVector=(-0.247206, 0.14513, 0.958033), 
    cameraTarget=(567.052, -191.665, -305.64), viewOffsetX=698.258, 
    viewOffsetY=-102.159)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2733.65, 
    farPlane=4447.63, width=4988.54, height=2049.03, cameraPosition=(1949.07, 
    -3461.55, -132.016), cameraUpVector=(0.083794, 0.36542, 0.927064), 
    cameraTarget=(432.575, 199.362, -12.5468), viewOffsetX=710.729, 
    viewOffsetY=-103.984)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2767.48, 
    farPlane=4184.93, width=5050.27, height=2074.39, cameraPosition=(1163.05, 
    -3506.51, -353.961), cameraUpVector=(0.0682532, 0.288746, 0.95497), 
    cameraTarget=(422.854, 379.353, -92.2282), viewOffsetX=719.525, 
    viewOffsetY=-105.271)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2653.03, 
    farPlane=4281.77, width=4841.43, height=1988.61, cameraPosition=(1649.43, 
    -3312.59, 785.512), cameraUpVector=(-0.0873491, 0.57272, 0.815084), 
    cameraTarget=(369.185, 290.205, -261.948), viewOffsetX=689.77, 
    viewOffsetY=-100.918)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2824.17, 
    farPlane=3891.86, width=5153.74, height=2116.89, cameraPosition=(625.738, 
    -3337.33, 444.154), cameraUpVector=(0.109923, 0.482319, 0.869072), 
    cameraTarget=(485.916, 573.797, -188.227), viewOffsetX=734.264, 
    viewOffsetY=-107.428)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2880.97, 
    farPlane=3930.38, width=5257.4, height=2159.46, cameraPosition=(523.747, 
    -3403.83, -320.271), cameraUpVector=(-0.0250144, 0.306009, 0.9517), 
    cameraTarget=(472.625, 558.618, -207.176), viewOffsetX=749.032, 
    viewOffsetY=-109.589)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2651.85, 
    farPlane=4358.74, width=4839.28, height=1987.73, cameraPosition=(1783.62, 
    -3386.26, 479.379), cameraUpVector=(-0.148767, 0.485426, 0.861528), 
    cameraTarget=(336.199, 227.039, -272.609), viewOffsetX=689.462, 
    viewOffsetY=-100.873)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2545, 
    farPlane=4762.69, width=4644.3, height=1907.64, cameraPosition=(3156.13, 
    -2790.66, 849.824), cameraUpVector=(-0.398437, 0.445056, 0.801981), 
    cameraTarget=(380.101, -210.555, -313.427), viewOffsetX=661.681, 
    viewOffsetY=-96.8085)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2585.59, 
    farPlane=4821.78, width=4718.37, height=1938.06, cameraPosition=(3330.08, 
    -2828.46, 409.497), cameraUpVector=(-0.429247, 0.294946, 0.853671), 
    cameraTarget=(408.543, -272.24, -394.735), viewOffsetX=672.233, 
    viewOffsetY=-98.3524)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2687.64, 
    farPlane=4491.42, width=4904.59, height=2014.55, cameraPosition=(2169.06, 
    -3428.8, -148.234), cameraUpVector=(-0.395114, 0.263561, 0.880012), 
    cameraTarget=(280.392, 35.581, -532.16), viewOffsetX=698.764, 
    viewOffsetY=-102.234)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2839.39, 
    farPlane=3996.34, width=5181.52, height=2128.3, cameraPosition=(662.54, 
    -3479.31, -73.9321), cameraUpVector=(-0.233693, 0.413839, 0.879844), 
    cameraTarget=(309.418, 444.987, -511.62), viewOffsetX=738.219, 
    viewOffsetY=-108.007)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2653.68, 
    farPlane=4237.52, width=4842.63, height=1989.1, cameraPosition=(1424.15, 
    -3416.19, 528.524), cameraUpVector=(-0.178541, 0.516234, 0.837631), 
    cameraTarget=(230.683, 246.985, -405.883), viewOffsetX=689.937, 
    viewOffsetY=-100.943)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2476.92, 
    farPlane=4564.89, width=4520.07, height=1856.61, cameraPosition=(2679.72, 
    -2968.03, 912), cameraUpVector=(-0.410461, 0.486006, 0.77157), 
    cameraTarget=(223.064, -168.412, -445.679), viewOffsetX=643.981, 
    viewOffsetY=-94.2193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2648.31, 
    farPlane=4393.5, width=2603.04, height=1069.19, viewOffsetX=791.341, 
    viewOffsetY=44.4747)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2641.35, 
    farPlane=4546.4, width=2596.2, height=1066.38, cameraPosition=(3186.6, 
    -2690.53, 919.625), cameraUpVector=(-0.412969, 0.465728, 0.782658), 
    cameraTarget=(274.801, -314.52, -342.241), viewOffsetX=789.263, 
    viewOffsetY=44.3579)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-TOP']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7-Copy2', 
    region=region4, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7-Copy1', 
    region=region5, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3-Copy1', 
    region=region7, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region8, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
layupOrientation = None
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-TOP']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7-Copy2', 
    region=region4, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7-Copy1', 
    region=region5, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3-Copy1', 
    region=region7, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region8, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
a = mdb.models['BP-2'].rootAssembly
a.regenerate()
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['Job-4']
mdb.Job(name='Job-4', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-4'].submit(consistencyChecking=OFF)
#: The job input file "Job-4.inp" has been submitted for analysis.
#: Job Job-4 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-4.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       11
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=81)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=59)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3410.96, 
    farPlane=4537.74, width=2043.61, height=839.408, cameraPosition=(2490.1, 
    -1129.03, 3464.8), cameraUpVector=(-0.356204, 0.932101, 0.0656177), 
    cameraTarget=(978.145, -42.718, -35.2172))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3241.51, 
    farPlane=4829.32, width=1942.09, height=797.708, cameraPosition=(3380.38, 
    -2968.36, 1152.21), cameraUpVector=(-0.441702, 0.414507, 0.795665), 
    cameraTarget=(980.381, -47.3379, -41.0256))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3104.67, 
    farPlane=4962.17, width=1860.11, height=764.035, cameraPosition=(4151.6, 
    -1504.73, 1854.34), cameraUpVector=(-0.701497, 0.246461, 0.6687), 
    cameraTarget=(993.959, -21.5702, -28.6643))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=58)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3057.18, 
    farPlane=5031.47, width=1831.66, height=752.349, cameraPosition=(4490.61, 
    -1257.28, 1374.74), cameraUpVector=(-0.596802, 0.25258, 0.761597), 
    cameraTarget=(999.764, -17.3334, -36.876))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3059.3, 
    farPlane=5026.61, width=1832.93, height=752.872, cameraPosition=(4595.78, 
    -170.693, 1632.31), cameraUpVector=(-0.676004, 0.252265, 0.692373), 
    cameraTarget=(1001.84, 4.15047, -31.7834))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3091.5, 
    farPlane=5028.48, width=1852.22, height=760.797, cameraPosition=(4373.18, 
    -2088.97, 248.906), cameraUpVector=(-0.253229, 0.361249, 0.897426), 
    cameraTarget=(997.513, -33.1402, -58.6764))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3041.1, 
    farPlane=5058.51, width=1822.03, height=748.395, cameraPosition=(4693.33, 
    -350.35, 1376.62), cameraUpVector=(-0.628011, 0.190322, 0.754572), 
    cameraTarget=(1005.05, 7.81079, -32.1145))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3052.11, 
    farPlane=5044.47, width=1828.62, height=751.104, cameraPosition=(4657.38, 
    -212.866, 1493.9), cameraUpVector=(-0.657989, 0.165459, 0.734625), 
    cameraTarget=(1004.29, 10.7114, -29.6402))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3038.65, 
    farPlane=5061.83, width=1820.56, height=747.792, cameraPosition=(4656.87, 
    -943.378, 1185.95), cameraUpVector=(-0.575297, 0.201208, 0.792811), 
    cameraTarget=(1004.28, -4.43149, -36.0238))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3083.24, 
    farPlane=4994.87, width=1847.28, height=758.767, cameraPosition=(4363.29, 
    -1142.76, 1737.85), cameraUpVector=(-0.647115, 0.320126, 0.691926), 
    cameraTarget=(998.056, -8.65882, -24.3224))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3066.03, 
    farPlane=5028.36, width=1836.97, height=754.533, cameraPosition=(4442.29, 
    -1610.12, 1115.9), cameraUpVector=(-0.484217, 0.359735, 0.797574), 
    cameraTarget=(999.517, -17.3004, -35.8224))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3052.68, 
    farPlane=5041.13, width=1828.98, height=751.249, cameraPosition=(4540.77, 
    -1215.86, 1284.47), cameraUpVector=(-0.546926, 0.330424, 0.769215), 
    cameraTarget=(1001.53, -9.23199, -32.3726))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3094.95, 
    farPlane=4987.82, width=1854.3, height=761.651, cameraPosition=(4263.98, 
    -1763.28, 1383.21), cameraUpVector=(-0.522202, 0.392917, 0.756915), 
    cameraTarget=(995.885, -20.3964, -30.3589))
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=3131.59, 
    farPlane=4951.18, width=1294.37, height=531.66, viewOffsetX=231.747, 
    viewOffsetY=-74.5697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3139.41, 
    farPlane=5018.29, width=1297.6, height=532.988, cameraPosition=(4502.62, 
    -1387.88, 1318.98), cameraUpVector=(-0.559318, 0.310656, 0.768542), 
    cameraTarget=(1030.94, -34.9628, -35.015), viewOffsetX=232.325, 
    viewOffsetY=-74.7559)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3102.24, 
    farPlane=5055.45, width=1866.27, height=766.568, viewOffsetX=274.326, 
    viewOffsetY=-52.6042)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TSAIW', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3084.27, 
    farPlane=5090.11, width=1855.47, height=762.129, viewOffsetX=271.49, 
    viewOffsetY=-52.5812)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3101.69, 
    farPlane=5135.9, width=1865.94, height=766.432, cameraPosition=(4675.3, 
    -1164.82, 1141.75), cameraUpVector=(-0.548958, 0.251103, 0.797241), 
    cameraTarget=(1062.66, -40.9214, -42.2595), viewOffsetX=273.023, 
    viewOffsetY=-52.8781)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3094.7, 
    farPlane=5136.38, width=1861.74, height=764.704, cameraPosition=(4682.28, 
    -1580.95, 350.505), cameraUpVector=(-0.414581, 0.147644, 0.897955), 
    cameraTarget=(1050.2, -58.8883, -105.036), viewOffsetX=272.408, 
    viewOffsetY=-52.7589)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3092.85, 
    farPlane=5137.81, width=1860.63, height=764.248, cameraPosition=(4690.15, 
    -1500.83, 543.45), cameraUpVector=(-0.425947, 0.216592, 0.87844), 
    cameraTarget=(1052.24, -51.3324, -73.6049), viewOffsetX=272.245, 
    viewOffsetY=-52.7273)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3094.22, 
    farPlane=5145.19, width=1861.46, height=764.589, cameraPosition=(4712.92, 
    -1406.59, 652.733), cameraUpVector=(-0.441726, 0.238311, 0.86492), 
    cameraTarget=(1057.78, -47.4539, -60.6333), viewOffsetX=272.366, 
    viewOffsetY=-52.7507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3100.8, 
    farPlane=5165.61, width=1865.42, height=766.218, cameraPosition=(4772.58, 
    -1220.2, 751.016), cameraUpVector=(-0.469076, 0.231592, 0.852252), 
    cameraTarget=(1073.03, -44.8467, -54.0374), viewOffsetX=272.946, 
    viewOffsetY=-52.8629)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3094.82, 
    farPlane=5146.6, width=1861.82, height=764.739, cameraPosition=(4715.72, 
    -1335.49, 776.299), cameraUpVector=(-0.472854, 0.234494, 0.849365), 
    cameraTarget=(1060.65, -47.0986, -58.4095), viewOffsetX=272.419, 
    viewOffsetY=-52.7609)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3095.89, 
    farPlane=5135.23, width=1862.47, height=765.004, cameraPosition=(4678.77, 
    -1280.14, 987.831), cameraUpVector=(-0.514659, 0.249653, 0.820244), 
    cameraTarget=(1057.65, -44.0472, -49.385), viewOffsetX=272.513, 
    viewOffsetY=-52.7792)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3111.82, 
    farPlane=5196.37, width=1872.05, height=768.941, cameraPosition=(4862.27, 
    -1040.65, 667.272), cameraUpVector=(-0.468355, 0.187839, 0.863342), 
    cameraTarget=(1094.52, -46.676, -62.3212), viewOffsetX=273.915, 
    viewOffsetY=-53.0507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3143.16, 
    farPlane=5165.03, width=1387.74, height=570.012, viewOffsetX=253.9, 
    viewOffsetY=-51.9399)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3151.26, 
    farPlane=5155.4, width=1391.32, height=571.481, cameraPosition=(4851.12, 
    -974.242, 808.69), cameraUpVector=(-0.496, 0.199844, 0.845013), 
    cameraTarget=(1095.12, -42.9905, -52.3826), viewOffsetX=254.554, 
    viewOffsetY=-52.0738)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3175.09, 
    farPlane=5131.56, width=1164.35, height=478.253, viewOffsetX=125.289, 
    viewOffsetY=-24.215)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-4.odb'])
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-4.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=58)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=59)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=58)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=58)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
