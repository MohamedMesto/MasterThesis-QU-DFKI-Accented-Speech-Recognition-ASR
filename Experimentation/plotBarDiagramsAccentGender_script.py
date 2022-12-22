############################## Bar chart: x='accent', y = 'accent_Duration_mean' Accent ='all Accent'#######################################
print("################################## Bar chart: x='accent', y = 'accent_Duration_mean' Accent ='all Accent' ###########################################")
# def plotBarChartsDurrationGenderAllAccent():
list_dataset_test_=['at','ca','ch','de_al','de_ni','de','fr','gb','it','ru','us']
list_dataset_test_accent=['Österreichisches Deutsch','Kanadisches Deutsch','Schweizerdeutsch','Alemannische Färbung,Schweizer Standart Deutsch','Niederländisch Deutsch',' Deutschland Deutsch','Französisch Deutsch	','Britisches Deutsch',' Italienisch Deutsch'
,'Russisch Deutsch','Amerikanisches Deutsch']

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
  
data_2 = {'Accent_short': ['at','ca','ch','de_al','de_ni','de','fr','gb','it','ru','us'],
                  'Accent_long': ['Österreichisches Deutsch','Kanadisches Deutsch','Schweizerdeutsch','Alemannische Färbung,Schweizer Standart Deutsch','Niederländisch Deutsch',' Deutschland Deutsch','Französisch Deutsch	','Britisches Deutsch',' Italienisch Deutsch'
,'Russisch Deutsch','Amerikanisches Deutsch']
                  }
dataset_accent = pd.DataFrame(data_2)



 
############################# 1- reading the dataset ##########################################################
dataset_validated_tsv = pd.read_csv('validated.tsv', sep='\t')


for i in range(0,len(dataset_accent)):


  accent_short_var=dataset_accent['Accent_short'][i]
  accent_long_var=dataset_accent['Accent_long'][i]

  ##

  # dataset_accent=f'dataset_test_{i}'
  # textfile_name=f'test_{i}.txt'
  dataset_test_ca = pd.read_csv(f'test_{accent_short_var}.txt', header=None, names=['audio_filepath','text','duration'])

  # dataset_test_ca=f'dataset_test_{i}'
  # extract the numeric values of the durations from the third Column and store it in a new column called
  dataset_test_ca['duration_numeric'] = dataset_test_ca['duration'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
  dataset_test_ca['duration_numeric'] =dataset_test_ca['duration_numeric'].div(10)
  # extract the numeric values of the durations from the third Column and store it in a new column called 
  #dataset_test_ca['audio_filepath_numeric'] = dataset_test_ca['audio_filepath'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)

  dataset_test_ca['audio_filepath_numeric'] = dataset_test_ca['audio_filepath'].str[-13:-5]



  # ############################# 2- extract the audio_filepath number and change them to integer################## 

  # get the audio file number and display it at dataset_validated_tsv['audio_filepath_numeric']
  dataset_validated_tsv['audio_filepath_numeric'] = dataset_validated_tsv['path'].str[-12:-4]
  dataset_validated_tsv['audio_filepath_numeric']=dataset_validated_tsv['audio_filepath_numeric'].astype('int')
  dataset_test_ca['audio_filepath_numeric']=dataset_test_ca['audio_filepath_numeric'].astype('int')

  ############################# 3- Drop all NaN gender and NaN Accent values, and show only the female gender and accent_long_var rows #############################
  dataset_validated_tsv.drop(dataset_validated_tsv[(dataset_validated_tsv['gender'] != 'female') | (dataset_validated_tsv['gender'].isna())| 
  (dataset_validated_tsv['accents'].isna())| (dataset_validated_tsv['accents']!=accent_long_var)].index, inplace=True)
  #dataset_validated_tsv



  ############################# 4- Merge using audio_filepath_numeric column ##################################
  ####################5-calculate the Mean of duration when the gender is female###########################
  dataset_test_ca_validated_tsv_female=pd.merge(dataset_test_ca,dataset_validated_tsv)
  dataset_test_ca_validated_tsv_female['gender']=dataset_test_ca_validated_tsv_female['gender'].astype("string")
  dataset_test_ca_validated_tsv_female['accent_Duration_mean_gender']=np.mean(dataset_test_ca_validated_tsv_female['duration_numeric'])
  #dataset_test_ca_validated_tsv_female

  ############################# 6- reading the dataset ##########################################################
  ############################# 7- extract the audio_filepath number and change them to integer################## 
  # get the audio file number and display it at dataset_validated_tsv['audio_filepath_numeric']

  dataset_validated_tsv = pd.read_csv('validated.tsv', sep='\t')
  dataset_validated_tsv['audio_filepath_numeric'] = dataset_validated_tsv['path'].str[-12:-4]
  dataset_validated_tsv['audio_filepath_numeric']=dataset_validated_tsv['audio_filepath_numeric'].astype('int')

  ############################# 8- Drop all NaN gender and NaN Accent values, and show only the male gender and accent_long_var rows #############################
  dataset_validated_tsv.drop(dataset_validated_tsv[(dataset_validated_tsv['gender'] != 'male') | (dataset_validated_tsv['gender'].isna())| (dataset_validated_tsv['accents'].isna())
  | (dataset_validated_tsv['accents']!=accent_long_var)].index, inplace=True)

  ############################# 9- Merge using audio_filepath_numeric column ##################################
  dataset_test_ca_validated_tsv_male=pd.merge(dataset_test_ca,dataset_validated_tsv)
  dataset_test_ca_validated_tsv_male['gender']=dataset_test_ca_validated_tsv_male['gender'].astype("string")

  #################### 10- calculate the Mean of duration when the gender is male###########################
  dataset_test_ca_validated_tsv_male['accent_Duration_mean_gender']=np.mean(dataset_test_ca_validated_tsv_male['duration_numeric'])
  #dataset_test_ca_validated_tsv_male
  ###### add/append the upper dataset dataset_test_ca_validated_tsv_female to the lower dataset dataset_test_ca_validated_tsv_male###########################
  ###### and call the result dataset_test_ca_validated_tsv_family
  dataset_test_ca_validated_tsv_family=dataset_test_ca_validated_tsv_female.append(dataset_test_ca_validated_tsv_male)
  dataset_test_ca_validated_tsv_family
  #################### 11- plot the dataset_test_ca_validated_tsv_family in Bar Chart #######################

  figure_duriation_distribution_accent=plt.figure(12,figsize=(20,20))  
  #plt.subplots(figure's number per column,figure's number per row)

  # Sup_plot_position=f'dataset_test_{i}'

  # Sup_plot_position=Sup_plot_position.astype(int)
  ax_duriation_distribution_accent_at=figure_duriation_distribution_accent.add_subplot(3,4,i+1)
  font1 = {'family':'serif','color':'blue','size':20}
  font2 = {'family':'serif','color':'darkred','size':15}

  plt.title(accent_long_var,fontdict  = font1)
  #ax.legend()
  ax = sns.barplot(x = 'gender', y = 'accent_Duration_mean_gender', data = dataset_test_at_validated_tsv_family)
 

  plt.savefig('plotBarDiagramsAccentGender_script.png')
