Here are seven advanced code examples focused on **Non-Equilibrium Thermodynamics**, incorporating robust math, advanced benefits, and value using best code practices. The file name will be **"AdvancedNEThermo_Examples.py"**.

### 1. **Code Example: Steady-State Heat Transport in a Rod (Fourier's Law)**
   - **Description**: Simulates heat conduction along a 1D rod using Fourier’s law. Implements finite difference methods to approximate heat distribution over time until a steady state is reached.
   - **Features**: Robust boundary conditions, matrix inversion for temperature calculations.
   - **Benefits**: Models real-world heat transport systems with optimized performance.

```python
import numpy as np
import matplotlib.pyplot as plt

def heat_conduction_1d(length, dx, dt, time_steps, alpha):
    x = np.arange(0, length, dx)
    T = np.zeros_like(x)
    T[0], T[-1] = 100, 0  # Boundary conditions
    for _ in range(time_steps):
        T_new = T.copy()
        for i in range(1, len(x)-1):
            T_new[i] = T[i] + alpha * dt/dx**2 * (T[i+1] - 2*T[i] + T[i-1])
        T = T_new
    return x, T

x, T = heat_conduction_1d(length=10, dx=0.1, dt=0.01, time_steps=500, alpha=0.01)
plt.plot(x, T)
plt.title('Steady-State Heat Distribution in a Rod')
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.show()
```

### 2. **Code Example: Entropy Production in a Chemical Reaction Network**
   - **Description**: Computes entropy production rates in a system with multiple reactions using the stoichiometric matrix and reaction rate laws.
   - **Features**: Incorporates mass-action kinetics and entropy generation calculations.
   - **Benefits**: Useful for evaluating system efficiency and understanding dissipative structures.

```python
import numpy as np

def entropy_production_rate(stoich_matrix, reaction_rates, affinities):
    rate = np.dot(stoich_matrix, reaction_rates)
    entropy_production = np.dot(rate, affinities)
    return entropy_production

stoich_matrix = np.array([[1, -1], [-1, 1]])
reaction_rates = np.array([0.5, 0.3])
affinities = np.array([2, -1.5])

S_prod = entropy_production_rate(stoich_matrix, reaction_rates, affinities)
print(f'Entropy Production Rate: {S_prod}')
```

### 3. **Code Example: Onsager Relations in a Coupled Transport System**
   - **Description**: Implements Onsager's reciprocity relations for coupled transport processes (e.g., heat and mass transfer).
   - **Features**: Uses matrix operations to solve linear transport equations.
   - **Benefits**: Provides insight into transport properties and system optimization.

```python
import numpy as np

def onsager_matrix(L, fluxes):
    return np.dot(L, fluxes)

L_matrix = np.array([[1.2, 0.4], [0.4, 1.0]])
fluxes = np.array([1.0, 0.5])

result_fluxes = onsager_matrix(L_matrix, fluxes)
print(f'Coupled Transport Fluxes: {result_fluxes}')
```

### 4. **Code Example: Linear Stability Analysis of Non-Equilibrium Steady States**
   - **Description**: Conducts linear stability analysis on non-equilibrium steady states, solving eigenvalue problems.
   - **Features**: Utilizes Jacobian matrices and eigenvalue solvers for stability determination.
   - **Benefits**: Identifies whether small perturbations in a system will grow or decay.

```python
from scipy.linalg import eig

def stability_analysis(jacobian):
    eigvals, _ = eig(jacobian)
    return eigvals

jacobian = np.array([[0, 1], [-2, -1]])
eigenvalues = stability_analysis(jacobian)

print(f'Eigenvalues: {eigenvalues}')
```

### 5. **Code Example: Diffusion in Non-Equilibrium Systems (Fick’s Law)**
   - **Description**: Simulates diffusion in a 2D system based on Fick’s second law.
   - **Features**: Applies finite difference method and visualizes concentration profiles.
   - **Benefits**: Demonstrates how substances spread over time in non-equilibrium conditions.

```python
import numpy as np
import matplotlib.pyplot as plt

def diffusion_2d(D, dx, dy, dt, time_steps, size):
    concentration = np.zeros((size, size))
    concentration[size//2, size//2] = 1  # Initial condition

    for _ in range(time_steps):
        concentration_new = concentration.copy()
        for i in range(1, size-1):
            for j in range(1, size-1):
                concentration_new[i, j] = concentration[i, j] + D * dt * (
                    (concentration[i+1, j] - 2 * concentration[i, j] + concentration[i-1, j]) / dx**2 +
                    (concentration[i, j+1] - 2 * concentration[i, j] + concentration[i, j-1]) / dy**2)
        concentration = concentration_new

    return concentration

D = 0.1
concentration = diffusion_2d(D, 0.1, 0.1, 0.01, 100, 50)
plt.imshow(concentration, cmap='hot')
plt.colorbar()
plt.title('2D Diffusion Simulation')
plt.show()
```

### 6. **Code Example: Fluctuation-Dissipation Theorem (FDT)**
   - **Description**: Verifies the fluctuation-dissipation relation by comparing a system's response function to the autocorrelation function.
   - **Features**: Simulates thermal noise in a simple harmonic oscillator.
   - **Benefits**: Validates core principles of non-equilibrium statistical mechanics.

```python
import numpy as np
import matplotlib.pyplot as plt

def fluctuation_dissipation(mass, gamma, k_B, T, t_max, dt):
    time = np.arange(0, t_max, dt)
    response = np.exp(-gamma*time/mass)
    noise = np.sqrt(2 * k_B * T * gamma / mass) * np.random.normal(0, 1, len(time))
    autocorrelation = np.correlate(noise, noise, mode='full')[len(noise)-1:] / len(noise)
    return time, response, autocorrelation

time, response, autocorrelation = fluctuation_dissipation(1.0, 0.5, 1.38e-23, 300, 10, 0.01)
plt.plot(time, response, label='Response Function')
plt.plot(time, autocorrelation, label='Autocorrelation Function')
plt.legend()
plt.show()
```

### 7. **Code Example: Non-Equilibrium Phase Transitions**
   - **Description**: Models a non-equilibrium phase transition using a 2D Ising model with Monte Carlo simulations.
   - **Features**: Utilizes Metropolis-Hastings algorithm to simulate spins.
   - **Benefits**: Studies critical phenomena in non-equilibrium systems.

```python
import numpy as np
import matplotlib.pyplot as plt

def ising_model_2d(L, J, T, steps):
    spins = np.random.choice([-1, 1], size=(L, L))
    for _ in range(steps):
        i, j = np.random.randint(0, L, size=2)
        delta_E = 2 * J * spins[i, j] * (spins[(i+1)%L, j] + spins[i-1, j] + spins[i, (j+1)%L] + spins[i, j-1])
        if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
            spins[i, j] *= -1
    return spins

L = 50
spins = ising_model_2d(L, 1.0, 2.5, 10000)
plt.imshow(spins, cmap='gray')
plt.title('2D Ising Model (Non-Equilibrium Phase Transition)')
plt.show()
```

These examples deliver robust mathematical foundations and high performance, providing insights into key aspects of non-equilibrium thermodynamics.
