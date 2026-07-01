import fitz

class PDFLoader:  #we may need extract_image() and other function that's why we are using class here instead of function
    '''Responsible for reading pdf and extracting texts'''

    def extract_text(self,pdf_path:str) ->str:
        document  = fitz.open(pdf_path)

        extracted_text = ""
        for page in document:
            print(len(page))
            extracted_text+=page.get_text()
        document.close()
        return extracted_text