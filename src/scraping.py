import os
import requests
import warnings
import zipfile
import glob
from tqdm import tqdm
from bs4 import BeautifulSoup
from src.static import DATA_DIR

FHFA_URL:str = 'https://www.fhfa.gov/data/multifamily-national-file-all-multifamily-properties-by-units-and-mortgages'

def get_page_data(url:str) -> BeautifulSoup:
    '''
    Gets a pages data
    Args:
        n: int -> number representing the page number
    Returns:
        A bs4 object full of the page info
    '''
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_file(url:str, dest_directory:str, filename:str) -> None:
    '''
    Uses requests to retrieve files from URLs and download them to the indicated directory
    '''
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{dest_directory}/{filename}', 'wb') as file:
            file.write(response.content)
    else:
        msg = f'Request for {url} failed: status code 200'
        warnings.warn()

def extract_zips():
    '''
    Extracts zip files in the DATA_DIR
    '''
    zip_files: list = glob.glob(f'{DATA_DIR}/*.zip')
    for filepath in zip_files:
        extract_to = filepath.strip('.zip')
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        os.remove(filepath)

def get_fhfa_data():
    '''
    executable to extract FHFA data from website
    '''
    soup:bs4.BeautifulSoup = get_page_data(FHFA_URL)
    a_tags:list[bs4.element.Tag] = soup.find_all('a')
    for a_tag in a_tags:
        if a_tag['href'].endswith(('.pdf', '.zip')):
            filename = a_tag['href'].split('/')[-1]
            get_file(url = f"https://www.fhfa.gov/{a_tag['href']}", dest_directory = DATA_DIR,
                    filename=filename)
    downloaded_zip_files: list = glob.glob(f"{DATA_DIR}/*.zip")
    extract_zips()


            

