### Intro

Imports documents from csv files into Elasticsearch

---

### Config files

+ `config.py`

  Config file to set:
  ```
  - es_index: Elasticsearch index optput
  - es_doctype: Elasticsearch type of documents optput
  - num_records: Records to import from csv files. To import all use: "len(df.index)"
  - num_processors: Number of cpus to use. For using max use: "cpu_count() - 2"   
  ```

+ `config_csv_files.csv`

  The script will use this list to get the set of csv files to import.

+ `config_map.py` 

  Defines the structure (based on record fields) of each csv file, that will be created and added to the document.

---

### Run

    pip install -r requirements.txt
    python3 import_csv_elasticsearch.py
