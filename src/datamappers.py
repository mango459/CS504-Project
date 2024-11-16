loan_column_mapper = {0: 'enterprise_flag', 1: 'record_number', 2: 'census_tract_2020',
                 3: 'tract_income_ratio', 4: 'affordability_cat', 5: 'date_of_mortgage_note',
                 6: 'purpose_of_loan', 7: 'type_of_seller', 8: 'federal_guarantee',
                   9: 'tot_num_units', 10:'underserved_areas_ind'}

unit_column_mapper = {0: 'enterprise_flag', 1: 'record_number', 2: 'num_bedrooms',
                 3: 'num_units', 4: 'affordability_level', 5: 'tenant_income_ind'}

loan_data_dict = {
    'enterprise_flag': {'1':'fannie', '2':'freddie'},
    'census_tract_2020': {'1': '<10%', '2': '>=10%, <30%', '3':'>=30% <100%', '9':'NaN'},
    'tract_income_ratio': {'1': '>0, <=80%', '2': '>10, <=120%', '3': '>120%', '9': 'NaN'},
    'affordability_cat': {'1' :  '>=20%, <40%',
                          '2' : '<20%, >=40%',
                          '3' : '>=20%, >=40%',
                          '4' : '<20%, <40%',
                          '8' : 'NaN',
                          '9' : 'NaN',
                          '0' :  'NaN'},
    'date_of_mortgage_note': {'1' : 'same year as acquired',
                              '2' : 'prior to year aquired',
                              '9' : 'NaN'},
    'purpose_of_loan': {'1' : 'purchase', '2' : 'refinance', '3' : 'new build',
                        '4' : 'improvement/rehab',
                        '9' : 'NaN'},
    'type_of_seller': {'1' : 'mortgage_company', '2' : 'SAIF or BIF',
                       '3' : 'credit_union', '4' : 'Other'},
    'federal_guarantee': {'1' : 'yes', '2' : 'no',
                          '3' : 'FHA', '9' : 'NaN'},
    'tot_num_units': {'1' : '5 - 24', '2' : '25-50', '3' : '51-99', '4' : '100-149',
                      '5' : '> 149', '9' : 'NaN'}
    }

unit_data_dict = {
    'enterprise_flag': {'1':'fannie', '2':'freddie'},
    'num_bedrooms': {'1': '0-1', '2':'>=2'},
    'affordability_level': {'1' :  '>=0, <=50%', '2' :  '>50, <=60%', '3' :  '>60, <=80%',
                            '4' :  '>80, <=100%', '5' :  '>100% ', '9' :  'NaN'},
    'tenant_income_ind': {'0' : 'No', '1' : 'Yes'}
    }

loan_data_mapper = {
    'year': lambda x: x,
    'enterprise_flag': lambda x: loan_data_dict['enterprise_flag'].get(x, x),
    'record_number': lambda x: x,
    'census_tract_2020': lambda x: loan_data_dict['census_tract_2020'].get(x, x),
    'tract_income_ratio': lambda x: loan_data_dict['tract_income_ratio'].get(x, x),
    'affordability_cat': lambda x: loan_data_dict['affordability_cat'].get(x, x),
    'date_of_mortgage_note': lambda x: loan_data_dict['date_of_mortgage_note'].get(x, x),
    'purpose_of_loan': lambda x: loan_data_dict['purpose_of_loan'].get(x, x),
    'type_of_seller': lambda x: loan_data_dict['type_of_seller'].get(x, x),
    'federal_guarantee': lambda x: loan_data_dict['federal_guarantee'].get(x, x),
    'tot_num_units': lambda x: loan_data_dict['tot_num_units'].get(x, x),
}

unit_data_mapper = {
    'year': lambda x: x,
    'enterprise_flag' : lambda x: unit_data_dict['enterprise_flag'].get(x, x),
    'record_number': lambda x: x,
    'num_bedrooms': lambda x: unit_data_dict['num_bedrooms'].get(x, x),
    'num_units': lambda x: x,
    'affordability_level': lambda x: unit_data_dict['affordability_level'].get(x, x),
    'tenant_income_ind': lambda x: unit_data_dict['tenant_income_ind'].get(x, x)
}