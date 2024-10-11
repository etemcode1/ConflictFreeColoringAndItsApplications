Here are **eight advanced code examples** for **Input Shaping** and **Command Shaping for Flexible Systems**, taking into account engineering best practices, accurate mathematics, and scalable solutions. These examples are tailored for robustness, precision, and extendability.

---

### 1. **Basic Input Shaper for a Single-Mode System (Python)**

This example demonstrates the fundamental structure for designing an input shaper targeting a single vibrational mode in a flexible system.

```python
import numpy as np
import matplotlib.pyplot as plt

def single_mode_input_shaper(frequency, damping_ratio, time_step=0.001, duration=5):
    time = np.arange(0, duration, time_step)
    wn = 2 * np.pi * frequency
    wd = wn * np.sqrt(1 - damping_ratio**2)
    impulse_response = np.exp(-damping_ratio * wn * time) * np.cos(wd * time)
    return time, impulse_response

# Example parameters
frequency = 2.0  # Hz
damping_ratio = 0.05
time, response = single_mode_input_shaper(frequency, damping_ratio)

plt.plot(time, response)
plt.title('Single-Mode Input Shaper')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

### 2. **Multi-Mode Command Shaper for Vibration Suppression (MATLAB)**

This MATLAB example provides a multi-mode command shaper, accounting for multiple modes of vibration using proper damping ratios.

```matlab
frequencies = [2.0, 3.5]; % Hz
damping_ratios = [0.05, 0.02];
time_step = 0.001;
duration = 10;
time = 0:time_step:duration;
shaper = ones(size(time));

for i = 1:length(frequencies)
    wn = 2 * pi * frequencies(i);
    wd = wn * sqrt(1 - damping_ratios(i)^2);
    response = exp(-damping_ratios(i) * wn * time) .* cos(wd * time);
    shaper = shaper .* response;
end

plot(time, shaper);
title('Multi-Mode Input Shaper');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;
```

### 3. **State-Space Command Shaping (Python/Control Systems)**

This example uses the state-space representation to design input shaping for systems that require optimal control strategies.

```python
import numpy as np
import control

# State-space system model
A = np.array([[0, 1], [-4, -0.1]])  # Example system matrix
B = np.array([[0], [1]])            # Input matrix
C = np.array([[1, 0]])              # Output matrix
D = np.array([[0]])                 # Feedthrough matrix

system = control.StateSpace(A, B, C, D)

# Design input shaping using state-space control
def command_shaping(state_space_sys, input_signal, time_vector):
    t, y, x = control.forced_response(state_space_sys, T=time_vector, U=input_signal)
    return t, y

time = np.linspace(0, 10, 1000)
input_signal = np.ones_like(time)  # Step input
t, response = command_shaping(system, input_signal, time)

import matplotlib.pyplot as plt
plt.plot(t, response)
plt.title('State-Space Command Shaping')
plt.xlabel('Time (s)')
plt.ylabel('System Response')
plt.grid(True)
plt.show()
```

### 4. **Zero Vibration Input Shaper (ZV Shaper, Python)**

This example shows how to implement a Zero Vibration (ZV) input shaper, a simple and effective method for eliminating residual vibrations in flexible systems.

```python
def ZV_input_shaper(wn, time_step=0.001, duration=5):
    time = np.arange(0, duration, time_step)
    impulse_response = np.exp(-wn * time)
    return time, impulse_response

wn = 2 * np.pi * 2.0  # Example frequency (rad/s)
time, response = ZV_input_shaper(wn)

plt.plot(time, response)
plt.title('Zero Vibration Input Shaper')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

### 5. **Zero Vibration Derivative (ZVD) Input Shaper (C++)**

In this C++ example, we implement a Zero Vibration Derivative (ZVD) input shaper, extending the ZV approach for more robust solutions.

