import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    merged = pd.merge(anon_df, aux_df, on=['age', 'gender', 'zip3'], how='inner')
    
    match_counts = merged['anon_id'].value_counts()
    unique_anon_ids = match_counts[match_counts == 1].index
    
    unique_matches = merged[merged['anon_id'].isin(unique_anon_ids)].copy()
    
    if 'name' in unique_matches.columns:
        unique_matches = unique_matches.rename(columns={'name': 'matched_name'})

    return unique_matches[['anon_id', 'matched_name']]



def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    if len(anon_df) == 0:
        return 0.0
        
    return len(matches_df) / len(anon_df)
