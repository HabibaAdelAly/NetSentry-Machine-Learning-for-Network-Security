import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data= pd.read_csv(r'C:\Users\exg7c\Desktop\University\Sem 5\Random\Project\data.csv');

data_list= pd.DataFrame(data);
print("Data frame:")
print(data)
print("type:")
print(data.dtypes)

# Check if there is any missing data or inf data 
data_check_NaN = data.isnull().values.any()
print("    check missing data:")
print(data_check_NaN)
data_check_inf = data.isin([np.inf, -np.inf]).values.any()
print("check for the infinity:")
print(data_check_inf)


#Getting the number of categories in each field
for field in list(data.columns.values):
    print(field, data[field].value_counts().count(), sep = ': ', end = '\n')
    
# Getting  Maximum, Minimum , average and variance 
for field in (data.select_dtypes(include=np.number)):
    variance =data[field].var()
    print ("variance     ",variance)
    print(data[field].describe(),  end='\n\n')
   
# creating  the quarters ranges in an array   
q_limits=[]
first=0
for counter in range (4):
    last=first+len(data.index)//4
    q_limits+=[first,last]
    first=last+1
    
#sorting each column and creating the 4 quarters and geting Maximum, Minimum , average and variance 
dataNumbers=data.select_dtypes(include=np.number)
for column in dataNumbers:
    data2=dataNumbers.sort_values(by=[column])
    datafield=data2[column]
    print (datafield)
    i=0
    q=1
    while i<len(q_limits) :
        quarter=datafield.iloc[q_limits[i]:q_limits[i+1]]
        print ("The data in Quarter number",q ,"of ",column, ":", quarter)
        print ("variance =  ",quarter.var())
        print(quarter.describe(),  end='\n\n')
        print ("       ")
        i+=2
        q+=1

# Expanding the attack type into a number of fields equal to the number of attacks  and saving it in new dataframe
new_data=data.join(data.Label.str.get_dummies())
print (new_data)

#Creating new dataframe given a specific attack type to each attack type
TCP_Dataframe=data.groupby('Label').get_group('TCP-SYN')
Normal_Dataframe=data.groupby('Label').get_group('Normal')
Diversion_Dataframe=data.groupby('Label').get_group('Diversion')
Blackhole_Dataframe=data.groupby('Label').get_group('Blackhole')
Overflow_Dataframe=data.groupby('Label').get_group('Overflow')
PortScan_Dataframe=data.groupby('Label').get_group('PortScan')



#Calculating pdf/pmf/CDF to each field and plotting it (For both Continous and discrete data)
#calculating Conditional probabilities to each field given a specific Attack Type and plotting it (For both Continous and discrete data) 
for field in list(data.columns.values):
    plt.figure()
    plt.xlabel(field)
    #value_counts(normalize=True) relative frequencies 
    probabilities = data[field].value_counts(normalize=True)
    print(probabilities)
    # printing the conditional probability
    conditional_probabilities_TCP=TCP_Dataframe[field].value_counts(normalize=True)
    print("Conditional Probabilities given TCP-SYN:   ", conditional_probabilities_TCP, "\n\n")  
    
    conditional_probabilities_Normal=Normal_Dataframe[field].value_counts(normalize=True)
    print("Conditional Probabilities given Normal:   ", conditional_probabilities_Normal, "\n\n") 
    
    conditional_probabilities_Diversion=Diversion_Dataframe[field].value_counts(normalize=True)
    print("Conditional Probabilities given Diversion:   ", conditional_probabilities_Diversion, "\n\n")  
    
    conditional_probabilities_Blackhole=Blackhole_Dataframe[field].value_counts(normalize=True)
    print("Conditional Probabilities given Blackhole:   ", conditional_probabilities_Blackhole, "\n\n")  
    
    conditional_probabilities_Overflow=Overflow_Dataframe[field].value_counts(normalize=True)
    print("Conditional Probabilities given Overflow:   ", conditional_probabilities_Overflow, "\n\n")  
    
    conditional_probabilities_PortScan=PortScan_Dataframe[field].value_counts(normalize=True)
    print("Conditional Probabilities given PortScan:   ", conditional_probabilities_PortScan, "\n\n")  
    
    if data[field].value_counts().count()<=20 :
        plt.title('PMF')
        plt.stem(probabilities.index, probabilities.values)
        plt.figure()
        plt.title('CDF')
        plt.histogram(data[field],cumulative=True)
        plt.title('PMF given TCP-SYN')
        plt.figure()
        plt.stem(conditional_probabilities_TCP)
    else:
        plt.title('PDF')
        sns.kdeplot(data[field])
        plt.figure()
        plt.title('CDF')
        sns.kdeplot(data[field],cumulative=True)
        plt.title('PDF given TCP-SYN')
        plt.figure()
        sns.kdeplot(TCP_Dataframe[field])
   
#Plotting a scatter graph between two dependent/independent dields
plt.xlabel('Received Bytes')
plt.ylabel('Sent Bytes')
plt.scatter(data['Received Bytes'],data['Sent Bytes'])
plt.figure()
plt.xlabel('Received Packets')
plt.ylabel('Sent Packets')
plt.scatter(data['Received Packets'],data['Sent Packets']) 
plt.figure()
plt.xlabel('Packets Looked Up')
plt.ylabel('Matched Packets')
plt.scatter(data['Packets Looked Up'],data['Matched Packets']) 

#Joint Probability
plt.figure()
sns.jointplot(data=data,x='Received Packets',y='Sent Packets',kind='kde')
sns.jointplot(data=TCP_Dataframe,x='Received Packets',y='Sent Packets',kind='kde')
plt.show()


#corelation
corr=new_data.corr()
print(corr)
        

             


