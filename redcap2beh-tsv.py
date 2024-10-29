## Property of Anne-Lise Marais, 2024 {maraisannelise98@gmail.com}

##This code creates single tsv file by subjects for BIDS data configuration, from a unified xslx/csv dataframe
##This code saves the tsv files in each subjects folder

##Case of a information spreaded in the redcap app, needing to extract data of ses-01 before merging ses-01 and ses-02 

##scripted on ipython

##requirements
## pip install pandas
## pip intall numpy

#before running the script 
#change paths lines 50 and 64
#change columns name lines 56, 71 and 77


import pandas as pd
import numpy as np
import os

##DEFS

def BIDS_id(data, session):
    #add BIDS identification
    data['BIDS_id'] = ['sub-0' + str(i).zfill(2) for i in range(1, len(data) + 1)]
    data.insert(0, 'BIDS_id', data.pop('BIDS_id'))
    #add session identification
    data.insert(1, 'session', session)
    return data

#save each tsv file in the corresp subject folder
def save_data(data, session, path):

    for sub, row in data.iterrows():
        # Transformer la ligne en DataFrame pour sauvegarde
        df = row.to_frame().T

        # Créer le nom du fichier et le chemin du dossier
        filename = f"{df['BIDS_id'].values[0]}_{session}_beh.tsv"
        folderpath = os.path.join(path, f"sub-00{sub+1}", session, 'beh')

        # Créer le dossier s'il n'existe pas
        os.makedirs(folderpath, exist_ok=True)

        # Sauvegarder en .tsv
        df.to_csv(os.path.join(folderpath, filename), sep='\t', index=False)


##MAIN

#Import data
rawdata = pd.read_excel('.../BIDS/your-redcap-data.xlsx', header=0)

# Extract REACTIONS questionnaire responses at session1 (before merging data)
data_ses01 = rawdata.loc[rawdata['redcap_event_name'] == 'your-row-name',['record_id','reactions_cog_sympt','reactions_cog_manif']]
data_ses01 = data_ses01.reset_index(drop=True)

#remember those columns
column_todelete = data_ses01.columns
#change column name to avoid conflict between reactions responses at ses01 and ses02
data_ses01.columns = ['ses01_' + col for col in data_ses01.columns]

#Add BIDS id
data_ses01 = BIDS_id(data_ses01,'ses-01')    

folderpath = '.../BIDS/your-study-name'
save_data(data_ses01, "ses-01", folderpath)

#delete reactions-ses01 from intial df to avoid conflict between responses at ses01 and ses02
rawdata.loc[rawdata['redcap_event_name'] == 'data_ses01-row-name', column_todelete] = np.nan

# Merge data by subject_id
data_combined = rawdata.groupby('record_id').apply(lambda x: x.ffill().bfill().iloc[0])
data_combined = data_combined.reset_index(drop=True)

data_ses02 = data_combined[['record_id','reactions_cog_sympt','reactions_cog_manif','pedsql_24_emotion2','pedsql_24_emotion3','sdq_q1','sdq_q2']]

#add BIDS id
data_test = BIDS_id(data_ses02,'ses-02')  


save_data(data_ses02, "ses-02", folderpath)