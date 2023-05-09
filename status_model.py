import torch
from transformers import AutoModelForCausalLM

# Define o caminho para o arquivo .pth com os parâmetros do modelo
model_path = "mini_GPT2_Pt.pth"

# Carrega os parâmetros do modelo salvos em .pth
model_state_dict = torch.load(model_path)

# Cria uma nova instância do modelo e carrega os parâmetros salvos
model = AutoModelForCausalLM.from_pretrained("pierreguillou/gpt2-small-portuguese", state_dict=model_state_dict)

# Obtém informações sobre o modelo
print(model.config)
