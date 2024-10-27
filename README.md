# Monte Carlo Simulation - Area Estimation

This project uses the Monte Carlo method to estimate areas, such as the value of π (Pi) and areas under a decreasing exponential function. The estimation is done by generating random points within a bounded region and counting how many points fall within the desired area.

The code was developed in Python.


## Project Structure

```
monte-carlo-simulation/
├── demos/
│   ├── calculating_pi.ipynb       # Demonstrative notebook for calculating Pi
│   └── area_exponential.ipynb     # Demonstrative notebook for exponential area estimation
├── src/
│   ├── main.py                    # Main functions for the simulation
│   └── utils.py                   # Auxiliary classes for geometric shapes
├── visualizations/
│   ├── Exp_Estimation.png         # Graph showing exponential area estimation results
│   └── Pi_Estimation.png          # Graph showing Pi estimation results
└── README.md                      # Project documentation
```
```


## ❕ Description ❕

### Calculating Pi using the Monte Carlo Method

The code generates random points within a square that circumscribes a circle. The proportion of points that fall inside the circle, relative to the total points generated, is used to estimate the value of Pi. The accuracy of the estimate improves as the number of points increases.

### Calculating Areas under an Exponential Function

To estimate the area under a decreasing exponential function, the code generates random points in a square bounded by the function. The proportion of points that fall below the curve of the function is used to calculate the area under the curve.

## Code

- **`main.py`**: Contains the main functions for the simulation:
  - `pi_monte_carlo()`: Estimates the value of Pi.
  - `plot_points()`: Plots the Pi estimation against the number of points.
  - `estimate_exponential_area()`: Estimates the area under an exponential function.

- **`utils.py`**: Contains auxiliary classes for the simulation:
  - `Circle`: Represents a circle and contains methods to calculate its real area and check if a point is inside it.
  - `Square`: Represents a square and generates random points within its boundaries.
  - `exponential_function`: Represents a decreasing exponential function and contains methods to calculate the real area under the curve and check if a point is below the curve.

## How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MatheusChiconi/Monte-Carlo-Method-Calculator.git
   cd monte-carlo-simulation

2. **Install the requirements**:

   This project uses Python and `matplotlib.pyplot`. Please ensure that these are installed on your machine.
   
   To install `matplotlib`, you can use:
   ```bash
   pip install -r requirements.txt

3. **Visualize the code running**:
    
    If you only want to see the code in action, use the `demos/` directory and open a Jupyter notebook file.