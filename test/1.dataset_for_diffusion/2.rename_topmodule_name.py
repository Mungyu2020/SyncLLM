import sys
import os
import glob
import subprocess
import re
from collections import deque
from optparse import OptionParser

from tqdm import tqdm
sys.path.insert(0, "//home/mgchoi/AST-J/Pyverilog")
import pyverilog
from pyverilog.vparser.parser import VerilogCodeParser
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

def rename_top_module(ast, topmodule):
    module_defs = []
    for child in ast.children():
        if child.__class__.__name__ == 'Description':
            for desc_child in child.children():
                if desc_child.__class__.__name__ == 'ModuleDef':
                    module_defs.append(desc_child)
    if len(module_defs) == 1:
        module_defs[0].name = topmodule
        return
    for module in module_defs:
        for child in module.children():
            if child.__class__.__name__ == 'InstanceList':
                module.name = topmodule
    return

def main():
    INPUT_DIR = "./RTL"
    verilog_files = glob.glob(os.path.join(INPUT_DIR, "*.v"))
    total_files = len(verilog_files) 
    print(f"Found {total_files} Verilog files.")
    for verilog_file in tqdm(verilog_files, desc="Renaming RTL topmodule name..."):
        topmodule = os.path.basename(verilog_file)
        topmodule = topmodule.rsplit('.', 1)[0]
        print(f"filename: {verilog_file} -> topmoudle: {topmodule}")
        codeparser = VerilogCodeParser([verilog_file])
        ast = codeparser.parse()
        rename_top_module(ast, topmodule)
        codegen = ASTCodeGenerator()
        rslt = codegen.visit(ast)
        file_path = f"./RTL_final/{topmodule}.v"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rslt)
        print(f"Saved {topmodule}...")

if __name__ == '__main__':
    main()