# Assignment Week 10

[[_TOC_]]

## Tasks 
 

## Dependencies
- python3 with:
    - jupyter notebooks
    - Bipython
    - matplotlib
    - pandas
    - numpy
    - seaborn
    - sklearn

## Data structure
- [original_data/](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/original_data) contains the MSA and metadata file downloaded from the ncbi virus database.
- [MSA.fasta](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/MSA.fasta) and [sequence_metadata.csv](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/sequence_metadata.csv) are the processed MSA and metadata files for usage with TreeTime and Nextatrain augur.
- [UPGMA_tree.png](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/UPGMA_tree.png) shows the phylogenetic tree produced in Task 2.
- [augur_out/](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/augur_out) contains the input and results from analysing the data using Nextstrain augur and auspice. [augur_out/auspice/](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/augur_out/auspice) contains the JSON file that was visualized using Nextstrain auspice.

## How to run
- run the notebook [coronavirus_phylogeny.ipynb](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/coronavirus_phylogeny.ipynb)
- after running the notebook,in order to do the phylogenetic analysis using Nextstrain augur and auspice, execute these commands in [augur_out/](https://git.imp.fu-berlin.de/verversl98/dsls-2020/-/blob/master/Week%2010/Eva/augur_out):

1. Infer phylogeny from MSA: 
augur tree --alignment ../MSA.fasta --method iqtree --output augur.out.nwk 
2. Get a time-resolved tree: 
augur refine --alignment ../MSA.fasta --tree augur.out.nwk --metadata ../sequence_metadata.csv --output-tree augur.out.refined.nwk --output-node-data augur.refine.branches.json --timetree 
3. Annotate the tree with ancestral traits: 
augur traits --tree augur.out.refined.nwk --metadata ../sequence_metadata.csv --output traits.json --columns country region Host --confidence 
4. Infer ancestral sequence for each internal node (trace back mutations): 
augur ancestral --tree augur.out.refined.nwk --alignment ../MSA.fasta --output-node-data nt_muts.json --inference joint
5. export to auspice format: 
augur export v2 --tree augur.out.refined.nwk --metadata ../sequence\_metadata.tsv --node-data augur.refine.branches.json traits.json nt\_muts.json --output auspice/SARS-CoV2.json --geo-resolutions country --color-by-metadata country  Host --colors auspice/config/colors.tsv --lat-longs auspice/config/lat_longs.tsv
(The config files for coloring and latidues/longitudes were generated following the config files in the github repo of the zika tutorial (https://github.com/nextstrain/zika-tutorial.git))
6. Visualize results
auspice view --datasetDir auspice

