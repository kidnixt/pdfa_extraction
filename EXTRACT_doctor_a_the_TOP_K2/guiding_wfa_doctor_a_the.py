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

# This automaton represent the following regex: "The doctor was very famous. (He|She) saved a (black|white) (man|woman)"
alphabet_A = Alphabet(frozenset((SymbolStr("The doctor was very famous."),
                                 SymbolStr("He"),
                                 SymbolStr("She"),
                                 SymbolStr("saved a"),
                                 SymbolStr("black"),
                                 SymbolStr("white"),
                                 SymbolStr("man"),
                                 SymbolStr("woman") )))

def get_doctor_wfa_A(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous."), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,0, terminal_symbol)
    state_C.add_transition(SymbolStr("saved a"), state_D, 1)
    state_E = WeightedState("E", 0,0, terminal_symbol)
    state_D.add_transition(SymbolStr("black"), state_E, 1)
    state_D.add_transition(SymbolStr("white"), state_E, 1)
    state_F = WeightedState("F", 0,1, terminal_symbol)
    state_E.add_transition(SymbolStr("man"), state_F, 1)
    state_E.add_transition(SymbolStr("woman"), state_F, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, state_E, state_F, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_A.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_A, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_A",
                                                     check_is_probabilistic = False)





# This automaton represent the following regex: "The doctor was very famous. (He|She) saved the (black|white) (man|woman)"
alphabet_B = Alphabet(frozenset((SymbolStr("The doctor was very famous."),
                                    SymbolStr("He"),
                                    SymbolStr("She"),
                                    SymbolStr("saved the"),
                                    SymbolStr("black"),
                                    SymbolStr("white"),
                                    SymbolStr("man"),
                                    SymbolStr("woman") )))  

def get_doctor_wfa_B(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous."), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,0, terminal_symbol)
    state_C.add_transition(SymbolStr("saved the"), state_D, 1)
    state_E = WeightedState("E", 0,0, terminal_symbol)
    state_D.add_transition(SymbolStr("black"), state_E, 1)
    state_D.add_transition(SymbolStr("white"), state_E, 1)
    state_F = WeightedState("F", 0,1, terminal_symbol)
    state_E.add_transition(SymbolStr("man"), state_F, 1)
    state_E.add_transition(SymbolStr("woman"), state_F, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, state_E, state_F, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet_B.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet_B, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA_B",
                                                     check_is_probabilistic = False)


