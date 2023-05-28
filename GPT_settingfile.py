import openai

def	GPT_chatbot(ASKING):
    completion = openai.ChatCompletion.create (
        model    = "gpt-3.5-turbo",     # モデルを選択
        messages = [{
                "role":"user",       # 役割
                "content":ASKING,   # メッセージ 
            }],
    
        # max_tokens  = 1024,             # 生成する文章の最大単語数
        # n           = 1,                # いくつの返答を生成するか
        # stop        = None,             # 指定した単語が出現した場合、文章生成を打ち切る
        # temperature = 0.5,              # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )
    return (completion["choices"][0]["message"]["content"])