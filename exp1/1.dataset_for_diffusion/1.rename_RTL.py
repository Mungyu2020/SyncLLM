import os
import re
import shutil

INPUT_DIR = "./Data/1.RTL_raw"
OUTPUT_DIR = "./Data/2.RTL"
if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR) 

for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".v"):
        continue

    clean_name = filename.strip("'")
    name_body, extension = os.path.splitext(clean_name)
    
    if '_' in name_body:
        target_name = name_body.split('_', 1)[1]
    else:
        target_name = name_body
    
    new_name_body = re.sub(r'[^0-9a-zA-Z]', '_', target_name)
    new_name_body = new_name_body.replace("_", "")
    if new_name_body[0].isdigit():
        new_name_body = "_" + new_name_body
    new_filename = new_name_body + extension
    
    src_path = os.path.join(INPUT_DIR, filename)
    dst_path = os.path.join(OUTPUT_DIR, new_filename)
    
    shutil.copy2(src_path, dst_path) 
    print(f"Success: {filename} -> {new_filename}")

print("\nFinished.")