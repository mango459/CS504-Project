loan_column_mapper = {1: 'enterprise_flag', 2: 'record_number', 3: 'census_tract_2020',
                 4: 'tract_income_ratio', 5: 'affordability_cat', 6: 'date_of_mortgage_note',
                 7: 'purpose_of_loan', 8: 'type_of_seller', 9: 'federal_guarantee',
                   10: 'tot_num_units'}

unit_column_mapper = {1: 'enterprise_flag', 2: 'record_number', 3: 'num_bedrooms',
                 4: 'num_units', 5: 'affordability_level', 6: 'tenant_income_ind'}

loan_data_dict = {
    'enterprise_flag': {'1':'fannie', '2':'freddie'},
    'census_tract_2020': {'1': '<10%', '2': '>=10%, <30%', '3':'>=30% <100%', '4':'missing'},
    'tract_income_ratio': {'1': '>0, <=80%', '2': '>10, <=120%', '3': '>120%', '4': 'missing'},
    'affordability_cat': {'1' :  '>=20% of the units in the property are affordable at or below'+\
                          '50% of Area Median Income (AMI), and <40% are affordable at or below'+\
                          '60% AMI', '2' : '<20% and >=40%','3' : '>=20% and >=40%',
                          '4' : '<20% and <40%', '8' : 'Not available', '9' : 'Not eligible',
                          '0' :  'Missing'},
    'date_of_mortgage_note': {'1' : 'originated in same year as acquired',
                              '2' : 'originated prior to calendar year of acquisition',
                              '9' : 'missing'},
    'purpose_of_loan': {'1' : 'Purchase', '2' : 'Refinancing (all types)', '3' : 'New construction',
                        '4' : 'Home Improvement/Rehabilitation',
                        '9' : 'Not applicable/not available'},
    'type_of_seller': {'1' : 'Mortgage Company', '2' : 'Savings Association Insurance Fund (SAIF)'+\
                       '- or Bank Insurance Fund (BIF)-insured depository institution',
                       '3' : 'NCUA-insured Credit Union', '4' : 'Other'},
    'federal_guarantee': {'1' : 'Yes (has some type of Federal Guarantee)', '2' : 'No',
                          '3' : 'FHA Risk Sharing', '9' : 'Not available'},
    'tot_num_units': {'1' : '5 to 24 units', '2' : '25 to 50', '3' : '51 to 99', '4' : '100 to 149',
                      '5' : 'over 149', '9' : 'Unknown'}
    }

unit_data_dict = {
    'enterprise_flag': {'1':'fannie', '2':'freddie'},
    'num_bedrooms': {'1': '0-1 bedroom', '2':'2 or more bedrooms'},
    'affordability_level': {'1' :  '>=0, <=50%', '2' :  '>50, <=60%', '3' :  '>60, <=80%',
                            '4' :  '>80, <=100%', '5' :  '>100% ', '9' :  'Not available'},
    'tenant_income_ind': {'0' : 'No or Not provided', '1' : 'Yes'}
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