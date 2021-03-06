import os
import tempfile
import unittest

import dotpruner
from dotpruner import utils
from dotpruner.__main__ import main

from .graphs import *

class TestDotPrunerAPI(unittest.TestCase):

    def setUp(self):
        self.SIMPLE_GRAPH = SIMPLE_GRAPH, PRUNED_SIMPLE_GRAPH
        self.SIMPLE_GRAPH_MAX = SIMPLE_GRAPH, MAX_PRUNED_SIMPLE_GRAPH
        self.COMPLEX_CFSM = COMPLEX_CFSM, PRUNED_COMPLEX_CFSM
    
    def test_prune_simple_cfsm(self):
        original_graph, expected = self.SIMPLE_GRAPH
        actual_graph = dotpruner.process_from_string(original_graph)
        self.assertTrue(utils.same_graph(actual_graph.to_string(), expected))
    
    def test_prune_simple_cfsm(self):
        original_graph, expected = self.SIMPLE_GRAPH_MAX
        actual_graph = dotpruner.process_from_string(original_graph,
                                                     node_picker=max)   
        self.assertTrue(utils.same_graph(actual_graph.to_string(), expected))

    def test_prune_complex_cfsm(self):
        original_graph, expected = self.COMPLEX_CFSM
        actual_graph = dotpruner.process_from_string(original_graph)
        self.assertTrue(utils.same_graph(actual_graph.to_string(), expected))

class TestDotPrunerCLI(unittest.TestCase):

    def setUp(self):
        temp_dir = tempfile.mkdtemp()
        self.input_path = os.path.join(temp_dir, 'sample.dot')
        self.output_path = os.path.join(temp_dir, 'output.dot')
        with open(self.input_path, 'w') as dot_file:
            dot_file.write(EMPTY_GRAPH)

    def test_cli_io(self):
        return_code = main([self.input_path, '-d', self.output_path])
        self.assertEqual(return_code, 0)

        with open(self.output_path, 'r') as dot_file:
            output_graph = dot_file.read()
        
        self.assertTrue(output_graph, EMPTY_GRAPH)