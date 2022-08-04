from flask import Flask, render_template, request, jsonify
from data import queries
from dotenv import load_dotenv

load_dotenv()
app = Flask('Human Genome Atlas')


@app.route('/')
def index():
    number_of_genes = queries.get_number_of_genes()
    number_of_diseases = queries.get_number_of_diseases()
    number_of_processes = queries.get_number_of_biological_process()
    return render_template('index.html', number_of_genes=number_of_genes,
                           number_of_diseases=number_of_diseases,
                           number_of_processes=number_of_processes)


@app.route('/genes')
def genes():
    gene_rows = queries.get_genes()
    return render_template('genes.html', genes=gene_rows)


@app.route('/api/search/genes')
def api_search_genes():
    search_term = request.args['searchTerm']
    gene_rows = queries.search_genes(search_term)
    return jsonify(gene_rows)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
