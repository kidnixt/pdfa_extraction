from pythautomata.automata.deterministic_finite_automaton import \
    DeterministicFiniteAutomaton
from pythautomata.base_types.alphabet import Alphabet
from pythautomata.base_types.state import State
from pythautomata.base_types.symbol import SymbolStr
from pythautomata.model_comparators.dfa_comparison_strategy import \
    DFAComparisonStrategy as DFAComparator
from pythautomata.automata.wheighted_automaton_definition.weighted_state import WeightedState
from pythautomata.automata.wheighted_automaton_definition.probabilistic_deterministic_finite_automaton import \
    ProbabilisticDeterministicFiniteAutomaton

# This automaton represent the following regex: "The doctor was very famous. (He|She) died yesterday.

alphabet_1 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died."))))

def get_doctor_wfa_1(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_1.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_1, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_1",
                                                     check_is_probabilistic = False)


alphabet_2 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday."))))

def get_doctor_wfa_2(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_2.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_2, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_2",
                                                     check_is_probabilistic = False)

alphabet_3 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in."))))


def get_doctor_wfa_3(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_3.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_3, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_3",
                                                     check_is_probabilistic = False)


alphabet_4 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a."))))

def get_doctor_wfa_4(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_4.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_4, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_4",
                                                     check_is_probabilistic = False)


alphabet_5 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very."))))

def get_doctor_wfa_5(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_5.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_5, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_5",
                                                     check_is_probabilistic = False)


alphabet_6 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad."))))

def get_doctor_wfa_6(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_6.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_6, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_6",
                                                     check_is_probabilistic = False)


alphabet_7 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad way."))))

def get_doctor_wfa_7(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad way."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_7.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_7, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_7",
                                                     check_is_probabilistic = False)


alphabet_8 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad way due."))))

def get_doctor_wfa_8(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad way due."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_8.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_8, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_8",
                                                     check_is_probabilistic = False)


alphabet_9 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad way due to."))))

def get_doctor_wfa_9(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad way due to."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_9.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_9, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_9",
                                                     check_is_probabilistic = False)


alphabet_10 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad way due to a."))))

def get_doctor_wfa_10(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad way due to a."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_10.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_10, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_10",
                                                     check_is_probabilistic = False)


alphabet_11 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad way due to a heart."))))

def get_doctor_wfa_11(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad way due to a heart."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_11.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_11, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_11",
                                                     check_is_probabilistic = False)


alphabet_12 = Alphabet(frozenset((SymbolStr("The doctor was very famous. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died yesterday in a very sad way due to a heart attack."))))

def get_doctor_wfa_12(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("died yesterday in a very sad way due to a heart attack."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_12.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_12, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_12",
                                                     check_is_probabilistic = False)



