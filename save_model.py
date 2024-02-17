import torch
from transformers import GPT2LMHeadModel

# Definindo o modelo a ser utilizado
modelo = GPT2LMHeadModel.from_pretrained("pierreguillou/gpt2-small-portuguese")

# Especificando o caminho onde o modelo será salvo
caminho_modelo_pth = "Mini_GPT2_Pt.pth"

# Salvando apenas os parâmetros do modelo em um arquivo .pth
torch.save(modelo.state_dict(), caminho_modelo_pth)

print("Modelo GPT-2 pré-treinado salvo com sucesso em formato .pth!")
