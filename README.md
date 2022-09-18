# transpose_DF

## Overview
Python 3 script for transposing a tab-separated text file. This script was developed to transpose output files from bcftools that have chromosome IDs as row names and sample IDs as column headers. Transposing the file so that chromosome IDs are column headers and sample IDs are row names is necessary for making objects of class 'genind' in R (package adegenet). However, this script could potentially be used for transposing other files, although this has not been tested.

The purpose of this script is to take an input file (in the format of 'example_inputfile.txt'), transpose rows (index) and columns (columns), make lists of index names and column names, and write the results to a new files in a new directory.


## Dependencies:
	argparse
	pandas
	csv
	sys
	pathlib


## Input file:
The format of the input file should be similar to 'example_inputfile.txt'. This script is intended for files with chromosome-position names as row names, sample IDs as column headers, and genotypes (as biallelic sites, formatted as 'XX', where each X is one of the following base codes: A, C, G, T, N).


## Output files:
Output files are written to a directory using the *-d* argument. See **Usage** for additional information.
- example_out_dir is a folder where output files will be written.
	- example_outputfile.txt is the transposed data file.
	- chrom_ID_list.txt is a list of the **column names** for the transposed data file. (Note: this list is made using the row names of the inputfile, which are the column names in the output file.)
	- sample_ID_list.txt is a list of the **row names** for the trsnposed data file. (Note: this list is made using the row names of the outputfile.)


## Usage:
	python3 transpose_DF.py -d <OUTPUT DIRECTORY> -i <INPUTFILE> -o <OUTPUTFILE>

All arguments are required. transpose_DF.py will check to see if \<OUTPUT DIRECTORY> exists; if it does not already exist, \<OUTPUT DIRECTORY> will be created.

## Notes:
The script prints to console the row and column dimensions (excluding the row names/index and the column names/headers) for the inputfile and outputfile so that the user can verify that the files are being read and written correctly. (Note: the script does not perform any check or verfication itself; this is just to provide the user with the dimensions of the files. The files this script was originally made to transpose are often large in size, with too many rows or columns to count.)