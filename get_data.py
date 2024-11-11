import config
import pandas as pd
from src.scraping import get_fhfa_data
from src.data_pipeline import data_pipeline
from src.static import DATA_DIR

if __name__ == '__main__':
    config.update_static()
    get_fhfa_data()
    loan_data, raw_loan_data = data_pipeline('loan')
    unit_data, raw_unit_data = data_pipeline('unit')
    raw_data = raw_loan_data.merge(raw_unit_data, how='left',
                                    on=['record_number', 'enterprise_flag', 'year'])
    nrows = raw_data.shape[0]
    raw_data = raw_data.drop_duplicates()
    if (dropped:=raw_data.shape[0] - nrows) > 0:
        print(f"raw_data: {dropped} duplicate rows dropped, {raw_data.shape[0]} remaining")
    raw_data.dropna(subset=['census_tract_2020', 'tract_income_ratio', 'affordability_cat',
                            'date_of_mortgage_note', 'purpose_of_loan', 'type_of_seller',
                            'federal_guarantee', 'tot_num_units', 'num_bedrooms',
                            'affordability_level', 'tenant_income_ind'], inplace=True)
    raw_data.to_csv(f'{DATA_DIR}/raw_data.csv', index=False)
    mapped_data = loan_data.merge(unit_data, how='left',
                                   on=['record_number', 'enterprise_flag', 'year'])
    nrows = mapped_data.shape[0]
    mapped_data = mapped_data.drop_duplicates()
    if (dropped:=mapped_data.shape[0] - nrows) > 0:
        print(f"raw_data: {dropped} duplicate rows dropped, {mapped_data.shape[0]} remaining")
    mapped_data.dropna(subset=['census_tract_2020', 'tract_income_ratio', 'affordability_cat',
                            'date_of_mortgage_note', 'purpose_of_loan', 'type_of_seller',
                            'federal_guarantee', 'tot_num_units', 'num_bedrooms',
                            'affordability_level', 'tenant_income_ind'], inplace=True)
    mapped_data.to_csv(f'{DATA_DIR}/mapped_data.csv', index=False)
    print('data prep complete.')
