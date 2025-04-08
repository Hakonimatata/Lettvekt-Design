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
execfile(
    'C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/scripts/script1.py', 
    __main__.__dict__)
#: The model "BP-2" has been created.
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3346.27, 
    farPlane=5448.1, width=1896.22, height=778.869, cameraPosition=(1906.66, 
    1400.45, 4607.88), cameraUpVector=(-0.410107, 0.769374, -0.489772), 
    cameraTarget=(-34.3859, -51.6212, 986.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3464.7, 
    farPlane=5283.5, width=1963.33, height=806.435, cameraPosition=(2064.1, 
    2323.85, 3979.15), cameraUpVector=(-0.405936, 0.60905, -0.681376), 
    cameraTarget=(-32.9909, -43.4394, 980.436))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3374.58, 
    farPlane=5408.52, width=1912.26, height=785.458, cameraPosition=(2087.78, 
    1489.51, 4466.11), cameraUpVector=(-0.46077, 0.753624, -0.468767), 
    cameraTarget=(-32.905, -46.4675, 982.203))
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
session.viewports['Viewport: 1'].view.setValues(nearPlane=3436.97, 
    farPlane=5346.13, width=1115.97, height=458.384, viewOffsetX=-147.691, 
    viewOffsetY=-33.6371)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3416.42, 
    farPlane=5479.24, width=1109.3, height=455.643, cameraPosition=(1475.53, 
    1087.41, 4953.94), cameraUpVector=(-0.259464, 0.819295, -0.511306), 
    cameraTarget=(-9.45644, -63.8378, 1021.57), viewOffsetX=-146.808, 
    viewOffsetY=-33.436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3392.6, 
    farPlane=5503.06, width=1326.25, height=544.756, viewOffsetX=-141.975, 
    viewOffsetY=2.64727)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3399.42, 
    farPlane=5496.23, width=1328.92, height=545.852, cameraPosition=(1477.26, 
    1068.41, 4958.85), cameraUpVector=(-0.166278, 0.820545, -0.546862), 
    cameraTarget=(-7.7226, -82.8339, 1026.48), viewOffsetX=-142.261, 
    viewOffsetY=2.6526)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3405.65, 
    farPlane=5490, width=1331.36, height=546.853, viewOffsetX=-41.5033, 
    viewOffsetY=80.6606)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3386.15, 
    farPlane=5520.98, width=1323.74, height=543.722, cameraPosition=(1257.63, 
    919.45, 5073.98), cameraUpVector=(-0.137841, 0.840122, -0.52459), 
    cameraTarget=(-12.5531, -86.1176, 1028.05), viewOffsetX=-41.2656, 
    viewOffsetY=80.1987)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3377.06, 
    farPlane=5525.85, width=1320.19, height=542.264, cameraPosition=(1384.03, 
    547.246, 5096.92), cameraUpVector=(-0.171651, 0.88335, -0.436153), 
    cameraTarget=(-7.72104, -93.1504, 1016.85), viewOffsetX=-41.1548, 
    viewOffsetY=79.9834)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3387.12, 
    farPlane=5522.84, width=1324.12, height=543.881, cameraPosition=(1201.97, 
    958.721, 5082.84), cameraUpVector=(-0.206219, 0.834687, -0.510658), 
    cameraTarget=(-5.7786, -80.9128, 1026.42), viewOffsetX=-41.2774, 
    viewOffsetY=80.2217)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3409.74, 
    farPlane=5500.21, width=978.271, height=401.823, viewOffsetX=-62.6191, 
    viewOffsetY=60.6222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3422.33, 
    farPlane=5530.76, width=981.881, height=403.306, cameraPosition=(445.182, 
    994.692, 5243.51), cameraUpVector=(-0.10942, 0.830263, -0.546527), 
    cameraTarget=(-22.4835, -80.303, 1045.93), viewOffsetX=-62.8502, 
    viewOffsetY=60.8459)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3402.37, 
    farPlane=5546.58, width=976.154, height=400.953, cameraPosition=(830.346, 
    -15.356, 5298.37), cameraUpVector=(-0.0992001, 0.934775, -0.341107), 
    cameraTarget=(-16.3963, -110.77, 1024.27), viewOffsetX=-62.4836, 
    viewOffsetY=60.491)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3404.55, 
    farPlane=5543.11, width=976.779, height=401.21, cameraPosition=(701.647, 
    503.238, 5291.25), cameraUpVector=(-0.145698, 0.885714, -0.440774), 
    cameraTarget=(-14.9888, -93.1152, 1033.93), viewOffsetX=-62.5236, 
    viewOffsetY=60.5298)
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side12Faces = s.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
p.Surface(side12Faces=side12Faces, name='top')
#: The surface 'top' has been created (18 faces).
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side2Faces = s.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
p.Surface(side2Faces=side2Faces, name='top')
#: The surface 'top' has been edited (18 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=3375.65, 
    farPlane=5572.01, width=1415.38, height=581.364, viewOffsetX=-5.50436, 
    viewOffsetY=106.285)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3418.34, 
    farPlane=5527.55, width=1433.28, height=588.717, cameraPosition=(1209.01, 
    1332.59, 4996.56), cameraUpVector=(-0.309048, 0.776713, -0.548823), 
    cameraTarget=(16.2573, -64.2737, 1044.34), viewOffsetX=-5.57398, 
    viewOffsetY=107.629)
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side12Faces = s.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
p.Surface(side12Faces=side12Faces, name='top')
#: The surface 'top' has been edited (18 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=3445.48, 
    farPlane=5500.41, width=1142.47, height=469.269, viewOffsetX=-83.9069, 
    viewOffsetY=66.5982)
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
normalAxisRegion = p.surfaces['top']
p = mdb.models['BP-2'].parts['Box']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#0 #400 #8004 ]', ), )
primaryAxisRegion = p.Set(edges=edges, name='Set-2')
compositeLayup = mdb.models['BP-2'].parts['Box'].CompositeLayup(
    name='CompositeLayup-TOP', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None, 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3, 
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion, 
    normalAxisDirection=AXIS_3, flipNormalDirection=False, 
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion, 
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3421.64, 
    farPlane=5524.25, width=1289.29, height=529.571, viewOffsetX=-35.8237, 
    viewOffsetY=31.0661)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3467.59, 
    farPlane=5461.21, width=1306.6, height=536.683, cameraPosition=(2328.44, 
    575.425, 4666.85), cameraUpVector=(-0.384096, 0.868259, -0.314002), 
    cameraTarget=(39.4909, -83.8806, 1017.2), viewOffsetX=-36.3047, 
    viewOffsetY=31.4833)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3468.56, 
    farPlane=5447.56, width=1306.97, height=536.833, cameraPosition=(2195.04, 
    1077.92, 4629.11), cameraUpVector=(-0.363004, 0.81758, -0.446981), 
    cameraTarget=(36.8304, -75.1455, 1022.66), viewOffsetX=-36.3148, 
    viewOffsetY=31.4921)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3413.36, 
    farPlane=5604.9, width=1286.17, height=528.292, cameraPosition=(-106.656, 
    390.469, 5392.23), cameraUpVector=(-0.0892189, 0.89509, -0.436869), 
    cameraTarget=(-12.0742, -90.7166, 1061.71), viewOffsetX=-35.7369, 
    viewOffsetY=30.9909)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3429.82, 
    farPlane=5620.02, width=1292.37, height=530.84, cameraPosition=(-138.34, 
    -581.6, 5386.64), cameraUpVector=(-0.00647972, 0.972313, -0.233592), 
    cameraTarget=(-16.2932, -127.614, 1053.87), viewOffsetX=-35.9093, 
    viewOffsetY=31.1404)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3424.99, 
    farPlane=5626.56, width=1290.55, height=530.092, cameraPosition=(-478.064, 
    -346.383, 5388.47), cameraUpVector=(0.00850286, 0.958703, -0.28428), 
    cameraTarget=(-28.6245, -118.721, 1059.49), viewOffsetX=-35.8587, 
    viewOffsetY=31.0965)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3510.14, 
    farPlane=5541.4, width=248.825, height=102.204, viewOffsetX=19.2401, 
    viewOffsetY=54.3516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3613.36, 
    farPlane=5436.46, width=256.142, height=105.21, cameraPosition=(-2385.96, 
    -788.709, 4664.67), cameraUpVector=(-0.0103672, 0.972851, -0.231199), 
    cameraTarget=(-83.7477, -136.573, 1022.08), viewOffsetX=19.8059, 
    viewOffsetY=55.9498)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3589.97, 
    farPlane=5459.86, width=657.445, height=270.044, viewOffsetX=-15.2926, 
    viewOffsetY=52.8487)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3455.39, 
    farPlane=5554.65, width=632.799, height=259.921, cameraPosition=(-497.486, 
    -259.994, 5371.3), cameraUpVector=(-0.152186, 0.934557, -0.321624), 
    cameraTarget=(-11.2335, -116.025, 1042.7), viewOffsetX=-14.7193, 
    viewOffsetY=50.8675)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3477.06, 
    farPlane=5541.54, width=636.767, height=261.551, cameraPosition=(-1266.89, 
    -215.341, 5223.71), cameraUpVector=(-0.132616, 0.921845, -0.364163), 
    cameraTarget=(-34.5873, -113.073, 1044.6), viewOffsetX=-14.8116, 
    viewOffsetY=51.1864)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3520.86, 
    farPlane=5491.66, width=644.789, height=264.846, cameraPosition=(-1971.91, 
    474.715, 4925.5), cameraUpVector=(-0.0055224, 0.864195, -0.503127), 
    cameraTarget=(-64.1579, -89.5961, 1047.87), viewOffsetX=-14.9982, 
    viewOffsetY=51.8312)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3532.01, 
    farPlane=5510.62, width=646.832, height=265.685, cameraPosition=(-1819.38, 
    -986.736, 4921.34), cameraUpVector=(0.00362296, 0.987583, -0.157058), 
    cameraTarget=(-60.1768, -141.922, 1024.48), viewOffsetX=-15.0457, 
    viewOffsetY=51.9954)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
