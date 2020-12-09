# Import some sick libs
import plaid
import json
import pandas as pd
import warnings

# Settings
# Base directory to save the new transaction files
base_dir = '/home/tstarr/devel/python/plaid-dl/'
# Location of Json with plaid credentials
plaid_cred_dir = '/home/tstarr/devel/python/plaid-dl/plaid-credentials.json'
# Equate account_id from Plaid and real account names
acc_dict = {
    'Ak0kqX4z9qsqB5pnaQd6fwQEJ9xnYYU6qOaa6': 'VSChecking',
    'v6p6xbq4ZxtzLakBoJpQhOaM5v8mYYHm3vLLV': 'VSSavings'
}

# Import super secret information from an un-tracked json file
with open(plaid_cred_dir) as json_file:
    cred_file = json.load(json_file)
    client_id = cred_file['client_id']
    secret = cred_file['secret']
    env = cred_file['env']
    access_token = cred_file['access_token']

# Get the start and end date from the user
print("Input start and end date")
print("Format: YYYY-MM-DD")
start_date = input('Start: ')
end_date = input('End: ')

# Start plaid client
client = plaid.Client(client_id=client_id,
                      secret=secret,
                      environment=env,
                      api_version='2019-05-29')
# Import transactions from my accounts
transactions_response = client.Transactions.get(access_token, start_date,
                                                end_date)

# Turn the response into a pandas DataFrame for ease of use
df_transactions = pd.DataFrame.from_dict(transactions_response['transactions'])

# Get the accounts tracked in transactions
accounts = df_transactions['account_id'].unique()
# Loop through keys and make sure they are set
for acc in accounts:
    if acc not in acc_dict.keys():
        warnings.warn('%s account_id doesn\'t have a real account associated' % acc)

# Loop through accounts and save a seperate csv for each
for key in acc_dict.keys():
    out_df = df_transactions[df_transactions['account_id'] == key]
    out_df.to_csv(base_dir + '%s_%s_%s.csv' % (acc_dict[key], start_date, end_date))
