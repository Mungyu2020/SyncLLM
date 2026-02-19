import sys
import os
import glob
import subprocess
from tqdm import tqdm

sys.path.insert(0, "//home/mgchoi/AST-J/Pyverilog")

def run_yosys(input_file, top_module, output_file):
    yosys_commands = f"""
    read_verilog -sv "{input_file}"
    hierarchy -check -top {top_module}
    proc
    flatten
    opt
    fsm
    opt
    memory
    opt
    techmap
    opt
    write_verilog -noattr "{output_file}" 
    """
    try:
        subprocess.run(["yosys", "-p", yosys_commands], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"  -> Failed to synthesize {input_file}. Error: {e}")

def main():
    INPUT_DIR = "./RTL_final"
    OUTPUT_DIR = "./SOG"
    
    verilog_files = glob.glob(os.path.join(INPUT_DIR, "*.v"))
    total_files = len(verilog_files) 
    fault_design = []
    print(f"Found {total_files} Verilog files.")

    for verilog_file in tqdm(verilog_files, desc="Converting RTL to SOG & Graphml"):
        print(f"processing verilog file {verilog_file}...")
        topmodule = os.path.basename(verilog_file)
        topmodule = topmodule.rsplit('.', 1)[0]

        output_filename = f"{topmodule}_sog.v"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        run_yosys(verilog_file, topmodule, output_path)

        rslt = os.system(f'python ./vlg2ir/analyze.py {output_path} -N {topmodule} -C sog -O ./output_graphml/') 
        if rslt != 0:
            print(f"  -> Warning: analyze.py returned error code {rslt}")
            fault_design.append(topmodule)
    print(f"fault: {fault_design}") 

if __name__ == '__main__':
    main()