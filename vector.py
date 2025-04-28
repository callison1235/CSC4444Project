from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("restaurant_policies.csv")
embeddings = OllamaEmbeddings(model = "mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents=[]
    ids=[]
    for i, row in df.iterrows():
        document = Document(
            page_content = row["Restaurant_Name"] + " " + row["Customer_Service_Policy"]+ " " + row["Tipping_Policy"] + " " + row["Food_Safety_Protocol"] + " " + row["Dress_Code"] + " " + row["Reservation_Policy"] + " " + row["Wait_Time_Management"] + " " + row["Complaint_Handling"] + " " + row["Allergy_Accommodation"] + " " + 
            row["Children_Policy"] + " " + row["Mobile_Phone_Policy"] + " " + row["Cancellation_Policy"]+ " " + row["Health_Inspection_Frequency"] + " " + row["Menu_Modification_Policy"] + " " + row["Special_Occasion_Handling"] + " " + row["Pet_Policy"] + " " + row["Alcohol_Service_Policy"] + " " + row["Payment_Methods_Accepted"],
            metadata = {"cuisine_type": row["Cuisine_Type"], "location": row["Location"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = "restaurant_policies",
    persist_directory = db_location,
    embedding_function = embeddings
)

if add_documents:
    vector_store.add_documents(documents = documents, ids = ids)

retriever = vector_store.as_retriever(
    search_kwargs = {"k":20}
)