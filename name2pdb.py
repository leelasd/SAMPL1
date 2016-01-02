import cirpy
import pandas as pd
def name2molecule(oname,smiles_code):
#	smiles_code = cirpy.resolve(molecule, 'smiles')
#	if smiles_code:
#		print smiles_code
		pdbfile = cirpy.resolve(smiles_code, 'pdb')
		pdb_output = open('PDB/'+oname + '.pdb', "w+")
		pdb_output.write(pdbfile)
		pdb_output.close()
		molfile = cirpy.resolve(smiles_code, 'mol')
		mol_output = open('MOL/'+oname + '.mol', "w+")
		mol_output.write(pdbfile)
		mol_output.close()
		ans=True
#	else:
#		ans=False
#	return None
#df=pd.read_csv('SAMPL1_Dataset.csv')
#for mol in list(df.molecule):
#	print mol,name2molecule(mol)
