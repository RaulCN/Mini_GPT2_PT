import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Carrega o tokenizer
tokenizer = AutoTokenizer.from_pretrained("pierreguillou/gpt2-small-portuguese")

# Carrega os parâmetros do modelo
model_path = "Mini_GPT2_Pt.pth"
model_state_dict = torch.load(model_path)

# Cria uma nova instância do modelo
model = AutoModelForCausalLM.from_pretrained("pierreguillou/gpt2-small-portuguese", state_dict=model_state_dict)

# Função para carregar a memória a partir de um arquivo de texto
def carregar_memoria(nome_arquivo):
    memoria = {}
    with open(nome_arquivo, "r") as f:
        linhas = f.readlines()
        for i in range(0, len(linhas), 3):
            pergunta = linhas[i].strip().split(": ")[1]
            resposta = linhas[i + 1].strip().split(": ")[1]
            memoria[pergunta] = resposta
    return memoria

# Caminho do arquivo de texto com a memória
arquivo_memoria = "memoria_namorada.txt"

# Carrega a memória do arquivo
memoria = carregar_memoria(arquivo_memoria)

# Loop da conversa
while True:
    # Prompt do usuário
    prompt = input("Digite sua mensagem: ")

    # Verifica se o prompt está na memória
    if prompt in memoria:
        resposta = memoria[prompt]
        print("Namorada Virtual:", resposta)
    else:
        # Codifica o prompt
        input_ids = tokenizer.encode(prompt, return_tensors="pt")

        # Gera a resposta
        output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

        # Decodifica a resposta
        resposta = tokenizer.decode(output[0], skip_special_tokens=True)

        # Armazena a conversa na memória
        memoria[prompt] = resposta

        # Exibe a resposta
        print("Namorada Virtual:", resposta)
