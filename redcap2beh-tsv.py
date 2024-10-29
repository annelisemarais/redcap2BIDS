##This code creates single tsv file by subjects for BIDS data configuration, from a unified xslx/csv dataframe
##This code saves the tsv files in each subjects folder

## Property of Anne-Lise Marais, 2024 {maraisannelise98@gmail.com}

##scripted on ipython

##requirements
## pip install pandas
## pip intall numpy

#before running the script, change path line 50 and 64


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
rawdata = pd.read_excel('Documents/BIDS/KAOUENN_raw_redcap.xlsx', header=0)

# Extract REACTIONS questionnaire responses at session1 (before merging data)
data_ses01 = rawdata.loc[rawdata['redcap_event_name'] == 'inc_arm_1',['record_id','reactions_cog_sympt','reactions_cog_manif','reactions_phy_sympt','reactions_phy_manif','reactions_behav_sympt','reactions_behav_manif','reactions_total_sympt','reactions_total_manif','reactions_yn_q1','reactions_yn_q2','reactions_yn_q3','reactions_yn_q4','reactions_yn_q5','reactions_yn_q6','reactions_yn_q7','reactions_yn_q8','reactions_yn_q9','reactions_yn_q10','reactions_yn_q11','reactions_yn_q12','reactions_yn_q13','reactions_yn_q14','reactions_yn_q15','reactions_yn_q16','reactions_yn_q17','reactions_yn_q18','reactions_yn_q19','reactions_yn_q20','reactions_yn_q21','reactions_yn_q22','reactions_yn_q23','reactions_yn_q24','reactions_yn_q25','reactions_yn_q26','reactions_yn_q27','reactions_yn_q28','reactions_yn_q29','reactions_yn_q30','reactions_yn_q31','reactions_yn_q32','reactions_yn_q33','reactions_yn_q34','reactions_yn_q35','reactions_yn_q36','reactions_yn_q37','reactions_yn_q38','reactions_yn_q39','reactions_yn_q40','reactions_yn_q41','reactions_yn_q42','reactions_yn_q43','reactions_yn_q44','reactions_yn_q45','reactions_yn_q46','reactions_yn_q47','reactions_yn_q48','reactions_severity_q1','reactions_severity_q2','reactions_severity_q3','reactions_severity_q4','reactions_severity_q5','reactions_severity_q6','reactions_severity_q7','reactions_severity_q8','reactions_severity_q9','reactions_severity_q10','reactions_severity_q11','reactions_severity_q12','reactions_severity_q13','reactions_severity_q14','reactions_severity_q15','reactions_severity_q16','reactions_severity_q17','reactions_severity_q18','reactions_severity_q19','reactions_severity_q20','reactions_severity_q21','reactions_severity_q22','reactions_severity_q23','reactions_severity_q24','reactions_severity_q25','reactions_severity_q26','reactions_severity_q27','reactions_severity_q28','reactions_severity_q29','reactions_severity_q30','reactions_severity_q31','reactions_severity_q32','reactions_severity_q33','reactions_severity_q34','reactions_severity_q35','reactions_severity_q36','reactions_severity_q37','reactions_severity_q38','reactions_severity_q39','reactions_severity_q40','reactions_severity_q41','reactions_severity_q42','reactions_severity_q43','reactions_severity_q44','reactions_severity_q45','reactions_severity_q46','reactions_severity_q47','reactions_severity_q48']]
data_ses01 = data_ses01.reset_index(drop=True)

#remember those columns
column_todelete = data_ses01.columns
#change column name to avoid conflict between reactions responses at ses01 and ses02
data_ses01.columns = ['ses01_' + col for col in data_ses01.columns]

#Add BIDS id
data_ses01 = BIDS_id(data_ses01,'ses-01')    

folderpath = '/Users/amarais/Documents/BIDS/shanoir_downloader-main/KAOUENN/KAOUENN'
save_data(data_ses01, "ses-01", folderpath)

#delete reactions-ses01 from intial df to avoid conflict between responses at ses01 and ses02
rawdata.loc[rawdata['redcap_event_name'] == 'inc_arm_1', column_todelete] = np.nan

# Merge data by subject_id
data_combined = rawdata.groupby('record_id').apply(lambda x: x.ffill().bfill().iloc[0])
data_combined = data_combined.reset_index(drop=True)