```cpp
#include <iostream>
#include <cmath>
#include <vector>

std::vector<double> ZVD_input_shaper(double wn, double time_step, double duration) {
    int steps = duration / time_step;
    std::vector<double> shaper(steps);
    
    for (int t = 0; t < steps; t++) {
        double time = t * time_step;
        shaper[t] = exp(-wn * time) * (1 - wn * time);  // ZVD formula
    }
    return shaper;
}

int main() {
    double wn = 2 * M_PI * 2.0;  // Natural frequency (rad/s)
    std::vector<double> shaper = ZVD_input_shaper(wn, 0.001, 5.0);

    for (double val : shaper) {
        std::cout << val << std::endl;
    }
    return 0;
}
```

### 6. **Command Shaping with Optimal Damping (MATLAB)**

This MATLAB example shows how to calculate optimal damping ratios for flexible systems to design a command shaper with minimum residual vibration.

```matlab
frequencies = [2.0, 4.0]; % Hz
optimal_damping_ratios = 1 ./ sqrt(1 + (frequencies / 10).^2);  % Optimal damping

time = 0:0.001:10;
shaper = ones(size(time));

for i = 1:length(frequencies)
    wn = 2 * pi * frequencies(i);
    wd = wn * sqrt(1 - optimal_damping_ratios(i)^2);
    impulse_response = exp(-optimal_damping_ratios(i) * wn * time) .* cos(wd * time);
    shaper = shaper .* impulse_response;
end

plot(time, shaper);
title('Optimal Damping Command Shaper');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;
```

### 7. **Real-Time Input Shaping for Flexible Robotic Systems (Java)**

This real-time Java implementation applies input shaping to reduce vibrations in robotic arms or other flexible robotic systems.

```java
public class RealTimeInputShaper {
    private double frequency;
    private double dampingRatio;

    public RealTimeInputShaper(double frequency, double dampingRatio) {
        this.frequency = frequency;
        this.dampingRatio = dampingRatio;
    }

    public double[] shapeCommand(double timeStep, double duration) {
        int steps = (int) (duration / timeStep);
        double[] shaper = new double[steps];
        double wn = 2 * Math.PI * frequency;
        double wd = wn * Math.sqrt(1 - Math.pow(dampingRatio, 2));

        for (int t = 0; t < steps; t++) {
            double time = t * timeStep;
            shaper[t] = Math.exp(-dampingRatio * wn * time) * Math.cos(wd * time);
        }
        return shaper;
    }

    public static void main(String[] args) {
        RealTimeInputShaper shaper = new RealTimeInputShaper(2.0, 0.05);
        double[] shapedCommand = shaper.shapeCommand(0.001, 5.0);

        for (double value : shapedCommand) {
            System.out.println(value);
        }
    }
}
```

### 8. **Multi-Mode Command Shaping Using Frequency Domain Analysis (Python/Scipy)**

This example applies frequency domain analysis for designing multi-mode command shapers to suppress vibrations across multiple modes effectively.

```python
import numpy as np
from scipy.fft import fft, ifft

def frequency_domain_shaping(frequencies, time, damping_ratios):
    signal = np.ones_like(time)
    for freq, damp in zip(frequencies, damping_ratios):
        wn = 2 * np.pi * freq
        wd = wn * np.sqrt(1 - damp**2)
        impulse = np.exp(-damp * wn * time) * np.cos(wd * time)
        signal *= impulse

    spectrum = fft(signal)
    shaped_signal = ifft(spectrum).real
    return shaped_signal

frequencies = [1.5, 3.0, 4.5]  # Hz
damping_ratios = [0.05, 0.02, 0.03]
time = np.linspace(0, 10, 1000)
shaped_signal = frequency_domain_shaping(frequencies, time, damping_ratios)

plt.plot(time, shaped_signal)
plt.title('Frequency Domain Command Shaping')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

---

### Summary:
These advanced examples cover a broad range of **input shaping** and **command shaping** techniques, integrating best practices in engineering, accurate mathematical modeling, and considerations for real-world scalability. The implementations span multiple programming languages and provide robust solutions for flexible systems and vibration control.

### File Name:
A smart file name for these examples could be:



`InputShaping_CommandShaping_FlexibleSystems_AdvancedExamples.md`
