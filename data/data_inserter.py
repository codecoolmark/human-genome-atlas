import os
import csv

from dotenv import load_dotenv

import psycopg
import psycopg.rows

import data_manager

load_dotenv()

with open("data/proteinatlas.tsv") as import_file:
    csv_reader = csv.DictReader(import_file, delimiter='\t')
    diseases_by_gene = {}
    biological_processes_by_gene = {}

    # insert all genes
    for row in csv_reader:
        gene = row['Gene']
        disease = row['Disease involvement'].strip()
        biological_process = row['Biological process'].strip()
        data_manager.execute_dml_statement("""
        insert into genes (gene, gene_synonym, ensembl, gene_description) 
        values (%(Gene)s, %(Gene synonym)s, %(Ensembl)s, %(Gene description)s);
        """, variables=row)
        if disease != '':
            diseases_by_gene[gene] = disease
        if biological_process != '':
            biological_processes_by_gene[gene] = biological_process

    # insert all diseases
    diseases = set(diseases_by_gene.values())
    for disease in diseases:
        if disease.strip() != '':
            data_manager.execute_dml_statement("""
                    insert into diseases (name) 
                    values (%(disease)s);
                    """, variables={'disease': disease})

    diseases = data_manager.execute_select("select name, id from diseases")
    disease_id_by_name = {}
    for disease in diseases:
        disease_id_by_name[disease['name']] = disease['id']

    # insert all biological processes
    processes = set(biological_processes_by_gene.values())
    for process in processes:
        if process.strip() != '':
            data_manager.execute_dml_statement("""
                    insert into biological_processes (name) 
                    values (%(process)s);
                    """, variables={'process': process.strip()})

    processes = data_manager.execute_select("select name, id from biological_processes")
    biological_process_id_by_name = {}
    for process in processes:
        biological_process_id_by_name[process['name']] = process['id']

    genes = data_manager.execute_select("select gene, id from genes")
    gene_id_by_gene = {}
    for gene in genes:
        gene_id_by_gene[gene['gene']] = gene['id']

    # insert m:n tables
    for gene, disease in diseases_by_gene.items():
        data_manager.execute_dml_statement("""
                        insert into genes_diseases (gene_id, disease_id) 
                        values (%(gene_id)s, %(disease_id)s)
                        """, variables={'gene_id': gene_id_by_gene[gene],
                                        'disease_id': disease_id_by_name[diseases_by_gene[gene]]})

    for gene, process in biological_processes_by_gene.items():
        data_manager.execute_dml_statement("""
                            insert into genes_biological_processes (gene_id, biological_process_id) 
                            values (%(gene_id)s, %(process_id)s)
                            """, variables={'gene_id': gene_id_by_gene[gene],
                                            'process_id': biological_process_id_by_name[
                                                biological_processes_by_gene[gene]]})
