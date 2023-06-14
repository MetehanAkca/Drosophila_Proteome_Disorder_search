import matplotlib.pyplot as plt
import data_parsing_for_analysis,glutamine
import seaborn as sns
import numpy as np

labels = ["TF","NON TF"]

#Length
TF_Lengths = np.array(data_parsing_for_analysis.tf_lengthts)
NTF_Lengths = np.array(data_parsing_for_analysis.ntf_lengthts)
length_data = [TF_Lengths,NTF_Lengths]

#Disordered region length

TF_DO_Lengths = np.array(data_parsing_for_analysis.tf_disorder_lengths)
NTF_DO_Lengths = np.array(data_parsing_for_analysis.ntf_disorder_lengths)
do_length_data = [TF_DO_Lengths,NTF_DO_Lengths]

#Disordered region disorder_charge at different pHs:

TF_Charges_At_5 = np.array(data_parsing_for_analysis.tf_charges_at_5)
NTF_Charges_At_5 = np.array(data_parsing_for_analysis.ntf_charges_at_5)
charge_at_5 = [TF_Charges_At_5, NTF_Charges_At_5]

TF_Charges_At_6 = np.array(data_parsing_for_analysis.tf_charges_at_6)
NTF_Charges_At_6 = np.array(data_parsing_for_analysis.ntf_charges_at_6)
charge_at_6 = [TF_Charges_At_6, NTF_Charges_At_6]

TF_Charges_At_7 = np.array(data_parsing_for_analysis.tf_charges_at_7)
NTF_Charges_At_7 = np.array(data_parsing_for_analysis.ntf_charges_at_7)
charge_at_7 = [TF_Charges_At_7, NTF_Charges_At_7]

TF_Charges_At_8 = np.array(data_parsing_for_analysis.tf_charges_at_8)
NTF_Charges_At_8 = np.array(data_parsing_for_analysis.ntf_charges_at_8)
charge_at_8 = [TF_Charges_At_8, NTF_Charges_At_8]

TF_Charges_At_9 = np.array(data_parsing_for_analysis.tf_charges_at_9)
NTF_Charges_At_9 = np.array(data_parsing_for_analysis.ntf_charges_at_9)
charge_at_9 = [TF_Charges_At_9, NTF_Charges_At_9]

#Start and stop positions
TF_Start = np.array(data_parsing_for_analysis.tf_start)
NTF_Start = np.array(data_parsing_for_analysis.ntf_start)
start = [TF_Start,NTF_Start]
TF_Stop = np.array(data_parsing_for_analysis.tf_stop)
NTF_Stop = np.array(data_parsing_for_analysis.ntf_stop)
stop = [TF_Stop,NTF_Stop]


#MW
TF_mw = np.array(data_parsing_for_analysis.tf_mw)
NTF_mw = np.array(data_parsing_for_analysis.ntf_mw)
MW = [TF_mw,NTF_mw]

#Aromaticity

TF_Aromaticity =np.array(data_parsing_for_analysis.tf_aromaticity)
NTF_Aromaticity =np.array(data_parsing_for_analysis.ntf_aromaticity)
Aromaticity = [TF_Aromaticity,NTF_Aromaticity]

#Instability Index

TF_instability_index = np.array(data_parsing_for_analysis.tf_instability_indexes)
NTF_instability_index = np.array(data_parsing_for_analysis.tf_instability_indexes)
instability_indexes = [TF_instability_index,NTF_instability_index]

#Flexibility

TF_flexibility = data_parsing_for_analysis.tf_flexibility
NTF_flexibility = data_parsing_for_analysis.ntf_flexibility
Flexibility = [TF_flexibility,NTF_flexibility]

#Gravay

TF_Gravy = np.array(data_parsing_for_analysis.tf_gravy)
NTF_Gravy = np.array(data_parsing_for_analysis.ntf_gravy)
Gravy = [TF_Gravy,NTF_Gravy]

#IsoselectricPoint

TF_isoelectric_point = np.array(data_parsing_for_analysis.tf_isoelectric_point)
NTF_isoelectric_point = np.array(data_parsing_for_analysis.ntf_isoelectric_point)
Isoelectric_point = [TF_isoelectric_point,NTF_isoelectric_point]

#Molar extiction coefficient

TF_molar_extinction_coefficient = data_parsing_for_analysis.tf_molar_extinction_coefficient
NTF_molar_extinction_coefficient = data_parsing_for_analysis.ntf_molar_extinction_coefficient
Molar_extinction_coefficient = [TF_molar_extinction_coefficient,NTF_molar_extinction_coefficient]

#Creating plots
fig, axs = plt.subplots(ncols=2,nrows=8,
                        constrained_layout =True ,
                        figsize=(8, 16)
                        )

ax_length = sns.violinplot(data=length_data, ax=axs[0,0],ylabel = 'Length').set(xticklabels=labels,title='Protein total length')
ax_do_length = sns.violinplot(data=do_length_data, ax=axs[0,1],ylabel = 'Disordered Region Length').set(xticklabels=labels,title='Disordered regions length')
ax_charge_at_5 = sns.violinplot(data=charge_at_5, ax=axs[1,0],).set(xticklabels=labels,title='Total Charge of disordred region at pH 5')
ax_charge_at_6 = sns.violinplot(data=charge_at_6, ax=axs[1,1]).set(xticklabels=labels,title='Total Charge of disordred region at pH 6')
ax_charge_at_7 = sns.violinplot(data=charge_at_7, ax=axs[2,0]).set(xticklabels=labels,title='Total Charge of disordred region at pH 7')
ax_charge_at_8 = sns.violinplot(data=charge_at_8, ax=axs[2,1]).set(xticklabels=labels,title='Total Charge of disordred region at pH 8')
ax_charge_at_9 = sns.violinplot(data=charge_at_9, ax=axs[3,0]).set(xticklabels=labels,title='Total Charge of disordred region at pH 9')
ax_start_positions = sns.violinplot(data=start, ax=axs[3,1],orient='h').set(yticklabels=labels,title='Disordered region start index percent')
ax_stop_positions = sns.violinplot(data=stop, ax=axs[4,0],orient='h').set(yticklabels=labels,title='Disordered Region Stop index percent')
ax_mw = sns.violinplot(data=MW, ax=axs[4,1]).set(xticklabels=labels,title='Disordered region molecular weight')
ax_aromaticity = sns.violinplot(data=Aromaticity, ax=axs[5,0]).set(xticklabels=labels,title='Disordered region aromaticity')
ax_instability_index = sns.violinplot(data=instability_indexes, ax=axs[5,1]).set(xticklabels=labels,title='Disordered region instability index')
ax_flexibility = sns.violinplot(data=Flexibility, ax=axs[6,0]).set(xticklabels=labels,title='Disordered region flexibility')
ax_gravy = sns.violinplot(data=Gravy, ax=axs[6,1]).set(xticklabels=labels,title='Disordered region gravy(i.e hydrophobicity')
ax_isoelectric_point = sns.violinplot(data=Isoelectric_point, ax=axs[7,0]).set(xticklabels=labels,title='Disordered region isoelectric point')
ax_molar_extinction_coefficient = sns.violinplot(data=Molar_extinction_coefficient, ax=axs[7,1]).set(xticklabels=labels,title='Disordered region molar extiction coefficient')

fig.tight_layout(pad = 50.0)


plt.show()


