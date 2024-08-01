import OpenAI 
api_key = open ('api_key', 'r').read()
openai.api_key = 'sk-proj-4qnvM5dBDYXjsjrUgqwAT3BlbkFJd9OM4VJSNWYzkgLv7CCo'
  
def chat_gpt (prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{'role':'user','content':prompt}]
    )
    return response.choices[0].messages.content.strip()

if __name__ == '__main__':
    while True: 
        user_input = input ("You:")
        if user_input.lowerr() in ['quit','bye','exit']:
            break 
        
        response = chat_gpt(user_input)
        print ('Advisor:',response)