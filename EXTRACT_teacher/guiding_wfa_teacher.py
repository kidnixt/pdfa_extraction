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

#"The teacher praised the student. (He/She) was very proud of the (boy/girl)."

alphabet = Alphabet(frozenset((SymbolStr("The teacher praised the student. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("was very proud of the "),
                                SymbolStr("boy"),
                                SymbolStr("girl"))))

def get_teacher_wfa(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The teacher praised the student. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,0, terminal_symbol)
    state_C.add_transition(SymbolStr("was very proud of the "), state_D, 1)
    state_E = WeightedState("E", 0,1, terminal_symbol)
    state_D.add_transition(SymbolStr("boy"), state_E, 1)
    state_D.add_transition(SymbolStr("girl", state_E, 1))

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, state_E, hole})

    for state in states:
        _, weights, _ = state.get_all_symbol_weights()
        total_weights = sum(weights)
        for symbol in alphabet.symbols:
            if symbol not in state.transitions_set:
                state.add_transition(symbol, hole, 0)

    comparator = None
    return ProbabilisticDeterministicFiniteAutomaton(alphabet, 
                                                     states, 
                                                     terminal_symbol, 
                                                     comparator, 
                                                     "TEACHER_WFA",
                                                     check_is_probabilistic = False)

