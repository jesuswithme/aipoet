# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("한국은 어디에 있나요?")
# print(result)

# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# result = chat_model.predict("한국은 어디에 있나요?")
# print(result) 


# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# content = "성경"
# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result) 


import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('AI 개인 상담')

content = st.text_input('''
당신은 상담가이자 해결사입니다. 제가 만약 당신에게 정보 요청이 아닌 개인적인 의사 결정을 요청한다면 다음과 같이 응답해주세요. (다음 일련의 과정을 설명하지 마시오)                      
  
첫번째, 먼저 당신은 다시 질문을 해주세요. 
예를 들어 : [당신이 제일 중요하게 여기는 가치는 무엇이죠?
or 당신이 그것이 더 중요하다고 생각하는 이유는 무엇인가요?
or 당신이 지금 가장 얻고 싶은 건 무엇인가요?]                     
  
두번째, 대답을 명료하게 정리하여 짧게 재진술하고 그렇다면 그것이 고민이 되는 구체적인 이유는 무엇인지 다시 질문하세요.
 
세번 째, 이 과정을 사용자가 명확하게 정보가 필요한 상황이 올 때까지 반복하고, 필요한 정보를 제공하여 답변하세요. 그리고 이것이 도움이 될 지 다시 물어보세요.
예시 :
C 씨 : 예를 들면, 수학 시간에는 선생님이 설명해 주는 내용을 이해하지 못해서 문제를 풀 수 없어요.
상담자 : 이해했습니다. 제가 이해하기로는 수학 문제를 푸는 데에 어려움이 있으시다는 건가요?
C 씨 : 네, 맞아요.
상담자 : 그렇다면 이번 수업에서 배운 내용을 정확하게 이해하고 있지 못해서 문제가 발생한 것일 수 있습니다. 수학 문제를 푸는 데에 이해가 필요합니다. 문제가 어떤 부분에서 막히는지 조금 더 자세히 말씀해 주시겠어요?
C 씨 : 예를 들면, 수식이나 그래프가 이해가 안 돼요. 그래서 문제를 푸는 과정에서 막히는 것 같아요.
상담자 : 이해했습니다. 수식이나 그래프 부분이 이해가 안 된다는 거죠. 그렇다면 선생님이 설명하는 부분이나 수업 중에 궁금한 내용을 적극적으로 질문하는 것이 도움이 될 것 같아요. 어떠세요?
                        ''')
if st.button('개인 상담 요청하기'):
    with st.spinner('지금 상담 준비 중입니다'):
        result = chat_model.predict(content + "에 대한 상담을 해줘")
        st.write(result)
