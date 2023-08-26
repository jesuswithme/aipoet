#from dotenv import load_dotenv
#load_dotenv()

#from langchain.llms import OpenAI
#llm = OpenAI()
#result = llm.predict("한국은 어디에 있나요?")
#print(result)

#from langchain.chat_models import ChatOpenAI
#chat_model = ChatOpenAI()
#result = chat_model.predict("한국은 어디에 있나요?")
#print(result) 


#from langchain.chat_models import ChatOpenAI
#chat_model = ChatOpenAI()
#content = "성경"
#result = chat_model.predict(content + "에 대한 시를 써줘")
#print(result) 


import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('AI 시인')

content = st.text_input('시의 주제를 제시해주세요')
if st.button('시 작성 요청하기'):
    with st.spinner('지금 시를 작성중입니다'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
