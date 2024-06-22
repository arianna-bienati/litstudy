# Lit rev automatation

## Project description
This project tests the [litstudy](https://nlesc.github.io/litstudy/index.html) Python package for automatic literature reviews. 
It shows the use case of a mapping review of the literature about or related to the Reggio Emilia Approach (REA), an educational philosophy centered on the child as a subject with strong developmental capabilities and rights.

## Repo contents
* `main`: Jupyter notebook that shows the results for the mapping review about the REA. It follows the example provided [here](https://nlesc.github.io/litstudy/example.html) by the litstudy team (with some customization).
* `NLP-REA.md` and `NLP-REA.pdf` are the .md and .pdf versions of the abstract written for presenting this study in the last lecture hold by prof. [Mineo](https://personale.unimore.it/rubrica/dettaglio/rmineo) in the framework of the PhD in [Reggio Childhood Studies](https://www.phdreggiochildhoodstudies.unimore.it/en/homepage-english/).
* `.scopus.db` *should* be the database with papers related to the REA retrieved from Scopus. It *should* be an ORACLE Berkeley DB. Further work on it should be done to understand the structure of the data contained in it. 
* `citation.html` is the network graph on co-citations. It does not display in the Jupyter notebook, but you can open it in your fav browser.

### Customization
* `custom_litstudy.py`: a Python script that adds to the `compute_country_histogram` function of the `litstudy` package the possibility to normalize per country population size. 
* `ISO_nationality_EN`: a mapping from country names to ISO codes.

### Personal struggles with installing and configuring litstudy
* if you are experiencing some errors while installing and importing litstudy, you might find the **Litstudy for dummies** guide in `CODE litstudy.md` useful.

## Get in touch
If you're also trying out some tools for literature review automatation (for your PhD or else) or you're using litstudy and you are customizing it, I would be super happy if we get in touch (arianna(dot)bienati(at)unimore(dot)it) and exchange some experiences!
