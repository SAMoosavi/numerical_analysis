# Numerical Analysis

A collection of Python scripts implementing basic numerical analysis methods. This project covers topics such as differentiation, integration, interpolation, and solving systems of linear equations.

## Features

- **Differentiation**
  - Forward Difference (`forward_difference.py`)
  - Backward Difference (`backward_difference.py`)
  - Additional derivative calculations (`derivation.py`, `differential.py`)

- **Integration**
  - Numerical integration methods (`integral.py`)

- **Interpolation**
  - Lagrange Interpolation (`lagrange.py`)
  - Newton Interpolation (`newton.py`)
  - Neville Interpolation (`neville.py`)
  - General interpolation routines (`interpolation.py`)

- **Linear Systems**
  - Solving systems of linear equations (`system_of_linear_equations.py`)

- **Main Entry Point**
  - `main.py` brings all the functionality together for quick testing and demonstrations.

## Requirements

- Python 3.x

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/SAMoosavi/numerical_analysis.git
cd numerical_analysis
```

## Usage

You can run the main script to execute examples or test the implemented methods:

```bash
python main.py
```

Alternatively, each module can be run or imported individually for custom experiments and further development.

## Examples

Here's a simple example of how you might use one of the modules:

```python
from lagrange import lagrange_interpolation

# Sample data points
x = [1, 2, 3, 4]
y = [2.0, 3.0, 5.0, 4.0]

# Compute the interpolated value at x = 2.5
result = lagrange_interpolation(x, y, 2.5)
print(f"Interpolated value at x=2.5: {result}")
```

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or new numerical methods to add, feel free to open an issue or submit a pull request.
