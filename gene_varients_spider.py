#!/usr/bin/python
# -*- coding:utf-8 -*-


from requests_html import HTMLSession
import json

dict2json = {}
session = HTMLSession()
r = session.get('https://ckb.jax.org/gene/grid')
print(len(r.html.links))

gene_link_dic = {gene.text:tuple(gene.absolute_links)[0] for gene in r.html.find('div.container-fluid div:nth-child(3) a')}
del gene_link_dic['']
del gene_link_dic['Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License']
for gene, link in gene_link_dic.items():
    r = session.get(link)
    if 'Additional content available in ' in r.html.html:
        pass
    else:
        selector2tr = 'div.container-fluid div:nth-child(4) div.col-lg-12 div.tab-content div#geneVariants tbody tr'
        gene_variants_tr_list = r.html.find(selector2tr)
        # gene_variants_tr_html = HTML(gene_variants_tr_list)
        dict2json[gene] = []
        for variant in gene_variants_tr_list:
            variant_info_list = variant.find('td')
            dict2json[gene].append({'Variant':variant_info_list[0].text, 'Imapct':variant_info_list[1].text, 'Protein Effect':variant_info_list[2].text, 'Variant Description':variant_info_list[3].text, 'Associated with drug Resistance':variant_info_list[4].text})

with open('gene_data.json', 'w') as f:
    json.dump(dict2json, f)