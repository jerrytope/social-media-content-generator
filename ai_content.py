import os
import openai
import config
# openai.api_key = config.OPENAI_API_KEY

# import openai

openai.api_key = config['development'].OPENAI_API_KEY

# Soft Tech Business Management software, created for small business to manage day to day tasks


# def Openaiquary(query):
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=query,
#     temperature=0.5,
#     max_tokens=200,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0)

#     if "choices" in response:
#         if len(response["choices"]) > 0:
#             answer = response['choices'][0]['text']
#         else:
#             answer = "sorry you beat the AI"
#     else:
#         answer = "sorry you beat the AI this time"


#     return answer


import openai

def Openaiquary(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ],
        temperature=0.5,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if "choices" in response:
        if len(response["choices"]) > 0:
            answer = response['choices'][0]['message']['content']
        else:
            answer = "sorry you beat the AI"
    else:
        answer = "sorry you beat the AI this time"

    return answer

