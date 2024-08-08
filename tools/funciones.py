import re
import geopandas as gpd
import pandas as pd
from unidecode import unidecode



def clean_text(text, validation_list=None):
    
    if validation_list is not None:
        text = re.sub(' +',' ', unidecode(str(text))).upper()
        return text if text in validation_list else "NA"
    else:
        return re.sub(' +',' ', unidecode(str(text))).upper()
    

def read_geojson(file_path):
    try:
        gdf = gpd.GeoDataFrame.from_file(file_path,crs='EPSG:4326')
        return gdf
    except ValueError as e:
        print(e)
