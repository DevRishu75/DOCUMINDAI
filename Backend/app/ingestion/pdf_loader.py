import fitz

class PDFLoader:
    ''' Loading pdf and extracting text from pdf'''

    def extract_text(self,pdf_path:str)->str:
        document = fitz.open(pdf_path)

        extracted_text = ""
        for page in document:
            extracted_text+= page.get_text()
        document.close()
        return extracted_text