import pandas as pd
import scipy.stats as st
import statsmodels.api as sm
from scipy.stats._continuous_distns import _distn_names


Data=pd.read_csv('data80.csv')
del Data['Unnamed: 0']

Data_test=pd.read_csv('data20.csv')
del Data_test['Unnamed: 0']


TCP_Dataframe=Data.groupby('Label').get_group('TCP-SYN')

#probabilities of attacks and its types

probability_type=(Data['Label'].value_counts()/Data['Label'].count())
probability_TCP=probability_type[1]





data=pd.read_csv(r'C:\Users\exg7c\Desktop\University\Sem 5\Random\Project\pdfs80.csv');
pdf_Data=pd.DataFrame(data)
del pdf_Data['Unnamed: 0']
del pdf_Data['Binary Label']
del pdf_Data['Label']


data2=pd.read_csv(r'C:\Users\exg7c\Desktop\University\Sem 5\Random\Project\pdfsTCP.csv');
pdf_TCP_Dataframe=pd.DataFrame(data2)
del pdf_TCP_Dataframe['Unnamed: 0']
del pdf_TCP_Dataframe['Binary Label']
del pdf_TCP_Dataframe['Label']


def whichpdf(name, parameters, x,y):
    if (name=='mielke') & (parameters=='k=0.79, s=0.38, loc=-1242.78, scale=224953.37'):
        y=st.mielke.pdf(x,k=0.79, s=0.38, loc=-1242.78, scale=224953.37 )
    if (name=='mielke') & (parameters=='k=1.31, s=0.35, loc=-128.94, scale=22776.26'):
        y=st.mielke.pdf(x,k=1.31, s=0.35, loc=-128.94, scale=22776.26 )
    if (name =='foldcauchy') & (parameters=='c=0.00, loc=-3.45, scale=1123.17'):
        y=st.foldcauchy.pdf(x, c=0.00, loc=-3.45, scale=1123.17)
    if (name =='foldcauchy') & (parameters=='c=0.01, loc=41.00, scale=1175.80'):
        y=st.foldcauchy.pdf(x, c=0.01, loc=41.00, scale=1175.80)
    if (name =='burr12') & (parameters=='c=3.73, d=0.17, loc=-0.10, scale=88.71'):
        y=st.burr12.pdf(x, c=3.73, d=0.17, loc=-0.10, scale=88.71)
    if (name =='wald') & (parameters=='loc=-32.33, scale=121.74'):
        y=st.wald.pdf(x,loc=-32.33, scale=121.74 )
    if (name =='wald') & (parameters=='loc=-27.72, scale=108.90'):
        y=st.wald.pdf(x,loc=-27.72, scale=108.90 )
    if (name =='wald') & (parameters=='loc=-8.03, scale=45.76'):
        y=st.wald.pdf(x,loc=-8.03, scale=45.76 )
    if (name =='exponweib') & (parameters=='a=1.22, c=0.68, loc=-0.00, scale=55104.27'):
        y=st.exponweib.pdf(x,a=1.22, c=0.68, loc=-0.00, scale=55104.27 )
    if (name =='betaprime') & (parameters=='a=2.08, b=0.55, loc=-2.27, scale=1120.51'):
        y=st.betaprime.pdf(x, a=2.08, b=0.55, loc=-2.27, scale=1120.51)
    if (name =='betaprime') & (parameters=='a=2.88, b=0.54, loc=-1.92, scale=761.56'):
        y=st.betaprime.pdf(x, a=2.88, b=0.54, loc=-1.92, scale=761.56)
    if (name =='dgamma') & (parameters=='a=0.44, loc=-0.00, scale=23707.59'):
        y=st.dgamma.pdf(x,a=0.44, loc=-0.00, scale=23707.59 )
    if (name =='halfgennorm') & (parameters=='beta=0.48, loc=278.00, scale=5956.00'):
        y=st.halfgennorm.pdf(x, beta=0.48, loc=278.00, scale=5956.00)
    if (name =='halfgennorm') & (parameters=='beta=0.46, loc=-0.00, scale=5330.79'):
        y=st.halfgennorm.pdf(x, beta=0.46, loc=-0.00, scale=5330.79)
    if (name =='norminvgauss') & (parameters=='a=3.70, b=3.68, loc=-0.54, scale=83.57'):
        y=st.norminvgauss.pdf(x, a=3.70, b=3.68, loc=-0.54, scale=83.57)
    if (name =='invgauss') & (parameters=='mu=115.44, loc=-6304.76, scale=43651.12'):
        y=st.invgauss.pdf(x, mu=115.44, loc=-6304.76, scale=43651.12)
    if (name =='halfcauchy') & (parameters=='loc=6728.00, scale=108365.25'):
        y=st.halfcauchy.pdf(x, loc=6728.00, scale=108365.25)
    if (name =='levy') & (parameters=='loc=40.35, scale=142.15'):
        y=st.levy.pdf(x, loc=40.35, scale=142.15)
    if (name =='rdist') & (parameters=='c=8.03, loc=131.70, scale=132.13'):
        y=st.rdist.pdf(x, c=8.03, loc=131.70, scale=132.13)
    if (name =='t') & (parameters=='df=0.39, loc=3.58, scale=1.62'):
        y=st.t.pdf(x, df=0.39, loc=3.58, scale=1.62)
    if (name =='halfgennorm') & (parameters=='beta=0.44, loc=278.00, scale=1850.88'):
        y=st.halfgennorm.pdf(x, beta=0.44, loc=278.00, scale=1850.88)
    if (name =='cauchy') & (parameters== 'loc=3.69, scale=1.91'):
        y=st.cauchy.pdf(x, loc=3.69, scale=1.91)
    if (name =='gennorm') & (parameters=='beta=0.40, loc=0.00, scale=92.46'):
        y=st.gennorm.pdf(x, beta=0.40, loc=0.00, scale=92.46)
    if (name =='gilbrat') & (parameters=='loc=-19511.06, scale=58893.87'):
        y=st.gilbrat.pdf(x, loc=-19511.06, scale=58893.87)
    if (name =='gennorm') & (parameters=='beta=0.40, loc=0.00, scale=92.46'):
        y=st.gennorm.pdf(x, beta=0.40, loc=0.00, scale=92.46)
    if (name =='johnsonsb') & (parameters=='a=1.55, b=0.89, loc=-27.97, scale=16574.65'):
        y=st.johnsonsb.pdf(x, a=1.55, b=0.89, loc=-27.97, scale=16574.65)
    return y


