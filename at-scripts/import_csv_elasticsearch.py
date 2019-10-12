import pandas as pd
import datetime
import pprint
from multiprocessing import Pool, TimeoutError, cpu_count
import ast
import json
from jsonmerge import merge
import sys
from elasticsearch import Elasticsearch
from config_map import configMap
from config import config

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
pd.options.mode.chained_assignment = None

pp = pprint.PrettyPrinter(indent=4)

# ------ elasticsearch settings ---------- #
es_client = Elasticsearch()
es_index = config['es_index']
es_doctype = config['es_doctype']
# ---------------------------------------- #


class bcolors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def extractEntities (pd_row,configMap,row_url):
    row_object = json.loads(pd_row)
    aux_arr_entities=[]
    for entity_configMap in configMap[row_url]['entities']:
        aux_entity={}
        for k,v in entity_configMap.items():
            aux_value=""
            if not isinstance(v, list):
                aux_value=v
            else:
                for vv in v:
                    aux_value += str(row_object[vv]) + " "
            aux_entity.update({k:' '.join(aux_value.split())})
        aux_arr_entities.append(aux_entity)        
    return aux_arr_entities


def createDBObject (pd_row,row_url,configMap):
    # print ("document: ", ' '.join(pd_row.split()) )
    aux_db_object = {
        "@context" : "http://schema.org",
        "@type" : "document",                                     
        "source" : row_url,
        "info" : ' '.join(pd_row.split()),
        "entities" : extractEntities(pd_row,configMap,row_url)
    }
    return aux_db_object


def processLine(tup):
    line, index = tup
    row = line.split(';')
    idx = row[0]
    row_url = row[1]

    print ()
    print ()
    print (bcolors.warning, '##########################################################################################', bcolors.end)
    print(" Id file: ",idx, ' - Processing:', row_url)
    print(" Id file: ",idx, ' - Starting at', datetime.datetime.now().replace(microsecond=0).isoformat())
    file = open(row_url)
    df = pd.read_csv(file, configMap[row_url]['delimiter'], names=configMap[row_url]['colum_names'] , low_memory=False, index_col=False, error_bad_lines=False)
    file.close()
    print(" Id file: ",idx, ' - Got: ', df.index, 'records')
    print (bcolors.warning, '##########################################################################################', bcolors.end)

    for i in range(eval(config['num_records'])):
        print()
        print(df.loc[[i]])
        db_object = createDBObject(df.loc[i].to_json(),row_url,configMap) 
        result = es_client.index(index=es_index, doc_type=es_doctype, body=db_object)
        if (result['result']=="created"):
            print(bcolors.green, result['result'],bcolors.end)
        else:
            print(bcolors.fail, result['result'],bcolors.end)
    
    print ()
    print(bcolors.green ,"Id file: ",idx, ' - DONE at', datetime.datetime.now().replace(microsecond=0).isoformat(),bcolors.end)    


with open('config_csv_files.csv') as csvfile:
    pool = Pool(processes=eval(config['num_processors']))
    lines_to_process = []
    for line in csvfile:
        lines_to_process.append((line, 1))
    pool.map(processLine, lines_to_process, chunksize=1)
    pool.close()
    pool.join()