import random
import pandas as pd 
import numpy as np

id_1 = 8164 #change to first student id
id_2 = 7998 #change to second student id
id_3 = 8125 #change to third student id "leave 0000 if team of 2"
random_seed = id_1+id_2+id_3
random.seed(random_seed)
data_path="Data.csv"#replace with data path
output_path="your_data.csv"#replace with output data path

all_data=pd.read_csv(data_path) 
all_columns = all_data.columns.tolist()

target_column = 'smoking'
extra_column = 'hemoglobin' 
extra2_column = 'Gtp'   

all_columns.remove(target_column)

selected_columns = random.sample(all_columns, 10)

selected_columns = np.append(selected_columns, extra_column)
selected_columns = np.append(selected_columns, extra2_column)
print(selected_columns) #MUST BE PRINTED
selected_columns = np.append(selected_columns, target_column)
print(selected_columns)
sample_df = all_data[selected_columns].copy()
sample_df.to_csv(output_path)   #From HERE YOU CAN SPLIT FOR TRAIN ,VALID AND TEST