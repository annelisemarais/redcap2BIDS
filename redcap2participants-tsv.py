## Property of Anne-Lise Marais, 2024 {maraisannelise98@gmail.com}

##This code creates a single participants.tsv file for BIDS data configuration, from a unified xslx/csv dataframe. This is used for KAOUENN project, please contact fanny.degeilh@inserm.fr for info

##scripted on ipython

##requirements
## pip install pandas
## pip intall numpy

#change paths line 17 and line 47 before running the script

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
rawdata = pd.read_excel('Documents/BIDS/KAOUENN_raw_redcap.xlsx', header=0)

###merge data by subject_id
data_combined = rawdata.groupby('record_id').apply(lambda x: x.ffill().bfill().iloc[0])
data_combined = data_combined.reset_index(drop=True)

###Separate session 1 and 2 to create a longitudinal dataframe

##Session 1

#extract columns from ses-01
participants_ses01 = data_combined[['record_id','group','sex','identification_complete','consent_1titulaire___1','consent_1titulaire___unk','consentement_complete','ci_age','ci_fr','ci_secu','ci_48h','ci_accidentel','ci_gcs','ci_pcs','critres_dinclusion_complete','cni_fam_accueil','cni_previous_tcc','cni_contreindication_mri','cni_diagnostic','cni_prema','cni_abus','cni_complication','cni_sedatif','critres_de_noninclusion_complete','injury_date','injury_time','firstcare_date','firstcare_time','injury_cause','injury_cause_other','injury_cause_description','tcc_symp_loc','tcc_symp_aoc','tcc_symp_amnesia','tcc_symp_headache','tcc_symp_emotion','tcc_symp_vomiting','tcc_symp_hematoma','tcc_symp_drowsiness','tcc_symp_fatigue','tcc_symp_dizziness','tcc_symp_sleep','tcc_symp_balance','tcc_symp_light','tcc_symp_noise','tcc_symp_concentration','tcc_symp_other','tcc_symp_other_specif','gcs_initial_eye','gcs_initial_verb','gcs_initial_motor','gcs_initial_eye_unk___0','gcs_initial_eye_unk___unk','gcs_initial_verb_unk___0','gcs_initial_verb_unk___unk','gcs_initial_motor_unk___0','gcs_initial_motor_unk___unk','gcs_initial_tot','gcs_initial_source','gcs_initial_source_other','gcs_low_eye','gcs_low_verb','gcs_low_motor','gcs_low_eye_unk___0','gcs_low_eye_unk___unk','gcs_low_verb_unk___0','gcs_low_verb_unk___unk','gcs_low_motor_unk___0','gcs_low_motor_unk___unk','gcs_low_tot','gcs_low_source','gcs_low_source_other','gcs15','gcs_reeval_date','gcs_reeval_time','oi_location','oi_location_other','oi_diag','oi_diag_other_specify','oi_severity','tcc_diag','tcc_fracture','tcc_fracture_location','tcc_fracture_nb','tcc_saignement','tcc_saignement_diag','tcc_saignement_diag_other','tcc_oi','tcc_oi_location','ct_yn','ct_data','ct_result','ct_abnormal','hospitalisation','hospit_duree','hospit_duree_unit','intubation','intubation_duree','chirurgie','chirurgie_detail','medicaments','ant_med','ant_med_diag1','ant_med_diag2','ant_med_diag3','ant_med_diag4','ant_med_diag5','ant_med_diag1_deb','ant_med_diag2_deb','ant_med_diag3_deb','ant_med_diag4_deb','ant_med_diag5_deb','ant_med_diag1_fin','ant_med_diag2_fin','ant_med_diag3_fin','ant_med_diag4_fin','ant_med_diag5_fin','ant_med_diag1_encours___1','ant_med_diag1_encours___unk','ant_med_diag2_encours___1','ant_med_diag2_encours___unk','ant_med_diag3_encours___1','ant_med_diag3_encours___unk','ant_med_diag4_encours___1','ant_med_diag4_encours___unk','ant_med_diag5_encours___1','ant_med_diag5_encours___unk','ant_med_diag1_medic','ant_med_diag2_medic','ant_med_diag3_medic','ant_med_diag4_medic','ant_med_diag5_medic','ant_chir','ant_chir_type_1','ant_chir_type_2','ant_chir_type_3','ant_chir_type_4','ant_chir_type_5','ant_chir_date_1','ant_chir_date_2','ant_chir_date_3','ant_chir_date_4','ant_chir_date_5','specialiste','specialiste_type_1','specialiste_type_2','specialiste_type_3','specialiste_type_4','specialiste_deb_1','specialiste_deb_2','specialiste_deb_3','specialiste_deb_4','specialiste_fin_1','specialiste_fin_2','specialiste_fin_3','specialiste_fin_4','specialiste_encours_1___1','specialiste_encours_1___unk','specialiste_encours_2___1','specialiste_encours_2___unk','specialiste_encours_3___1','specialiste_encours_3___unk','specialiste_encours_4___1','specialiste_encours_4___unk','traitement','questionnaire_medical_complete','taille','poids','pas','pad','temperature','examen_clinique_complete','taille_naissance','poids_naissance','perimcrane_naissance','caracteristiques_de_lenfant_a_la_naissance_complete','tel1','tel1_date','irmdrv','irm_date_prevue','appel_telephonique_n1_complete','tel2','tel2_date','ic_inc_verif','irm_red_confirm_2','appel_telephonique_n2_b4a7_complete']]

