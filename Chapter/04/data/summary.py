from openai import OpenAI # 오픈 AI 라이브러리 가져오기
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key) # 오픈 AI 클라이언트의 인스턴스 생성

def summarize_txt(file_path: str):
    client = OpenAI(api_key=api_key)  # 클라이언트 인스턴스 생성
    with open(file_path, "r", encoding="utf-8") as f:
        txt = f.read()
	
    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 저자의 문제 인식과 주장을 파악하고, 주요 내용을 요약하라.SystemError

    작성해야 하는 포맷은 다음과 같다.

    # 제목

    ## 저자의 문제 인식 및 주장

    ## 저자 소개


    ============== 이하 텍스트 =============

    {txt}
    '''
    
    print(system_prompt)
    print("======================================")
    
    response = client.chat.completions.create(
	    model="gpt-4o",   
	    temperature=0.1, 
	    messages=[
            {"role": "system", "content": system_prompt},
        ]
	)
    return response.choices[0].message.content 

if __name__ == "__main__":
    file_path = "04/output/computing_machinery.txt"
    
    summary = summarize_txt(file_path)
    print(summary)
    
    with open("04/output/computing_machinery_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)  # 요약 결과를 파일에 저장