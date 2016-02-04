# Lethality_Prediction_Drosophila

As of 14/12/2015 the code contained within this Repo is of dev form and therefore is set into small scripts which must be manually 
run along with the input files being manually selected. This is to make debugging as efficient as possible.

  Scripts:
To start, the Ontology scripts should first be executed. These are labelled in order -1 to -3.

Next there are 5 scripts (1 to 5) and are to be executed in order. 

There are two additional files, Remove_IMP and Remove_ISS which can be operationally run just before the 3_Vector.py file. 
If either of these files are used, then the input and output file names for the removal files and Vector will have to be modified.

Input Files:
##########################
gene_association.fb - http://flybase.org/static_pages/downloads/FB2015_04/go/gene_association.fb.gz 
##########################################

###################################
allele_phenotype_data_fb_2015_04.tsv - flybase.org/static_pages/downloads/FB2015_04/alleles/allele_phenotypic_data_fb_2015_04.tsv.gz
###################################

#########################
GO.obo - http://geneontology.org/ontology/go-basic.obo
format-version: 1.2
data-version: releases/2015-10-24
date: 23:10:2015 15:28
saved-by: rph
auto-generated-by: TermGenie 1.0
################


