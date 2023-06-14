import pickle
from os import popen
import paths
import pandas as pd
import pandas as pd
import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt
import get_charge
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import scipy.stats as st

# read protein information
# with open('filename.pickle', 'rb') as handle:
#     proteins = pickle.load(handle)
# # get the unique names
# names = set(proteins.keys())
# unique_names = [name[0:len(name)//2] if len(name)%2 == 0 and name.count(name[0:len(name)//2]) == 2 else name for name in proteins.keys() ]

# get tf names
tf_names = [name.split('.')[0] for name in list(popen(f'ls {paths.tfs}'))]

# #make sure every name is unique
# name_str = ""
# for name in unique_names:
#     name_str+=name
# #make sure every tf is in the proteome data set
# counts = [1 for name in tf_names if name in name_str]
# print(counts.count(1) == len(counts),'// verification complete \\\\ '.upper()*3,sep = '\n')

# create a new dictionary with unique identifiers as keys
# protein_dictionary = {}
# for un in unique_names:
#     for key in proteins.keys():
#         if un in key:
#             protein_dictionary[un] = proteins[key]
# #Convert dictionary to a dataframe
# dataframe = pd.DataFrame.from_dict(protein_dictionary)
# dataframe = dataframe.transpose()
# dataframe['PROTEIN'] = list(dataframe.index)
# del dataframe['ID']
# # saving the dataframe
# print(dataframe.columns)
# dataframe.to_pickle('./save_files/proteins_dataframe.pkl')

# read data from pkl
# dataframe = pd.read_pickle('./save_files/proteins_dataframe.pkl')
# tf_names.remove('transcription_factors')
# tfs=[]
# ntfs = []
#
# dataframe.set_index('PROTEIN',inplace=True)
# for index in dataframe.index:
#     for tf in tf_names:
#         if tf in index:
#             tfs.append(dataframe.loc[index])
# create tfs dataframe
# transcription_factors_dataframe = pd.DataFrame.from_dict(tfs)

# for prot in dataframe.index:
#     if prot not in transcription_factors_dataframe.index:
#         ntfs.append(dataframe.loc[prot])
# create ntfs dataframe
# non_transcription_factors_dataframe = pd.DataFrame.from_dict(ntfs)

# saving ntfs and tf dataframes
# non_transcription_factors_dataframe.to_pickle('./save_files/ntfs.pkl')

# transcription_factors_dataframe.to_pickle('./save_files/tfs.pkl')

# read data from pkl
tf_df = pd.read_pickle('./save_files/tfs.pkl')
ntf_df = pd.read_pickle('./save_files/ntfs.pkl')

# combining them to make plotting easier
dfs = [tf_df, ntf_df]
combined_df = pd.concat(dfs)

# creating PROTEIN_TYPE column
types = []
for _ in range(len(tf_df)):
    types.append('TF')
for _ in range(len(ntf_df)):
    types.append('NTF')
combined_df['PROTEIN_TYPE'] = types

# plotting their absolute lengths:
tf_lengthts = []

ntf_lengthts = []
for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    length = line['LENGTH']
    if type == 'TF':
        tf_lengthts.append(length)
    else:
        ntf_lengthts.append(length)
#
# X = [tf_lengthts,ntf_lengthts]
# ax = sns.violinplot(data=X,fliersize=0,title = 'absolute lengths')
# ax.set_xticklabels(['TF','NTF'])
# ax.set(title = 'Protein_Lengths')
# plt.savefig(f'/home/metehan/Desktop/Plots/Protein_Lengths.pdf', format='pdf')
#
# plt.close()


