# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by hakon on Tue Apr  8 17:13:30 2025
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
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-2" has been created.
#: Job BP-2 completed successfully. 
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3297.66, 
    farPlane=5575.54, width=1868.68, height=767.556, cameraPosition=(-1043.58, 
    890.581, 5119.76), cameraUpVector=(-0.669277, 0.422575, -0.611146), 
    cameraTarget=(-34.3857, -51.6212, 986.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3341.91, 
    farPlane=5494.37, width=1893.76, height=777.856, cameraPosition=(275.086, 
    1744.37, 4950.46), cameraUpVector=(-0.530238, 0.601233, -0.597801), 
    cameraTarget=(-11.0893, -36.5377, 983.016))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3392.78, 
    farPlane=5487.05, width=1922.59, height=789.699, cameraPosition=(-2304.23, 
    657.208, 4638.42), cameraUpVector=(0.189623, 0.873178, -0.449002), 
    cameraTarget=(-46.067, -51.2805, 978.784))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3297.15, 
    farPlane=5584.43, width=1868.4, height=767.44, cameraPosition=(-754.755, 
    601.984, 5235.07), cameraUpVector=(0.274556, 0.861421, -0.427285), 
    cameraTarget=(-17.559, -52.2965, 989.762))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3369.12, 
    farPlane=5512.46, width=966.615, height=397.035, viewOffsetX=-3.98256, 
    viewOffsetY=34.3839)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3370.88, 
    farPlane=5514.61, width=967.12, height=397.243, cameraPosition=(-167.139, 
    234.119, 5333.91), cameraUpVector=(0.101866, 0.914199, -0.392256), 
    cameraTarget=(-0.356888, -59.7311, 988.794), viewOffsetX=-3.98465, 
    viewOffsetY=34.4019)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3384.03, 
    farPlane=5495.45, width=970.894, height=398.793, cameraPosition=(-980.547, 
    813.636, 5153.48), cameraUpVector=(0.243236, 0.849256, -0.468615), 
    cameraTarget=(-19.8209, -47.924, 990.679), viewOffsetX=-4.0002, 
    viewOffsetY=34.5361)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3385.75, 
    farPlane=5498.52, width=971.389, height=398.996, cameraPosition=(1271.08, 
    408.339, 5137.27), cameraUpVector=(0.125676, 0.865517, -0.484856), 
    cameraTarget=(18.9227, -55.4063, 988.627), viewOffsetX=-4.00224, 
    viewOffsetY=34.5537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3416.05, 
    farPlane=5458.2, width=980.083, height=402.567, cameraPosition=(763.559, 
    1517.8, 4999.45), cameraUpVector=(0.0680983, 0.74471, -0.663905), 
    cameraTarget=(14.1112, -32.2212, 995.712), viewOffsetX=-4.03806, 
    viewOffsetY=34.863)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3368.52, 
    farPlane=5515.81, width=966.446, height=396.966, cameraPosition=(320.717, 
    347.882, 5317.35), cameraUpVector=(-0.0517204, 0.907652, -0.416524), 
    cameraTarget=(13.5941, -55.4863, 988.713), viewOffsetX=-3.98187, 
    viewOffsetY=34.3779)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3372.57, 
    farPlane=5509.72, width=967.609, height=397.444, cameraPosition=(563.978, 
    604.193, 5264.03), cameraUpVector=(-0.0978104, 0.881286, -0.462351), 
    cameraTarget=(19.4738, -50.2171, 989.757), viewOffsetX=-3.98666, 
    viewOffsetY=34.4193)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3430.18, 
    farPlane=5449, width=984.139, height=404.233, cameraPosition=(-1879.25, 
    762.361, 4849.84), cameraUpVector=(0.151871, 0.86183, -0.483926), 
    cameraTarget=(-29.7222, -46.726, 987.362), viewOffsetX=-4.05476, 
    viewOffsetY=35.0072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3423.82, 
    farPlane=5455.35, width=1187.52, height=487.771, viewOffsetX=9.26742, 
    viewOffsetY=32.7332)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3402.35, 
    farPlane=5477.02, width=1180.07, height=484.712, cameraPosition=(-1276.25, 
    1311.57, 4945.43), cameraUpVector=(0.311033, 0.784774, -0.536086), 
    cameraTarget=(-28.0325, -32.5692, 992.028), viewOffsetX=9.2093, 
    viewOffsetY=32.5279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3379.6, 
    farPlane=5504.69, width=1172.18, height=481.471, cameraPosition=(-1118.94, 
    967.366, 5089.09), cameraUpVector=(0.275178, 0.830016, -0.485129), 
    cameraTarget=(-24.2689, -39.6422, 992.537), viewOffsetX=9.14772, 
    viewOffsetY=32.3104)
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-2" has been created.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3523.4, 
    farPlane=5193.05, width=2259.62, height=928.133, viewOffsetX=65.1269, 
    viewOffsetY=36.5534)
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-2" has been created.
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3723.41, 
    farPlane=5107.09, width=2109.94, height=866.652, cameraPosition=(-3887.5, 
    790.21, 2840.46), cameraUpVector=(0.385846, 0.846815, -0.366097), 
    cameraTarget=(-34.3854, -51.6212, 986.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3447.79, 
    farPlane=5438.34, width=1953.75, height=802.5, cameraPosition=(-2799.22, 
    553.92, 4306.69), cameraUpVector=(0.441306, 0.867771, -0.228521), 
    cameraTarget=(-20.3297, -54.673, 1004.94))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3327.46, 
    farPlane=5594.06, width=1885.57, height=774.493, cameraPosition=(-668.672, 
    997.241, 5196.94), cameraUpVector=(0.35725, 0.796362, -0.488036), 
    cameraTarget=(20.348, -46.2089, 1021.94))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3404.99, 
    farPlane=5525.93, width=1929.5, height=792.54, cameraPosition=(-2236.18, 
    -256.044, 4757.61), cameraUpVector=(0.147663, 0.955838, -0.254106), 
    cameraTarget=(-15.6822, -75.0165, 1011.84))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3333.28, 
    farPlane=5593.53, width=1888.87, height=775.849, cameraPosition=(-368.232, 
    1035.88, 5226.69), cameraUpVector=(0.0599676, 0.830787, -0.55335), 
    cameraTarget=(29.1728, -43.9936, 1023.1))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3349.5, 
    farPlane=5580.72, width=1898.06, height=779.624, cameraPosition=(54.1748, 
    1156.93, 5213.08), cameraUpVector=(0.0568545, 0.813081, -0.579368), 
    cameraTarget=(39.126, -41.1413, 1022.78))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3374.13, 
    farPlane=5556.09, width=1492.81, height=613.168, viewOffsetX=-3.25716, 
    viewOffsetY=-36.4616)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3369.47, 
    farPlane=5585.02, width=1490.74, height=612.32, cameraPosition=(-969.416, 
    423.14, 5251.37), cameraUpVector=(0.22111, 0.891954, -0.394371), 
    cameraTarget=(18.8444, -57.8076, 1034), viewOffsetX=-3.25266, 
    viewOffsetY=-36.4112)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3369.65, 
    farPlane=5574.66, width=1490.82, height=612.352, cameraPosition=(-228.931, 
    836.856, 5288.06), cameraUpVector=(0.207886, 0.839305, -0.502346), 
    cameraTarget=(40.6828, -48.1085, 1029.15), viewOffsetX=-3.25283, 
    viewOffsetY=-36.4131)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3400.9, 
    farPlane=5543.4, width=1038.01, height=426.361, viewOffsetX=5.8654, 
    viewOffsetY=-17.7665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3400.89, 
    farPlane=5559.8, width=1038.01, height=426.36, cameraPosition=(-537.514, 
    300.006, 5338.7), cameraUpVector=(0.168327, 0.904804, -0.391147), 
    cameraTarget=(31.2808, -61.6218, 1032.91), viewOffsetX=5.86539, 
    viewOffsetY=-17.7665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3410.54, 
    farPlane=5556.55, width=1040.95, height=427.57, cameraPosition=(318.006, 
    610.455, 5331.25), cameraUpVector=(0.148951, 0.864322, -0.480375), 
    cameraTarget=(55.6704, -53.0971, 1031.83), viewOffsetX=5.88203, 
    viewOffsetY=-17.8169)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3401.64, 
    farPlane=5529.08, width=1038.24, height=426.454, cameraPosition=(-818.575, 
    833.716, 5210.64), cameraUpVector=(0.251122, 0.843819, -0.474244), 
    cameraTarget=(24.486, -47.1618, 1026.45), viewOffsetX=5.86668, 
    viewOffsetY=-17.7704)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3399.6, 
    farPlane=5546.42, width=1037.62, height=426.2, cameraPosition=(-818.79, 
    484.168, 5271.52), cameraUpVector=(0.170024, 0.890489, -0.422044), 
    cameraTarget=(22.4218, -55.5718, 1029.45), viewOffsetX=5.86317, 
    viewOffsetY=-17.7598)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3401.72, 
    farPlane=5535.28, width=1038.27, height=426.466, cameraPosition=(-550.449, 
    838.38, 5255.31), cameraUpVector=(0.126938, 0.853736, -0.504997), 
    cameraTarget=(28.658, -46.9542, 1027.43), viewOffsetX=5.86682, 
    viewOffsetY=-17.7709)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3406.46, 
    farPlane=5530.54, width=1039.72, height=427.062, viewOffsetX=75.2599, 
    viewOffsetY=23.7151)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3389.95, 
    farPlane=5524.72, width=1034.68, height=424.992, cameraPosition=(-964.691, 
    606.612, 5209.9), cameraUpVector=(0.21189, 0.876013, -0.433247), 
    cameraTarget=(18.9984, -47.7023, 1014.86), viewOffsetX=74.8951, 
    viewOffsetY=23.6002)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3390.23, 
    farPlane=5524.44, width=1034.77, height=425.028, cameraPosition=(-965.904, 
    623.613, 5206.96), cameraUpVector=(0.361578, 0.8453, -0.393357), 
    cameraTarget=(17.7851, -30.7014, 1011.92), viewOffsetX=74.9013, 
    viewOffsetY=23.6022)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3408.11, 
    farPlane=5486.59, width=1040.23, height=427.271, cameraPosition=(-1049.71, 
    1241.27, 5039.92), cameraUpVector=(0.542895, 0.71738, -0.436613), 
    cameraTarget=(18.8274, -0.327538, 1001.25), viewOffsetX=75.2962, 
    viewOffsetY=23.7266)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3407.56, 
    farPlane=5487.14, width=1106.45, height=454.472, viewOffsetX=155.25, 
    viewOffsetY=67.9397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3382.1, 
    farPlane=5407.51, width=1098.18, height=451.077, cameraPosition=(-1958.93, 
    676.775, 4775.92), cameraUpVector=(0.481294, 0.828234, -0.287026), 
    cameraTarget=(16.1133, -40.1547, 957.619), viewOffsetX=154.09, 
    viewOffsetY=67.4321)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3402.72, 
    farPlane=5412.12, width=1104.88, height=453.827, cameraPosition=(-1634.04, 
    1341.86, 4767.65), cameraUpVector=(0.517806, 0.741504, -0.426671), 
    cameraTarget=(11.604, -31.6454, 972.974), viewOffsetX=155.029, 
    viewOffsetY=67.8431)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3377.84, 
    farPlane=5437, width=1494.48, height=613.853, viewOffsetX=174.567, 
    viewOffsetY=57.2183)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3457.12, 
    farPlane=5645.36, width=1529.55, height=628.26, cameraPosition=(652.6, 
    968.716, 5302.21), cameraUpVector=(-0.120847, 0.828907, -0.546177), 
    cameraTarget=(37.6694, -119.409, 1127.04), viewOffsetX=178.664, 
    viewOffsetY=58.5612)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3415.81, 
    farPlane=5366.67, width=1511.28, height=620.753, cameraPosition=(-2720.5, 
    154.773, 4347.29), cameraUpVector=(0.238153, 0.917334, -0.319032), 
    cameraTarget=(-70.2523, -148.256, 900.754), viewOffsetX=176.529, 
    viewOffsetY=57.8615)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3388.23, 
    farPlane=5405.37, width=1499.08, height=615.743, cameraPosition=(-2170.08, 
    1104.68, 4564.7), cameraUpVector=(0.285941, 0.808491, -0.514373), 
    cameraTarget=(-90.268, -138.732, 942.19), viewOffsetX=175.104, 
    viewOffsetY=57.3943)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3994.08, 
    farPlane=4496.83, width=1767.13, height=725.846, cameraPosition=(-4063.69, 
    1238.99, 844.213), cameraUpVector=(0.614623, 0.784766, -0.0798805), 
    cameraTarget=(66.5908, -150.768, 784.036), viewOffsetX=206.415, 
    viewOffsetY=67.6571)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3307.4, 
    farPlane=5028.09, width=1463.32, height=601.056, cameraPosition=(-1962.87, 
    2356.03, -1927.38), cameraUpVector=(0.665235, 0.546619, 0.508596), 
    cameraTarget=(159.243, -196.52, 896.691), viewOffsetX=170.927, 
    viewOffsetY=56.0252)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3298.82, 
    farPlane=5036.67, width=1757.23, height=721.779, viewOffsetX=74.3715, 
    viewOffsetY=34.3182)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3307.06, 
    farPlane=5028.43, width=1761.62, height=723.582, cameraPosition=(-1952.61, 
    2365.19, -1926.82), cameraUpVector=(0.574248, 0.564399, 0.593037), 
    cameraTarget=(169.504, -187.364, 897.256), viewOffsetX=74.5573, 
    viewOffsetY=34.4039)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3087.52, 
    farPlane=5317.14, width=1644.68, height=675.547, cameraPosition=(-1207.39, 
    303.652, -3116.56), cameraUpVector=(-0.0173965, 0.896971, 0.441746), 
    cameraTarget=(179.136, -76.0969, 997.766), viewOffsetX=69.6079, 
    viewOffsetY=32.12)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3211.07, 
    farPlane=5154.76, width=1710.49, height=702.581, cameraPosition=(-1899.3, 
    1641.47, -2449.35), cameraUpVector=(0.443352, 0.718114, 0.536425), 
    cameraTarget=(174.087, -148.02, 940.801), viewOffsetX=72.3933, 
    viewOffsetY=33.4053)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3080.91, 
    farPlane=5335.01, width=1641.16, height=674.101, cameraPosition=(-832.683, 
    -267.107, -3218.57), cameraUpVector=(-0.0812352, 0.946368, 0.312711), 
    cameraTarget=(163.711, -46.5753, 1018.52), viewOffsetX=69.4588, 
    viewOffsetY=32.0512)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3083.16, 
    farPlane=5325.66, width=1642.36, height=674.595, cameraPosition=(-622.478, 
    548.003, -3224.32), cameraUpVector=(0.0423239, 0.883231, 0.467024), 
    cameraTarget=(151.885, -87.126, 1017.3), viewOffsetX=69.5095, 
    viewOffsetY=32.0746)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3097.87, 
    farPlane=5302.37, width=1650.19, height=677.814, cameraPosition=(-908.576, 
    863.78, -3111.28), cameraUpVector=(0.264532, 0.834216, 0.483846), 
    cameraTarget=(149.411, -115.721, 1001.58), viewOffsetX=69.841, 
    viewOffsetY=32.2276)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
