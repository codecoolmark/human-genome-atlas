from flask import Flask, render_template, url_for
from data import queries
import math
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


@app.route('/diseases')
def diseases():
    diseases = queries.get_diseases()
    return render_template('diseases.html', diseases=diseases)


@app.route('/api/genes/by-disease/<int:disease_id>')
def get_genes_by_disease(disease_id):
    genes = queries.get_genes_by_disease_id(disease_id)
    return {'genes': genes}

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