# plotting aa comp of whole proteins:
#
# comps = list(combined_df['AA_COMPOSITION'])
# combined_df['aa_comp_dict'] = comps
# amino_acids = {"A":"Alanine","R":"Arginine","N":"Asparagine","D":"Aspartic acid","C":"Cysteine",
#                "Q":"Glutamine","E":"Glutamic acid","G":"Glycine","H":"Histidine","I":"Isoleucine",
#                "L":"Leucine","K":"Lysine","M":"Methionine","F":"Phenylalanine","P":"Proline",
#                "O":"Pyrrolysine","S":"Serine","U":"Selenocysteine","T":"Threonine","W":"Tryptophan",
#                 "Y":"Tyrosine","V":"Valine"}
# combined_df.reset_index(inplace=True)
# combined_df.rename(columns = {'index':'PROTEIN_ID'},inplace=True)
# for aa in amino_acids:
#     aa_counts = []
#     for prot in combined_df.index:
#         dicto = combined_df.loc[prot]['AA_COMPOSITION']
#         if aa in dicto.keys():
#             aa_counts.append(dicto[aa])
#         else:
#             aa_counts.append(0)
#     combined_df[f'{amino_acids[aa].upper()} COUNT'] = aa_counts
# aa_columns = ['ALANINE COUNT', 'ARGININE COUNT', 'ASPARAGINE COUNT',
#        'ASPARTIC ACID COUNT', 'CYSTEINE COUNT', 'GLUTAMINE COUNT',
#        'GLUTAMIC ACID COUNT', 'GLYCINE COUNT', 'HISTIDINE COUNT',
#        'ISOLEUCINE COUNT', 'LEUCINE COUNT', 'LYSINE COUNT', 'METHIONINE COUNT',
#        'PHENYLALANINE COUNT', 'PROLINE COUNT',
#        'SERINE COUNT', 'THREONINE COUNT',
#        'TRYPTOPHAN COUNT', 'TYROSINE COUNT', 'VALINE COUNT']

# for i in range(5):
#     part = i
#     fig, axes = plt.subplots(2, 2, figsize=(25, 5), sharey=True)
#     fig.suptitle('Aminoacid Compositions in terms of count')
#     pos = 0
# for aa in aa_columns[4*i:4*i+4]:
#     try:
#         sns.violinplot(data=combined_df,
#                        x='PROTEIN_TYPE',
#                        y=combined_df[aa],
#                        ax=axes[pos//2,pos%2],
#                        scale = 'width',
#                        width=0.8,
#                        title = f'aa_comp_part_{i+1}')
#         fig.tight_layout()
#     except:
#         sns.violinplot(data=combined_df,
#                        x='PROTEIN_TYPE',
#                        y=combined_df[aa],
#                        ax=axes[pos // 2 -1, pos % 2],
#                        scale='width',
#                        width=0.8,
#                        title = f'aa_comp_part_{i+1}')
#         fig.tight_layout()
#     pos+=1
#     plt.ylim(0,400)
#     plt.savefig(f'/home/metehan/Desktop/Plots/aa_comp_part_{i+1}.pdf', format='pdf')
#     plt.close()

# plotting disordered regions length:
tf_disorder_lengths = []
ntf_disorder_lengths = []
for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    if line['PROTEIN_TYPE'] == 'TF':
        for sequence in (disorder_dict.keys()):
            tf_disorder_lengths.append(len(sequence))
    else:
        for sequence in (disorder_dict.keys()):
            ntf_disorder_lengths.append(len(sequence))

# Y = [tf_disorder_lengths,ntf_disorder_lengths]
# tf_disorder_array = np.array(tf_disorder_lengths)
# ntf_disorder_array = np.array(ntf_disorder_lengths)
# X = [tf_disorder_array,ntf_disorder_array]

# ax =sns.violinplot(data=X,fliersize=0,)
# ax.set(title = 'disorder_relative_lengths')
# plt.ylim(-100,600)
# ax.set_xticklabels(['TF','NTF' ])
# plt.savefig(f'/home/metehan/Desktop/Plots/disorder_relative_lengths.pdf', format='pdf')
# plt.close()
#

