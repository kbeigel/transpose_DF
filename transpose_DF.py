#!/usr/bin/env python3

# Import libraries
import argparse
import pandas as pd
import csv
import sys
from pathlib import Path


# Get arguments from commandline input and parses them with argparse; requires argparse
def Get_Arguments():

	parser = argparse.ArgumentParser(description='Transposing file so that samples are rows and loci are columns.')
	parser.add_argument("-d", "--directory", type=str, required=True, help="Run subfolder")
	parser.add_argument("-i", "--inputfile", type=str, required=True, help="Input text file")
	parser.add_argument("-o", "--outputfile", type=str, required=True, help="Output text file")

	args = parser.parse_args()

	return args


# Transpose DataFrame of file and write the result to a new tab-separated CSV
	# Read tab-separated file (infile) into pandas.DataFrame (with column 0 as index and row 0 as headers), transpose DataFrame,
	# write transposed DataFrame object to new tab-separated file using commandline args ('/directory/outputfile'); requires pandas
def Transpose_DF(infile):
		with open(infile, 'r') as f:
			outfile = (pd.read_csv(f, sep='\t', index_col=0, header=0)).T
			outfile.to_csv('{}/{}.txt'.format(arguments.directory, arguments.outputfile), sep='\t')


# Print rows and column dimensions for a data frame (header and index not included in count)
	# Read file (infile), count number of lines ("rows"), print count
	# Read file (infile), split first line of file into list based on tab separation
	# Remove list item at position 0 (original header for col 0), print length of list ("columns")
def Print_Dimensions(infile):

	with open(infile, 'r') as f:
		for count, line in enumerate(f):
			pass
		print(' Number of rows: ', count)

	with open(infile, 'r') as f:
		first_line = f.readline()
		column_list = list(first_line.split('\t'))
		column_list.remove(column_list[0])
		print(' Number of columns: ', len(column_list))


# Make a text file of index (row) names for a given file
	# Read file (infile), make list of index names, remove list item 0 (header),
	# convert list to DataFrame and write to tab-separated csv with
	# new column header as ID_type
def Write_Index_List(infile, ID_type):

	ID_list = []
	with open(infile, 'r') as f:
		for line in f:
			ID = line.split("	")[0]
			ID_list.append(ID)

		ID_list.remove(ID_list[0])
		df = pd.DataFrame({('{}').format(ID_type):ID_list})
		df.to_csv('{}/{}_ID_list.txt'.format(arguments.directory, ID_type), sep='\t')


########################### MAIN ###########################

	# Collect commandline arguments using Get_Arguments() function
	arguments = Get_Arguments()

	# Define output directory; check if directory already exists; if not, make the directory; requires Path from pathlib
	dir = arguments.directory
	if Path(dir).exists() == True:
		pass
	else:
		Path(arguments.directory).mkdir()

	# Display input file dimensions using Print_Dimensions function
	print('\nINPUT FILE DIMENSIONS (rows = chrom-pos, columns = samples)')
	Print_Dimensions(arguments.inputfile)

	# Write a list of row names for inputfile to a new file
	Write_Index_List(arguments.inputfile, 'chrom')

	# Read file to DataFrame and tranposed, write output to a new file
	print('\nTRANSPOSING DATAFRAME')
	Transpose_DF(arguments.inputfile)

	# Display output file dimensions using Print_Dimensions function
	print('\nOUTPUT FILE DIMENSIONS (rows = samples, columns = chrom-pos)')
	Print_Dimensions(dir+'/'+arguments.outputfile+'.txt')

	# Write a list of row names for outputfile to a new file
	print('\nWriting list of samples to txt file.')
	Write_Index_List(dir+'/'+arguments.outputfile+'.txt', 'sample')