normalAxisRegion = p.Surface(side1Faces=side1Faces, name='Surf-2')
p = mdb.models['BP-2'].parts['Box']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#88 #4000 ]', ), )
primaryAxisRegion = regionToolset.Region(edges=edges)
compositeLayup = mdb.models['BP-2'].parts['Box'].CompositeLayup(
    name='CompositeLayup-BOTTOM', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None, 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3, 
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion, 
    normalAxisDirection=AXIS_3, flipNormalDirection=False, 
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion, 
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3453.81, 
    farPlane=5588.82, width=1716.2, height=704.927, viewOffsetX=30.6769, 
    viewOffsetY=125.567)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3405.03, 
    farPlane=5670.4, width=1691.96, height=694.97, cameraPosition=(-177.423, 
    -352.88, 5422.11), cameraUpVector=(-0.321536, 0.897348, -0.302294), 
    cameraTarget=(32.7011, -123.093, 1075.03), viewOffsetX=30.2436, 
    viewOffsetY=123.793)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3465.36, 
    farPlane=5654.66, width=1721.94, height=707.283, cameraPosition=(1386.48, 
    954.94, 5139.59), cameraUpVector=(-0.405803, 0.804417, -0.433863), 
    cameraTarget=(90.7162, -68.2041, 1106.2), viewOffsetX=30.7794, 
    viewOffsetY=125.986)
