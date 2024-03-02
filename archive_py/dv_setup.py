import pandas as pd
from fredapi import Fred

# Function to setup Fred access
def setup_fred_access(api_key):
    return Fred(api_key=api_key)

# Function to download state coincident index
def download_state_coincident_index(fred, state_series_ids):
    state_coincident_index = pd.DataFrame()
    for series_id in state_series_ids:
        state_data = fred.get_series(series_id)
        state_coincident_index = pd.concat([state_coincident_index, state_data], axis=1)
    state_coincident_index.columns = state_series_ids
    return state_coincident_index

# Function to convert state coincident index to long format
def convert_to_long_format(state_coincident_index):
    state_long = state_coincident_index.stack().reset_index()
    state_long['level_0'] = pd.to_datetime(state_long['level_0'])
    state_long = state_long.rename(columns={0: 'Coincident_Index', 'level_0': 'Date', 'level_1': 'series_id'})
    return state_long

# Function to read state mapping data
def read_state_mapping_data(file_path):
    return pd.read_csv(file_path)

# Function to join state coincident index and state mapping data
def join_data(state_long, state_mapping_data):
    return pd.merge(state_long, state_mapping_data, on='series_id', how='left')

# Function to calculate district scores
def calculate_district_scores(merged_data):
    district_score_by_date = merged_data.groupby(['Date', 'district']).apply(lambda x: (x['Coincident_Index'] * x['share']).sum()).reset_index()
    district_score_by_date.rename(columns={0: 'district_coincident_index'}, inplace=True)
    return district_score_by_date

# Function to pivot district score data
def pivot_data(district_score_by_date):
    return district_score_by_date.pivot(index='Date', columns='district', values='district_coincident_index')

# Main function
def dv():
    api_key = "b40f40a14d67c7903b44700db6b7b6e7"
    state_series_ids = [
    "ALPHCI", "AKPHCI", "AZPHCI", "ARPHCI", "CAPHCI", "COPHCI", "CTPHCI", "DEPHCI", "FLPHCI", "GAPHCI",
    "HIPHCI", "IDPHCI", "ILPHCI", "INPHCI", "IAPHCI", "KSPHCI", "KYPHCI", "LAPHCI", "MEPHCI", "MDPHCI",
    "MAPHCI", "MIPHCI", "MNPHCI", "MSPHCI", "MOPHCI", "MTPHCI", "NEPHCI", "NVPHCI", "NHPHCI", "NJPHCI",
    "NMPHCI", "NYPHCI", "NCPHCI", "NDPHCI", "OHPHCI", "OKPHCI", "ORPHCI", "PAPHCI", "RIPHCI", "SCPHCI",
    "SDPHCI", "TNPHCI", "TXPHCI", "UTPHCI", "VTPHCI", "VAPHCI", "WAPHCI", "WVPHCI", "WIPHCI", "WYPHCI"
    ]
    fred = setup_fred_access(api_key)
    state_coincident_index = download_state_coincident_index(fred, state_series_ids)
    state_long = convert_to_long_format(state_coincident_index)
    state_mapping_data = read_state_mapping_data("state_gdp_shares.csv")
    merged_data = join_data(state_long, state_mapping_data)
    district_score_by_date = calculate_district_scores(merged_data)
    district_score_wide = pivot_data(district_score_by_date)
