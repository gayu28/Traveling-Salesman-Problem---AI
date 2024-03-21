import subprocess
import random

def generate_inputs(N, P, N_mean, N_variance, K, random_seed):
    """
    Generate TSP input files using genTSP.py script.
    """
    command = f"python generate_TSP.py -n {N} -k {K} -u {N_mean} -v {N_variance} -p {P}"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    # Define ranges for parameters
   
    N_values = range(100, 1001, 100)  # Range of N from 50 to 1000
    N_mean_values =  range(50, 200, 50)# Plausible values for N_mean
    N_variance_values = range(5, 50, 10)  # Plausible values for N_variance
    K_values = [100, 500, 1000, 5000, 1000, 1500]  # Plausible values for K
    random_seed_values = [42, 123, 456]  # Plausible values for random_seed
    

    # Generate 100 random combinations of parameters
    for _ in range(10):
        N = random.choice(N_values)
        P = 1
        N_mean = random.choice(N_mean_values)
        N_variance = random.choice(N_variance_values)
        K = random.choice(K_values)
        random_seed = random.choice(random_seed_values)
        
        generate_inputs(N, P, N_mean, N_variance, K, random_seed)