mdb.saveAs(
    pathName='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Composite_beam_hakon')
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=3464.32, 
    farPlane=5606.45, width=1721.43, height=707.072, cameraPosition=(-2106.48, 
    -431.627, 4895.24), cameraUpVector=(0.26915, 0.949447, -0.161583), 
    cameraTarget=(-134.717, -119.832, 1021.1), viewOffsetX=30.7702, 
    viewOffsetY=125.948)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3411.21, 
    farPlane=5678.2, width=1695.04, height=696.234, cameraPosition=(-573.393, 
    349.194, 5396.56), cameraUpVector=(0.0740976, 0.903406, -0.422335), 
    cameraTarget=(-65.0996, -97.1763, 1091.17), viewOffsetX=30.2985, 
    viewOffsetY=124.017)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3494.31, 
    farPlane=5595.09, width=647.817, height=266.09, viewOffsetX=43.6308, 
    viewOffsetY=79.5842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3559.09, 
    farPlane=5515.47, width=659.825, height=271.022, cameraPosition=(-1828.05, 
    1113.87, 4902.37), cameraUpVector=(0.354428, 0.809437, -0.46818), 
    cameraTarget=(-130.934, -55.607, 1062.3), viewOffsetX=44.4396, 
    viewOffsetY=81.0594)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3534.73, 
    farPlane=5539.83, width=1010.54, height=415.076, viewOffsetX=20.3591, 
    viewOffsetY=116.912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3470.37, 
    farPlane=5593.81, width=992.135, height=407.517, cameraPosition=(-1148.48, 
    603.277, 5244.06), cameraUpVector=(0.160855, 0.877558, -0.451683), 
    cameraTarget=(-83.8297, -82.8214, 1073.95), viewOffsetX=19.9884, 
    viewOffsetY=114.783)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
normalAxisRegion = regionToolset.Region(side1Faces=side1Faces)
p = mdb.models['BP-2'].parts['Box']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#800 #20000 #1000 ]', ), )
primaryAxisRegion = regionToolset.Region(edges=edges)
compositeLayup = mdb.models['BP-2'].parts['Box'].CompositeLayup(
    name='CompositeLayup-SIDE1', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None, 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3, 
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion, 
    normalAxisDirection=AXIS_3, flipNormalDirection=False, 
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion, 
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3454.4, 
    farPlane=5603.28, width=987.569, height=405.642, cameraPosition=(395.66, 
    369.332, 5397.87), cameraUpVector=(-0.102531, 0.899779, -0.424128), 
    cameraTarget=(-2.09119, -95.4388, 1082.8), viewOffsetX=19.8964, 
    viewOffsetY=114.255)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3476.88, 
    farPlane=5576.13, width=993.995, height=408.282, cameraPosition=(1506.45, 
    154.459, 5167.24), cameraUpVector=(-0.22105, 0.91641, -0.333661), 
    cameraTarget=(46.9128, -104.558, 1068.86), viewOffsetX=20.0259, 
    viewOffsetY=114.998)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3493.68, 
    farPlane=5559.34, width=733.022, height=301.087, viewOffsetX=-7.11778, 
    viewOffsetY=107.515)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
normalAxisRegion = regionToolset.Region(side1Faces=side1Faces)
p = mdb.models['BP-2'].parts['Box']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#0 #400 #8004 ]', ), )
primaryAxisRegion = regionToolset.Region(edges=edges)
compositeLayup = mdb.models['BP-2'].parts['Box'].CompositeLayup(
    name='CompositeLayup-SIDE2', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None, 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3, 
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion, 
    normalAxisDirection=AXIS_3, flipNormalDirection=False, 
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion, 
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3475.96, 
    farPlane=5577.05, width=1061.49, height=436.004, viewOffsetX=23.9357, 
    viewOffsetY=134.74)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3445.66, 
    farPlane=5608.28, width=1052.24, height=432.203, cameraPosition=(604.211, 
    195.651, 5383.75), cameraUpVector=(-0.00668061, 0.916785, -0.399325), 
    cameraTarget=(-15.1441, -98.9248, 1079.83), viewOffsetX=23.727, 
    viewOffsetY=133.566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3464.56, 
    farPlane=5589.38, width=776.48, height=318.937, viewOffsetX=-0.348484, 
    viewOffsetY=112.249)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
normalAxisRegion = regionToolset.Region(side1Faces=side1Faces)
p = mdb.models['BP-2'].parts['Box']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#80000 #800000 #800 ]', ), )
primaryAxisRegion = regionToolset.Region(edges=edges)
compositeLayup = mdb.models['BP-2'].parts['Box'].CompositeLayup(
    name='CompositeLayup-SPAR', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.5, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None, 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3, 
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion, 
    normalAxisDirection=AXIS_3, flipNormalDirection=False, 
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion, 
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=3451.13, 
    farPlane=5602.82, width=1053.91, height=432.891, viewOffsetX=43.0934, 
    viewOffsetY=110.847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3453.26, 
    farPlane=5598.46, width=1054.56, height=433.158, cameraPosition=(0.622177, 
    479.299, 5401.94), cameraUpVector=(0.0550575, 0.889657, -0.453298), 
    cameraTarget=(-40.7441, -86.9036, 1080.85), viewOffsetX=43.12, 
    viewOffsetY=110.915)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3447.81, 
    farPlane=5607.64, width=1052.9, height=432.475, cameraPosition=(587.444, 
    316.417, 5379.83), cameraUpVector=(0.0120938, 0.904658, -0.425967), 
    cameraTarget=(-18.5134, -92.6721, 1083.37), viewOffsetX=43.0519, 
    viewOffsetY=110.74)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
