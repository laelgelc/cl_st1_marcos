from bs4 import BeautifulSoup
import pandas as pd

# Parsing the document
with open('vuam_test.xml', 'r', encoding='utf8', newline='\n') as xml_doc:
    soup = BeautifulSoup(xml_doc, 'lxml-xml')

# Capturing the desired information
rows = []
for group in soup.find_all('group'):
    for text in group.find_all('text', recursive=False):
        xml_id = text.get('xml:id', '')
        for element in text.find_all(['w', 'c']):
            lemma = element.get('lemma', '')
            word_type = element.get('type', '')
            text_content = element.text.strip()
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
            rows.append([xml_id, lemma, word_type, text_content, seg_function, seg_type, seg_vici_morph, seg_text])

# Creating the DataFrame
df = pd.DataFrame(rows, columns=['xml:id', 'lemma', 'type', 'text', 'seg function', 'seg type', 'seg vici:morph', 'seg text'])

df.dtypes

df

df.to_json('vuam_test.jsonl', orient='records', lines=True)

df.to_csv('vuam_test.tsv', sep='\t', index=False, encoding='utf-8', lineterminator='\n')