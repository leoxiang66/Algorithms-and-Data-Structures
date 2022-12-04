if __name__ == '__main__':
    from automata import DFA, Node, Link

    s0 = Node("s0")
    s1 = Node("s1")
    s2 = Node("s2")

    s0_0_s0 = Link(s0, '0', s0)
    s0_1_s1 = Link(s0, '1', s1)
    s1_0_s2 = Link(s1, '0', s2)
    s1_1_s0 = Link(s1, '1', s0)
    s2_0_s1 = Link(s2, '0', s1)
    s2_1_s2 = Link(s2, '1', s2)

    s0.add_link(s0_0_s0)
    s0.add_link(s0_1_s1)
    s1.add_link(s1_0_s2)
    s1.add_link(s1_1_s0)
    s2.add_link(s2_0_s1)
    s2.add_link(s2_1_s2)

    a = DFA(s0, [s0, s1, s2], s0)

    print(a)
    print(a.accepts('1011101')) #True
    print(a.accepts('10111011')) #False