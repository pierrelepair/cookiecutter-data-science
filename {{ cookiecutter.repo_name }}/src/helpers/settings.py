import os 
import json

def get_raw_data_path(index=0):
    wd = os.getcwd()
    with open(wd  + "/SETTINGS.json", 'r') as f:
        config = json.load(f)
    raw_file = config["source_dl"][index]["filename"]
    return (wd + "/" + config['raw_data_path'] + "/" + raw_file)

def get_clean_data_path():
    wd = os.getcwd()
    with open(wd  + "/SETTINGS.json", 'r') as f:
        config = json.load(f)
    return (wd + "/" + config['clean_data_path'])

def get_seed():
    wd = os.getcwd()
    with open(wd  + "/SETTINGS.json", 'r') as f:
        config = json.load(f)
    return (int(config['seed']))

def get_models_path():
    wd = os.getcwd()
    with open(wd  + "/SETTINGS.json", 'r') as f:
        config = json.load(f)
    return (wd + "/" + config['model_checkpoint_dir'])

