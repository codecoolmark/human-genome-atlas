from data import data_manager


def get_number_of_genes():
    row, = data_manager.execute_select('select count(*) as number_of_genes from genes')
    return row['number_of_genes']


def get_number_of_diseases():
    row, = data_manager.execute_select('select count(*) as number_of_diseases from diseases')
    return row['number_of_diseases']


def get_number_of_biological_process():
    row, = data_manager.execute_select('select count(*) as number_of_processes from biological_processes')
    return row['number_of_processes']


def get_diseases():
    diseases = data_manager.execute_select("""
    select * from diseases order by name
    """)
    return diseases


def get_genes_by_disease_id(disease_id):
    genes = data_manager.execute_select("""
        select * from genes
        join genes_diseases on genes.id = genes_diseases.gene_id
        where disease_id = %(disease_id)s
    """, variables={'disease_id': disease_id})
    return genes
