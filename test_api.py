import openai
import os

GPT_ORGANIZATIONKEY = os.environ.get['GPTORGANIZATIONKEY']
GPT_APIKEY = os.environ.get['GPTAPIKEY']

if (GPT_ORGANIZATIONKEY == None or GPT_APIKEY == None)
	print("環境変数にキーが設定されていません")
	exit()

openai.organization = GPT_ORGANIZATIONKEY
openai.api_key = GPT_APIKEY


