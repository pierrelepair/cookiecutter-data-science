# -*- coding: utf-8 -*-
import json
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import wget



def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    # Read config

    with open(str(project_dir.absolute()) + "/SETTINGS.json", 'r') as f:
        config = json.load(f)
    dl_url = config["SOURCE_DATA"]
    dl_tgt = str(project_dir.absolute()) + '/' + config["RAW_DATA_PATH"]
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    logger.info('downloading from ' + dl_url)
    wget.download(url=dl_url,out=dl_tgt)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]



    # import some data to play with


    main()
