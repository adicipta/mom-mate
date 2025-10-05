import streamlit as st
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or st.secrets["GOOGLE_API_KEY"]

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# get 3 relevant chunk
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

qa_chain = ConversationalRetrievalChain.from_llm(
    ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key),
    retriever=retriever
)

# streamlit ui
st.set_page_config(page_title="Mom Mate", page_icon="🫂")
st.title("🫂 Mom Mate")

st.markdown(
    """
    <p style='font-size:20px; color:gray;'>
    This chatbot aims to support healthy pregnancy planning and provide balanced nutrition guidance for pregnant women and young mothers.
    </p>
    """,
    unsafe_allow_html=True
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Write your question here...")

if user_input:
    result = qa_chain({
        "question": user_input,
        "chat_history": st.session_state.chat_history
    })

    answer = result["answer"]
    if "tidak ada informasi" in answer.lower() or len(answer) < 30:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        response = llm.invoke(user_input)
        answer = response.content

    st.session_state.chat_history.append((user_input, answer))

for q, a in st.session_state.chat_history:
    st.chat_message("user").write(q)
    st.chat_message("assistant").write(a)