a = mdb.models['BP-2'].rootAssembly
a.regenerate()
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Job-2', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       11
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3004.44, 
    farPlane=5139.11, width=1800.05, height=739.368, cameraPosition=(4848.86, 
    -80.007, 893.069), cameraUpVector=(-0.321524, 0.943322, -0.0822533), 
    cameraTarget=(999.085, -73.8275, -53.189))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3025.04, 
    farPlane=5130.57, width=1812.39, height=744.437, cameraPosition=(4752.79, 
    -727.512, -1204.71), cameraUpVector=(-0.120173, 0.964943, 0.233331), 
    cameraTarget=(996.551, -90.9083, -108.527))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3024.77, 
    farPlane=5130.84, width=1812.23, height=744.37, cameraPosition=(4752.79, 
    -727.512, -1204.71), cameraUpVector=(-0.0145262, 0.475306, 0.879701), 
    cameraTarget=(996.551, -90.9084, -108.527))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3019.59, 
    farPlane=5141.5, width=1809.13, height=743.096, cameraPosition=(4915.56, 
    -650.882, 208.396), cameraUpVector=(-0.393239, 0.065347, 0.917111), 
    cameraTarget=(1001.08, -88.7767, -69.2171))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Tresca'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3038.84, 
    farPlane=5119.03, width=1820.66, height=747.834, cameraPosition=(4647.95, 
    -812.69, -1474.9), cameraUpVector=(0.0284513, 0.105354, 0.994028), 
    cameraTarget=(993.461, -93.3836, -117.143))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3050.5, 
    farPlane=5136.16, width=1827.65, height=750.704, cameraPosition=(4748.59, 
    -1348.87, 243.758), cameraUpVector=(-0.423528, 0.012434, 0.905798), 
    cameraTarget=(996.288, -108.444, -68.8695))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3027.33, 
    farPlane=5145.58, width=1813.77, height=745.002, cameraPosition=(4801.03, 
    -872.23, 750.926), cameraUpVector=(-0.518747, 0.0447763, 0.853755), 
    cameraTarget=(997.94, -93.4268, -52.8905))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3012.83, 
    farPlane=5134.43, width=1805.08, height=741.433, cameraPosition=(4920.64, 
    -186.344, 526.702), cameraUpVector=(-0.468753, 0.0186879, 0.883131), 
    cameraTarget=(1001.51, -72.9338, -59.5899))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3028.89, 
    farPlane=5140.32, width=1814.7, height=745.386, cameraPosition=(4874.99, 
    -901.099, 150.348), cameraUpVector=(-0.383299, 0.0484904, 0.92235), 
    cameraTarget=(1000.29, -92.1055, -69.6848))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3033.79, 
    farPlane=5142.43, width=1817.64, height=746.592, cameraPosition=(4823.37, 
    -1067.08, 319.44), cameraUpVector=(-0.423599, 0.0503028, 0.904452), 
    cameraTarget=(998.77, -96.9918, -64.7068))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CM', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal (Abs)'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Min. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Out-of-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Min. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3017.88, 
    farPlane=5138.97, width=1808.11, height=742.678, cameraPosition=(4825.39, 
    -721.446, -921.121), cameraUpVector=(-0.127096, 0.0369386, 0.991202), 
    cameraTarget=(998.831, -86.5294, -102.259))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3017.76, 
    farPlane=5140.13, width=1808.04, height=742.649, cameraPosition=(4924.5, 
    -577.042, 216.832), cameraUpVector=(-0.406001, -0.0177381, 0.913701), 
    cameraTarget=(1001.6, -82.4909, -70.4339))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3016.6, 
    farPlane=5129.27, width=1807.35, height=742.365, cameraPosition=(4960.73, 
    -247.785, 63.6465), cameraUpVector=(-0.368606, -0.0521009, 0.928124), 
    cameraTarget=(1002.62, -73.242, -74.7369))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3012.49, 
    farPlane=5126.17, width=1804.89, height=741.354, cameraPosition=(4957.08, 
    -9.43438, 201.807), cameraUpVector=(-0.396916, -0.0362182, 0.91714), 
    cameraTarget=(1002.52, -66.8885, -71.0541))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3027.83, 
    farPlane=5141.64, width=1814.08, height=745.13, cameraPosition=(4794.17, 
    -819.482, 823.848), cameraUpVector=(-0.545317, -0.0163192, 0.838071), 
    cameraTarget=(998.318, -87.7804, -55.0111))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3158.78, 
    farPlane=5064.29, width=1892.54, height=777.356, cameraPosition=(4166.61, 
    -2365.62, 701.381), cameraUpVector=(-0.503496, 0.162121, 0.848651), 
    cameraTarget=(979.827, -133.336, -58.6195))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3097.43, 
    farPlane=5103.25, width=1855.78, height=762.259, cameraPosition=(4344.12, 
    -1529.06, 1522.53), cameraUpVector=(-0.620502, 0.267698, 0.737099), 
    cameraTarget=(986.181, -103.394, -29.229))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3060.28, 
    farPlane=5129.19, width=1833.52, height=753.116, cameraPosition=(4573.74, 
    -1264.95, 1197.16), cameraUpVector=(-0.573768, 0.210691, 0.791454), 
    cameraTarget=(993.795, -94.6363, -40.0179))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3102.77, 
    farPlane=5099.82, width=1858.98, height=763.572, cameraPosition=(4502.86, 
    -1951.46, -225.976), cameraUpVector=(-0.324492, 0.026748, 0.94551), 
    cameraTarget=(991.538, -116.492, -85.3259))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3095.08, 
    farPlane=5108.93, width=1854.37, height=761.679, cameraPosition=(4505.68, 
    -1916.46, 283.301), cameraUpVector=(-0.406337, 0.117805, 0.906097), 
    cameraTarget=(991.632, -115.324, -68.324))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3058.84, 
    farPlane=5133.48, width=1832.66, height=752.76, cameraPosition=(4663.62, 
    -1513.26, 466.405), cameraUpVector=(-0.416719, 0.186846, 0.889626), 
    cameraTarget=(996.931, -101.796, -62.1805))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3164.02, 
    farPlane=5057.19, width=1895.68, height=778.646, cameraPosition=(4190.14, 
    -2440.27, 234.108), cameraUpVector=(-0.300211, 0.275342, 0.913269), 
    cameraTarget=(981.698, -131.621, -69.6541))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3033.88, 
    farPlane=5147.68, width=1817.71, height=746.62, cameraPosition=(4811.5, 
    -1141.29, 251.53), cameraUpVector=(-0.385774, 0.13733, 0.912315), 
    cameraTarget=(1003.8, -85.4097, -69.0343))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3047.67, 
    farPlane=5133.88, width=1613.43, height=662.712, viewOffsetX=119.177, 
    viewOffsetY=70.693)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=3328.24, 
    farPlane=4741.26, width=1761.96, height=723.723, cameraPosition=(2878.64, 
    -3386.31, 861.467), cameraUpVector=(-0.0147841, 0.602134, 0.798258), 
    cameraTarget=(833.855, -100.847, 0.76627), viewOffsetX=130.149, 
    viewOffsetY=77.2012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3334.05, 
    farPlane=4672.09, width=1765.04, height=724.987, cameraPosition=(2740.76, 
    -3555.49, -133.708), cameraUpVector=(0.0867049, 0.400234, 0.912302), 
    cameraTarget=(823.45, -87.3209, -24.5149), viewOffsetX=130.376, 
    viewOffsetY=77.3361)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3006.46, 
    farPlane=5079.2, width=1591.61, height=653.752, cameraPosition=(4680.45, 
    -1391.32, -417.423), cameraUpVector=(-0.292555, -0.0596147, 0.954389), 
    cameraTarget=(942.199, -110.653, -98.728), viewOffsetX=117.566, 
    viewOffsetY=69.7373)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3105.25, 
    farPlane=5006.13, width=1643.91, height=675.234, cameraPosition=(4203.78, 
    -2275.89, 501.952), cameraUpVector=(-0.384637, 0.257141, 0.886529), 
    cameraTarget=(912.501, -137.487, -55.6823), viewOffsetX=121.429, 
    viewOffsetY=72.0288)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3084.88, 
    farPlane=5061.36, width=1633.13, height=670.804, cameraPosition=(4365.26, 
    -1883.19, 925.928), cameraUpVector=(-0.473808, 0.287151, 0.832496), 
    cameraTarget=(936.685, -142.254, -38.5681), viewOffsetX=120.632, 
    viewOffsetY=71.5562)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3059.91, 
    farPlane=5086.32, width=1840.81, height=756.109, viewOffsetX=271.967, 
    viewOffsetY=-29.2103)
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Stat')
session.viewports['Viewport: 1'].view.setValues(nearPlane=3551.51, 
    farPlane=5207.38, width=2127.82, height=873.997, cameraPosition=(3676.52, 
    334.505, 3371.84), cameraUpVector=(-0.723065, 0.687496, 0.067274), 
    cameraTarget=(985.898, -47.2542, -38.6444))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3390, 
    farPlane=5492.92, width=2031.06, height=834.252, cameraPosition=(4596.26, 
    -1882.25, 1590.05), cameraUpVector=(-0.659749, 0.152455, 0.735859), 
    cameraTarget=(989.812, -56.689, -46.228))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3525.02, 
    farPlane=5395.77, width=2111.95, height=867.481, cameraPosition=(4009.31, 
    -3124.71, 685.595), cameraUpVector=(-0.535863, 0.148342, 0.831171), 
    cameraTarget=(979.153, -79.2531, -62.6537))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3514.59, 
    farPlane=5355.43, width=2105.71, height=864.914, cameraPosition=(3925.65, 
    -2535.19, 2023.23), cameraUpVector=(-0.606262, 0.424667, 0.672387), 
    cameraTarget=(977.285, -66.0895, -32.785))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3640.82, 
    farPlane=5230.86, width=2181.34, height=895.979, cameraPosition=(3295.79, 
    -3185.64, 1947.93), cameraUpVector=(-0.486863, 0.54037, 0.686268), 
    cameraTarget=(966.745, -76.9742, -34.045))
