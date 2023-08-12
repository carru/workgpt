import streamlit as st
from workgpt import WorkGPT
from constants import *

st.set_page_config(
    page_title=WEBUI_APP_NAME,
    page_icon='🤖',
    layout='wide'
)
st.title(WEBUI_APP_NAME)

@st.cache_resource # concurrency issues
def get_workgpt():
    return WorkGPT()

workgpt = get_workgpt()
result = []

st.info(f'''
        ⚠️ READ ME (no, seriously) ⚠️\n
        This is little more than an experiment at this stage. Do not take answers at face value; it can and will return incorrect information.\n
        Be specific with your questions and add context.\n
        Always refer to the sources used to generate the response for more information related to your query.\n
        {WEBUI_APP_NAME} has read the following Confluence spaces: {WEBUI_CONFLUENCE_SPACES_READ}\n
        ''')

with st.form('myform'):
    query_text = st.text_area('Enter your question:')
    col1, col2 = st.columns(2)
    with col1:
        k_docs = st.number_input('How many sources to search', 1, None, 4, 1)
    with col2:
        generate = st.form_submit_button('Generate answer')
        search = st.form_submit_button('Search only')

if len(query_text):
    with st.spinner('Thinking...'):
        if generate:
            response = workgpt.get_answer(query_text, int(k_docs))
            result.append(response)
        elif search:
            # TODO
            pass

if len(result):
    st.subheader('Answer:')
    response['result']
    st.subheader('Sources:')
    for document in response['source_documents']:
        st.write(f"[{document.metadata['title']}]({document.metadata['source']})")
        document.page_content
    
    st.divider()
    st.text('(Debug) Full reponse:')
    response