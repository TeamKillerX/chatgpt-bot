### chatgpt-bot

![Python Version](https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor)
![Issues](https://img.shields.io/github/issues/TeamKillerX/chatgpt-bot?style=for-the-badge&logo=appveyor)
![Forks](https://img.shields.io/github/forks/TeamKillerX/chatgpt-bot?style=for-the-badge&logo=appveyor)
![Stars](https://img.shields.io/github/stars/TeamKillerX/chatgpt-bot?style=for-the-badge&logo=appveyor)

### Disclaimer
```
️                       ⚠️ WARNING FOR YOU ️ ️⚠️
   chatgpt is used to help your account activities on Telegram
   We are not responsible for what you misuse in this repository
   !  Be careful when using this repository!
   If one of the members misuses this repository, we are forced to ban you
   Never ever abuse this repository
```

### Deploy to Branch [Heroku]

1. <b>Go to github, your fork</b>
2. <b>Delete your fork. If you didn't fork, go to step</b>
3. <b>Fork repo.</b>
4. <b>edit</b> 👉 [.env](https://github.com/TeamKillerX/chatgpt-bot/blob/main/.env_sample)
5. <b>Go to heroku</b>
6. <b>Desktop view</b>
7. <b>Go to deploy tab</b>
8. <b>Connect your github account</b>
9. <b>Deploy Main branch.</b>

### Deploy to Heroku
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TeamKillerX/chatgpt-bot)


### Tutorial Vps
```console
Rendy@Ubuntu~ $ git clone https://github.com/TeamKillerX/chatgpt-bot
Rendy@Ubuntu~ $ cd chatgpt-bot
Rendy@Ubuntu~ $ pip3 install -r requirements.txt
Rendy@Ubuntu~ $ cp .env_sample .env
Rendy@Ubuntu~ $ nano .env
Rendy@Ubuntu~ $ python3 bot.py
```

### Example payload 

```python
# chatGPT-3

payload = {
   "model": "text-davinci-003", 
   "prompt": "Hello World", 
   "max_tokens": 200, 
   "temperature": 0, 
   "top_p": 1, 
   "n": 1, 
   "stream": False, 
   "logprobs": None, 
   "stop": None
}

headers = {
   "Content-Type": "application/json", 
   "Authorization": f"Bearer {OPENAI_API}"
}

url = "https://api.openai.com/v1/completions"

response = requests.post(url, json=payload, headers=headers)
data_example = response.json()

message_text = data_example["choices"][0]["text"]

await message.edit_text(message_text) # await or client.send_message(message.chat.id, message_text, reply_to_message_id=message.id)
```
### Library
* [Dan](https://github.com/pyrogram) For [Pyrogram](https://github.com/pyrogram/pyrogram)


### Contributors
<b>you can pull requests here</b>
https://github.com/TeamKillerX/chatgpt-bot/pulls

<a href="https://github.com/TeamKillerX/chatgpt-bot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TeamKillerX/chatgpt-bot" />
</a>


### Credits
```
https://github.com/TeamKillerX/chatgpt-bot
```
### Donate
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.buymeacoffee.com/randydev)
