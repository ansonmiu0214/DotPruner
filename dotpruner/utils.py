"""
This module holds utility methods for parsing components
of DOT graphs and performing the actual pruning.
"""

import collections
import pydot
import typing
import sys

DEFAULT_NODE_PICKER = min

identity = lambda x: x

class Node:
    """
    A class to represent outgoing edges connected to a node.
    """

    def __init__(self):
        self._edges = []

    def add_edge(self, dst, attrs):
        """Add outgoing edge with attributes `attrs` to `dst` node.
        
        Args:
            dst: Name of destination node
            attrs: Key-value mapping of edge attributes
        """

        self._edges.append((dst, attrs))
    
    def edges(self, *, transform_key=identity):
        """Gets the outgoing edges connected to this node.

        Args:
            transform_key: A function to transform the destination node
                value. Defaults to the identity function.
        Returns:
            A list of tuples, with each tuple defined by the (possibly
            transformed) endpoint and attributes of each edge. The list
            is sorted in ascending order of names.
        """

        return sorted([(transform_key(key), value) for key, value in self._edges],
                       key=lambda pair: pair[0])


def parse_graph_from_file(filename: str) -> pydot.Graph:
    graph, *_ = pydot.graph_from_dot_file(filename)
    return graph

def parse_graph_from_string(data: str) -> pydot.Graph:
    graph, *_ = pydot.graph_from_dot_data(data)
    return graph

def parse_edges(graph: pydot.Graph) -> typing.Mapping[str, Node]:
    """Parse edges from graph.

    Args:
        graph (pydot.Graph): The graph to parse
    Returns:
        typing.Mapping[str, Node]: A mapping of name to edges for each node.
    """

    node_to_edges = collections.defaultdict(Node)

    for edge in graph.get_edges():
        src = edge.get_source()
        dst = edge.get_destination()
        attrs = edge.get_attributes()

        node_to_edges[src].add_edge(dst, attrs)

    return node_to_edges

def parse_nodes(graph: pydot.Graph) -> typing.Mapping[str, typing.Mapping[str, str]]:
    """Parse nodes from graph.

    Args:
        graph (pydot.Graph): The graph to parse
    Returns:
        typing.Mapping[str, typing.Mapping]: A mapping of name to attributes for each node.
    """

    return {node.get_name(): node.get_attributes()
            for node in graph.get_nodes()}

def prune_graph(node_to_edges: typing.Mapping[str, Node],
                initial_lookup: typing.Mapping[str, str], *,
                pick_node) -> typing.Mapping[str, str]:
    """Prunes the graph of nodes that share the same outgoing edges.

    This works by 'merging' nodes using a lookup table, initially
    `initial_lookup`: if two nodes `x` and `y` are the same, the `pick_node`
    function defines the node to be preserved. Suppose `x` is to be preserved:
    then the lookup table maps `y` to `x`.

    This process terminates when one iteration over the `node_to_edges`
    mapping results in no nodes being pruned. The function returns the
    final lookup table defining the nodes that have been 'merged'.

    Args:
        node_to_edges (typing.Mapping[str, Node]): A mapping of name to edges for each node.
        initial_lookup (typing.Mapping[str, str]): Lookup table for pruning.
        node_picker: A function that, given the names of two nodes to be pruned,
            picks the node to preserved.
    Returns:
        typing.Mapping[str, str] The final lookup table that maps nodes
        in the original graph to their 'pruned version'.
    """
    final_lookup = dict(**initial_lookup)
    should_prune_again = False

    for curr_node_name, curr_node in node_to_edges.items():
        for other_node_name, other_node in node_to_edges.items():

            if final_lookup[curr_node_name] == final_lookup[other_node_name]:
                continue

            # FIXME: let user customise definition of `edge equality`
            lookup_fn = lambda dst: final_lookup[dst]
            curr_edges = curr_node.edges(transform_key=lookup_fn)
            other_edges = other_node.edges(transform_key=lookup_fn)

            if curr_edges == other_edges:
                should_prune_again = True

                root_node_name = pick_node(curr_node_name, other_node_name)
                child_node_name = curr_node_name if root_node_name == other_node_name else other_node_name

                final_lookup[child_node_name] = root_node_name

    return prune_graph(node_to_edges, final_lookup, pick_node=pick_node) \
        if should_prune_again else final_lookup

def same_graph(graph_1: str, graph_2: str) -> bool:
    """Compares the string representation of two DOT graphs for equality.

    Args:
        graph_1 (str): String representation of graph 1
        graph_2 (str): String representation of graph 2
    Returns:
        bool: True iff `graph_1` equals `graph_2`
    """

    return sorted([line for line in graph_1.splitlines() if line.strip()]) \
        == sorted([line for line in graph_2.splitlines() if line.strip()])

def info(msg, **kwargs):
    print(f'INFO: {msg}', **kwargs, file=sys.stdout)

def error(msg, **kwargs):
    print(f'ERROR: {msg}', **kwargs, file=sys.stderr)