import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class HeatDiffuser:
    def __init__(self, initialConditions, length, heatConstant, timeResolution):
        self.temperatureGrid = initialConditions
        self.length = length
        self.gridPoints = len(self.temperatureGrid)
        self.physicalResolution = self.length/self.gridPoints
        self.timeResolution = timeResolution
        self.temperatureHistory = [self.temperatureGrid]
        self.timeHistory = [0]
        self.heatConstant = heatConstant
        self.multiplicationConstant = self.heatConstant*(self.timeResolution/(self.physicalResolution)**2)

    def simulate(self, timeLimit:float):
        time = 0
        while time<timeLimit:
            time += self.timeResolution
            evolvingTemperatureGrid = [0]*self.gridPoints
            for count in range(self.gridPoints):
                tempAtPoint = self.temperatureGrid[count]
                if count==0 or count==self.gridPoints-1:
                    self.temperatureGrid[count] = 0
                    continue
                preTemp = self.temperatureGrid[count-1]
                postTemp = self.temperatureGrid[count+1]
                newTempAtPoint = tempAtPoint + self.multiplicationConstant*(postTemp-2*tempAtPoint+preTemp)
                evolvingTemperatureGrid[count] = newTempAtPoint
            self.temperatureGrid = evolvingTemperatureGrid
            self.temperatureHistory.append(self.temperatureGrid)
            self.timeHistory.append(time)
    
    def plot(self, save=False):
        fig, ax = plt.subplots()
        xAxis = np.arange(0, self.length, self.physicalResolution)
        line, = ax.plot(xAxis, self.temperatureHistory[0])
        ax.set_xlabel("Length")
        ax.set_ylabel("Temperature")
        def animate(i):
            line.set_ydata(self.temperatureHistory[i])
            # ax.text(0.95, 0.95, f"i = {i}", transform=ax.transAxes, ha='right')
            return line,
        ani = animation.FuncAnimation(
            fig, animate, frames=len(self.temperatureHistory), interval=50, blit=True
        )
        if save:
            ani.save("heatDiffusion.gif", writer="ffmpeg")
        else:
            plt.show()
