import networkx as nx
import os
import re
import sys
import glob
from tqdm import tqdm

def clean_name(name):
    return re.sub(r'\.|\[|\]|\\|:', r'_', str(name))

def main():
    INPUT_DIR = "./Data/4.Output_graphml"
    OUTPUT_DIR = "./Data/5.Img_graphml"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    input_files = glob.glob(os.path.join(INPUT_DIR, "*.graphml"))
    fault_list = [] 
    for img in tqdm(input_files, desc="Converting graphml to png"):
        print(f"processing {img}...")
        G = nx.read_graphml(img)

        filename = os.path.basename(img)
        base_name = os.path.splitext(filename)[0]
        
        dot_outfile = os.path.join(OUTPUT_DIR, f"{base_name}.dot")
        png_outfile = os.path.join(OUTPUT_DIR, f"{base_name}.png")

        lines = []
        lines.append(f"digraph {clean_name(base_name)} {{")
        try:
            for node_id, data in G.nodes(data=True):
                clean_id = clean_name(node_id)
                label = data.get('name', node_id)
                node_type = str(data.get('type', 'unknown')).lower()
                
                style_attr = ""
                
                if 'reg' in node_type:
                    style_attr = "[style=filled, color=lightblue]"
                elif 'wire' in node_type:
                    style_attr = "[style=filled, color=red]"
                elif 'input' in node_type or 'in' == node_type:
                    style_attr = "[style=filled, color=black, fontcolor=white]"
                elif 'output' in node_type or 'out' == node_type:
                    style_attr = "[style=filled, color=green]"
                elif 'const' in node_type:
                    style_attr = "[style=filled, color=grey]"
                elif any(x in node_type for x in ['op', 'and', 'or', 'not', 'xor', 'nand', 'nor', 'mux', 'add', 'sub', 'concat']):
                    style_attr = "[style=filled, color=pink]"
                else:
                    style_attr = f'[label="{label}"]'

                if style_attr:
                    style_attr = style_attr.replace("[", f'[label="{label}", ')
                else:
                    style_attr = f'[label="{label}"]'
                    
                lines.append(f"    {clean_id} {style_attr};")

            for u, v in G.edges():
                u_clean = clean_name(u)
                v_clean = clean_name(v)
                lines.append(f"    {u_clean} -> {v_clean};")

            lines.append("}")

            with open(dot_outfile, "w") as f:
                f.write("\n".join(lines))

            os.system(f"dot -Tpng {dot_outfile} -o {png_outfile}")
        except Exception as e:
            print(f"Error processing {base_name}: {e}") 
            fault_list.append(base_name)
    print(f"fault_list: {fault_list}")


if __name__ == "__main__":
    main()