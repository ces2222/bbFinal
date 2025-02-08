## ReadMe - Essay 1 notebooks

* classification_algorithms_tests.ipynb - Shows how different ML models do on binary prediction of recession; random forest, SVM, logit, KNN, XGBoost, AdaBoost, Artificial NN, 
* Beige Book classification models.ipynb - Does random forest model; confusion matrix and feature importance graphs included
* descriptiveStats.ipynb - This file provides descriptive statistics and visualizations of the main variables in essay 1.
* Beige Book classification models_with_SMOTE_Youden.ipynb - Used SMOTE to balance dataset before training classification model of Beige Book sentiment; didn't end up using because it didn't help much; but could come back to it if requested
* control_variables.ipynb - This file contains code to obtain data by Federal Reserve district for: 1. Population (annual since 1970), 2. Unemployment (monthly, 1990-2015), 3. Job levels (monthly, 1990-present); just used job levels
* tokenizing_bb.ipynb - breaks Beige Books into chunks and randomly selects some
* regional_analysis.ipynb - This notebook extends the analysis done in the first paper to a regional level. Did not end up using it but could if requested.
* dv_import.ipynb - Uses a function to call FRED API to create DV - district coincident index; includes some plots
* Beige Book classification models regional.ipynb - does classification for 1 district; includes SMOTE, optimal threshold, confusion matrix, feature importance; did not use but could
* sentiment_calculations.ipynb - This file sets up the datasets. It can take some time to run. Subsequent analyses can just import the CSV files it creates: 1. bbNoText.csv is all of the numerical values, plus the dates. It doesn't include the Beige Books texts. It's a lot smaller file. 2. bbText.csv includes all of the Beige Book texts and the sentiment scores per sentence. It's a larger file.
