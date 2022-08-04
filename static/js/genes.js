const searchInput = document.getElementById('search-input');

searchInput.addEventListener('keyup', async function(event) {
   const searchTerm = searchInput.value;
   const searchParams = new URLSearchParams();
   searchParams.set('searchTerm', searchTerm);
   const url = '/api/search/genes?' + searchParams.toString();
   const response = await fetch(url);
   const genes = await response.json();
   const geneTableBody = document.getElementById('gene-table-body');
   geneTableBody.innerHTML = '';
   genes.forEach(function(gene) {
      const geneRow = document.createElement('tr');
      const nameColumn = document.createElement('td');
      nameColumn.textContent = gene.gene;
      const descriptionColumn = document.createElement('td');
      descriptionColumn.textContent = gene.gene_description;
      geneRow.append(nameColumn, descriptionColumn);
      geneTableBody.appendChild(geneRow);
   });
});
