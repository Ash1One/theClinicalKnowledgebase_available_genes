#!/usr/bin/python
# -*- coding:utf-8 -*-


from requests_html import HTMLSession

dict2tsv = {}
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
        r = session.get(link+'&tabType=GENE_LEVEL_EVIDENCE')
        selector = 'div.container-fluid div.row div.col-lg-12 div.tab-content div#associatedEvidence'
        gene_level_evidence_tr_list = r.html.find(selector, first=True).find('table', first=True).find('tr')
        for evidence in gene_level_evidence_tr_list:
            evidence_list = evidence.find('td')
            dict2tsv[gene] = {'Molecular Profile':evidence_list[0].text, 'Indication/Tumor Type':evidence_list[1].text, 'Response Type':evidence_list[2].text, 'Therapy Name':evidence_list[3].text, 'Approval Status':evidence_list[4].text, 'Evidence Type':evidence_list[5].text, 'Efficacy Evidence':evidence_list[6].text, 'References':evidence_list[7].text}

with open('gene_level_evidence.tsv', 'w') as f:
    f.write('Gene\tMolecular Profile\tIndication/Tumor Type\tResponse Type\tTherapy Name\tApproval Status\tEvidence Type\tEfficacy Evidence\tReferences\n')
    for gene, evidence in dict2tsv.items():
        f.write(gene+'\t')
        f.write(evidence['Molecular Profile']+'\t')
        f.write(evidence['Indication/Tumor Type']+'\t')
        f.write(evidence['Response Type']+'\t')
        f.write(evidence['Therapy Name']+'\t')
        f.write(evidence['Approval Status']+'\t')
        f.write(evidence['Evidence Type']+'\t')
        f.write(evidence['Efficacy Evidence']+'\t')
        f.write(evidence['References']+'\n')