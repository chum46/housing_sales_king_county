import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import gauss
from lin_reg import best_line
%matplotlib inline


def df_corr (df):
    """
    This function takes in a dataframe where the first column is the target 
    (dependent variable) and the rest are features to be analyzed. 
    We are looking for variables that are highly correlated with the target 
    variable.
    Returns a list of positively correlated variables and a list of 
    negatively correlated variables. Also plots the heatmap, pair plots, 
    and prints the results.
    """
    import seaborn as sns
    sns.set(rc={'figure.figsize':(8, 8)})
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
        if corr[0,j] > 0.5:
            print ('     ', flds[0], ' ', flds[j], ' ', corr[0,j])
            pos_corr.append(flds[j])
    print ("NEGATIVE CORRELATIONS:")
    for j in range(1, cols):
        if corr[0,j] < -0.5:
            print ('     ', flds[0], ' ', flds[j], ' ', corr[0,j])
            neg_corr.append(flds[j])
    # Pair Plots
    df_pos = df[pos_corr]
    df_neg = df[neg_corr]
    sns.pairplot(df_pos)
    sns.pairplot(df_neg)
    return pos_corr, neg_corr


def  (dfall):
    """
    FSM with Statsmodels
    """
    return none


def lr_linear (dfall):
    """
    Check the assumptions of Linear Regression
    1. Linearity

    Linear regression assumes that the input variable linearly predicts the output variable. We already
    qualitatively checked that with a scatter plot. But it's also a good idea to use a statistical test.
    This one is the Rainbow test which is available from the diagnostic submodule of StatsModels
    """
    return none

def lr_normality (dfall):
    """
    2. Normality

    Linear regression assumes that the residuals are normally distributed. It is possible to check
    this qualitatively with a Q-Q plot. The fit model object has an attribute called resid, which is
    an array of the difference between predicted and true values. Store the residuals in the variable
    below, show the qq plot, and interepret. You are looking for the theoretical quantiles and the
    sample quantiles to line up.
    """
    return none

def lr_homoscad(dfall):
    """
    3. Homoscadasticity

    Linear regression assumes that the variance of the dependent variable is homogeneous across
    different values of the independent variable(s). We can visualize this by looking at the predicted
    life expectancy vs. the residuals.
    """
    return none

def lr_independence (dfall):
    """
    4. Independence

    The independence assumption means that the independent variables must not be too collinear. Right
    now we have only one independent variable, so we don't need to check this yet.
    """
    return none


def best_line(X, Y):
    """This function plots the best-fit line for a group of datapoints broken into
    a set of independent variable values (X) and a set of dependent variable values (Y)"""
    import numpy as np
    from matplotlib import pyplot as plt
    
    X_bar = np.mean(X)
    Y_bar = np.mean(Y)
    
    X_diffs = np.asarray([i - X_bar for i in X])
    Y_diffs = np.asarray([i - Y_bar for i in Y])
    
    num = X_diffs.dot(Y_diffs)
    
    denom = np.sqrt((X_diffs ** 2).sum() * (Y_diffs ** 2).sum())
    
    r_pearson = num / denom
    
    beta_1 = r_pearson * Y_diffs.std() / X_diffs.std()
    
    beta_0 = Y_bar - beta_1 * X_bar
    
    Xs = np.linspace(np.min(X), np.max(X), 100)
    Ys = beta_1 * Xs + beta_0
    plt.plot(X, Y, 'ro', label='datapoints')
    plt.plot(Xs, Ys, 'k', label=f'y={round(beta_1, 2)}x+{round(beta_0, 2)}')
    plt.legend()
    plt.show();