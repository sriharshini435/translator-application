import streamlit as st
from deep_translator import GoogleTranslator as gt
st.set_page_config(page_title="translator app",layout="wide")
st.title("Translation application")
st.subheader("this application translates one language to another")
st.divider()
langs = gt().get_supported_languages ()
text=st.text_area("enter the text to translate",height=150)
c1,c2=st.columns(2)
with c1:
    source_lang=st.selectbox("source language",options=langs)
with c2:
    target_lang=st.selectbox("target language",options=langs)


if st.button("translate"):
    if text.strip() != "":
        model=gt(source=source_lang,target=target_lang)
        result=model.translate(text)
        st.success(result)
    else:
        st.error("please enter a valid text")
