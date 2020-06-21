### THIS PROJECT IS CURRENTLY IN PROGRESS

# Table of Contents

<!--ts-->
 * [Files and Folders of Note]
 * [General Setup Instructions]
 * [Context of Project]
 * [Preview of Results]
 * [Data]
 * [Process]
 * [Results]
 * [Strengths and Limitations]
 * [Real World Application]
<!--te-->

# Files and Folders of Note
```
.
├── README.md
├── notebooks
│   ├── exploratory
│   │   ├── 02_cm_download_and_explore_data.ipynb
│   └── report
│       └── 00_final_report_and_summary
├── references
│   └── 
├── reports
│   └── figures
│       └── 
└── src
    └── cm_functions.py
    |
    └── data_cleaning.py
    
```
#### Repo Navigation Links
 - [system requirements]
 - [presentation.pdf]
 - [final summary notebook](https://github.com/chum46/mod2_housing_sales/blob/master/notebooks/report/00_final_report_and_summary.ipynb)
 - [exploratory notebooks folder](https://github.com/chum46/mod2_housing_sales/tree/master/notebooks/exploratory)
 - [src folder](https://github.com/chum46/mod2_housing_sales/tree/master/src)
 - [references](https://github.com/chum46/mod2_housing_sales/tree/master/references)
 
# General Setup Instructions 

Ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/) 

### `housing` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `housing` conda environment. To do so, please run the following commands *in your terminal*:
```bash
# create the housing conda environment
conda env create -f environment.yml
# activate the housing conda environment
conda activate housing
# if needed, make housing available to you as a kernel in jupyter
python -m ipykernel install --user --name housing --display-name "Python 3 (housing)"
```

# Context of Project

This project is aimed to help homeowners and potential homeowners in King County understand how specific features affect home sale prices in the area. The data we will use can be downloaded from here: https://info.kingcounty.gov/assessor/DataDownload/default.aspx. Through our analysis our end goal is to build a statistical model that is representative of the real world data.

The following questions are addressed:

1. Does higher square footage increase home sale price?
2. Does having a porch increases home sale price?
3. Does having a waterfront increase home sale prices?
4. Does the presence of a nuisance (power lines, traffic noise, airport noise) lower home sale prices?
5. Using this data, can a statistical model be built that accurately represents housing prices in King County?


# Preview of Results
![Porch Bargraph](notebooks/exploratory/GPorch.png)

### Figure 1. 
We can see there is about a 200,000 difference in home Sale Price when a home has a porch addition. Showing houses with a porch on average have a higher over all value.


# Data
WIP

# Process
2. Does having a porch increases home sale price?
To adress this business question we had to craft the neccesary dataframes that would shows us the values pertaining to residences with a porch. This was done by residential building dataframe and finding all value columns values that pertain to a porch and create a data frame that matched that criteria. The same ideology was used to make a dataframe that consisted of residences without a porch. After, both dataframes were made they were then joined on the "PIN" column found within all dataframes created in prior section. The means of the mean sale price of the porch and no-porch data frames were taken and then plotted against one another.
# Results
When looking at the correlation bewtween sale price and porch there seems to be a correlation between the two. Properties that have a porch on avergae sold for a higher price than those that did not. There also seemd to minute linear correaltion between the target variable(SalePruce) and the feature(porches).  

# Application

WIP

# Next Steps

When it comes to analyzing the the significance of the porch data we can delve deeper into making a stronger correlation. Also, when looking at the square footage of a closed versus open porch there may be some correlations to sale price. Given time I beleive this could yield fruitful results. 