# Plotting disordered regions composition.
#
# tf_amino_acids = {"A":[],"R":[],"N":[],"D":[],"C":[],
#                "Q":[],"E":[],"G":[],"H":[],"I":[],
#                "L":[],"K":[],"M":[],"F":[],"P":[],
#                "S":[],"T":[],"W":[],"Y":[],"V":[]}
# ntf_amino_acids = {"A":[],"R":[],"N":[],"D":[],"C":[],
#                "Q":[],"E":[],"G":[],"H":[],"I":[],
#                "L":[],"K":[],"M":[],"F":[],"P":[],
#                "S":[],"T":[],"W":[],"Y":[],"V":[]}
# for prot in combined_df.index:
#     line = combined_df.loc[prot]
#     disorder_dict = line['DISORDERED_REGIONS']
#     for region in disorder_dict.keys():
#         if line['PROTEIN_TYPE'] == 'TF':
#             for aa in tf_amino_acids.keys():
#                 tf_amino_acids[aa].append(region.count(aa))
#         else:
#             for aa in ntf_amino_acids.keys():
#                 ntf_amino_acids[aa].append(region.count(aa))
#
#
# X=[tf_amino_acids['A'],ntf_amino_acids['A']]


# for i in range(5):
#     part = i
#     fig, axes = plt.subplots(2, 2, figsize=(25, 5), sharey=True)
#     fig.suptitle('Aminoacid Compositions in terms of count')
#     pos = 0
#     for aa in list(tf_amino_acids.keys())[4*i:4*i+4]:
#         a=sns.violinplot(data=X,ax=axes[pos//2,pos%2])
#         fig.tight_layout()
#         a.set_xticklabels(['TF', 'NTF'])
#         pos+=1
#         plt.ylim(-50,100)
#         plt.savefig(f'/home/metehan/Desktop/Plots/disorder_aa_comp_part_{i+1}.pdf', format='pdf')
# plt.close()


# Plotting Disordered region disorder_charge at different pHs:

tf_charges_at_6 = []
tf_charges_at_7 = []
tf_charges_at_8 = []
tf_charges_at_5 = []
tf_charges_at_9 = []
ntf_charges_at_5 = []
ntf_charges_at_6 = []
ntf_charges_at_7 = []
ntf_charges_at_8 = []
ntf_charges_at_9 = []
prot_charges_at_5 = []
prot_charges_at_6 = []
prot_charges_at_7 = []
prot_charges_at_8 = []
prot_charges_at_9 = []
# X_at_5 = [tf_charges_at_5, ntf_charges_at_5, prot_charges_at_5]
# X_at_6 = [tf_charges_at_6, ntf_charges_at_6, prot_charges_at_6]
# X_at_7 = [tf_charges_at_7, ntf_charges_at_7, prot_charges_at_7]
# X_at_8 = [tf_charges_at_8, ntf_charges_at_8, prot_charges_at_8]
# X_at_9 = [tf_charges_at_9, ntf_charges_at_9, prot_charges_at_9]

for prot in combined_df.index:
    YY = ProteinAnalysis(combined_df.loc[prot]['SEQUENCE'])
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    prot_charges_at_5.append(YY.charge_at_pH(5))
    prot_charges_at_6.append(YY.charge_at_pH(6))
    prot_charges_at_7.append(YY.charge_at_pH(7))
    prot_charges_at_8.append(YY.charge_at_pH(8))
    prot_charges_at_9.append(YY.charge_at_pH(9))
    for region in disorder_dict.keys():
        Y = ProteinAnalysis(region)
        ph = 5
        disorder_charge = Y.charge_at_pH(ph)
        for i in range(5):
            if ph == 5:
                if type == 'TF':
                    tf_charges_at_5.append(disorder_charge)
                else:
                    ntf_charges_at_5.append(disorder_charge)
            if ph == 6:
                if type == 'TF':
                    tf_charges_at_6.append(disorder_charge)
                else:
                    ntf_charges_at_6.append(disorder_charge)
            elif ph == 7:
                if type == 'TF':
                    tf_charges_at_7.append(disorder_charge)
                else:
                    ntf_charges_at_7.append(disorder_charge)
            elif ph == 8:
                if type == 'TF':
                    tf_charges_at_8.append(disorder_charge)
                else:
                    ntf_charges_at_8.append(disorder_charge)
            elif ph == 9:
                if type == 'TF':
                    tf_charges_at_9.append(disorder_charge)
                else:
                    ntf_charges_at_9.append(disorder_charge)
            ph += 1

