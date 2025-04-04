# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Buck')
    mdb.models['BP-1'].Gravity(name='Load-1', createStepName='Step-Buck', 
        comp3=-9810.0, distributionType=UNIFORM, field='')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-Stat')
    mdb.models['BP-1'].Gravity(name='Load-2', createStepName='Step-Stat', 
        comp3=-9810.0, distributionType=UNIFORM, field='')


