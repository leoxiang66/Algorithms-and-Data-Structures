from .base import Node, Link

class DFA:
    def __init__(self, initial_node, nodes, terminal_node):
        self.initial_node = initial_node
        self.nodes = nodes
        self.terminal_node = terminal_node
    def get_next_node(self, current_node, etiquette):
        for link in current_node.links:
            if link.etiquette == etiquette:
                return link.to_node
        return None
    def accepts(self, string):
        node = self.initial_node
        for character in string:
            node = self.get_next_node(node, character)
        return self.terminal_node.equals(node)
    def __str__(self):
        automata = "Initial node: %s\nTerminal node: %s\n" % (self.initial_node.val, self.terminal_node.val)
        for node in self.nodes:
            automata += node
        return automata
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)




