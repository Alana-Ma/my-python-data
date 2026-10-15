import random
import statistics
import matplotlib.pyplot as plt


def populate(num_rates,min_wt,max_mt,mode_wt):
    rates_wt = []
    for i in range(num_rates):
        rates_wt.append(int(random.triangular(min_wt,max_mt,mode_wt)))
    return rates_wt

def fitness(population,goal):
    ave = statistics.mean(population)
    return ave/goal

def select(population,to_retain):
    sorted_population = sorted(population)
    to_retain_bySex = to_retain//2
    member_per_sex = len(sorted_population)//2
    females = sorted_population[:member_per_sex]
    males = sorted_population[member_per_sex:]
    selected_Females = females[-to_retain_bySex:]
    selected_Males = males[-to_retain_bySex:]
    return selected_Males,selected_Females

def breed(males,females,litter_size):
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male,female in zip(males,females):
        for child in range(litter_size):
            child = random.randint(female,male)
            children.append(child)
    return children


def mutate(children,mutate_odds,mutate_min,mutate_max):
    for index,rat in enumerate(children):
        if random.random()<= mutate_odds:
            children[index] = round(rat*random.uniform(mutate_min,mutate_max))
    return children



GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.02
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTER_PER_YEAR = 10
GENERATION_LIMIT = 500


generation = 0
parents = populate(NUM_RATS,INITIAL_MIN_WT,INITIAL_MAX_WT,INITIAL_MODE_WT)
print("initial population weight - {}".format(parents))
pop_fitness = fitness(parents,GOAL)
print("Initial population fitness = {}".format(pop_fitness))
print("Number to retain is",NUM_RATS)

ave_wt = []
while pop_fitness <1 and generation < GENERATION_LIMIT:
    sel_males,sel_females = select(parents,NUM_RATS)
    children = breed(sel_males,sel_females,LITTER_SIZE)
    children = mutate(children,MUTATE_ODDS,MUTATE_MIN,MUTATE_MAX)
    parent = sel_males + sel_females + children
    pop_fitness = fitness(parents,GOAL)
    print("Generation:{} fitness = {:.4f}".format(generation,pop_fitness))
    ave_wt.append(int(statistics.mean(parents )))
    generation += 1

print("finish!")
print("Average weight per generation = {}".format(ave_wt))
print("Number of generation is",generation)
print("Number of years",generation//LITTER_PER_YEAR)

# 遗传算法也许并不能找到最优解 - “足够好”的解 - 随机性
