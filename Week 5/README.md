# DS in LS Week 5

[[_TOC_]]

## Tasks
1. Implement a SIR model to simulate Covid-19 spreading.
2. Extend your model, as described in the project proposal:
    1. Add a fourth category of the population for exposed (but not yet infectious) people. Thus 
        people become susceptible, exposed, infected, and finally recovered.
    2. Add a new parameter for the incubation period.
    3. Add a category for those who die, rather than recover, from COVID-19. And again, a new
        parameter for the likelihood of death or recovery. This would not be constant (but changes
        over time).
    4. Take more factors into account: at least population age proportions and two more (e.g. preexisting medical conditions).
    5. Consider the availability of hospital beds or ventilators which has an impact on the death rate.
    6. Make as many parameters time-dependent as possible, since it’s likely that parameters such
        as infection rates would fluctuate.
3. Fit the model to real-world data, either Germany or Berlin.
    1. Time range (at least): 01.03.2020 – 30.04.2020
    2. Possible data source: https://github.com/jgehrcke/covid-19-germany-gae
4. Perform simulations about various scenarios (with fitted version)
    1. This should include at least: lock-down, people are reducing social contacts a lot, people are
        reducing social contacts moderately, people are reducing social contacts moderately and are
        wearing masks.

## How to run

### Dependencies:
python 3 with the following libraries installed:
- scipy
- numpy
- matplotlib
- lmfit
- pandas
- datetime
- jupyter notebooks

### Data:
Download the RKI COVID19 dataset from this git (old version):
- [RKI COVID19](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%205/RKI_COVID19.csv)

Download the RKI COVID19 dataset from NPGEO (up to the current day):
- [RKI COVID19](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/data)

place it in the same directory as the scripts from this repository

### Run the notebooks
open one of the following notebooks using Jupyter Notebooks and run it:
- building the model from the ground up + fitting to the number of deaths: [DSinLS_Week_5_SEIRD_death_based.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%205/DSinLS_Week_5_SEIRD_death_based.ipynb)
- for fitting to the number of infected [DSinLS_Week_5_SEIRD_infected_based.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%205/DSinLS_Week_5_SEIRD_infected_based.ipynb)

