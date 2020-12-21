import numpy as np
import pandas as pd

# Clean up the script for furthur analysis
def clean_script(df, drop_cols):
    # Drop columns we don't need
    df = df.drop(drop_cols, axis=1)
    # Make new dataframe to return
    df_int = pd.DataFrame(columns=df.columns)
    # Loop through different emitters
    for emitter in pd.unique(df["Emitter Name"]):
        em_df = df[df["Emitter Name"] == emitter]
        # Loop through different modes defined by the user input Mode Key 
        for mode_key in pd.unique(em_df["Mode Key"]):
            em_md_df = em_df[em_df["Mode Key"] == mode_key]
            # Combine rows by taking the first non-null row. This combines the sub-modes for the different beams
            df_int = df_int.append(em_md_df.groupby('Emitter Name')[list(em_md_df.columns)[1:]].first().reset_index())
    # Return cleaned dataframe
    return df_int

def add_emit_time(df):
    times = []
    for i in range(len(df)):
        df_cnt = df.iloc[i].count()
        #times = times.append(df_cnt["On"])
    return df_cnt 






df = pd.read_csv("ex_script.csv") 
drop_cols = ['Emitter Mode', 'Frequency (Mhz)', 'PRI (usec)', 'PW (usec)','Scan Type (Scan Time)']
clean_df = clean_script(df, drop_cols)
tst = add_emit_time(clean_df)
