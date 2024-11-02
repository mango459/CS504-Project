import config
from src.scraping import get_fhfa_data
from src.data_pipeline import data_pipeline
from src.static import DATA_DIR

if __name__ == '__main__':
    config.update_static()
    get_fhfa_data()
    loan_data, raw_loan_data = data_pipeline('loan')
    unit_data, raw_unit_data = data_pipeline('unit')
    loan_data.to_csv(f'{DATA_DIR}/loan_data.csv', index=False)
    raw_loan_data.to_csv(f'{DATA_DIR}/raw_loan_data.csv', index=False)
    unit_data.to_csv(f'{DATA_DIR}/unit_data.csv', index=False)
    raw_unit_data.to_csv(f'{DATA_DIR}/raw_unit_data.csv', index=False)
    print('data prep complete.')
