import numpy as np


# Define the objective function (you can replace this with any function you want to minimize)
def objective_function(x):
    return sum(x ** 2)


# Define the bounds for the decision variables
lower_bound = -5
upper_bound = 5

# Define parameters for the Clonal Selection Algorithm
population_size = 50
max_generations = 100
mutation_rate = 0.1
cloning_factor = 5

# Initialize population
population = np.random.uniform(low=lower_bound, high=upper_bound, size=(population_size, 2))

# Main loop of the Clonal Selection Algorithm
for generation in range(max_generations):
    # Evaluate affinity of antibodies (fitness)
    fitness = [objective_function(antibody) for antibody in population]

    # Sort population based on fitness (minimization problem)
    sorted_indices = np.argsort(fitness)
    population = population[sorted_indices]
    fitness = [fitness[i] for i in sorted_indices]

    # Clone antibodies based on affinity (top clones have higher affinity)
    clones = np.repeat(population[:cloning_factor], cloning_factor, axis=0)

    # Introduce random mutations in cloned antibodies
    mutated_clones = clones + mutation_rate * np.random.uniform(low=-1, high=1, size=clones.shape)

    # Replace least fit antibodies with mutated clones
    population[-cloning_factor:] = mutated_clones[:cloning_factor]

    # Print the best solution found so far
    best_solution = population[0]
    best_fitness = fitness[0]
    print("Generation:", generation, "Best Solution:", best_solution, "Best Fitness:", best_fitness)

# Print the final best solution found by the algorithm
print("Final Best Solution:", best_solution, "Final Best Fitness:", best_fitness)
