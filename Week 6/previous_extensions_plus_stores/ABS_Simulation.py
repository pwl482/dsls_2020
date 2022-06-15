import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import animation, rc
from IPython.display import HTML

warnings.simplefilter('ignore')

from covid_abs.abs import *
from covid_abs.graphics import *

sim = Simulation(
    # Percentage of infected in initial population
    initial_infected_perc = 0.05,
    # Percentage of immune in initial population
    initial_immune_perc = 0.01,
    # Length of simulation environment
    length=500,
    # Height of simulation environment
    height=500,
    # Size of population
    population_size=1000,
    # percentage of people with medical preconditions
    condition_perc=0.2,
    # Minimal distance between agents for contagion
    contagion_distance=5.,
    # Maximum percentage of population which Healthcare System can handle simutaneously
    critical_limit=0.05,
    # Mobility ranges for agents, by Status
    amplitudes = {
        Status.Susceptible : 5,
        Status.Recovered_Immune : 5,
        Status.Infected : 5
        },
    # stores per 1000
    stores_per_thousand=4
)

anim = execute_simulation(sim, iterations=100)

#rc('animation', html='jshtml')
rc('animation', html='html5')
#anim

save_gif(anim, 'do_nothing.gif')