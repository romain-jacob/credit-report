# CRediT

This package generates CRediT reports for research items. [CRediT](https://www.casrai.org/credit.html) is a taxonamy developed and supported by [CASRAI](https://www.casrai.org/).

## Description

This package parses the a contribution file (in csv format) and produces a concise pdf report. This report can be easily linked/appended to a research paper (or other outputs) to unambiguously describe the respective contributions of the authors. 

## Requirements

* The parser is written in python (3.6). See `environment.lock.yaml` for the complete dependencies.
* The PDF is generated using LaTeX. The standard `article` class is used. The following packages are required:
  * inputenc
  * hypperref
  * tabularx
  * longtable
  * calc

## Usage

1. Open `files/contributions_template.xlt` and fill-in the authors contributions.
1. Save the file as `files/contrib.csv`, using comma (,) as separator.
1. Open `notebooks/compile_CRediT.ipynb` notebook (e.g., Juputer Lab).
1. Fill-in the item meta data; "title" is compulsory, all other fields are optional.
1. Execute the cell to compile the CRediT report; your report is available as `files/CRediT.pdf`.


## Note

This project has been set up using PyScaffold 3.2.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
