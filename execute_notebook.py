#!/usr/bin/env python
"""Execute notebook and verify all cells run without errors"""
import subprocess
import sys
import json

print("Executing notebook...")
result = subprocess.run(
    [sys.executable, "-m", "nbconvert", "--to", "notebook", 
     "--execute", "--ExecutePreprocessor.timeout=600",
     "notebooks/Actuarial_Analytics_Assignment.ipynb",
     "--output", "notebooks/Actuarial_Analytics_Assignment_executed.ipynb"],
    capture_output=True,
    text=True,
    cwd="."
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)

if result.returncode == 0:
    print("\n✅ Notebook executed successfully!")
    
    # Count executed cells
    with open("notebooks/Actuarial_Analytics_Assignment_executed.ipynb", "r") as f:
        nb = json.load(f)
    
    code_cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
    executed_cells = [c for c in code_cells if c.get("execution_count") is not None]
    
    print(f"✅ {len(executed_cells)}/{len(code_cells)} code cells executed")
    
else:
    print("\n❌ Notebook execution failed!")
    sys.exit(1)
