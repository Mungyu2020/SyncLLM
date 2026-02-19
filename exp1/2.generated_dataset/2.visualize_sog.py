import sys
import os
import glob
from tqdm import tqdm

sys.path.append("./pyverilog") 
import pyverilog
from pyverilog.vparser.parser import VerilogCodeParser

sys.path.append("./vlg2ir") 
from vlg2ir.AST_analyzer import AST_analyzer

def main():
    INPUT_DIR = "./Data/4.SOG"
    OUTPUT_DIR = "./Data/5.Img_sog/"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    sog_files = glob.glob(os.path.join(INPUT_DIR, "*.v"))
    total_files = len(sog_files) 
    print(f"Found {total_files} Verilog files.")
    fault_list = []
    for sog_file in tqdm(sog_files, desc="Converting SOG to png"):
        filename = os.path.basename(sog_file)
        topmodule = os.path.splitext(filename)[0]
        print(f"processing {topmodule}...")
        try:
            codeparser = VerilogCodeParser([sog_file])
            ast = codeparser.parse()
            
            ast_analysis = AST_analyzer(ast)
            ast_analysis.AST2Graph(ast)
            g = ast_analysis.graph
            
            g.show_graph(topmodule, OUTPUT_DIR)
            
        except Exception as e:
            print(f"Error processing {topmodule}: {e}") 
            fault_list.append(topmodule)
    print(f"fault_list: {fault_list}")

if __name__ == '__main__':
    main()
    os.system("rm parser.out parsetab.py")