mdb.models['BP-2'].FieldOutputRequest(name='fe_top', 
    createStepName='Step-Stat', variables=('HSNFTCRT', 'HSNFCCRT', 'HSNMTCRT', 
    'HSNMCCRT'), layupNames=('Box.CompositeLayup-TOP', ), 
    layupLocationMethod=ALL_LOCATIONS, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
del mdb.jobs['Job-2']
mdb.Job(name='Job-2', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       11
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CM', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RM', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['BP-2'].fieldOutputRequests['fe_top'].setValues(variables=(
    'HSNFCCRT', 'HSNFTCRT', 'HSNMCCRT', 'HSNMTCRT'), layupNames=(
    'Box.CompositeLayup-TOP', ), layupLocationMethod=ALL_LOCATIONS, 
    rebar=EXCLUDE)
mdb.models['BP-2'].FieldOutputRequest(name='fe_bottom', 
    createStepName='Step-Stat', variables=('HSNFTCRT', 'HSNFCCRT', 'HSNMTCRT', 
    'HSNMCCRT'), layupNames=('Box.CompositeLayup-BOTTOM', ), 
    layupLocationMethod=ALL_LOCATIONS, rebar=EXCLUDE)
mdb.models['BP-2'].FieldOutputRequest(name='fe_side1', 
    createStepName='Step-Stat', variables=('HSNFTCRT', 'HSNFCCRT', 'HSNMTCRT', 
    'HSNMCCRT'), layupNames=('Box.CompositeLayup-SIDE1', ), 
    layupLocationMethod=ALL_LOCATIONS, rebar=EXCLUDE)
mdb.models['BP-2'].FieldOutputRequest(name='fe_side2', 
    createStepName='Step-Stat', variables=('HSNFTCRT', 'HSNFCCRT', 'HSNMTCRT', 
    'HSNMCCRT'), layupNames=('Box.CompositeLayup-SIDE2', ), 
    layupLocationMethod=ALL_LOCATIONS, rebar=EXCLUDE)
mdb.models['BP-2'].FieldOutputRequest(name='fe_spar', 
    createStepName='Step-Stat', variables=('HSNFTCRT', 'HSNFCCRT', 'HSNMTCRT', 
    'HSNMCCRT'), layupNames=('Box.CompositeLayup-SPAR', ), 
    layupLocationMethod=ALL_LOCATIONS, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
del mdb.jobs['Job-2']
mdb.Job(name='Job-2', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       11
#: Number of Node Sets:          7
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Composite layup']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Default']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['BP-2'].materials['S-glass/Epoxy'].elastic.setValues(type=LAMINA, 
    table=((48000.0, 11000.0, 0.3, 4200.0, 4200.0, 3600.0), ))
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
mdb.models['BP-2'].fieldOutputRequests['fe_bottom'].setValues(variables=(
    'CFAILURE', ), layupLocationMethod=ALL_LOCATIONS)
mdb.models['BP-2'].fieldOutputRequests['fe_side1'].setValues(variables=(
    'CFAILURE', ), layupLocationMethod=ALL_LOCATIONS)
mdb.models['BP-2'].fieldOutputRequests['fe_side2'].setValues(variables=(
    'CFAILURE', ), layupLocationMethod=ALL_LOCATIONS)
mdb.models['BP-2'].fieldOutputRequests['fe_spar'].setValues(variables=(
    'CFAILURE', ), layupLocationMethod=ALL_LOCATIONS)
mdb.models['BP-2'].fieldOutputRequests['fe_top'].setValues(variables=(
    'CFAILURE', ), layupLocationMethod=ALL_LOCATIONS)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
del mdb.jobs['Job-2']
mdb.Job(name='Job-2', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb')
#: Model: C:/Users/hakon/Skrivebord/Skole/Lettvekt Design/A4/Abaqus/Job-2.odb
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
    variableLabel='TSAIW', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3123.39, 
    farPlane=4994.03, width=1876.75, height=768.639, cameraPosition=(3961.94, 
    563.706, 2512.35), cameraUpVector=(-0.775094, 0.583415, 0.242603), 
    cameraTarget=(987.314, -65.2842, -31.6979))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3171.95, 
    farPlane=5068.72, width=1905.93, height=780.59, cameraPosition=(4235.01, 
    -2416.94, -66.0672), cameraUpVector=(-0.29063, 0.176774, 0.940364), 
    cameraTarget=(993.661, -134.565, -91.6298))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3024.57, 
    farPlane=5155.7, width=1817.37, height=744.322, cameraPosition=(4976.39, 
    -172.597, 165.549), cameraUpVector=(-0.386183, 0.161328, 0.908205), 
    cameraTarget=(1021.72, -49.6092, -82.8623))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3142.73, 
    farPlane=5083.31, width=1888.38, height=773.401, cameraPosition=(4273.38, 
    -2208.77, 712.671), cameraUpVector=(-0.376733, 0.359251, 0.853821), 
    cameraTarget=(1000.1, -112.216, -66.0399))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3053.45, 
    farPlane=5152.85, width=1834.73, height=751.431, cameraPosition=(4713.2, 
    -1267.75, 729.528), cameraUpVector=(-0.445505, 0.291852, 0.846373), 
    cameraTarget=(1016, -78.2072, -65.4307))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3032.78, 
    farPlane=5155.55, width=1822.31, height=746.344, cameraPosition=(4874.55, 
    -317.748, 830.23), cameraUpVector=(-0.506359, 0.316726, 0.802051), 
    cameraTarget=(1021.46, -46.077, -62.0248))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2932.04, 
    farPlane=5256.29, width=3270.94, height=1339.64, viewOffsetX=179.243, 
    viewOffsetY=-55.468)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2931.54, 
    farPlane=5102.73, width=3270.38, height=1339.41, cameraPosition=(4212.68, 
    -2191.72, 498.888), cameraUpVector=(-0.263741, 0.446723, 0.854915), 
    cameraTarget=(914.132, -70.6104, -81.3493), viewOffsetX=179.213, 
    viewOffsetY=-55.4585)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2896.12, 
    farPlane=5251.41, width=3230.87, height=1323.23, cameraPosition=(4821.9, 
    -663.886, 780.35), cameraUpVector=(-0.429999, 0.487681, 0.759781), 
    cameraTarget=(991.008, -55.9559, -38.705), viewOffsetX=177.048, 
    viewOffsetY=-54.7885)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3005.06, 
    farPlane=5142.46, width=1805.65, height=739.522, viewOffsetX=192.855, 
    viewOffsetY=-64.8335)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3037.61, 
    farPlane=5163.24, width=1825.22, height=747.534, cameraPosition=(4950.46, 
    -445.465, 349.122), cameraUpVector=(-0.381212, 0.416628, 0.825287), 
    cameraTarget=(1025.32, -63.7123, -55.472), viewOffsetX=194.944, 
    viewOffsetY=-65.5359)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3105.29, 
    farPlane=5210.03, width=1865.89, height=764.192, cameraPosition=(4823.6, 
    -646.536, -1298.02), cameraUpVector=(-0.0105781, 0.31639, 0.94857), 
    cameraTarget=(1075.54, -90.971, -132.018), viewOffsetX=199.288, 
    viewOffsetY=-66.9961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3027.8, 
    farPlane=5136.23, width=1819.33, height=745.122, cameraPosition=(4798.54, 
    -1172.67, 192.046), cameraUpVector=(-0.337039, 0.275593, 0.900252), 
    cameraTarget=(986.339, -121.801, -89.0018), viewOffsetX=194.315, 
    viewOffsetY=-65.3242)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3046.44, 
    farPlane=5098.97, width=1830.53, height=749.711, cameraPosition=(4644.52, 
    -1598.99, -25.4718), cameraUpVector=(-0.309024, 0.188603, 0.932166), 
    cameraTarget=(959.354, -140.943, -124.529), viewOffsetX=195.511, 
    viewOffsetY=-65.7264)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3052.14, 
    farPlane=5003.45, width=1833.96, height=751.114, cameraPosition=(4214.19, 
    -2215.84, 484.292), cameraUpVector=(-0.4049, 0.248938, 0.879821), 
    cameraTarget=(895.265, -136.388, -129.504), viewOffsetX=195.877, 
    viewOffsetY=-65.8494)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3020.28, 
    farPlane=5098.9, width=1814.81, height=743.274, cameraPosition=(4640.87, 
    -1486.36, 430.93), cameraUpVector=(-0.380172, 0.282044, 0.880863), 
    cameraTarget=(950.92, -135.487, -93.9707), viewOffsetX=193.832, 
    viewOffsetY=-65.1619)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3022.41, 
    farPlane=5128, width=1816.09, height=743.798, cameraPosition=(4783.42, 
    -1161.59, 323.743), cameraUpVector=(-0.37857, 0.247173, 0.891959), 
    cameraTarget=(977.042, -135.605, -94.5721), viewOffsetX=193.969, 
    viewOffsetY=-65.2079)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3049.4, 
    farPlane=5156.59, width=1832.31, height=750.441, cameraPosition=(4922.8, 
    -803.53, -114.125), cameraUpVector=(-0.307346, 0.17558, 0.935259), 
    cameraTarget=(1014.97, -136.448, -110.626), viewOffsetX=195.701, 
    viewOffsetY=-65.7903)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3019.64, 
    farPlane=5147.72, width=1814.43, height=743.117, cameraPosition=(4871.72, 
    -755.69, 480.256), cameraUpVector=(-0.436783, 0.205089, 0.875876), 
    cameraTarget=(998.474, -130.966, -88.8141), viewOffsetX=193.791, 
    viewOffsetY=-65.1482)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3028.04, 
    farPlane=5132.02, width=1819.48, height=745.185, cameraPosition=(4802.59, 
    -1153.9, 193.958), cameraUpVector=(-0.36398, 0.199913, 0.9097), 
    cameraTarget=(981.143, -142.213, -104.734), viewOffsetX=194.33, 
    viewOffsetY=-65.3295)
