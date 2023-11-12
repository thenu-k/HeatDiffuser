from HeatDiffuser.HeatDiffuser import HeatDiffuser
import math

'''
Note: 
To prevent divergence, the following condition must be met:
heatConstant*(timeResolution/(physicalResolution)**2)<0.5
'''

initialConditions = [0]*100
initialConditions[0] = 100
initialConditions[-1] = 100

diffuser = HeatDiffuser(
    initialConditions=initialConditions,
    constantPoints=[0,99],
    length=50,
    heatConstant=1,
    timeResolution=0.01
)

diffuser.simulate(
    timeLimit=1000
)
diffuser.animate(
    save=False,
    interval=1
)