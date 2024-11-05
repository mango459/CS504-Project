import config
import pandas as pd
from src.scraping import get_fhfa_data
from src.data_pipeline import data_pipeline
from src.static import DATA_DIR

if __name__ == '__main__':
    #config.update_static()
    get_fhfa_data()
    loan_data, raw_loan_data = data_pipeline('loan')
    unit_data, raw_unit_data = data_pipeline('unit')
    raw_data = raw_unit_data.merge(raw_loan_data, how='left',
                                    on=['record_number', 'enterprise_flag', 'year'])
    nrows = raw_data.shape[0]
    raw_data = raw_data.drop_duplicates()
    if (dropped:=raw_data.shape[0] - nrows) > 0:
        print(f"raw_data: {dropped} duplicate rows dropped, {raw_data.shape[0]} remaining")
    raw_data.to_csv(f'{DATA_DIR}/raw_data.csv')
    mapped_data = unit_data.merge(loan_data, how='left',
                                   on=['record_number', 'enterprise_flag', 'year'])
    nrows = mapped_data.shape[0]
    mapped_data = mapped_data.drop_duplicates()
    if (dropped:=mapped_data.shape[0] - nrows) > 0:
        print(f"raw_data: {dropped} duplicate rows dropped, {mapped_data.shape[0]} remaining")
    mapped_data.to_csv(f'{DATA_DIR}/mapped_data.csv')
    print('data prep complete.')
