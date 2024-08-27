from bs4 import BeautifulSoup
import pandas as pd
with open('vuam_test.xml', 'r', encoding='utf8', newline='\n') as xml_doc:
    soup = BeautifulSoup(xml_doc, 'lxml-xml')
rows = []
for element in soup.find_all(['w', 'c']):
    lemma = element.get('lemma', '')
    word_type = element.get('type', '')
    text = element.text.strip()
    seg = element.find('seg')
    if seg:
        seg_function = seg.get('function', '')
        seg_type = seg.get('type', '')
        seg_vici_morph = seg.get('vici:morph', '')
        seg_text = seg.text.strip()
    else:
        seg_function = ''
        seg_type = ''
        seg_vici_morph = ''
        seg_text = ''
    rows.append([lemma, word_type, text, seg_function, seg_type, seg_vici_morph, seg_text])
df = pd.DataFrame(rows, columns=['lemma', 'type', 'text', 'seg function', 'seg type', 'seg vici:morph', 'seg text'])
df.dtypes
df
df.to_json('vuam_test.jsonl', orient='records', lines=True)
df.to_csv('vuam_test.tsv', sep='\t', index=False, encoding='utf-8', lineterminator='\n')
