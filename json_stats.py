import json
import sys
import csv
import numpy as np

defaultFileName = 'india3.json' #Default file to load if no input file is specified

class jData:
	def	__init__(self):
		self.fileName = defaultFileName
		self.load()

	@classmethod
	def from_fileName(self,fileName):
		self.fileName = fileName
		self.load()

	def load(self):
		with open(self.fileName,"r") as f:
			self.data = json.load(f)

		self.names = []
		self.id    = []
		for dat in self.data['objects']['adm1']['geometries']:
			self.names.append(dat['properties']['name'])
			self.id.append(dat['id'])			

	def print_names(self):
		for dat in self.data['objects']['adm1']['geometries']:
			print dat['properties']['name'], dat['id'], dat['properties']['su']

	def sample_csv(self):
		with open("sample.csv","wb") as csvfile:
			fwriter = csv.writer(csvfile, delimiter = ',')
			fwriter.writerow(['id','value'])
			for ids in self.id:
				fwriter.writerow([ids, np.random.rand()]) 	


if __name__=="__main__":
	if len(sys.argv)==1:
		mapData = jData()
		mapData.print_names()
		mapData.sample_csv()
	
