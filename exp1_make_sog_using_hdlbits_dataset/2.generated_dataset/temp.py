import sys
import os
import glob
from tqdm import tqdm
import graphviz

sys.path.append("./pyverilog") 
import pyverilog
from pyverilog.vparser.parser import VerilogCodeParser

sys.path.append("./vlg2ir") 
from vlg2ir.AST_analyzer import AST_analyzer

def visualize_AST(root_node, filename="tree"):
    dot = graphviz.Digraph('Tree')
    dot.attr('node', shape='box')
    def visit(node):
        dot.node(str(id(node)), f"{node.__class__.__name__}")
        for c in node.children():
            dot.edge(str(id(node)), str(id(c)))
            visit(c)
    visit(root_node)
    dot.render(filename, view=False, format='png', cleanup=True)

def main():
    WORK_DIR = os.getcwd()
    TARGET_DESIGN = "TwoGates"
    INPUT_PATH = f"{WORK_DIR}/SOG/{TARGET_DESIGN}_sog.v"
    codeparser = VerilogCodeParser([INPUT_PATH])
    ast = codeparser.parse()

    visualize_AST(ast) 
    ast_analysis = AST_analyzer(ast)
    ast_analysis.AST2Graph(ast)
    g = ast_analysis.graph
            
    #g.show_graph(TARGET_DESIGN)       

if __name__ == '__main__':
    main()