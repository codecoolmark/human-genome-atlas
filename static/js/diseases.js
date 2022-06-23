let diseaseListItem = document.querySelectorAll('[data-disease-id]');

let genContainer = null;

let createGenList = function (genes, listItem) {
    if (genContainer !== null) {
        genContainer.remove();
    }
    genContainer = document.createElement('div');
    let genListTitle = document.createElement('p');
    genListTitle.textContent = 'Genes related to that disease';
    genContainer.appendChild(genListTitle);
    let genList = document.createElement('ul');
    genContainer.appendChild(genList);
    listItem.appendChild(genContainer);
    genes.forEach(gene => {
        let genListItem = document.createElement('li')
        genListItem.textContent = gene.gene;
        genList.appendChild(genListItem);
    });
};

diseaseListItem.forEach(listItem => {
    listItem.addEventListener('click', async event => {
        let diseaseId = event.target.dataset['diseaseId'];
        let fetchResult = await fetch('/api/genes/by-disease/' + diseaseId);
        let json = await fetchResult.json();
        let genes = json.genes;
        createGenList(genes, event.target);
    });
});

