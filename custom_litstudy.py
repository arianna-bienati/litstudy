import pandas as pd
import pypopulation
from litstudy.stats import compute_histogram

country_codes_df = pd.read_csv('ISO_nationality_EN.tsv', sep='\t')

country_name_to_iso = dict(zip(country_codes_df['CountryName'], country_codes_df['Alpha-2 code']))

def extract_country(aff):
    from litstudy.continent import COUNTRY_TO_CONTINENT

    # Sometimes affiliation has given country
    country = aff.country
    if country:
        return country

    # Sometimes the country is in the affiliation name
    name = aff.name
    if name:
        for country in COUNTRY_TO_CONTINENT.keys():
            if country in name:
                return country

    return None

def get_population_for_country(country_name):
    # Convert the country name to ISO code
    iso_code = country_name_to_iso.get(country_name)
    if iso_code:
        # Retrieve population using pypopulation
        return pypopulation.get_population(iso_code)
    return None

def compute_country_histogram(docs, normalize=False, **kwargs) -> pd.DataFrame:
    """Compute a histogram of number of documents by affiliation country, optionally normalizing by population."""

    def extract(doc):
        result = set()
        for author in doc.authors or []:
            for aff in author.affiliations or []:
                country = extract_country(aff)
                if country:
                    result.add(country)
        return result

    histogram = compute_histogram(docs, extract, **kwargs)

    # Reset index to make 'Country' a column
    histogram = histogram.reset_index()
    
    # Rename columns to expected names
    histogram.rename(columns={'index': 'Country', 'Frequency': 'Count'}, inplace=True)

    if normalize:
        histogram['Population'] = histogram['Country'].apply(get_population_for_country)
        histogram['NormalizedCount'] = histogram.apply(
            lambda row: row['Count'] / row['Population'] if row['Population'] else None, axis=1
        )
        histogram.sort_values(by='NormalizedCount', ascending=False, inplace=True)

    return histogram.reset_index(drop=True)
