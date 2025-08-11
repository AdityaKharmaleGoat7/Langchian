# Runnable lambda is a simple runnable that allows you to
# define a function that can be invoked with a single input.
# It can be useful for creating custom logic that can be reused
# across different parts of your application.

#in desi language, "aap kisi bhi function ko runnable bana sakte hain"


from langchain.schema.runnable import RunnableSequence, RunnableLambda

def word_counter(text):
    """Count the number of words in a given text."""
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

res = runnable_word_counter.invoke("This is a test sentence to count the words.")

print(f"Number of words: {res}")

#Just pass the fucntion to RunnableLambda
#and it will be invoked with the input you provide.
