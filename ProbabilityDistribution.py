import numpy as np
import matplotlib.pyplot as plt
import os

def simulate_normal_distribution(mean=0, std_dev=1, num_samples=1000):
    """Simulates a normal distribution and plots the histogram."""
    samples = np.random.normal(mean, std_dev, num_samples)
    plt.figure()
    plt.hist(samples, bins=30, edgecolor='black', alpha=0.7, density=True)
    plt.title(f"Normal Distribution (mean={mean}, std_dev={std_dev})")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"plots/normal_distribution_mean{mean}_std{std_dev}.png")
    plt.show()

    # Calculate summary statistics
    mean_val = np.mean(samples)
    median_val = np.median(samples)
    variance_val = np.var(samples)
    print(f"Normal Distribution: mean={mean_val}, median={median_val}, variance={variance_val}")

def simulate_binomial_distribution(n=10, p=0.5, num_samples=1000):
    """Simulates a binomial distribution and plots the histogram."""
    samples = np.random.binomial(n, p, num_samples)
    plt.figure()
    plt.hist(samples, bins=30, edgecolor='black', alpha=0.7, density=True)
    plt.title(f"Binomial Distribution (n={n}, p={p})")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"plots/binomial_distribution_n{n}_p{p}.png")
    plt.show()

    # Calculate summary statistics
    mean_val = np.mean(samples)
    median_val = np.median(samples)
    variance_val = np.var(samples)
    print(f"Binomial Distribution: mean={mean_val}, median={median_val}, variance={variance_val}")

def simulate_poisson_distribution(lam=3, num_samples=1000):
    """Simulates a Poisson distribution and plots the histogram."""
    samples = np.random.poisson(lam, num_samples)
    plt.figure()
    plt.hist(samples, bins=30, edgecolor='black', alpha=0.7, density=True)
    plt.title(f"Poisson Distribution (λ={lam})")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"plots/poisson_distribution_lambda{lam}.png")
    plt.show()

    # Calculate summary statistics
    mean_val = np.mean(samples)
    median_val = np.median(samples)
    variance_val = np.var(samples)
    print(f"Poisson Distribution: mean={mean_val}, median={median_val}, variance={variance_val}")

def simulate_exponential_distribution(scale=1, num_samples=1000):
    """Simulates an exponential distribution and plots the histogram."""
    samples = np.random.exponential(scale, num_samples)
    plt.figure()
    plt.hist(samples, bins=30, edgecolor='black', alpha=0.7, density=True)
    plt.title(f"Exponential Distribution (scale={scale})")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"plots/exponential_distribution_scale{scale}.png")
    plt.show()

    # Calculate summary statistics
    mean_val = np.mean(samples)
    median_val = np.median(samples)
    variance_val = np.var(samples)
    print(f"Exponential Distribution: mean={mean_val}, median={median_val}, variance={variance_val}")

def main():
    # Create 'plots' directory if it doesn't exist
    if not os.path.exists("plots"):
        os.makedirs("plots")
    
    # Simulate and plot distributions
    simulate_normal_distribution(mean=0, std_dev=1, num_samples=1000)
    simulate_binomial_distribution(n=10, p=0.5, num_samples=1000)
    simulate_poisson_distribution(lam=3, num_samples=1000)
    simulate_exponential_distribution(scale=1, num_samples=1000)

if __name__ == "__main__":
    main()
