import warnings
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm
from scipy.stats._continuous_distns import _distn_names
import matplotlib
import matplotlib.pyplot as plt


data= pd.read_csv(r'C:\Users\exg7c\Desktop\University\Sem 5\Random\Project\data.csv');
data_main= pd.DataFrame(data);

data_80= data_main.sample(n=None, frac= 0.8, replace=False, weights=None, random_state= 1, axis=None)
data_20 = data_main.drop(data_80.index)

data_80.to_csv('data80.csv')
Data=pd.read_csv('data80.csv')
del Data['Unnamed: 0']

data_20.to_csv('data20.csv')
Data_test=pd.read_csv('data20.csv')
del Data_test['Unnamed: 0']

Attack_Dataframe=Data.groupby('Binary Label').get_group('Attack')
Normal_Dataframe=Data.groupby('Binary Label').get_group('Normal')
TCP_Dataframe=Data.groupby('Label').get_group('TCP-SYN')
Blackhole_Dataframe=Data.groupby('Label').get_group('Blackhole')
Overflow_Dataframe=Data.groupby('Label').get_group('Overflow')
PortScan_Dataframe=Data.groupby('Label').get_group('PortScan')
Diversion_Dataframe=Data.groupby('Label').get_group('Diversion')

pdf_Data = pd.DataFrame()
pdf_Attack_Dataframe = pd.DataFrame()
pdf_Normal_Dataframe = pd.DataFrame()
pdf_TCP_Dataframe = pd.DataFrame()
pdf_Blackhole_Dataframe = pd.DataFrame()
pdf_Overflow_Dataframe = pd.DataFrame()
pdf_PortScan_Dataframe = pd.DataFrame()
pdf_Diversion_Dataframe = pd.DataFrame()



# Create models from data
def best_fit_distribution(data, bins=200, ax=None):
    """Model data by finding best fit distribution to data"""
    # Get histogram of original data
    y, x = np.histogram(data, bins=bins, density=True)
    x = (x + np.roll(x, -1))[:-1] / 2.0

    # Best holders
    best_distributions = []

    # Estimate distribution parameters from data
    for ii, distribution in enumerate([d for d in _distn_names if not d in ['levy_stable', 'studentized_range']]):

        print("{:>3} / {:<3}: {}".format( ii+1, len(_distn_names), distribution ))

        distribution = getattr(st, distribution)

        # Try to fit the distribution
        try:
            # Ignore warnings from data that can't be fit
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore')
                
                # fit dist to data
                params = distribution.fit(data)

                # Separate parts of parameters
                arg = params[:-2]
                loc = params[-2]
                scale = params[-1]
                
                # Calculate fitted PDF and error with fit in distribution
                pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
                sse = np.sum(np.power(y - pdf, 2.0))
                
                # if axis pass in add to plot
                try:
                    if ax:
                        pd.Series(pdf, x).plot(ax=ax)
                except Exception:
                    pass

                # identify if this distribution is better
                best_distributions.append((distribution, params, sse))
        
        except Exception:
            pass

    
    return sorted(best_distributions, key=lambda x:x[2])

def make_pdf(dist, params, size=10000):
    """Generate distributions's Probability Distribution Function """

    # Separate parts of parameters
    arg = params[:-2]
    loc = params[-2]
    scale = params[-1]

    # Get sane start and end points of distribution
    start = dist.ppf(0.01, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.01, loc=loc, scale=scale)
    end = dist.ppf(0.99, *arg, loc=loc, scale=scale) if arg else dist.ppf(0.99, loc=loc, scale=scale)

    # Build PDF and turn into pandas Series
    x = np.linspace(start, end, size)
    y = dist.pdf(x, loc=loc, scale=scale, *arg)
    pdf = pd.Series(y, x)

    return pdf


    
for field in list(Normal_Dataframe.columns):
    if(Data[field].value_counts().count()>20):
        data= Data[field]
        ax = data.plot(kind='hist', bins=50, density=True, alpha=0.5, color=list(matplotlib.rcParams['axes.prop_cycle'])[1]['color'])
        # Find best fit distribution
        best_distibutions = best_fit_distribution(data, 200, ax)
        best_dist = best_distibutions[0]

        # Make PDF with best params 
        pdf = make_pdf(best_dist[0], best_dist[1])
        param_names = (best_dist[0].shapes + ', loc, scale').split(', ') if best_dist[0].shapes else ['loc', 'scale']
        param_str = ', '.join(['{}={:0.2f}'.format(k,v) for k,v in zip(param_names, best_dist[1])])
        dist_str = '{}({})'.format(best_dist[0].name, param_str)
        pdf_Normal_Dataframe[field]=[best_dist[0].name, param_str]
    else:
       probabilities=(Normal_Dataframe[field].value_counts()/Normal_Dataframe[field].count())
       pdf_Normal_Dataframe[field]=['discrete', probabilities]
        
pdf_Normal_Dataframe.to_csv('pdfs of the normal')
    
    