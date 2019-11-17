# theClinicalKnowledgebase_spider
Two samll spider for obtaining the available genes' variants and gene level evidences of [the Clinical Knowledgebase](https://ckb.jax.org/).
## Running
```python gene_spider.py```
```python gene_level_evidence_spider.py```
## Output
1. a json file named "gene_data.json" containing the basic variant information of available genes of the Clinical Knowledgebase.
2. a tsv file named "gene_level_evidence.tsv" containing gene level evidence for gene variant.
## Requirements
* Python 3
* [requests-html](https://github.com/psf/requests-html)