session.viewports['Viewport: 1'].view.setValues(nearPlane=3198.98, 
    farPlane=5201.25, width=385.968, height=158.536, viewOffsetX=132.028, 
    viewOffsetY=43.875)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3586.84, 
    farPlane=4851.67, width=432.766, height=177.758, cameraPosition=(-2464.22, 
    2530.91, -1413.45), cameraUpVector=(0.814723, 0.489842, 0.310293), 
    cameraTarget=(94.6081, -185.396, 837.864), viewOffsetX=148.036, 
    viewOffsetY=49.1946)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3557.32, 
    farPlane=4881.18, width=800.127, height=328.65, viewOffsetX=165.738, 
    viewOffsetY=79.5876)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3732.03, 
    farPlane=4727.5, width=839.423, height=344.791, cameraPosition=(-2760.38, 
    2800.33, -667.971), cameraUpVector=(0.892853, 0.426624, 0.144239), 
    cameraTarget=(54.4752, -183.355, 804.63), viewOffsetX=173.878, 
    viewOffsetY=83.4963)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3686.06, 
    farPlane=4773.46, width=1452.85, height=596.755, viewOffsetX=208.81, 
    viewOffsetY=123.853)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3129.36, 
    farPlane=5191.73, width=1233.43, height=506.628, cameraPosition=(-1615.74, 
    1002.16, -2806.63), cameraUpVector=(0.39633, 0.807081, 0.437656), 
    cameraTarget=(235.098, -152.671, 966.314), viewOffsetX=177.274, 
    viewOffsetY=105.148)
