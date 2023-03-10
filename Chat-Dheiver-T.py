import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.set_page_config(page_title="Chat-Dheiver-T", page_icon=":robot:", layout="wide")

# Adicionar o logotipo do ChatGPT
st.sidebar.header("ChatGPT")
st.sidebar.image("https://i.imgur.com/4uOgDYK.png")

# Adicionar um estilo CSS personalizado
st.markdown("""
<style>
body {
    background-color: #1f1f1f;
    color: #ffffff;
    font-family: Arial;
}
</style>
""", unsafe_allow_html=True)

# Adicionar um campo de entrada de pergunta semelhante
st.header("Digite sua pergunta:")
input_text = st.text_area("", value="", height=100)

# Adicionar um botão de envio semelhante
output_length = st.slider("Quantidade de palavras na resposta:", min_value=1, max_value=100, value=20, step=1)
if st.button("Gerar texto"):
    output = query({"inputs": input_text, "max_length": output_length})
    if isinstance(output, list):
        output = output[0]
    if "generated_text" in output:
        generated_text = output["generated_text"]
        st.header("Resposta:")
        st.write(generated_text)
    else:
        st.write("Erro ao gerar texto")

st.write("Desenvolvido por dheiver.com.br")