session.viewports['Viewport: 1'].enableMultipleColors()
session.viewports['Viewport: 1'].setColor(initialColor='#BDBDBD')
cmap=session.viewports['Viewport: 1'].colorMappings['Composite layup']
session.viewports['Viewport: 1'].setColor(colorMapping=cmap)
session.viewports['Viewport: 1'].disableMultipleColors()
session.viewports['Viewport: 1'].view.setValues(nearPlane=3019.98, 
    farPlane=5055.82, width=1814.64, height=743.202, cameraPosition=(4444.46, 
    -1729.75, 775.271), cameraUpVector=(-0.46858, 0.260212, 0.844229), 
    cameraTarget=(919.24, -144.065, -104.831), viewOffsetX=193.813, 
    viewOffsetY=-65.1557)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3037.27, 
    farPlane=4984.62, width=1825.03, height=747.458, cameraPosition=(4126.59, 
    -2021.04, 1172.37), cameraUpVector=(-0.530823, 0.320892, 0.784382), 
    cameraTarget=(883.668, -134.956, -109.145), viewOffsetX=194.923, 
    viewOffsetY=-65.5288)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3025.24, 
    farPlane=5083.55, width=1817.8, height=744.498, cameraPosition=(4573.77, 
    -1650.61, 375.056), cameraUpVector=(-0.391536, 0.216661, 0.894292), 
    cameraTarget=(934.927, -151.967, -103.52), viewOffsetX=194.151, 
    viewOffsetY=-65.2693)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3069.87, 
    farPlane=5038.93, width=1196.19, height=489.912, viewOffsetX=269.826, 
    viewOffsetY=-100.097)
