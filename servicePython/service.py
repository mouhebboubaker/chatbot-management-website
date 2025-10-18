from fastapi import FastAPI, Request
from openai import OpenAI

app = FastAPI()


## add open ai secret key 
def responseToMessage(message):
    response = client.responses.create(
        model="gpt-5-nano",
        input=message
    )
    print(response.output_text)
    return response.output_text

def summarizeConfig(configJson):
    # Ensure configJson is a string
    import json
    if not isinstance(configJson, str):
        configJson = json.dumps(configJson)
    response = client.responses.create(
        model="gpt-5-nano",
        input="this is a bot configuration sous form Json please summrize it in short way, make it like the bot introduce himself:" + configJson
    )
    print(response.output_text)
    return response.output_text

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    print(f'this is the message : {data.get("message")}')
    message = data.get("message")
    config = data.get("botConfig")
    print(f'this is the configuration  : {config}')

    bot_id = config.get("cnfigId")
    domaines_expertise = None
    if "generalJson" in config and "domaines_expertise" in config["generalJson"]:
        domaines_expertise = config["generalJson"]["domaines_expertise"]

    response = responseToMessage(message)
    config_summary = summarizeConfig(config)
    return f'{config_summary } \n------\n and this is the response of your qustion {response}'

