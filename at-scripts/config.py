config = {
    "es_index" : "banamex-arr7",           # Elasticsearch index optput     
    "es_doctype" : "doctype",              # Elasticsearch type of documents optput
    "num_records" : "len(df.index)",       # Records to import from csv files. To import all use: "len(df.index)" 
    "num_processors" : "1"                 # Number of cpus to use. For using max use: "cpu_count() - 2"  
}