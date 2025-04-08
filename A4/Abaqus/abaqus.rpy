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
