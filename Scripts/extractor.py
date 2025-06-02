
import os
from llama_index.core import VectorStoreIndex,Settings
from llama_index.core import SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = "your api key"

# Load documents 
documents = SimpleDirectoryReader('replace/your/file/path').load_data()

# Create an index
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine()

Extractor_prompt_tmpl_str=(
"you are an expert cv extractor system which can extract the important details from the cv given.\n"
"Extract the following informations from the given context.\n"
"1. name of the person :\n"
"2. email of the person :\n"
"3.address of the person :\n "
"4. mobile number :\n"
"5. previous experiences : \n"

"Context information is below.\n"
"---------------------\n"
"{context_str}\n"
"---------------------\n"
"Given the context information and not prior knowledge, "
"give the informations asked.\n"
"Query: {query_str}\n"
"Answer: "

)


from llama_index.core import PromptTemplate
Extractor_prompt_tmpl=PromptTemplate(Extractor_prompt_tmpl_str)

query_engine.update_prompts(
{"response_synthesizer:text_qa_template": Extractor_prompt_tmpl}
)

#query
response = query_engine.query("provide the rerequired informations?")
print(response)