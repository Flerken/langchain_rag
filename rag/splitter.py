from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from unstructured_inference.inference.layoutelement import separate

def get_chunks(file: Path):

    with open(file, encoding="utf-8") as f:
        text = f.read()

    chunk_size = 1000
    chunk_overlap = 150

    book_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("##", "Часть"),
            ("###", "Глава"),
        ],
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    book_chunks = book_splitter.split_text(text)


    #for book_chunk in book_chunks:
    #    book_chunk.metadata.update({"Книга": "Война и мир, том 1"})
    #    print(book_chunk)
    #    print("==" * 50)
    #
    chunks = text_splitter.split_documents(book_chunks)

    #for chunk in chunks:
    #    print(chunk)
    #    print("==" * 50)
    #
    #print(len(book_chunks))
    #print(len(chunks))

    return chunks