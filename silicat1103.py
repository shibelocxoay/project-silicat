import streamlit as st
st.set_page_config(page_title="IELTS Speaking Part 1", layout="wide")
st.title("Welcome")
st.write("Let's get a 9.0 in Speaking, shall we?")

question = st.text_area('YOUR QUESTION')
answer = st.text_area('YOUR ANSWER')

import google.generativeai as palm

palm.configure(api_key='AIzaSyC5cO9QnEIOl1JBVevevVFDsEx_mqNp258')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

prompt = """

Acting as an IELTS senior examiner in the IELTS Speaking test (specialized in Part 1), you need to give scores related to 1) Lexical Resources and 2) Grammatical range and accuracy bsaed on IELTS descriptors. Next, you need to give each explanation to each criterion and give a rewritten version of the answer provided."

"""
prompt = prompt + "Question:\n" + question + "Answer:\n" + answer

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=10000,
)

st.write('Feedback about your answer:\n', completion.result)