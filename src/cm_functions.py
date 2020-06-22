import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import gauss
from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor


def df_corr (df, th):
    """
    This function takes in a dataframe and correlation threshold where the 
    first column is the target (dependent variable) and the rest are features to be analyzed
    in a linear regression or multiple linear regression model. 
    We are looking for variables that are highly correlated with the target 
    variable but not collinear.
    Returns a list of positively correlated variables and a list of 
    negatively correlated variables. Also plots the heatmap, pair plots, 
    and prints the results summary.
    """
    import seaborn as sns
    sns.set(rc={'figure.figsize':(15, 15)})
    mask = np.triu(np.ones_like(df.corr(), dtype=np.bool))
    sns.heatmap(df.corr(), mask=mask);
    corrMatrix = df.corr()
    rows, cols = corrMatrix.shape
    flds = list(corrMatrix.columns)
    corr = df.corr().values
    neg_corr = []
    pos_corr = []
    print ("POSITIVE CORRELATIONS:")
    for j in range(1, cols):
        if corr[0,j] > th:
            print ('     ', flds[0], ' ', flds[j], ' ', corr[0,j])
            pos_corr.append(flds[j])
    print ("NEGATIVE CORRELATIONS:")
    for j in range(1, cols):
        if corr[0,j] < -th:
            print ('     ', flds[0], ' ', flds[j], ' ', corr[0,j])
            neg_corr.append(flds[j])
    # Pair Plots
    df_pos = df[pos_corr]
    df_neg = df[neg_corr]
    if pos_corr:
        sns.pairplot(df_pos)
    if neg_corr:
        sns.pairplot(df_neg)
    return pos_corr, neg_corr


def get_fsm (df):
    """
    FSM with Statsmodels
    how to call this function: fsm = get_fsm(df)
    - df argument should have target as first column 
    and features in the following columns
    - all column names should be strings

    returns fsm data and a print out of the summary, 
    rsquared and beta values for each feature
    """
    from statsmodels.formula.api import ols
    columns = list(df.columns)
    target = columns[0]
    features = columns[1:]
    features = '+'.join(features)
    formula = "{}~{}".format(target,features)
    fsm = ols(formula=formula, data=df).fit()
    rsquared = fsm.rsquared
    params = fsm.params
    print(f'Rsquared: {rsquared}')
    print('BETA values:')
    print(params)
    print('------------------------------------')
    print(' ')
    print(fsm.summary())
    return fsm

def lr_linear (fsm):
    """
    1. Linearity

    Linear regression assumes that the input variable linearly predicts the output variable. We already
    qualitatively checked that with the scatter plots, but it's also a good idea to use a statistical test.
    
    This one is the Rainbow test which is available from the diagnostic submodule of StatsModels
    """
    rainbow_statistic, rainbow_p_value = linear_rainbow(fsm)
    print("Rainbow statistic:", rainbow_statistic)
    print("Rainbow p-value:", rainbow_p_value)
    return rainbow_statistic,rainbow_p_value


def lr_qq (fsm):
    """
    2. Error Independence Assumption Check
    This function performs a qq plot
    Linear regression assumes that the residuals are independent. It is possible to check
    this qualitatively with a Q-Q plot. The fit model object has an attribute called resid, which is
    an array of the difference between predicted and true values. 
    """
    fsm_resids = fsm.resid
    import statsmodels.api as sm
    sm.qqplot(fsm_resids)
    return 


def lr_homoscad(fsm, df):
    """
    3. Homoscedasticity Assumption Check:
    We want to make sure that the variance of our residuals is the same across our data.
    This function outputs:
    - A scatter plot of the residuals along the fitted data in order to visually
    indicate how homoscedastic our residuals are. 
    """
#     - Perfoms the Breusch-Pagan Lagrange Multiplier test for heteroscedasticity and outputs
#     the results.
    fsm_resids = fsm.resid
    y_hat = fsm.predict()
    fig, ax = plt.subplots()
    ax.scatter(y_hat, fsm_resids)
    y = df.iloc[:,0]
#     lm, lm_p_value, fvalue, f_p_value = het_breuschpagan(y-y_hat, df.iloc[:, 1:])
#     print("Lagrange Multiplier p-value:", lm_p_value)
#     print("F-statistic p-value:", f_p_value)
#     print("\n")
#     print("The null hypothesis is homoscedasticity, alternative hypothesis is heteroscedasticity.\
#     Thus returning a low p-value means that the current model violates the homoscedasticity assumption")
    

def lr_independence (df):
    """
    4. Independence
    The independence assumption means that the independent variables must not be too collinear.
    """
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    rows = df.iloc[:, 1:].values
    vif_df = pd.DataFrame()
    vif_df["VIF"] = [variance_inflation_factor(rows, i) for i in range(len(df.columns)-1)]
    vif_df["feature"] = list(df.columns[1:])
    print(vif_df) 
    print("\n")
    print("VIF needs to be smaller than 5.")
    
def rpt_iwfnt (srp_df):
    srp_df = pd.merge(sales_and_res, parcels, on='PIN', how='inner', suffixes=('_sales', '_res'))
    srp_df['is_waterfront'] = (srp_df['WfntLocation'] != 0).astype('int')
    cat_dict = {0:'NOT WATERFRONT',1:'WATERFRONT'}
    srp_df['is_waterfront'] = pd.Categorical(srp_df['is_waterfront'].map(cat_dict))
    import matplotlib as mpl
    import matplotlib.pylab as pylab
    import seaborn as sns
    params = {'legend.fontsize': 'medium',
             'axes.labelsize': 'x-large',
             'axes.titlesize':'x-large',
             'xtick.labelsize':'large',
             'ytick.labelsize':'large'}
    pylab.rcParams.update(params)
    sns.set_style({'font.family':'Gill Sans MT', 'font.sans-serif':['Gill Sans']})
    sns.set(font_scale=2)
    sns.set_style("whitegrid")
    is_wfnt_labels = srp_df['is_waterfront'].unique()
    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_subplot(111)
    is_wfnt_boxplot = sns.boxplot(x=srp_df["is_waterfront"], y=srp_df["SalePrice"], data=srp_df,  ax=axes).set(
        xlabel=None, 
        ylabel='Sale Price'
    )
    fig.suptitle('2019 Waterfront Residential Housing Sale Price', fontsize=36)

    sns.set_style({'font.family':'Gill Sans MT', 'font.sans-serif':['Gill Sans']})
    axes.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
