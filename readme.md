**Heat Diffusion Simulator**

![](https://raw.githubusercontent.com/thenu-k/HeatDiffuser/main/Media/heatDiffusion.gif)

This programme simulates heat diffusion in a single dimensional rod with Dirilecht boundary conditions using the finite differences method. 
The heat equation in one dimension is given by:

$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

where $u$ is the temperature, $t$ is time, $x$ is the position and $\alpha$ is the thermal diffusivity. Using the finite differences method, the heat equation can be discretised as follows:

$$u_i^{n+1} = u_i^n + \frac{\alpha \Delta t}{\Delta x^2} (u_{i+1}^n - 2u_i^n + u_{i-1}^n)$$

where $u_i^n$ is the temperature at position $x_i$ and time $t_n$.

To ensure stability, the following condition must be satisfied:

$$\frac{\alpha \Delta t}{\Delta x^2} \leq \frac{1}{2}$$


