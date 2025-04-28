from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import pandas as pd
import random

# Load restaurant data for reference
df = pd.read_csv("restaurant_policies.csv")
restaurant_names = df["Restaurant_Name"].tolist()

model = OllamaLLM(model="llama3.2")

# Initialize memory storage
current_restaurant = None
conversation_history = []

# Function to extract restaurant name from text
def extract_restaurant_name(text):
    for name in restaurant_names:
        if name.lower() in text.lower():
            return name
    return None

template = """
You are a manager and are training a new hire waiter at a restaurant.
Your response is dependent on the place you work at.

These are the policies you should follow when formulating a response: {policies}

{restaurant_context}

{prompt_instruction}

Answer their questions based on how you would approach the situation as a manager and try to teach the new hire how to handle a situation.
Question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# ---- FIRST: Ask for restaurant before anything ----
print("\n----------------------------------------------------------------------\n")
print("Welcome to your training session!")

# Show a numbered list to make it easier
print("\nWhich restaurant are you working at? Please select from the list below:\n")
for idx, name in enumerate(restaurant_names, start=1):
    print(f"{idx}. {name}")

# Get valid input
while True:
    choice = input("\nEnter the restaurant number or name: ").strip()
    
    # If they typed a number
    if choice.isdigit():
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(restaurant_names):
            current_restaurant = restaurant_names[choice_idx]
            break
        else:
            print("Invalid number. Please try again.")
    
    # If they typed a name
    else:
        selected_restaurant = extract_restaurant_name(choice)
        if selected_restaurant:
            current_restaurant = selected_restaurant
            break
        else:
            print("Restaurant not found. Please try again.")

print(f"\nGreat! We'll be training at {current_restaurant}!\n")

# ---- NOW: Begin regular question loop ----
while True:
    print("\n----------------------------------------------------------------------\n")
    question = input("Ask me, your manager, anything you need! (q to quit): \n")
    print("\n\n")
    
    if question.lower() == "q":
        print("Goodbye! Training session ended.")
        break

    conversation_history.append(question)

    restaurant_context = f"Currently discussing restaurant: {current_restaurant}"
    prompt_instruction = ""

    # Query using restaurant + question
    combined_query = f"{current_restaurant} {question}"
    policies = retriever.invoke(combined_query)

    # Run the AI
    result = chain.invoke({
        "policies": policies,
        "question": question,
        "restaurant_context": restaurant_context,
        "prompt_instruction": prompt_instruction
    })
    
    print(result)
