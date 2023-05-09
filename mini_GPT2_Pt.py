import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Carrega o tokenizer
tokenizer = AutoTokenizer.from_pretrained("pierreguillou/gpt2-small-portuguese")

# Carrega os parâmetros do modelo salvos em .pth já criado
model_path = "mini_GPT2_Pt.pth"
model_state_dict = torch.load(model_path)

# Cria uma nova instância do modelo e carrega os parâmetros salvos
model = AutoModelForCausalLM.from_pretrained("pierreguillou/gpt2-small-portuguese", state_dict=model_state_dict)

# Usa o modelo para gerar uma sequência de texto
prompt = "Qual o sentido da vida?"
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
