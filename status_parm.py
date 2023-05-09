import torch

model_path = "mini_GPT2_Pt.pth"
model_state_dict = torch.load(model_path)

for key in model_state_dict.keys():
    print(key)