data_ses02 = data_combined[['record_id','reactions_cog_sympt','reactions_cog_manif','reactions_phy_sympt','reactions_phy_manif','reactions_behav_sympt','reactions_behav_manif','reactions_total_sympt','reactions_total_manif','reactions_yn_q1','reactions_yn_q2','reactions_yn_q3','reactions_yn_q4','reactions_yn_q5','reactions_yn_q6','reactions_yn_q7','reactions_yn_q8','reactions_yn_q9','reactions_yn_q10','reactions_yn_q11','reactions_yn_q12','reactions_yn_q13','reactions_yn_q14','reactions_yn_q15','reactions_yn_q16','reactions_yn_q17','reactions_yn_q18','reactions_yn_q19','reactions_yn_q20','reactions_yn_q21','reactions_yn_q22','reactions_yn_q23','reactions_yn_q24','reactions_yn_q25','reactions_yn_q26','reactions_yn_q27','reactions_yn_q28','reactions_yn_q29','reactions_yn_q30','reactions_yn_q31','reactions_yn_q32','reactions_yn_q33','reactions_yn_q34','reactions_yn_q35','reactions_yn_q36','reactions_yn_q37','reactions_yn_q38','reactions_yn_q39','reactions_yn_q40','reactions_yn_q41','reactions_yn_q42','reactions_yn_q43','reactions_yn_q44','reactions_yn_q45','reactions_yn_q46','reactions_yn_q47','reactions_yn_q48','reactions_severity_q1','reactions_severity_q2','reactions_severity_q3','reactions_severity_q4','reactions_severity_q5','reactions_severity_q6','reactions_severity_q7','reactions_severity_q8','reactions_severity_q9','reactions_severity_q10','reactions_severity_q11','reactions_severity_q12','reactions_severity_q13','reactions_severity_q14','reactions_severity_q15','reactions_severity_q16','reactions_severity_q17','reactions_severity_q18','reactions_severity_q19','reactions_severity_q20','reactions_severity_q21','reactions_severity_q22','reactions_severity_q23','reactions_severity_q24','reactions_severity_q25','reactions_severity_q26','reactions_severity_q27','reactions_severity_q28','reactions_severity_q29','reactions_severity_q30','reactions_severity_q31','reactions_severity_q32','reactions_severity_q33','reactions_severity_q34','reactions_severity_q35','reactions_severity_q36','reactions_severity_q37','reactions_severity_q38','reactions_severity_q39','reactions_severity_q40','reactions_severity_q41','reactions_severity_q42','reactions_severity_q43','reactions_severity_q44','reactions_severity_q45','reactions_severity_q46','reactions_severity_q47','reactions_severity_q48','pedsql_24_physique1','pedsql_24_physique2','pedsql_24_physique3','pedsql_24_physique4','pedsql_24_physique5','pedsql_24_physique6','pedsql_24_physique7','pedsql_24_physique8','pedsql_24_emotion1','pedsql_24_emotion2','pedsql_24_emotion3','pedsql_24_emotion4','pedsql_24_emotion5','pedsql_24_relation1','pedsql_24_relation2','pedsql_24_relation3','pedsql_24_relation4','pedsql_24_relation5','pedsql_24_ecole1','pedsql_24_ecole2','pedsql_24_ecole3','pedsql_57_physique1','pedsql_57_physique2','pedsql_57_physique3','pedsql_57_physique4','pedsql_57_physique5','pedsql_57_physique6','pedsql_57_physique7','pedsql_57_physique8','pedsql_57_emotion1','pedsql_57_emotion2','pedsql_57_emotion3','pedsql_57_emotion4','pedsql_57_emotion5','pedsql_57_relation1','pedsql_57_relation2','pedsql_57_relation3','pedsql_57_relation4','pedsql_57_relation5','pedsql_57_ecole1','pedsql_57_ecole2','pedsql_57_ecole3','pedsql_57_ecole4','pedsql_57_ecole5','sdq_q1','sdq_q2','sdq_q3','sdq_q4','sdq_q5','sdq_q6','sdq_q7','sdq_q8','sdq_q9','sdq_q10','sdq_q11','sdq_q12','sdq_q13','sdq_q14','sdq_q15','sdq_q16','sdq_24_q17','sdq_417_q17','sdq_q18','sdq_q19','sdq_24_q20','sdq_417_q20','sdq_24_q21','sdq_417_q21','sdq_q22','sdq_q23','sdq_24_q24','sdq_24_25','sdq_q25_oui_depuis','sdq_q25_oui_gene','sdq_q25_oui_maison','sdq_q25_oui_amis','sdq_q25_oui_apprenti','sdq_q25_oui_loisir','sdq_q25_oui_burden']]

#add BIDS id
data_test = BIDS_id(data_ses02,'ses-02')  


save_data(data_ses02, "ses-02", folderpath)