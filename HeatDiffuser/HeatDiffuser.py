import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

class HeatDiffuser:
    def __init__(self, initialConditions, length, heatConstant, timeResolution, constantPoints=[]):
        self.temperatureGrid = initialConditions
        self.constantPoints = constantPoints
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
                if count in self.constantPoints:
                    evolvingTemperatureGrid[count] = tempAtPoint
                    continue
                preTemp = self.temperatureGrid[count-1]
                postTemp = self.temperatureGrid[count+1]
                newTempAtPoint = tempAtPoint + self.multiplicationConstant*(postTemp-2*tempAtPoint+preTemp)
                evolvingTemperatureGrid[count] = newTempAtPoint
            self.temperatureGrid = evolvingTemperatureGrid
            self.temperatureHistory.append(self.temperatureGrid)
            self.timeHistory.append(time)
    
    def animate(self, save=False, interval=50):
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
            fig, animate, frames=len(self.temperatureHistory), interval=interval, blit=True
        )
        if save:
            if not os.path.exists("Media"):
                os.mkdir("Media")
            ani.save("Media/heatDiffusion.gif", writer="ffmpeg")
        else:
            plt.show()
    
    def plot(self,frame=-1):
        xAxis = np.arange(0, self.length, self.physicalResolution)
        plt.plot(xAxis, self.temperatureHistory[frame])
        plt.xlabel("Length")
        plt.ylabel("Temperature")
        plt.show()
