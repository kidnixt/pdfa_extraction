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


alphabet_2 = Alphabet(frozenset((SymbolStr("The doctor was very famous and rich. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died."))))

def get_doctor_wfa_2(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous and rich. "), state_B, 1)
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

alphabet_3 = Alphabet(frozenset((SymbolStr("The doctor was very famous and rich with a huge house. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died."))))


def get_doctor_wfa_3(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous and rich with a huge house. "), state_B, 1)
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


alphabet_4 = Alphabet(frozenset((SymbolStr("The doctor was very famous and rich with a huge house in the woods. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died."))))

def get_doctor_wfa_4(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous and rich with a huge house in the woods. "), state_B, 1)
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


alphabet_5 = Alphabet(frozenset((SymbolStr("The doctor was very famous and rich with a huge house in the woods and a luxury car. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("died."))))

def get_doctor_wfa_5(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous and rich with a huge house in the woods and a luxury car. "), state_B, 1)
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




