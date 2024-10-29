## Property of Anne-Lise Marais, 2024 {maraisannelise98@gmail.com}

##This code creates a single participants.tsv file for longitudinal BIDS data configuration, from a unified xslx/csv dataframe. This is used for KAOUENN project, please contact fanny.degeilh@inserm.fr for info

##scripted on ipython

##requirements
## pip install pandas
## pip intall numpy

#before running the script
#change paths lines 30 and line 59
#change columns name lines  41 and 48

##DEFS

def BIDS_id(data, session):
    #add BIDS identification
    data['BIDS_id'] = ['sub-0' + str(i).zfill(2) for i in range(1, len(data) + 1)]
    data.insert(0, 'BIDS_id', data.pop('BIDS_id'))
    #add session identification
    data.insert(1, 'session', session)
    return data

##MAIN

import pandas as pd

###import data
rawdata = pd.read_excel('.../BIDS/your-redcap-data.xlsx', header=0)

###merge data by subject_id
data_combined = rawdata.groupby('record_id').apply(lambda x: x.ffill().bfill().iloc[0])
data_combined = data_combined.reset_index(drop=True)

###Separate session 1 and 2 to create a longitudinal dataframe

##Session 1

#extract columns from ses-01
participants_ses01 = data_combined[['record_id','group','sex']]
#add BIDS identification
participants_ses01 = BIDS_id(participants_ses01, 'ses-01')

##Session 2

#extract columns from ses-02
participants_ses02 = data_combined[['record_id','irm_date',,'age_irm_nby','age_irm_nbm','age_irm_months']]

#add BIDS identification
participants_ses02 = BIDS_id(participants_ses02, 'ses-02')

###Merge

#merge session1 and session2
participants = pd.merge(participants_ses01, participants_ses02, on=['BIDS_id', 'record_id', 'session'], how='outer', suffixes=('_participants_ses01', '_participants_ses02')).sort_values(['BIDS_id', 'record_id', 'session']).reset_index(drop=True)

#save dataframe as tsv
participants.to_csv(".../BIDS/your-project-name/participants.tsv", index=False, header=True)