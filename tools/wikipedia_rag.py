from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from tools.wikipedia_tool import WikipediaTool


class WikipediaRAG:
    def __init__(self):
        self._wiki = WikipediaTool()
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", ". ", " ", ""],
        )
        self._indexed_pages = {}
        self._retriever = None

    def _rebuild_retriever(self):
        all_docs = []
        for title, chunks in self._indexed_pages.items():
            for i, chunk in enumerate(chunks):
                all_docs.append(Document(page_content=chunk, metadata={"title": title, "chunk": i}))
        self._retriever = BM25Retriever.from_documents(all_docs, k=5) if all_docs else None

    def index_page(self, title: str) -> str:
        text = self._wiki.content(title)
        if not text:
            return ""
        chunks = self._splitter.split_text(text)
        self._indexed_pages[title] = chunks
        self._rebuild_retriever()
        return f"Indexed '{title}': {len(chunks)} chunks, {sum(len(c) for c in chunks)} chars"

    def query(self, question: str, page_title: str = None) -> str:
        if page_title:
            chunks = self._indexed_pages.get(page_title)
            if not chunks:
                return f"Page '{page_title}' not indexed yet. Read it first."
            docs = [Document(page_content=c, metadata={"title": page_title, "chunk": i}) for i, c in enumerate(chunks)]
            retriever = BM25Retriever.from_documents(docs, k=5)
            results = retriever.invoke(question)
        else:
            if not self._retriever:
                return "No pages indexed yet."
            results = self._retriever.invoke(question)

        if not results:
            return "No relevant chunks found."

        return "\n\n---\n\n".join(f"[{r.metadata['title']}]\n{r.page_content}" for r in results)

    @property
    def indexed_titles(self):
        return list(self._indexed_pages.keys())
