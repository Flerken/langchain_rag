from langchain_docling.loader import DoclingLoader, ExportType

FILE_PATH = "../docs/techweek.pdf"

loader = DoclingLoader(FILE_PATH, export_type=ExportType.DOC_CHUNKS)

documents = loader.load()

for document in documents:
    print(document)
    print("=" * 30)