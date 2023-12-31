### Documentation

This is a Python snippet that integrates ChatGPT API with a system instruction that gives ChatGPT an inner thoUght process. It follows chain-of-thought prompting principles where the model will 'plan' before responding with an answer or guidance. It is specifically inspired by Josh Tenenbaum's lecture on incorporating models of the world, comprising of objects and agents with beliefs and goals, to artificial intelligence systems.

### Use Case

You can implement this code in your ChatGPT assistant to improve the model's answer quality. You can also use the prompt in other non-ChatGPT applications.

### Notes

**Brief response**: I deliberately set this model to respond in a brief paragraph, as the bullet-point storms ChatGPT always do gets verbose and tedious. The intent is that the inner thought mechanism can improve straightforward, readable responses.
**Chat History**: That this code comes with a chat history for the model's context. You can have a continous conversation with the model by using and reusing the ask() function.

### Functions
hide_inner_thought(): Define a simple regex to hide the inner thought, hiding it from the user's end
print_without_inner_thought(): Prints the conversation without showing the model's inner thought for cleaner UI. Note that the inner thought is retained in the model's context.
full_history(): Prints the conversation and showing the model's inner thought, for your evaluation.
ask(prompt): Prompt the model. 
