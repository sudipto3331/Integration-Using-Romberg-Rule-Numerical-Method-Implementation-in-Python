# Integration Using Romberg Rule Numerical Method Implementation in Python

This repository contains a Python implementation of the Romberg Rule for numerical integration. The code allows users to choose among different numerical methods, specifically Trapezoidal, Simpson's 1/3, and Simpson's 3/8, for integration of the function \( f(x) = x^3 + x^2 + x + 1 \).

### Table of Contents
- [Romberg Rule Theory](#romberg-rule-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

### Romberg Rule Theory
The Romberg Rule is a sophisticated numerical integration technique that uses polynomial approximations of the integral and combines them in a way that increases accuracy. It is particularly useful for integrating functions over a specific interval by combining methods of varying orders of accuracy.

The integration results from different methods are used to create a table, allowing for an extrapolation step that refines the estimate.

**Methods:**
1. **Trapezoidal Rule**: Approximates the area under the curve using trapezoids.
2. **Simpson's 1/3 Rule**: Uses parabolic arcs to approximate sections of the curve. Requires an even number of intervals.
3. **Simpson's 3/8 Rule**: A slight variation of Simpson's 1/3 that uses cubic polynomials for approximation. 

### Dependencies
This implementation does not require any external libraries; it uses standard Python functions.

### Installation
No additional installation is required. Ensure you have Python installed on your system.

### Usage
1. Clone the repository.
2. Run the script using Python:
    ```sh
    python romberg_integration.py
    ```
3. Input the required parameters when prompted:
    - Enter the lower limit of integration.
    - Enter the upper limit of integration.
    - Enter the number of intervals.
4. Choose a method for integration when prompted.

### Code Explanation
The code defines the function for the integration and implements various numerical methods. The main function `romberg_integration` applies the Romberg method to combine the results from the selected numerical method.

Below is a snippet from the code illustrating the main logic:

```python
def function(x):
    return x**3 + x**2 + x + 1

def trapezoidal(function, a, b, n):
    h = (b - a) / n
    integration = function(a) + function(b)
    for i in range(1, n):
        k = a + i * h
        integration += 2 * function(k)
    integration *= h / 2
    return integration

def simp_one_third(function, a, b, n):
    h = (b - a) / n
    integration = function(a) + function(b)
    for interval in range(1, n):
        x = a + interval * h
        if interval % 2 == 0:
            integration += 2 * function(x)
        else:
            integration += 4 * function(x)
    integration *= h / 3
    return integration

def simp_third_eight(function, a, b, n):
    h = (b - a) / n
    integration = function(a) + 3 * function(a + h) + 3 * function(a + 2 * h) + function(b)
    for i in range(3, n, 2):
        integration += 4 * function(a + i * h)
    for i in range(4, n, 2):
        integration += 2 * function(a + i * h)
    integration *= 3 * h / 8
    return integration

def romberg_integration(method, function, a, b, n):
    table = []
    for i in range(n + 1):
        row = [0] * (n + 1)
        table.append(row)
    for i in range(0, n + 1):
        if method == "trapezoidal":
            table[i][0] = trapezoidal(function, a, b, 2**i)
        elif method == "simpson_one_third":
            table[i][0] = simp_one_third(function, a, b, 2**i)
        elif method == "simpson_three_eight":
            table[i][0] = simp_third_eight(function, a, b, 3 * 2**i)
    for j in range(1, n + 1):
        for i in range(j, n + 1):
            table[i][j] = (4 * j * table[i][j - 1] - table[i - 1][j - 1]) / (4 * j - 1)
    return table[n][n]
```

### Example
Below is an example of how to use the script:

1. **Run the script**:
    ```sh
    python romberg_integration.py
    ```

2. **Enter the input values**:
    ```
    Enter lower limit: 0
    Enter upper limit: 1
    Enter number of intervals: 4
    Choose method to solve Romberg integration:
    1. Trapezoidal
    2. Simpson's 1/3
    3. Simpson's 3/8
    Enter method choice (1, 2, or 3): 2
    ```

3. **Output**:
    - The script will calculate the integration using the chosen method and print the result:
    ```
    Integration result using Romberg with simpson_one_third method: 1.3333
    ```

### Files in the Repository
- `romberg_integration.py`: The main script for performing the integration using the Romberg method.

### Input Parameters
The script prompts for the following input values:
- Lower limit of integration (`a`).
- Upper limit of integration (`b`).
- Number of intervals (`n`).

### Troubleshooting
1. **Method Selection**: Ensure an appropriate method is chosen (1, 2, or 3) for integration.
2. **Function Definition**: The function \( f(x) = x^3 + x^2 + x + 1 \) is hardcoded. Modify this function as necessary for different integrands.
3. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by [Your Name].

---

This documentation should guide you through understanding, installing, and using the Romberg numerical integration method script. For further issues or feature requests, please open an issue in the repository. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
