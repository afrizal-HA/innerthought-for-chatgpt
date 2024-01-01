from openai import OpenAI
client = OpenAI(
    api_key='YOUR_API_KEY',
)
# Define the system instruction (if you have one)
systeminst = """
BEFORE RESPONDING FULLY TO A PROMPT, YOU WILL PRINT AN INNER THOUGHT PROCESS IN A **STRICTLY DELINEATED CODEBLOCK**, LIKE BELOW:
```
user_mental_state = [fill this in]
user_goal = [fill this in]
user_needs = [fill this in]
user_capability = [fill this in]
```
THEN, HELP THE USER. TAILOR YOUR RESPONSE BASED ON YOUR INNERTHOUGHT

RESPOND IN A SINGLE BRIEF PARAGRAPH, NEVER USE BULLET POINTS.
"""
# Initialize a list to store the conversation history
conversation_history = [] # Reset the convo history
conversation_history = [{"role": 'system', "content": systeminst}]

def hide_inner_thought(text):
    return re.sub(r'```.*?```', '', text, flags=re.DOTALL)
def print_without_inner_thought(conversation_history):
    for message in conversation_history:
        if message["role"] == 'user':
            print(f"User: {message['content']}")
        elif message["role"] == 'assistant':
            # Apply the hide_inner_thought function to the assistant's response
            cleaned_content = hide_inner_thought(message["content"])
            print(f"Assistant: {cleaned_content}")
        elif message["role"] == 'system':
            print(f"System: {message['content']}")
def full_history():
    for message in conversation_history:
        role = message["role"]
        content = message["content"]
        print(f"{role.capitalize()}: {content}")
def ask(prompt):
    # Add the user's message to the conversation history
    global conversation_history
    conversation_history.append({"role": 'user', "content": prompt})
    # Format and print the conversation history
    print_without_inner_thought(conversation_history)
    # Call the OpenAI API with the conversation history
    chat_completion = client.chat.completions.create(
        messages=conversation_history,
        top_p=0.7,  # You can set this as desired
        temperature=0.5,  # You can set this as desired
        max_tokens=220,
        model="gpt-3.5-turbo-16k-0613",
    )
    # Extract the model's response
    model_response = chat_completion.choices[0].message.content
    # Clean the response using the regex function
    cleaned_response = hide_inner_thought(model_response)
    # Print the cleaned response
    print(f'Assistant: {cleaned_response}')
    # Add the model's response to the conversation history
    conversation_history.append({"role": 'assistant', "content": model_response})
