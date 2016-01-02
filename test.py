#import cirpy
import numpy as np
import pandas as pd
import pubchempy as pcp
from name2pdb import *
import cirpy
import pandas as pd
def name2molecule(oname,smiles_code):
       oname=''.join(oname.split())
       pdbfile = cirpy.resolve(smiles_code, 'pdb')
       pdb_output = open('PDB/'+oname + '.pdb', "w+")
       pdb_output.write(pdbfile)
       pdb_output.close()
       molfile = cirpy.resolve(smiles_code, 'mol')
       mol_output = open('MOL/'+oname + '.mol', "w+")
       mol_output.write(molfile)
       mol_output.close()
       ans=True
       return None
df=pd.read_csv('SAMPL1_Dataset.csv')
for oname,smiles in zip(df.molecule,df.SMILES):
	if oname != 'nitroxyacetone':
		print oname,smiles
		name2molecule(oname,smiles)
