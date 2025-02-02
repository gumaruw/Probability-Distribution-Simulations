# Probability Distribution Simulations

## Description
This project involves simulating different probability distributions (normal, binomial, poisson, exponential, etc.) and visualizing them. We use NumPy to generate the distributions and Matplotlib to plot their histograms. Additionally, we calculate summary statistics for each distribution.

## Usage
1. Run the `distributions.py` file.
2. The script will generate different probability distributions and plot their histograms.
3. The generated plots will be saved in the `plots/` directory.
4. Summary statistics for each distribution will be printed in the console.

## Techniques
- Random number generation with NumPy
- Probability concepts
- Statistical distributions
- Visualization with Matplotlib
- Summary statistics (mean, median, variance)

## Example Analyses
### Normal Distribution
- Mean: 0
- Standard Deviation: 1

### Binomial Distribution
- Number of Trials: 10
- Probability of Success: 0.5

### Poisson Distribution
- Lambda: 3

### Exponential Distribution
- Scale: 1

## Running the Script
1. Ensure you have the required dependencies installed:
   ```bash
   pip install numpy matplotlib
2. Run the script:
   ```bash
   python distributions.py

## Dependencies
- Python 3.x
- NumPy
- Matplotlib

## Example Output
Normal Distribution: mean=0.025252294242363617, median=0.01526122175876599, variance=0.965995470031564
![image](https://github.com/user-attachments/assets/63be8e53-b439-436a-b614-2c288955ccea)

Binomial Distribution: mean=5.01, median=5.0, variance=2.4898999999999996
![image](https://github.com/user-attachments/assets/9719c4fb-a725-4a80-9b95-d357794bc364)

Poisson Distribution: mean=2.933, median=3.0, variance=2.8345109999999996
![image](https://github.com/user-attachments/assets/20e1291e-4adf-45f5-adf5-556538bb9242)

Exponential Distribution: mean=1.0480187829318945, median=0.7301395919244639, variance=1.0815014878627593
![image](https://github.com/user-attachments/assets/357a6774-ae36-4d31-8c75-6f6efbe1138a)

## Generated Plots
- normal_distribution_mean0_std1.png: Shows the histogram of the normal distribution.
- binomial_distribution_n10_p0.5.png: Shows the histogram of the binomial distribution.
- poisson_distribution_lambda3.png: Shows the histogram of the poisson distribution.
- exponential_distribution_scale1.png: Shows the histogram of the exponential distribution.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
