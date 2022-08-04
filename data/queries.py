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


def get_genes():
    return data_manager.execute_select('select * from genes')


def search_genes(search_term):
    return data_manager.execute_select('''
        select * from genes
        where gene ilike %(search_term)s or gene_description ilike %(search_term)s
    ''', {'search_term': f'%{search_term}%'})
