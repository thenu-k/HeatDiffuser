from HeatDiffuser.HeatDiffuser import HeatDiffuser
import math

'''
Note: 
To prevent divergence, the following condition must be met:
heatConstant*(timeResolution/(physicalResolution)**2)<0.5
'''

diffuser = HeatDiffuser(
    initialConditions=[100*math.sin(x*math.pi/10)**2 for x in range(100)],
    length=50,
    heatConstant=1,
    timeResolution=0.01
)

diffuser.simulate(10)
diffuser.plot(save=True)