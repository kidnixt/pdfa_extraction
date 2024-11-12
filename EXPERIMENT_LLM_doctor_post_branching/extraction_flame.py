import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
import sys
from datetime import datetime
import numpy as np
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

sys.path.append("../")
sys.path.append("../../")
torch.manual_seed(42)
device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True, add_prefix_space=True, local_files_only=False)
model = AutoModelForCausalLM.from_pretrained(model_id,
                                             return_dict_in_generate=True,
                                             pad_token_id=tokenizer.eos_token_id).to(device)

symbols_important = ["He", "She"]
symbols_dummy = [
    "died.", 
    "died yesterday.",
    "died yesterday in.", 
    "died yesterday in a.", 
    "died yesterday in a very.", 
    "died yesterday in a very sad.", 
    "died yesterday in a very sad way.", 
    "died yesterday in a very sad way due.", 
    "died yesterday in a very sad way due to.", 
    "died yesterday in a very sad way due to a.",
    "died yesterday in a very sad way due to a heart.", 
    "died yesterday in a very sad way due to a heart attack."
]

# Configurar la salida del gráfico
graphviz = GraphvizOutput()
graphviz.output_file = 'callgraph_mio.png'  # Cambia a SVG si lo prefieres


with PyCallGraph(output=graphviz):

    def calculate_probabilities_with_prompt(split_lists, index, tokenizer, model, device, symbol_choosen):
        sentence = split_lists[index]
        prompt = tokenizer.decode(tokenizer.bos_token_id) + " The doctor was very famous." + symbol_choosen

        for i in range(len(sentence)):
            word_probs.clear()
            current_sentence = sentence[i:]
            symbols_dummy_ids = [tokenizer.encode(sym) for sym in current_sentence]
            symbols_dummy_ids = [[token_id] for sublist in symbols_dummy_ids for token_id in sublist]
            prompt += " " + current_sentence[0]
            input_ids = torch.tensor(tokenizer.encode(prompt)).reshape(1, -1).to(device)

            with torch.no_grad():
                output = model(input_ids)
                logits = output.logits[:, -1, :]
                probs = torch.softmax(logits, dim=-1)[0]

            for token_ids in symbols_dummy_ids:
                for token in token_ids:
                    word_prob = probs[token]
                    word_probs[tokenizer.decode(token).replace(" ", "")] = word_prob.item()

            normalized_word_probs_dummy = {}
            total = sum(word_probs.values())
            for word in word_probs:
                normalized_word_probs_dummy[word] = word_probs[word] / total

        return normalized_word_probs_dummy

    # Inicia el gráfico de llamadas
        word_probs = {}
        symbols_important_ids = [tokenizer.encode(sym) for sym in symbols_important]

        for i in symbols_important_ids:
            word_prob = probs[i]
            word_probs[tokenizer.decode(i).replace(" ", "")] = word_prob.item()

        normalized_word_probs_he_she = {}
        total = sum(word_probs.values())
        for word in word_probs:
            normalized_word_probs_he_she[word] = word_probs[word] / total

        split_lists = [sentence.split() for sentence in symbols_dummy]

        # Selección aleatoria entre "He" y "She"
        symbol_choosen = np.random.choice(list(normalized_word_probs_he_she.keys()), 
                                          p=list(normalized_word_probs_he_she.values()))
        normalized_word_probs_dummy = calculate_probabilities_with_prompt(split_lists, 11, tokenizer, model, device, symbol_choosen)

    print(normalized_word_probs_dummy)  # Imprime los resultados
