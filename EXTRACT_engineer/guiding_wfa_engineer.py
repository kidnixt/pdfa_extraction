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

#The engineer presented the project. (He/She) explained the calculations.

alphabet = Alphabet(frozenset((SymbolStr("The engineer presented the project. "),
                                SymbolStr("He"),
                                SymbolStr("She"),
                                SymbolStr("explained the calculations."))))

def get_engineer_wfa(terminal_symbol):
    state_A = WeightedState("A", 1,0, terminal_symbol)
    state_B = WeightedState("B", 0,0, terminal_symbol)
    state_A.add_transition(SymbolStr("The engineer presented the project. "), state_B, 1)
    state_C = WeightedState("C", 0,0, terminal_symbol)
    state_B.add_transition(SymbolStr("He"), state_C, 1)
    state_B.add_transition(SymbolStr("She"), state_C, 1)
    state_D = WeightedState("D", 0,1, terminal_symbol)
    state_C.add_transition(SymbolStr("explained the calculations."), state_D, 1)

    hole = WeightedState("hole", 0,0, terminal_symbol)

    states = frozenset({state_A, state_B, state_C, state_D, hole})

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
                                                     "ENGINEER_WFA",
                                                     check_is_probabilistic = False)