probability_not_given=1
probability_given_TCP=1
number_of_row=5438
	   
for field in list (pdf_Data.columns):
    x=Data_test.iloc[number_of_row][field]
    name= pdf_Data.iloc[0][field]
    parameters=pdf_Data.iloc[1][field]
    y=1
    whichpdf(name, parameters,x,y)
    if name=='discrete':
        probabilities=(Data[field].value_counts()/Data[field].count())
        for k in range (len(probabilities)):
            if(probabilities.index[k]==x):
                y=probabilities.values[k]
            else:
                break;
                
    probability_not_given= y*probability_not_given
    
    #calculating the probability given TCP
    name2=pdf_TCP_Dataframe.iloc[0][field]
    parameters2=pdf_TCP_Dataframe.iloc[1][field]
    y=1
    whichpdf(name2, parameters2,x,y)
    if name2=='discrete':
        probabilities2=(TCP_Dataframe[field].value_counts()/TCP_Dataframe[field].count())
        for k in range (len(probabilities2)):
            if(probabilities2.index[k]==x):
                y=probabilities2.values[k]
            else:
                break;
                
    probability_given_TCP=y*probability_given_TCP
    
    
bayes_tcp=(probability_given_TCP*probability_TCP)/(probability_not_given)
final_bayes_tcp=bayes_tcp*100

print(final_bayes_tcp)


def comparison (final_bayes):
    if (final_bayes>24):
        print('TCP is expected')
    else:
        print('No TCP is expected')
        
comparison(final_bayes_tcp)
print('What really happened is: ' + Data_test.iloc[number_of_row]['Label'])



