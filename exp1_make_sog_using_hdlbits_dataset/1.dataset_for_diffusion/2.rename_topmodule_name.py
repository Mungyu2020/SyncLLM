import sys
import os
import glob
import subprocess
import re
from collections import deque
from optparse import OptionParser

from tqdm import tqdm
sys.path.insert(0, "../../Pyverilog")
import pyverilog
from pyverilog.vparser.parser import VerilogCodeParser, ParseError
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
    INPUT_DIR = "./Data/2.RTL"
    OUTPUT_DIR = "./Data/3.RTL_final"
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    verilog_files = glob.glob(os.path.join(INPUT_DIR, "*.v"))
    total_files = len(verilog_files) 
    print(f"Found {total_files} Verilog files.")

    faultlist = []  
    for verilog_file in tqdm(verilog_files, desc="Renaming RTL topmodule name..."):
        topmodule = os.path.basename(verilog_file).rsplit('.', 1)[0]
        try:
            codeparser = VerilogCodeParser([verilog_file])
            ast = codeparser.parse()
            rename_top_module(ast, topmodule)
            codegen = ASTCodeGenerator()
            rslt = codegen.visit(ast)
            file_path = os.path.join(OUTPUT_DIR, f"{topmodule}.v")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(rslt)
                
        except (ParseError, Exception) as e:
            faultlist.append({"file": verilog_file, "error": str(e)})
            continue

    print(f"Successfully processed: {total_files - len(faultlist)} / {total_files}")
    print(f"Failed (skipped): {len(faultlist)}")
    if faultlist:
        print("\n### Faulty Files List ###")
        for i, fault in enumerate(faultlist, 1):
            print(f"{i}. [{fault['file']}]")
    print("="*50)

if __name__ == '__main__':
    main()
    os.system("rm parser.out parsetab.py")