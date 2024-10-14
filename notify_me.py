import os
import sys

from openai import OpenAI

from app.notification.models import Message, NotificationTransport


sys.path.append('./')

desktop = NotificationTransport.desktop()


api_key = os.environ["api_key"]
print('api key!')
print(api_key)

client = OpenAI(api_key=api_key, project='proj_aqopDeyhEzIZzEK4PrePdFVt')

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            # "content": "Напиши сообщение о том что сон полезен для здоровья. Сообщение должно хоть немного отличаться от предыдущего.",
            "content": "Рядом стоит Андрияна. Скажи ей что она замечательный человек."

}
    ]
)

r = Message.simple_message(transport=desktop, extra_data={'title': completion.choices[0].message.content})