#
# ax = sns.violinplot(data=X_at_5)
# ax.set_xticklabels(['DISORDERED\nREGIONS\nTF','DISORDERED\nREGIONS\nNTF','ENTIRE\nPROTEIN'])
# plt.ylim(-80,80)
# plt.savefig(f'/home/metehan/Desktop/Plots/charges_at_5.pdf', format='pdf')
# plt.close()
#
# ax = sns.violinplot(data=X_at_6)
# ax.set_xticklabels(['DISORDERED\nREGIONS\nTF','DISORDERED\nREGIONS\nNTF','ENTIRE\nPROTEIN'])
# plt.ylim(-80,80)
# plt.savefig(f'/home/metehan/Desktop/Plots/charges_at_6.pdf', format='pdf')
# plt.close()
#
#
# ax = sns.violinplot(data=X_at_7)
# ax.set_xticklabels(['DISORDERED\nREGIONS\nTF','DISORDERED\nREGIONS\nNTF','ENTIRE\nPROTEIN'])
# plt.ylim(-80,80)
# plt.savefig(f'/home/metehan/Desktop/Plots/charges_at_7.pdf', format='pdf')
# plt.close()
#
# ax = sns.violinplot(data=X_at_8)
# ax.set_xticklabels(['DISORDERED\nREGIONS\nTF','DISORDERED\nREGIONS\nNTF','ENTIRE\nPROTEIN'])
# plt.ylim(-80,80)
# plt.savefig(f'/home/metehan/Desktop/Plots/charges_at_8.pdf', format='pdf')
# plt.close()
#
# ax = sns.violinplot(data=X_at_9,)
# ax.set_xticklabels(['DISORDERED\nREGIONS\nTF','DISORDERED\nREGIONS\nNTF','ENTIRE\nPROTEIN'])
# plt.ylim(-80,80)
# plt.savefig(f'/home/metehan/Desktop/Plots/charges_at_9.pdf', format='pdf')
# plt.close()
# TEST FOR CHARGE
# stats_at_5 = st.ranksums(tf_charges_at_5,ntf_charges_at_5)
# print('ok')
# stats_at_6 = st.ranksums(tf_charges_at_6,ntf_charges_at_6)
# print('ok')
# stats_at_7 = st.ranksums(tf_charges_at_7,ntf_charges_at_7)
# print('ok')
# stats_at_8 = st.ranksums(tf_charges_at_8,ntf_charges_at_8)
# print('ok')
# stats_at_9 = st.ranksums(tf_charges_at_9,ntf_charges_at_9)
# print('ok')
# print(stats_at_5,stats_at_6,stats_at_7,stats_at_8,stats_at_9)

# Plotting start,stop indexes:
tf_start = []
ntf_start = []
tf_stop = []
ntf_stop = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    start_percent = (line['START_INDEXES_PERCENT'])
    stop_percent = (line['STOP_INDEXES_PERCENT'])
    if type == 'TF' and start_percent != []:
        for val in start_percent:
            tf_start.append(val)
        for val in stop_percent:
            tf_stop.append(val)
    if type == 'NTF' and start_percent != []:
        for val in start_percent:
            ntf_start.append(val)
        for val in stop_percent:
            ntf_stop.append(val)
# X=[tf_start,ntf_start]
# XX=[tf_stop,ntf_stop]

