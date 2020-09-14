import unittest
from dotpruner import utils

from .graphs import *

class TestParseGraph(unittest.TestCase):
    
    def test_parse_from_string_empty(self):
        graph = utils.parse_graph_from_string(EMPTY_GRAPH)
        self.assertEqual(graph.get_name(), 'EMPTY')

    def test_parse_from_string_nonempty(self):
        graph = utils.parse_graph_from_string(FLOWCHART)
        self.assertEqual(graph.get_name(), 'FLOWCHART')

class TestParseComponents(unittest.TestCase):

    def setUp(self):
        self.empty = utils.parse_graph_from_string(EMPTY_GRAPH)
        self.flow_chart = utils.parse_graph_from_string(FLOWCHART)

    def test_parse_nodes_from_empty(self):
        nodes = utils.parse_nodes(self.empty)
        self.assertSetEqual(set(nodes.keys()), set())

    def test_parse_nodes_from_nonempty(self):
        nodes = utils.parse_nodes(self.flow_chart)
        self.assertSetEqual(set(nodes.keys()), set(['a', 'b', 'c']))
        self.assertEqual(nodes['a']['label'], '"node one"')
        self.assertEqual(nodes['b']['label'], '"node two"')
        self.assertEqual(nodes['c']['label'], '"node three"')

    def test_parse_edges_from_empty(self):
        node_to_edges = utils.parse_edges(self.empty)
        self.assertSetEqual(set(node_to_edges.keys()), set())

    def test_parse_simple_edges_from_nonempty(self):
        node_to_edges = utils.parse_edges(self.flow_chart)
        self.assertSetEqual(set(node_to_edges.keys()), set(['a', 'b']))
        self.assertSequenceEqual(node_to_edges['a'].edges(), [('b', {})])
        self.assertSequenceEqual(node_to_edges['b'].edges(), [('c', {})])