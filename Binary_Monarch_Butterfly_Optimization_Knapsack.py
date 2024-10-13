To solve the **0–1 Knapsack Problem** using a **novel Binary Monarch Butterfly Optimization (BMBO)** algorithm, we need to adapt the continuous nature of Monarch Butterfly Optimization (MBO) into a binary version. In the 0–1 knapsack problem, items are either included or excluded from the knapsack, and the goal is to maximize the total value without exceeding the weight capacity. These examples integrate AI and automation for optimization, while considering scalability, efficiency, and real-world economic constraints.

### File Name: `Binary_Monarch_Butterfly_Optimization_Knapsack.py`

### 1. **Binary Representation of Monarch Butterflies**
This code initializes a population of binary monarch butterflies, where each butterfly represents a solution to the knapsack problem. Each element in the binary vector represents whether an item is selected (1) or not (0).

```python
import numpy as np

# Problem parameters
n_items = 50
weights = np.random.randint(1, 20, size=n_items)  # Random weights
values = np.random.randint(10, 100, size=n_items)  # Random values
capacity = 100  # Maximum weight the knapsack can hold
n_butterflies = 30  # Population size

# Initialize binary population
population = np.random.randint(2, size=(n_butterflies, n_items))

# Fitness function to evaluate total value and weight
def fitness_function(solution):
    total_weight = np.sum(solution * weights)
    total_value = np.sum(solution * values)
    return total_value if total_weight <= capacity else 0
```
**Reasoning**: The binary representation ensures each butterfly corresponds to a valid knapsack solution. Fitness is computed based on the total value of selected items, constrained by the knapsack's weight capacity.

---

### 2. **Migration Operator in Binary Monarch Butterflies**
This migration operator allows butterflies to migrate between two zones, mimicking the migration process in real butterflies. For binary values, migration is performed by flipping bits with a certain probability.

```python
# Migration parameters
migration_rate = 0.3

def migrate(butterfly):
    for i in range(len(butterfly)):
        if np.random.rand() < migration_rate:
            butterfly[i] = 1 - butterfly[i]  # Flip bit
    return butterfly

# Apply migration to the population
for i in range(n_butterflies):
    population[i] = migrate(population[i])
```
**Reasoning**: Migration introduces diversity into the population by allowing bits to flip, thereby promoting exploration in the solution space. This increases the algorithm's ability to escape local optima.

---

### 3. **Adjustment Operator for Feasible Solutions**
This operator ensures that butterflies (solutions) remain within the feasible space, i.e., their total weight does not exceed the knapsack's capacity. Solutions exceeding the capacity are penalized.

```python
def adjust_solution(solution):
    while np.sum(solution * weights) > capacity:
        # Randomly drop an item to reduce weight
        drop_index = np.random.choice(np.where(solution == 1)[0])
        solution[drop_index] = 0
    return solution

# Apply adjustment to the population
population = np.array([adjust_solution(butterfly) for butterfly in population])
```
**Reasoning**: The adjustment operator ensures the solutions remain feasible by dropping items if the total weight exceeds the knapsack's capacity. This prevents invalid solutions from being considered during optimization.

---

### 4. **Monarch Butterfly Selection Based on Fitness**
This selection process chooses the best-performing butterflies (solutions) based on fitness scores. It uses a binary tournament selection to maintain diversity while favoring higher-quality solutions.

```python
def select_butterflies(population, fitness_scores):
    selected_population = []
    for i in range(len(population)):
        # Select two random butterflies and pick the fitter one
        idx1, idx2 = np.random.choice(len(population), 2, replace=False)
        selected_population.append(population[idx1] if fitness_scores[idx1] > fitness_scores[idx2] else population[idx2])
    return np.array(selected_population)

# Evaluate fitness of the population
fitness_scores = np.array([fitness_function(butterfly) for butterfly in population])

# Select the next generation of butterflies
population = select_butterflies(population, fitness_scores)
```
**Reasoning**: Tournament selection is computationally efficient and ensures that fitter solutions have a higher chance of survival while maintaining population diversity, preventing premature convergence.

---

### 5. **Dynamic Migration Rate Adjustment Based on Iteration**
To balance exploration and exploitation, the migration rate is dynamically adjusted over iterations, starting high to explore and gradually decreasing to focus on exploitation.

```python
def dynamic_migration_rate(iteration, max_iterations):
    return migration_rate * (1 - iteration / max_iterations)

# Apply dynamic migration over iterations
max_iterations = 100
for iteration in range(max_iterations):
    current_migration_rate = dynamic_migration_rate(iteration, max_iterations)
    population = np.array([migrate(butterfly) for butterfly in population])
```
**Reasoning**: Dynamically adjusting the migration rate allows the algorithm to explore more aggressively in the early stages and refine its search near the end, improving overall convergence performance.

---

### 6. **Parallelization of Fitness Evaluation for Large Populations**
This example uses parallelization to evaluate the fitness of multiple butterflies simultaneously, significantly improving computational efficiency in larger populations.

```python
from joblib import Parallel, delayed

# Parallel fitness evaluation
fitness_scores = Parallel(n_jobs=-1)(delayed(fitness_function)(butterfly) for butterfly in population)
```
**Reasoning**: Parallelization ensures scalability by leveraging multiple processors to handle larger populations and faster evaluations, leading to more efficient optimization in real-world scenarios.

---

### 7. **Binary Crossover Operator for Monarch Butterflies**
A binary crossover operator creates new solutions by recombining parent butterflies. This helps generate diverse offspring while inheriting traits from both parents.

```python
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, n_items - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# Apply crossover to generate offspring
offspring_population = []
for i in range(0, len(population), 2):
    parent1, parent2 = population[i], population[i + 1]
    child1, child2 = crossover(parent1, parent2)
    offspring_population.extend([child1, child2])
```
**Reasoning**: The crossover operator combines traits from two solutions, promoting diversity in the population while allowing the algorithm to explore new solutions. This helps avoid stagnation in the search process.

---

### 8. **Multi-Objective Optimization: Balancing Value and Weight**
This example extends BMBO to handle multi-objective optimization, allowing trade-offs between value and weight. It uses a weighted fitness function to ensure solutions are balanced between both objectives.

```python
def multi_objective_fitness(solution):
    total_weight = np.sum(solution * weights)
    total_value = np.sum(solution * values)
    weight_penalty = max(0, total_weight - capacity)  # Penalty for exceeding capacity
    return total_value - weight_penalty * 10  # Balance between value and weight

# Evaluate fitness based on multi-objective criteria
fitness_scores = np.array([multi_objective_fitness(butterfly) for butterfly in population])
```
**Reasoning**: Incorporating multi-objective optimization allows the algorithm to find solutions that balance value and weight, providing realistic trade-offs in real-world economic applications.

---

### Summary
These eight advanced code examples demonstrate the implementation of **Binary Monarch Butterfly Optimization (BMBO)** for solving the **0-1 knapsack problem** with AI-driven optimization and automation. The migration and selection operators ensure robust exploration, while crossover and dynamic adjustments refine the search. Scalability is achieved through parallelization, and multi-objective optimization allows balancing between competing goals. This approach delivers remarkable performance, scalability, and value in real-world scenarios.

**Key Aspects**:
- Binary representation and fitness evaluation for knapsack solutions
- Migration and adjustment operators to explore solution space
- Tournament selection and dynamic migration rate adjustment
- Parallelization for large-scale optimization and multi-objective trade-offs
