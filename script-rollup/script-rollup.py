import numpy as np
import pandas as pd

# Settings
secs_per_cell = 30

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


def det_emit_times(row):
    return list(row).count("On")*secs_per_cell

def count_engagements(row):
    return list(row).count("Off")







df = pd.read_csv("ex_script.csv") 
drop_cols = ['Emitter Mode', 'Frequency (Mhz)', 'PRI (usec)', 'PW (usec)','Scan Type (Scan Time)']
clean_df = clean_script(df, drop_cols)
tst = df.apply(det_emit_times, axis=1)
