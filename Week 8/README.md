# Assignment Week 8 + 9

[[_TOC_]]

## Tasks 
Analyzing the Epidemiological Outbreak of COVID-19: A Visual Exploratory Data Analysis (EDA) Approach
- Load row data
- Data pre processing
- Load Germany map
- Changepoint Analysis
- Choropleth map
    - Infection number in 16 Bundesländer
    - Death number in 16 Bundesländer
- Choropleth map over time
    - Infection number in 16 Bundesländer over time
    - Death number in 16 Bundesländer over time
- Bubble map over time
    - Infection number in 16 Bundesländer over time
    - Death number in 16 Bundesländer over time
- Bar chart
    - Comparative case analysis of 16 Bundesländer in Germany
    - Number of 16 Bundesländer in Germany to which COVID-19 spread over the time (line chart)
    - Number of Confirmed/Death/Recovered Cases in Germany (stacked bar chart)
    - Number of Confirmed cases in Germany
    - Number of Death cases in Germany
    - Number of Recovered cases in Germany
    - Number of Confirmed/Death/Recovered cases in Germany (with subplots)
- Tree map
    - Number of Confirmed cases in 16 Bundesländer
    - Number of Death cases in 16 Bundesländer
    - Number of Recovered cases in 16 Bundesländer
- Time Series Analysis
    - Change point detection for the number of infected cases per day for all 16 Bundesländer
    - 

## Dependencies
- python3 with:
    - jupyter notebooks
    - ruptures
	- plotly, plotly-orca
    - numpy, pandas, matplotlib, datetime, math
    - json, sys, changefinder
    - for MacOS, psutil needed to be installed in addition to plotyl-orca

## Get the data
- [RKI COVID19](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/data) for the daily real world data.
- [Map of Bundesländer in Germany](https://github.com/isellsoap/deutschlandGeoJSON/tree/master/2_bundeslaender)

## How to run
- Store the two data files into the same folder as the notebook below
- open [COVID-19_VEDA_and_Changepoints.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%208/COVID-19_VEDA_and_Changepoints.ipynb) and run it
