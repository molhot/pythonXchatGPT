# -*- coding: utf-8 -*-

import openai
import os
import GPT_settingfile

GPT_ORGANIZATIONKEY = os.environ.get('GPTORGANIZATIONKEY')
GPT_APIKEY = os.environ.get('GPTAPIKEY')

if (GPT_ORGANIZATIONKEY == None or GPT_APIKEY == None):
	print("環境変数にキーが設定されていません")
	exit()

openai.organization = GPT_ORGANIZATIONKEY
openai.api_key = GPT_APIKEY

user_input = input("聞きたいことを入力してください >> ")
print(GPT_settingfile.GPT_chatbot(user_input))