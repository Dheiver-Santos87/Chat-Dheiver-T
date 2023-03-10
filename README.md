Chat-Dheiver-T
Este é um chatbot simples que utiliza o modelo BERT em português "neuralmind/bert-base-portuguese-cased" para responder perguntas em português. A interface do chatbot é construída com o Streamlit.

Pré-requisitos
Antes de executar o código, você precisa ter o Python 3 instalado em sua máquina. Além disso, é necessário instalar as seguintes bibliotecas Python:

streamlit
requests
Você pode instalá-las usando o pip:
pip install streamlit requests

Como executar o código
Para executar o chatbot, abra um terminal ou prompt de comando e execute o seguinte comando:
streamlit run chatbot.py

Isso abrirá o chatbot em seu navegador padrão. Basta digitar uma pergunta em português e clicar no botão "Gerar resposta" para receber uma resposta do modelo BERT.

Personalização
Você pode personalizar o chatbot modificando o valor da variável API_URL para utilizar outro modelo de linguagem suportado pelo Hugging Face. Além disso, você pode modificar o valor da variável API_TOKEN se estiver utilizando um modelo que requer autenticação.

Agradecimentos
Este código foi desenvolvido com base nos exemplos fornecidos pela equipe do Hugging Face e pelo Streamlit. Agradecemos a ambos pela disponibilização dessas ferramentas incríveis para a comunidade de desenvolvedores de inteligência artificial e ciência de dados.
