## Mini_GPT2_PT: Salvando o modelo GPT-2 pré-treinado em formato .pth
O modelo GPT-2 pré-treinado "pierreguillou/gpt2-small-portuguese" é um modelo de linguagem de grande escala treinado em uma grande quantidade de texto em português, fornecido pela biblioteca Transformers da Hugging Face. Esse modelo pode ser facilmente carregado e usado para gerar sequências de texto a partir de um prompt de entrada.

Porém, se você precisa usar o modelo em outro ambiente ou personalizá-lo para seus próprios dados, pode ser útil salvá-lo em formato .pth, que contém apenas os parâmetros do modelo em um arquivo menor e mais fácil de ser carregado.

O script Mini_GPT2_PT.py permite baixar o modelo "pierreguillou/gpt2-small-portuguese" em formato .pth usando a biblioteca PyTorch. O modelo é então salvo em um arquivo com a função torch.save(), que salva apenas os parâmetros do modelo em um arquivo .pth.

Ao salvar o modelo em formato .pth, você pode carregá-lo em outros scripts Python usando a classe AutoModelForCausalLM e os parâmetros salvos em .pth usando a função load_state_dict() da classe torch.nn.Module. Isso permite que você carregue e use o modelo em outros ambientes onde a biblioteca PyTorch está instalada, sem precisar instalar a biblioteca Transformers ou baixar o arquivo binário completo do modelo.

Além disso, é possível personalizar o modelo antes de salvá-lo em formato .pth, ajustando seus parâmetros para atender às suas necessidades específicas. Por exemplo, você pode ajustar o número de camadas, o tamanho do embedding ou o número de neurônios em cada camada antes de salvá-lo.

Em resumo, o script Mini_GPT2_PT.py mostra como salvar o modelo GPT-2 pré-treinado "pierreguillou/gpt2-small-portuguese" em formato .pth usando a biblioteca PyTorch. Isso permite que você carregue e use o modelo em outros ambientes onde a biblioteca PyTorch está instalada, sem precisar instalar a biblioteca Transformers ou baixar o arquivo binário completo do modelo.
