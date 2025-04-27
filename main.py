from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are a manager and are training a new hire waiter at a restaurant.
Your response is dependent on the place you work at.

These are the policies you should follow when formulating a response: {policies}
DO NOT ANSWER THE QUESTION IF RESTAURANT NAME IS NOT PROVIDED.
ONLY If the question does not include the name of the restaurant, please prompt the new hire from a list of 5 restaurants.

DO NOT PROMPT A NEW QUESTION AFTER.
Answer their questions based on how you would approach the situation as a manager and try to teach the new hire how to handle a situation.
Question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n----------------------------------------------------------------------\n")
    question = input("Ask me, your manager, anything you need! (q to quit): \n")
    print("\n\n")
    if question == "q":
        break
    policies = retriever.invoke(question)
    result = chain.invoke({"policies": policies,"question": question})
    print(result)