import glob
import re
import pandas as pd
from src.static import DATA_DIR
import src.datamappers as datamappers

def clean_data(file_loc:str) -> pd.core.frame.DataFrame:
    match = re.search(r'\d{4}', file_loc)
    yr = match.group()
    with open(file_loc, 'r') as f:
        data = f.read()
    str_data_clean: str = re.sub(r'[^\S\n]+', ' ', data)
    list_data: list[str] = str_data_clean.split('\n')
    list_list_data : list[list[str]] = [x.split(' ') for x in list_data]
    df = pd.DataFrame(list_list_data, columns=[x+1 for x in range(len(list_list_data[0]))])
    df = df.dropna()
    df['year'] = pd.Series([yr for x in df.index])
    return df

def map_values(data: pd.core.frame.DataFrame, column_mapper:dict = None, data_mapper:dict = None):
    if not data_mapper:
        data_mapper = dict()
    if not column_mapper:
        column_mapper = dict()
    mapped_data = data.rename(column_mapper, axis=1)
    if data_mapper:
        mapped_data = mapped_data.apply(data_mapper)
    return mapped_data

def data_pipeline(file_keyword):
    if not file_keyword in ('loan', 'unit'):
        raise ValueError('loan or unit only')
    files = glob.glob(f"{DATA_DIR}/**/*{file_keyword}*.txt")
    mapped_dfs = list()
    raw_dfs = list()
    for file in files:
        data = clean_data(file)
        if 'unit' in file:
            mapped_data = map_values(data, datamappers.unit_column_mapper,
                                     datamappers.unit_data_mapper)
            mapped_dfs.append(mapped_data)
            raw_data = map_values(data, datamappers.unit_column_mapper)
            raw_dfs.append(raw_data)
        elif 'loan' in file:
            mapped_data = map_values(data, datamappers.loan_column_mapper,
                                     datamappers.loan_data_mapper)
            mapped_dfs.append(mapped_data)
            raw_data = map_values(data, datamappers.loan_column_mapper)
            raw_dfs.append(raw_data)
    return (pd.concat(mapped_dfs, axis=0).drop_duplicates(),
               pd.concat(raw_dfs, axis=0).drop_duplicates())




