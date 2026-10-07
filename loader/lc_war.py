from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("../docs/war-and-peace-1.txt", encoding="utf-8") as f:
    text = f.read()

chunk_size = 2000
chunk_overlap = 200

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=[r"\s#{2}\s.*\n", r"\s#{3}\s.*\n","\n\n", "\n", " ", ""],
    is_separator_regex=True,
    keep_separator=False,
)

chunks = text_splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print("==" * 50)