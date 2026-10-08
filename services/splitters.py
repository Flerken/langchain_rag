from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter



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


async def get_book_chunks(book_text: str):

    book_chunks = book_splitter.split_text(book_text)
    return text_splitter.split_documents(book_chunks)

    #for chunk in chunks:
    #    print(chunk)
    #    print("==" * 50)
    #
    #print(len(book_chunks))
    #print(len(chunks))