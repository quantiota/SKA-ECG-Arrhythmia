"""Configuration for the MIT-BIH Arrhythmia ECG stream."""
import os

# QuestDB ILP (line protocol) — ingestion path, 9009
ILP_CONFIG = {
    'host': os.getenv('QDB_ILP_HOST', os.getenv('QDB_PG_HOST', 'localhost')),
    'port': int(os.getenv('QDB_ILP_PORT', '9009')),
}

# QuestDB pg-wire — queries and DDL, 8812
QDB_CONFIG = {
    'dbname': os.getenv('QDB_PG_NAME', 'qdb'),
    'user': os.getenv('QDB_PG_USER', 'admin'),
    'password': os.getenv('QDB_PG_PASSWORD', 'quest'),
    'host': os.getenv('QDB_PG_HOST', 'localhost'),
    'port': os.getenv('QDB_PG_PORT', '8812'),
}

# ECG Stream Configuration
ECG_CONFIG = {
    'table': 'ecg_arrhythmia_steps',
    'data_dir': os.getenv('ECG_DATA', 'data'),
    'records': 'records.txt',        # MIT-BIH record names and IDs, in order
    'dataset': 'mitdb/1.0.0',
    'channel': 'MLII',               # one fixed lead for every record
    # MIT-BIH records were sampled at 360 Hz and last 30 minutes; each is
    # streamed whole, at the native rate: 1 sample = 1/360 s. No resampling.
    'rate_hz': 360.0,
    'packet_steps': 360,             # one packet per second
    'max_steps': None,               # None = every record, whole length
}

# Logging Configuration
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s %(levelname)s %(message)s',
    'file': 'logs/ecg_validation.log',
}