#add BIDS identification
participants_ses01 = BIDS_id(participants_ses01, 'ses-01')

##Session 2

#extract columns from ses-02
participants_ses02 = data_combined[['record_id','irm_date','earlyterm','adverse_event','trainement_modif','visite_de_suivi_n1_irm_complete','fam_irm','fam_irm_no','irm_parent','irm_cartoon','irm_loc','irm_loc_no','irm_loc_deb','irm_loc_end','irm_loc_trials','irm_loc_best','irm_loc_comment','irm_t1w','irm_t1w_no','irm_t1w_deb','irm_t1w_end','irm_t1w_trials','irm_t1w_best','irm_t1w_comment','irm_flair','irm_flair_no','irm_flair_deb','irm_flair_end','irm_flair_trials','irm_flair_best','irm_flair_comment','irm_swi','irm_swi_no','irm_swi_deb','irm_swi_end','irm_swi_trials','irm_swi_best','irm_swi_comment','irm_qsm','irm_qsm_no','irm_qsm_deb','irm_qsm_end','irm_qsm_trials','irm_qsm_best','irm_qsm_comment','irm_dwi','irm_dwi_no','irm_dwi_deb','irm_dwi_end','irm_dwi_trials','irm_dwi_best','irm_dwi_comment','irm_asl','irm_asl_no','irm_asl_deb','irm_asl_end','irm_asl_trials','irm_asl_best','irm_asl_comment','irm_rest','irm_rest_no','irm_rest_deb','irm_rest_end','irm_rest_trials','irm_rest_best','irm_rest_comment','irm_complete','questionnaires_parents','questionnaires_parents_no','questionnaires_de_suivi_parents_complete','inclusion_date','inclusion_visit','inclusion_visit_autre','finsuivi_date','lastprocess_date','finetude_date','finetude_visit','finetude_visit_autre','etude_tout','fin_adveevent','medinv_comment','attest_invest_date','attest_invest_nom','attest_invist_signature','fin_detude_complete','traitement_nom_1','traitement_nom_2','traitement_nom_3','traitement_nom_4','traitement_nom_5','traitement_nom_6','traitement_nom_7','traitement_nom_8','traitement_nom_9','traitement_nom_10','traitement_dosage_1','traitement_dosage_2','traitement_dosage_3','traitement_dosage_4','traitement_dosage_5','traitement_dosage_6','traitement_dosage_7','traitement_dosage_8','traitement_dosage_9','traitement_dosage_10','traitement_poso_1','traitement_poso_2','traitement_poso_3','traitement_poso_4','traitement_poso_5','traitement_poso_6','traitement_poso_7','traitement_poso_8','traitement_poso_9','traitement_poso_10','traitement_admin_1','traitement_admin_2','traitement_admin_3','traitement_admin_4','traitement_admin_5','traitement_admin_6','traitement_admin_7','traitement_admin_8','traitement_admin_9','traitement_admin_10','traitement_admin_autre_1','traitement_admin_autre_2','traitement_admin_autre_3','traitement_admin_autre_4','traitement_admin_autre_5','traitement_admin_autre_6','traitement_admin_autre_7','traitement_admin_autre_8','traitement_admin_autre_9','traitement_admin_autre_10','traitement_indic_1','traitement_indic_2','traitement_indic_3','traitement_indic_4','traitement_indic_5','traitement_indic_6','traitement_indic_7','traitement_indic_8','traitement_indic_9','traitement_indic_10','traitement_datedeb_1','traitement_datedeb_2','traitement_datedeb_3','traitement_datedeb_4','traitement_datedeb_5','traitement_datedeb_6','traitement_datedeb_7','traitement_datedeb_8','traitement_datedeb_9','traitement_datedeb_10','traitement_datefin_1','traitement_datefin_2','traitement_datefin_3','traitement_datefin_4','traitement_datefin_5','traitement_datefin_6','traitement_datefin_7','traitement_datefin_8','traitement_datefin_9','traitement_datefin_10','traitement_dateencours_1','traitement_dateencours_2','traitement_dateencours_3','traitement_dateencours_4','traitement_dateencours_5','traitement_dateencours_6','traitement_dateencours_7','traitement_dateencours_8','traitement_dateencours_9','traitement_dateencours_10','traitement_visitnum_1','traitement_visitnum_2','traitement_visitnum_3','traitement_visitnum_4','traitement_visitnum_5','traitement_visitnum_6','traitement_visitnum_7','traitement_visitnum_8','traitement_visitnum_9','traitement_visitnum_10','traitements_concomitants_complete','earlyterm_date','earlyterm_motif','earlyterm_daeth_date','earlyterm_violation','earlyterm_retrait','earlyterm_perdu','earlyterm_autre','sortie_prmature_de_ltude_complete','adverse_event_description','adverse_event_date','adverse_event_death___1','adverse_event_death___unk','adverse_event_death_date','adverse_event_death_cause','adverse_event_autopsie','adverse_event_vital___1','adverse_event_vital___unk','adverse_event_hospit___1','adverse_event_hospit___unk','adverse_event_hospit_deb','adverse_event_hospit_fin','adverse_event_hospit_encours','adverse_event_anomalie___1','adverse_event_anomalie___unk','adverse_event_invalid___1','adverse_event_invalid___unk','adverse_event_medic___1','adverse_event_medic___unk','adverse_event_medic_specif','adverse_event_lien','adverse_event_action','adverse_event_evol','adverse_event_decla_date','evenements_indesirables_complete','questionnaires_intro_timestamp','age_irm_nby','age_irm_nbm','age_irm_months','parentaleduc_titulaire1','parentaleduc_titulaire2','questionnaires_intro_complete']]

#add BIDS identification
participants_ses02 = BIDS_id(participants_ses02, 'ses-02')

###Merge

#merge session1 and session2
participants = pd.merge(participants_ses01, participants_ses02, on=['BIDS_id', 'record_id', 'session'], how='outer', suffixes=('_participants_ses01', '_participants_ses02')).sort_values(['BIDS_id', 'record_id', 'session']).reset_index(drop=True)

#save dataframe as tsv
participants.to_csv("/Users/amarais/Documents/BIDS/shanoir_downloader-main/KAOUENN/KAOUENN/participants.tsv", index=False, header=True)