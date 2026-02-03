# api_key = 'f0be915e-09a5-4002-92ee-165fc8e4c55a'

# documentation link
# https://www.volcengine.com/docs/82379/1302008
from volcenginesdkarkruntime import Ark

# # lite 128k model
# model = "ep-20241107235447-4g2vh"

# # pro-128k model
model = "ep-20241108225503-4l4z2"

client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model=model,
    messages = [
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "常见的十字花科植物有哪些？"},
    ],
)
print(completion.choices[0].message.content)





