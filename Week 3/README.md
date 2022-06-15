# DS in LS Week 3

[[_TOC_]]

## Tasks
### Part 1
- Redo and understand an existing clustering approach for the CORD-19 data – or do your own.
- Find your cluster of interest, i.e. the one that contains mainly papers about your chosen topic (from week 2).
- Select at least 5 papers from this cluster that fit to your interest.
- Add the LINK and TITLE of these papers to a  table.

### Part 2
- Add a (or more) paper related to the chosen software (week 2) to the dataset. 
- Redo the clustering and identify the cluster the added paper(s) became a member of. (Does this make sense?)
- The papers that were added to the CORD-19 set can be found in Data_Collection/

### Part 3
- Create a dataset that contains only the selected papers by all the course participants.
- Perform the same clustering algorithm and analyse the resulting clusters. In your report, state for each cluster:
    - the number of contained articles,
    - the main keywords, and
    - a topic that describes – or summarizes – this cluster (e.g. “Diagnostics”).
- Optional: create a Word-Cloud for each cluster.

## How to run

### Download the data
For Task 1 and Task 2:
Download the CORD-19 data and kaggle resources and put the unzipped folders into the Week 3/ directory. The data is available here:
- [Kaggle: COVID-19 Open Research Dataset Challenge (CORD-19)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
- [Kaggle resources](https://www.kaggle.com/solonick/kaggle-resources)


For Task 3 (the storage directories can be set in the task 3 notebook, see below):
- [Kaggle: COVID-19 Open Research Dataset Challenge (CORD-19)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) / [Semantic Scholar (CORD-19)](https://www.semanticscholar.org/cord19/download)
- [Student picked papers](https://freieuniversitaetberlin-my.sharepoint.com/:x:/g/personal/tconrad_fu-berlin_de/EXggHxzqdrFNotODF3hUCM0BU2HSJyzOQTb0Mv0MsYd_8Q?e=L4PRP5)

### Task 1
- open the notebook [covid-19-literature-clustering-Task-1.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%203/covid-19-literature-clustering-Task-1.ipynb)
- make sure, the downloaded data lies in the same directory as the notebook
- run the notebook (the output is saved in Data\_Collection/Task\_1/)

### Task 2
- open the notebook [covid-19-literature-clustering-Task-2.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%203/covid-19-literature-clustering-Task-2.ipynb)
- make sure, the downloaded data lies in the same directory as the notebook
- run the notebook (the output is saved in Data\_Collection/Task\_2/)

### Task 3
- open the notebook:
    - [covid-19-literature-clustering-task3.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%203/covid-19-literature-clustering-task3.ipynb)
- Set the paths for the data and library directories in one of the first cells:
    - root_path (Path to the root of the CORD-19 data set from Kaggle / Semantic Sholar)
    - lib_path (Path where bokeh scripts should be stored)
    - student_df_path (Path to where the student picked papers file is stored)
- run the notebook

another version:
- download [covid-19-literature-clustering-task3-peng.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%203/covid-19-literature-clustering-task3-peng.ipynb), and put it into the folder where you put kaggle
- download [DSinLS-SS2020-List-peng.excel](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%203/DSLS-SS2020-List-peng.excel), put it under 'kaggle\input\CORD-19-research-challenge' 
- run the notebook