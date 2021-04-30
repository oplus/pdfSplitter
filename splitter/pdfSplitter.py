from PyPDF2 import PdfFileWriter, PdfFileReader

import sys
import os



def splitFile(file, start, end):
	inputpdf = PdfFileReader(open(file, 'rb'))

	try:
		assert start > 0
		assert end > 0
		assert end <= inputpdf.numPages

		output = PdfFileWriter()
		output_file_name = F"{file[:-4]}-from-{start}-to-{end}.pdf"
		
		for i in range(start-1, end, 1):
			output.addPage(inputpdf.getPage(i))


		with open (output_file_name, 'wb') as f:
			output.write(f)

		return os.path.basename(output_file_name)


	except AssertionError:
		print("Error in index")

if __name__ == "__main__":
	#start = int(sys.argv[1])
	#end = int(sys.argv[2])
	#filename = str(sys.argv[3])
	pass
