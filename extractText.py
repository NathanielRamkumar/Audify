import PyPDF2 
import os

def pdfToText(pdf_path):
    pdfFile = f"{os.path.dirname(__file__)}/PDF Files/{pdf_path}"

    # Detailed error Handling, im so responsible
    if os.path.exists(pdfFile) and pdfFile.endswith(".pdf"): # The easy way
        pass
    else: # The hard way
        if not os.path.exists(pdfFile):
            raise Exception("File no exist")
        elif not pdfFile.endswith(".pdf"):
            raise Exception(f"This ain't a pdf its a \"{pdfFile[pdfFile.find('.'):]}\"")
        else:
            raise Exception("how do you mess up this badly")

    # This is what we're here for
    with open(pdfFile, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        return text

def copyToTxt(fileName,txtFileName, unique=0): # I hate nebraska
    txtFile = f"{os.path.dirname(__file__)}/Txt Files/{txtFileName}.txt"
    if unique:
        i=0
        while os.path.exists(txtFile):
            txtFile = f"{os.path.dirname(__file__)}/Txt Files/{txtFileName[:]}{i}.txt"
            i+=1
    with open(txtFile,'w') as t:
        t.write(pdfToText(fileName).replace('\n \n \n','\n').replace('\n \n',' ').replace('�',''))


# tets
if __name__ == "__main__":
    copyToTxt("report2.pdf", "epic",1)

