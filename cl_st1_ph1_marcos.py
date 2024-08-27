import pandas as pd
df = pd.read_xml('debate.xml')
df.dtypes
df['Date'] = pd.to_datetime(df['Date'])
df.dtypes
df
df.to_json('debate.jsonl', orient='records', lines=True)
df.to_csv('debate.tsv', sep='\t', index=False, encoding='utf-8', lineterminator='\n')