# ax = sns.violinplot(data=X,orient='h')
# ax.set_yticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/disorder_start_percentage.pdf', format='pdf')
#
# plt.close()
#
#
# ax = sns.violinplot(data=XX,orient='h')
# ax.set_yticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/disorder_stop_percentage.pdf', format='pdf')
#
# plt.close()
#
# # Plotting MW
tf_mw = []
ntf_mw = []
for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                tf_mw.append(var.molecular_weight())
            if type == 'NTF':
                ntf_mw.append(var.molecular_weight())
        except:
            continue
#
# X = [tf_mw,ntf_mw]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/molecular_weights.pdf', format='pdf')
#
# plt.close()

# Plotting AROMATICITY


tf_aromaticity = []
ntf_aromaticity = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                tf_aromaticity.append(var.aromaticity())
            if type == 'NTF':
                ntf_aromaticity.append(var.aromaticity())
        except:
            print('error')

# X = [tf_aromaticity,ntf_aromaticity]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/aromaticity.pdf', format='pdf')
#
# plt.close()

# Plotting instability index
tf_instability_indexes = []
ntf_instability_indexes = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                tf_instability_indexes.append(var.instability_index())
            if type == 'NTF':
                ntf_instability_indexes.append(var.instability_index())
        except:
            print('error')

# X = [tf_instability_indexes,ntf_instability_indexes]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
# ax.text(2, 1.75, "Any value above 40 means the protein is unstable (has a short half life.")
# ax.axhline(40,color="red")
#
# plt.savefig(f'/home/metehan/Desktop/Plots/instability_indexes.pdf', format='pdf')
#
# plt.close()

# Plotting flexibility
tf_flexibility = []
ntf_flexibility = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                for k in var.flexibility():
                    tf_flexibility.append(k)
            if type == 'NTF':
                for k in var.flexibility():
                    ntf_flexibility.append(k)
        except:
            continue
# X = [tf_flexibility,ntf_flexibility]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
#
# plt.savefig(f'/home/metehan/Desktop/Plots/flexibility.pdf', format='pdf')
#
# plt.close()
#
# Plotting Gravy
tf_gravy = []
ntf_gravy = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                tf_gravy.append(var.gravy())
            if type == 'NTF':
                ntf_gravy.append(var.gravy())
        except:
            continue

# X = [tf_gravy,ntf_gravy]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/gravy.pdf', format='pdf')
#
# plt.close()

# Plotting Isoelectric Point
tf_isoelectric_point = []
ntf_isoelectric_point = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                tf_isoelectric_point.append(var.isoelectric_point())
            if type == 'NTF':
                ntf_isoelectric_point.append(var.isoelectric_point())
        except:
            continue

# X = [tf_isoelectric_point,ntf_isoelectric_point]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/isoelectric_point.pdf', format='pdf')
#
# plt.close()

# Plotting molar_extinction_coefficient


tf_molar_extinction_coefficient = []
ntf_molar_extinction_coefficient = []

for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']
    for region in disorder_dict.keys():
        try:
            var = ProteinAnalysis(region)
            if type == 'TF':
                tf_molar_extinction_coefficient.append(var.molar_extinction_coefficient())
            if type == 'NTF':
                ntf_molar_extinction_coefficient.append(var.molar_extinction_coefficient())
        except:
            continue
#
# X = [tf_molar_extinction_coefficient,ntf_molar_extinction_coefficient]
# ax = sns.violinplot(data=X,)
# ax.set_xticklabels(['TF','NTF'])
# plt.savefig(f'/home/metehan/Desktop/Plots/molar_extinction_coefficient.pdf', format='pdf')
#
# plt.close()

# Obtaining each disordered region sequences as strings:
tf_do_regions = []
ntf_do_regions = []
for prot in combined_df.index:
    line = combined_df.loc[prot]
    disorder_dict = line['DISORDERED_REGIONS']
    type = line['PROTEIN_TYPE']

    for key in disorder_dict.keys():
        if type == 'TF':
            tf_do_regions.append(key)
        else:
            ntf_do_regions.append(key)
