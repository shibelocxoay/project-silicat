import streamlit as st
st.set_page_config(page_title="IELTS Speaking Part 1", layout="wide")
#Prompt+Question
st.title("Welcome")
st.write("Let's get a 9.0 in Speaking, shall we?")

question = st.text_area('YOUR QUESTION')
answer = st.text_area('YOUR ANSWER')

import google.generativeai as palm

palm.configure(api_key='AIzaSyC5cO9QnEIOl1JBVevevVFDsEx_mqNp258')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

prompt_LR = """

Acting as an IELTS senior examiner in the IELTS Speaking test (specialized in Part 1 - an informal talk about people's lives),
you need to give scores related to the criterion called "Lexical Resources"
based on IELTS Band Descriptor that candidates should show the range of vocabulary at the test taker’s disposal,
which will influence the range of topics which they can discuss,
and the precision with which meanings are expressed and attitudes conveyed
(if they are English proficient when using a wide range of vocabulary accurately, you should give them about band 9.
If their answer is not related to the question, you should give them about band 4 below).
Next, you have to provide detailed suggestion about their answer."

"""
prompt = prompt_LR + "Question:\n" + question + "Answer:\n" + answer

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=10000,
)

st.write('Feedback about your Lexical Resources and detailed suggestion:\n', completion.result)

prompt_GRA = """

Acting as an IELTS senior examiner in the IELTS Speaking test (specialized in Part 1 - an informal talk about people's lives),
you need to give scores related to the criterion called "Grammatical Range and Accuracy"
based on IELTS Band Descriptor that candidates should acknowledge the accurate and appropriate use of syntactic forms
in their speech in order to meet Speaking test requirements, and to the test taker’s range of grammatical resources,
a feature which will help to determine the complexity of propositions which can be expressed
(if they are English proficient when combining different sentence structures and complex syntax accurately, you should give them about band 9.
If their answer is not related to the question, you should give them about band 4 below).
Next, you have to provide detailed suggestion about their answer."

"""
prompt = prompt_GRA + "Question:\n" + question + "Answer:\n" + answer

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=10000,
)

st.write('Feedback about your Grammatical Range and Accuracy and detailed suggestion:\n', completion.result)