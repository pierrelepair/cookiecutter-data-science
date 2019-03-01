# -*- coding: utf-8 -*-
import json
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import wget
import sys



def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)

    dl_url = config["SOURCE_DATA"]
    dl_tgt = str(project_dir.absolute()) + '/' + config["RAW_DATA_PATH"]
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    logger.info('downloading raw data from ' + dl_url)
    logger.info('downloading to ' + dl_tgt)
    try:
        wget.download(url=dl_url,out=dl_tgt)
    except Exception as e:
        logger.error('an exception occured while attempting to download raw data: ' + str(type(e)))
        sys.exit(2)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger(__name__)
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # Read project config
    try:
        with open(str(project_dir.absolute()) + "/SETTINGS.json", 'r') as f:
            config = json.load(f)
    except Exception as e:
        logger.error('an exception occured while attempting to read project config: ' + str(type(e)))
        sys.exit(1)


    # import some data to play with


    main()
