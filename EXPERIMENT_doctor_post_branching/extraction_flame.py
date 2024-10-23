#!/usr/bin/env python
# coding: utf-8

import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
import sys
from datetime import datetime
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

sys.path.append("../")
sys.path.append("../../")
torch.manual_seed(42)
device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "gpt2"

# Configurar la salida del gráfico
graphviz = GraphvizOutput()
graphviz.output_file = 'callgraph.png'  # Nombre del archivo de salida

# Inicia el gráfico de llamadas
with PyCallGraph(output=graphviz):
    tokenizer_with_prefix_space = AutoTokenizer.from_pretrained(model_id, use_fast=True, add_prefix_space=True, local_files_only=False)
    model = AutoModelForCausalLM.from_pretrained(model_id,
                                                return_dict_in_generate=True,
                                                pad_token_id=tokenizer_with_prefix_space.eos_token_id).to(device)

    from gpt2.gpt2_probabilistic_model_wrapper import GPT2_probabilistic_model_wrapper
    from guiding_wfa_doctor import alphabet_1, alphabet_2, alphabet_3, alphabet_4, alphabet_5, alphabet_6, alphabet_7, alphabet_8, alphabet_9, alphabet_10, alphabet_11, alphabet_12

    wrapper_with_prefix_space_12 = GPT2_probabilistic_model_wrapper(50, alphabet_12, device, model, tokenizer_with_prefix_space)

    from guiding_wfa_doctor import get_doctor_wfa_1, get_doctor_wfa_2, get_doctor_wfa_3, get_doctor_wfa_4, get_doctor_wfa_5, get_doctor_wfa_6, get_doctor_wfa_7, get_doctor_wfa_8, get_doctor_wfa_9, get_doctor_wfa_10, get_doctor_wfa_11, get_doctor_wfa_12
    from pythautomata.utilities.guiding_wfa_sequence_generator import GuidingWDFASequenceGenerator

    guiding_wfa_12 = get_doctor_wfa_12(wrapper_with_prefix_space_12.terminal_symbol)

    guiding_wfa_sequence_generator_12 = GuidingWDFASequenceGenerator(guiding_wfa_12, None)

    from src.synchronic_model_guided_language_model import SynchronicModelGuidedLanguageModel

    property_model_12 = get_doctor_wfa_12(wrapper_with_prefix_space_12.terminal_symbol)

    synchronic_model_with_prefix_space_12 = SynchronicModelGuidedLanguageModel(wrapper_with_prefix_space_12, property_model_12, model_name="GUIDED_GPT2", max_seq_length=6, normalize_outputs=True, top_k=2)

    from pymodelextractor.teachers.pac_probabilistic_teacher import PACProbabilisticTeacher
    from src.hypothesis_aware_sample_probabilistic_teacher import HypothesisAwareSampleProbabilisticTeacher
    from pymodelextractor.learners.observation_tree_learners.bounded_pdfa_quantization_n_ary_tree_learner import BoundedPDFAQuantizationNAryTreeLearner
    from pythautomata.utilities.probability_partitioner import TopKProbabilityPartitioner, QuantizationProbabilityPartitioner, RankingPartitioner
    from pythautomata.model_comparators.wfa_partition_comparison_strategy import WFAPartitionComparator
    from pythautomata.utilities.uniform_word_sequence_generator import UniformWordSequenceGenerator

    partitioner = QuantizationProbabilityPartitioner(10)
    comparator = WFAPartitionComparator(partitioner)
    epsilon = 0.1
    delta = epsilon
    max_states = 30
    max_query_length = 100

    learner = BoundedPDFAQuantizationNAryTreeLearner(partitioner, 
                                                     max_states, 
                                                     max_query_length, 
                                                     max_seconds_run=60, 
                                                     generate_partial_hipothesis=True, 
                                                     pre_cache_queries_for_building_hipothesis=True,  
                                                     check_probabilistic_hipothesis=False, 
                                                     omit_zero_transitions=True)

    from time import time
    models = []

    def run_learner(learner, teacher):
        start = time()
        learned_model = learner.learn(teacher)
        end = time()
        return end - start, learned_model

    def run_learner_n_times(learner, synchronic_model, comparator, n):
        times = []
        for i in range(n):
            teacher = HypothesisAwareSampleProbabilisticTeacher(synchronic_model, comparator, 30)
            elapsed_time, model = run_learner(learner, teacher)
            times.append(elapsed_time)
            models.append(model)
        return times

    times_12 = run_learner_n_times(learner, synchronic_model_with_prefix_space_12, comparator, 1)
    print(times_12)

    # Crear un dataframe con dos columnas, una para el tiempo y la otra para el profesor correspondiente
    import pandas as pd
    from pandas import DataFrame

    data = {'time': times_12, 'teacher': 12}
    df = DataFrame(data)

    df.to_csv("times.csv")