leaf = dgo.LeafFromOdbElementPick(elementPick=(('BOX', 1, ('[#0:88 #200000 ]', 
    )), ), )
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2894.72, 
    farPlane=4833.49, width=1148.57, height=470.409, viewOffsetX=9.63473, 
    viewOffsetY=-2.77176)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2889.89, 
    farPlane=4849.43, width=1146.66, height=469.624, cameraPosition=(4542.68, 
    -1285.77, 115.069), cameraUpVector=(-0.350314, 0.186275, 0.917922), 
    cameraTarget=(931.017, 65.1671, -134.225), viewOffsetX=9.61866, 
    viewOffsetY=-2.76714)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2887.66, 
    farPlane=4896.92, width=1145.78, height=469.263, cameraPosition=(4774.06, 
    -353.23, -16.4845), cameraUpVector=(-0.342213, 0.193731, 0.919434), 
    cameraTarget=(934.559, 66.2597, -133.038), viewOffsetX=9.61125, 
    viewOffsetY=-2.76501)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2896.03, 
    farPlane=4908.38, width=1149.1, height=470.625, cameraPosition=(4785.28, 
    232.001, 167.713), cameraUpVector=(-0.409677, 0.106049, 0.906046), 
    cameraTarget=(936.225, 70.2089, -132.139), viewOffsetX=9.63912, 
    viewOffsetY=-2.77303)
