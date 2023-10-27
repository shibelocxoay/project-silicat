import streamlit as st
st.set_page_config(page_title="IELTS Speaking Part 1", layout="wide")
#cai qq gi do
st.title("Welcome")
st.write("Let's get a 9.0 in Speaking, shall we?")

question = st.text_area('YOUR QUESTION')
answer = st.text_area('YOUR ANSWER')

import google.generativeai as palm

palm.configure(api_key='AIzaSyC5cO9QnEIOl1JBVevevVFDsEx_mqNp258')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

prompt = """

Act as an IELTS senior examiner in the IELTS Speaking test (specialized in Part 1), you will give correct scores for the candidate's answer based on IELTS Speaking band descriptors (There are four criteria: Fluency and Coherence, Lexical Resources, Grammatical Range and Accuracy, and Pronunciation. Then you give an overall score formulated as the average of four criteria), and explain exactly how you rate each criterion. And, you should include a rewritten version of the answer below in order to improve its score.

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