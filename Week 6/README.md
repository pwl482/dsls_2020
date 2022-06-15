# Assignment Week 6

[[_TOC_]]

## Tasks
- Understand the Silva ABM model to simulate Covid-19 spreading [BACKGROUND](https://towardsdatascience.com/agent-based-simulation-of-covid-19-health-and-economicaleffects-6aa4ae0ff397), [CODE](https://colab.research.google.com/drive/1xXyRq9DSq9kjUxu8mf6By-d2GJvzjquk)
- Add calculation (and reporting) of the R parameter (average effective reproductive number) in each simulated time-step
- Try to fit the model to real-world data, either Germany or Berlin
- Extend your model
- Perform simulations for SOME scenarios, here:
    - add a category for the exposed but not yet infectious
    - take more factors into account, like pre-existing medical conditions
    - Add central location(s) that people use, here supermarkets

## Dependencies
- python3 with:
    - jupyter notebooks
    - numpy, pandas, matplotlib

## Installation and Data
for the simple model without extensions open:
- [Silva ABM model](https://colab.research.google.com/drive/1xXyRq9DSq9kjUxu8mf6By-d2GJvzjquk)

for the model with all extensions:
- copy the notebook for simulation into a directory of choice: [Week_6_scenarios_revised_Agent_Based_Simulation_of_COVID_19.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%206/scenarios/Week_6_scenarios_revised_Agent_Based_Simulation_of_COVID_19.ipynb)
- copy the folder [covid_abs](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/tree/master/Week%206/previous_extensions_plus_stores/covid_abs) and its content into the same directory

## How to run
- run the notebook: [Week_6_scenarios_revised_Agent_Based_Simulation_of_COVID_19.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%206/scenarios/Week_6_scenarios_revised_Agent_Based_Simulation_of_COVID_19.ipynb) or [Silva ABM model](https://colab.research.google.com/drive/1xXyRq9DSq9kjUxu8mf6By-d2GJvzjquk)