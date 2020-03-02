import re
import matplotlib as plt

"""Als resultaat lever je individueel op:

Een python script met alleen de backbone structuur: dus alleen de functie namen + docstrings.
Denk eraan dat binnen een docstring staat beschreven:
Een samenvatting van wat de functie doet
Welke variabelen de functie binnen komen en welke datastructuur is dit? Hoe ziet deze datastructuur er dan uit?
Welke variabelen returned worden, welke datastructuur is dit? Hoe ziet deze datastructuur eruit?
Deze opdracht mag je inleveren op github in een python file
"""

def read_file(file):
    """
    This function reads a file and takes cancer gene data from it uses re
    This data is stored in a dictionary

    input: TDB-file
    output: gene data dictionary
    """


def piechart(gene_data_dictionary):
    """
    This function takes a dictionary with integers as values and generates a piechart
    input: dictionary with integers as values
    output: pychart displaying the integers
    """


def main():
    file = cancer.tdb
    gene_data_dictionary = read_file(file)
    piechart(gene_data_dictionary)
    
main()