import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import random
from deap import base, creator, tools, algorithms

# Load or generate data related to spray drying of coconut milk
# Replace X and y with your actual dataset
X = np.random.rand(100, 5)  # Example input data (replace with actual data)
y = np.random.rand(100)  # Example output data (replace with actual data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the evaluation function for the genetic algorithm
def evaluate(individual):
    # Decode individual (chromosome) and set genetic algorithm parameters
    neurons = individual[0]  # Number of neurons in the hidden layer
    layers = individual[1]  # Number of hidden layers

    # Create and train the neural network model
    model = MLPRegressor(hidden_layer_sizes=(neurons,) * layers, activation='relu', solver='adam', max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate the model on the testing set
    predictions = model.predict(X_test)
    mse = mean_squared_error(predictions, y_test)

    # Return the mean squared error as the fitness value
    return mse,

# Define genetic algorithm parameters
POPULATION_SIZE = 10
GENERATIONS = 5

# Create types for fitness and individuals in the genetic algorithm
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize toolbox
toolbox = base.Toolbox()

# Define attributes and individuals
toolbox.register("attr_neurons", random.randint, 1, 100)  # Number of neurons
toolbox.register("attr_layers", random.randint, 1, 5)  # Number of layers
toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.attr_neurons, toolbox.attr_layers), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Genetic operators
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=1, up=100, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create initial population
population = toolbox.population(n=POPULATION_SIZE)

# Run the genetic algorithm
for gen in range(GENERATIONS):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fitnesses = toolbox.map(toolbox.evaluate, offspring)
    for ind, fit in zip(offspring, fitnesses):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))

# Get the best individual from the final population
best_individual = tools.selBest(population, k=1)[0]

# Print the best parameters found
print("Best Parameters:", best_individual)
