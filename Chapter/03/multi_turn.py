from openai import OpenAI # 오픈 AI 라이브러리 가져오기
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key) # 오픈 AI 클라이언트의 인스턴스 생성

def get_ai_response(messages):
	response = client.chat.completions.create(
	    model="gpt-4o",    # 응답 생성에 사용할 모델 지정
	    temperature=0.9,   # 응답 생성에 사용할 temperature 지정
	    messages=messages, # 대화 기록을 입력으로 전달
	)
	return response.choices[0].message.content  # 생성된 응답의 내용 반환

messages=[        
	        {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
] # 초기 시스템 메시지 설정
	
while True:
	user_input = input("사용자: ") # 사용자 입력받기
	
	if user_input == "exit":
		break
	
	messages.append({"role": "user", "content": user_input})
	ai_response = get_ai_response(messages)
	messages.append({"role": "assistant", "content": ai_response})
	print("AI: " + ai_response) # AI 응답 출력