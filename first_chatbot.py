
## My First chatbot model using GenAI API       
from google import genai
import os 
# print("API KEY :",os.getenv('GEMINI_API_KEY'))
client=genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

History=[]
while True :
    prompt=input('Enter the prompt : ')
    History.append(f'user prompt :{prompt}')

    if prompt.lower() =='exit':
        print('Good Bye')
        break
    response=client.models.generate_content(
        model='gemini-1.5-pro-preview-0409',
        contents=History
    )
    print(response.text)
    History.append(f'model response:{response.text}')

print(History)
