import os
import pandas as pd

DATA_PATH = '/Users/AUCHLY1/SideProjects/tsa-claims/tsa_data/claims-2010-2013_0.csv'

def get_df():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        return df
    else:
        print("Cannot locate input file: %s" % DATA_PATH)
        raise FileNotFoundError

def scrub_data(df):
    # Rename columns
    columns = ['claim_number', 'date_received', 'incident_date', 'airport_code', 'airport_name',
               'airline_name', 'claim_type', 'claim_site', 'item_category', 'close_amount', 'disposition']
    df.columns = columns

    # Turn dates into datetime objects
    df['date_received'] = pd.to_datetime(df['date_received'])
    df['incident_date'] = pd.to_datetime(df['incident_date'])

    # For simplicity, remove any rows that are missing an airline or airport
    df = df[df.airline_name != '-']
    df = df[df.airport_name != '-']

    return df

if __name__ == '__main__':
    df = get_df()
    scrubbed = scrub_data(df)
    print(scrubbed)