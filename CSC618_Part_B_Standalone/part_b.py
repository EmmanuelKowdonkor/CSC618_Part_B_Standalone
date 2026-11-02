"""Controlled eight-document experiment, transcribed from CSC 618 Week 10."""
import csv
import json
from pathlib import Path
from statistics import mean
from evaluation import evaluate, ndcg_at_k, dcg_at_k

OUT = Path(__file__).parent / 'results'
OUT.mkdir(exist_ok=True)
DOCUMENTS = {
 'D1':'Neural networks and deep learning methods for image classification',
 'D2':'BM25 ranking functions for information retrieval',
 'D3':'Convolutional neural networks for image recognition',
 'D4':'Language models and probabilistic document retrieval',
 'D5':'Image classification using machine learning',
 'D6':'BM25, query likelihood, and document ranking',
 'D7':'Unigram language models for text search',
 'D8':'Web crawling and link analysis'}
QUERIES = {'Q1':'Neural networks for image classification',
           'Q2':'BM25 information retrieval',
           'Q3':'Language models and document retrieval'}
RELEVANT = {'Q1':{'D1','D3','D5'}, 'Q2':{'D2','D4','D6'}, 'Q3':{'D4','D6','D7'}}
RANKINGS = {
 'A':{'Q1':['D1','D2','D3','D5','D4'], 'Q2':['D2','D1','D4','D6','D3'],
      'Q3':['D4','D2','D6','D7','D1']},
 'B':{'Q1':['D2','D1','D4','D3','D6'], 'Q2':['D1','D4','D2','D5','D6'],
      'Q3':['D1','D4','D3','D7','D6']}}
GRADES_Q1 = {'D1':3,'D3':2,'D5':1}


def main():
    rows = []
    summary = {}
    for system in ('A','B'):
        scores = []
        for query in QUERIES:
            result = evaluate(RANKINGS[system][query], RELEVANT[query])
            scores.append(result)
            rows.append(dict(System=system, Query=query, **result))
        summary[system] = dict(MAP=mean(x['AP'] for x in scores),
                               MRR=mean(x['RR'] for x in scores),
                               nDCG5_Q1=ndcg_at_k(RANKINGS[system]['Q1'], GRADES_Q1),
                               DCG5_Q1=dcg_at_k(RANKINGS[system]['Q1'], GRADES_Q1))
    with (OUT/'part_b_per_query.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    (OUT/'part_b_summary.json').write_text(json.dumps(summary,indent=2))
    for row in rows: print(row)
    print('AGGREGATE:',json.dumps(summary,indent=2))


if __name__ == '__main__': main()
