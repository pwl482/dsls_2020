# Assignment Week 7

[[_TOC_]]

## Tasks
1.  Understand time-series prediction approaches
2.  Perform data-based time series prediction and compare three approaches on three different data sets. 
    -   Use the number of confirmed cases for (i) the real data for Germany, from (ii) one of yourSIR scenarios and from (iii) one of your agent-based scenarios. For the real data, use datafrom 01.03.2020-20.04.2020 for training and then predict 21.04.-30.04.2020. For the data from (ii) and (iii), choose some appropriate training and prediction range.
    -   Use the following prediction approaches:(a)  Use at least one "classical" time-series approach.(b)  Use the Prophet library.(c)  Use some ML algorithm, e.g. a LSTM neural network
    -   Compare the results of the approaches (qualitatively and using the Root Mean SquaredError)
3.  Compare data-based and model-based time series prediction
    -   Use the number of confirmed cases from (i) one of your SIR scenarios and from (ii) one of your agent-based scenarios. Choose some appropriate training and prediction range.
    1.  Fit your best SIR-based model to the data.
    2.  Use the best approach from the previous section.
    3.  Compare the results of the approaches (qualitatively and using the Root Mean SquaredError).
    
## Dependencies
- python3 with:
    - jupyter notebooks
    - numpy, pandas, matplotlib, datetime, scipy, math, fbprophet, glob, sklearn, pytorch, random, statsmodels, time

## Get the data
The data files were read with pandas using the filepaths representing the structure of this repository. SEIRCD\_daily.csv and do\_nothing_reduced.csv are located in this week's folder. RKI\_COVID19.csv is located in the folder of week 5.
- [SEICRD_daily.csv](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%207/correct_counting_for_rki_dataset_and_SEICRD/SEICRD_daily.csv) for the SEICRD daily compartment counts
- [do_nothing_reduced.csv](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%207/correct_counting_for_rki_dataset_and_SEICRD/do_nothing_reduced.csv) for the ABM daily data
- [RKI COVID19](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/data) for the daily real world data

## How to run
Run the linked notebooks:
-   In task 2, we perform thee time series prediction approaches on the [real data](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/tree/master/Week%207/Peng/task2_a.ipynb), the [SIR-generated data](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/tree/master/Week%207/Peng/task2_b.ipynb) and the [ABS-generated data](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/tree/master/Week%207/Peng/task2_c.ipynb).
-   In task 3, we compare [data-based and model-based time series prediction with respect to SIR-generated and ABS-generated data](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%207/Week7_Task3_data_vs_model_ts_prediction.ipynb)