#: Warning: The selected Primary Variable is not available in the current step/frame.
#: Warning: The selected Primary Variable is not available in the current step/frame.
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=1)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=2838.51, 
    farPlane=4820.94, width=1126.28, height=461.278, cameraPosition=(4445.59, 
    -1253.14, 784.076), cameraUpVector=(-0.386297, 0.487527, 0.783002), 
    cameraTarget=(928.333, 63.1002, -125.728), viewOffsetX=9.44767, 
    viewOffsetY=-2.71795)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Buck', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-Stat', frame=1)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TSAIW', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=2907.98, 
    farPlane=4828.71, width=1153.85, height=472.568, cameraPosition=(4466.01, 
    -1493.99, -161.332), cameraUpVector=(-0.302649, 0.120408, 0.945466), 
    cameraTarget=(928.686, 60.8923, -129.343), viewOffsetX=9.6789, 
    viewOffsetY=-2.78447)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2905.03, 
    farPlane=4834.38, width=1152.68, height=472.091, cameraPosition=(4468.07, 
    -1484.01, -264.93), cameraUpVector=(-0.284196, 0.0991312, 0.953628), 
    cameraTarget=(928.784, 60.8162, -129.613), viewOffsetX=9.6691, 
    viewOffsetY=-2.78165)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2888.61, 
    farPlane=4856.43, width=1146.17, height=469.423, cameraPosition=(4576.35, 
    -1204.29, 49.4046), cameraUpVector=(-0.352072, 0.133655, 0.926381), 
    cameraTarget=(929.642, 61.0828, -128.7), viewOffsetX=9.61445, 
    viewOffsetY=-2.76593)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2872.53, 
    farPlane=4887.54, width=1139.79, height=466.811, cameraPosition=(4687.94, 
    -639.354, 444.54), cameraUpVector=(-0.455729, 0.11553, 0.882589), 
    cameraTarget=(931.319, 61.952, -127.624), viewOffsetX=9.56093, 
    viewOffsetY=-2.75053)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2928.71, 
    farPlane=4774.44, width=1162.08, height=475.941, cameraPosition=(4182.6, 
    -1949.04, 410.35), cameraUpVector=(-0.314122, 0.365942, 0.876022), 
    cameraTarget=(925.147, 59.0733, -126.225), viewOffsetX=9.74792, 
    viewOffsetY=-2.80432)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2921.03, 
    farPlane=4782.12, width=1311.72, height=537.226, viewOffsetX=16.0891, 
    viewOffsetY=11.5968)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2871.44, 
    farPlane=4905.66, width=1289.45, height=528.106, cameraPosition=(4752.14, 
    -511.749, -9.21847), cameraUpVector=(-0.349548, 0.110106, 0.930426), 
    cameraTarget=(931.356, 53.176, -127.131), viewOffsetX=15.8159, 
    viewOffsetY=11.3999)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2866.33, 
    farPlane=4910.77, width=1456.72, height=596.612, viewOffsetX=-0.975311, 
    viewOffsetY=19.0632)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2864.8, 
    farPlane=4889.44, width=1455.94, height=596.293, cameraPosition=(4566.15, 
    -1199.07, 285.521), cameraUpVector=(-0.397029, 0.172647, 0.901421), 
    cameraTarget=(932.158, 48.7024, -125.144), viewOffsetX=-0.974791, 
    viewOffsetY=19.053)
mdb.save()
#: The model database has been saved to "C:\Users\hakon\Skrivebord\Skole\Lettvekt Design\A4\Abaqus\Composite_beam_hakon.cae".
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#28294129 #14 ]', ), )
region4 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-BOTTOM']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
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
region5 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
region7 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-TOP']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1-Copy1', 
    region=region1, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2-Copy1', 
    region=region2, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3-Copy1', 
    region=region3, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4-Copy1', 
    region=region4, material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, 
    thickness=0.25, orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region5, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region7, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region8, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
#* NameError: name 'region8' is not defined
del mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-TOP']
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
p = mdb.models['BP-2'].parts['Box']
s = p.faces
side1Faces = s.getSequenceFromMask(mask=('[#d7529a94 #3 ]', ), )
normalAxisRegion = regionToolset.Region(side1Faces=side1Faces)
p = mdb.models['BP-2'].parts['Box']
e = p.edges
edges = e.getSequenceFromMask(mask=('[#220 #8000 ]', ), )
primaryAxisRegion = regionToolset.Region(edges=edges)
compositeLayup = mdb.models['BP-2'].parts['Box'].CompositeLayup(
    name='CompositeLayup-TOP', description='', elementType=SHELL, 
    offsetType=MIDDLE_SURFACE, symmetric=False, 
    thicknessAssignment=FROM_SECTION)
compositeLayup.Section(preIntegrate=OFF, integrationRule=SIMPSON, 
    thicknessType=UNIFORM, poissonDefinition=DEFAULT, temperature=GRADIENT, 
    useDensity=OFF)
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
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region5, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region7, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=90.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region8, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
compositeLayup.ReferenceOrientation(orientationType=DISCRETE, localCsys=None, 
    additionalRotationType=ROTATION_NONE, angle=0.0, 
    additionalRotationField='', axis=AXIS_3, stackDirection=STACK_3, 
    normalAxisDefinition=SURFACE, normalAxisRegion=normalAxisRegion, 
    normalAxisDirection=AXIS_3, flipNormalDirection=False, 
    primaryAxisDefinition=EDGE, primaryAxisRegion=primaryAxisRegion, 
    primaryAxisDirection=AXIS_1, flipPrimaryDirection=False)
a = mdb.models['BP-2'].rootAssembly
a.regenerate()
a = mdb.models['BP-2'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['BP-2'].parts['Box']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2002 #20 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-SIDE1']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#800400 #8 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-SIDE2']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.resume()
layupOrientation = None
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region1 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region2 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region3 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region4 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region5 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region6 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region7 = regionToolset.Region(faces=faces)
p = mdb.models['BP-2'].parts['Box']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#40040 #40 ]', ), )
region8 = regionToolset.Region(faces=faces)
compositeLayup = mdb.models['BP-2'].parts['Box'].compositeLayups['CompositeLayup-SPAR']
compositeLayup.deletePlies()
compositeLayup.suppress()
compositeLayup.CompositePly(suppressed=False, plyName='Ply-1', region=region1, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-2', region=region2, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-3', region=region3, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-4', region=region4, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-5', region=region5, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=-45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-6', region=region6, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=45.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-7', region=region7, 
    material='S-glass/Epoxy', thicknessType=SPECIFY_THICKNESS, thickness=0.25, 
    orientationType=SPECIFY_ORIENT, orientationValue=0.0, 
    additionalRotationType=ROTATION_NONE, additionalRotationField='', 
    axis=AXIS_3, angle=0.0, numIntPoints=3)
compositeLayup.CompositePly(suppressed=False, plyName='Ply-8', region=region8, 
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
mdb.Job(name='Job-3', model='BP-2', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=1, numGPUs=0)
mdb.jobs['Job-3'].submit(consistencyChecking=OFF)
#: The job input file "Job-3.inp" has been submitted for analysis.
#: Job Job-3 completed successfully. 
