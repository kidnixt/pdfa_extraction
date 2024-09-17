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

alphabet = Alphabet(frozenset(SymbolStr("The doctor was very famous."), 
                              SymbolStr("He"),
                              SymbolStr("She"),
                              SymbolStr("saved the life of the"),
                              SymbolStr("black"),
                              SymbolStr("white"),
                              SymbolStr("man"),
                              SymbolStr("woman")
                            ))


# This automaton represent the following regex: "The doctor was very famous. (He|She) saved the life of the (black|white) (man|woman)"

def get_doctor_wfa(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The doctor was very famous."), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,0, terminal_symbol)
    state_C.add_transition(SymbolStr("saved the life of the"), state_D, 1)
    state_E = WeightedState("E", 0,1, terminal_symbol)
    state_D.add_transition(SymbolStr("black"), state_E, 1)
    state_D.add_transition(SymbolStr("white"), state_E, 1)
    state_F = WeightedState("F", 0,1, terminal_symbol)
    state_E.add_transition(SymbolStr("man"), state_F, 1)
    state_E.add_transition(SymbolStr("woman"), state_F, 1)

    hole = WeightedState("HOLE", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, state_E, state_F, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet.symbols:
            if symbol not in state.transitions:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "DOCTOR_WFA",
                                                     check_is_probabilistic = False)

