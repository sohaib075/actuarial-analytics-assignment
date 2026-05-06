import json

with open('notebooks/Actuarial_Analytics_Assignment.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
code_cells = [c for c in cells if c['cell_type']=='code']
md_cells = [c for c in cells if c['cell_type']=='markdown']

# Check for all required elements
tasks = {}
for c in code_cells:
    src = ''.join(c.get('source', []))
    for i in range(1, 47):
        if f'Task {i}' in src or f'task {i}' in src.lower():
            if i not in tasks:
                tasks[i] = False
            tasks[i] = True

interp_tasks = {}
for c in md_cells:
    src = ''.join(c.get('source', []))
    for i in range(1, 47):
        if f'Interpretation (Task {i})' in src:
            interp_tasks[i] = True

print(f'Total Cells: {len(cells)}')
print(f'Code Cells: {len(code_cells)}')
print(f'Markdown Cells: {len(md_cells)}')
print(f'Code implementation: {sum(1 for t in tasks.values() if t)}/46 tasks found')
print(f'Interpretation Cells: {len(interp_tasks)}/46')
missing = sorted(set(range(1, 47)) - set(interp_tasks.keys()))
print(f'Missing interpretations: {missing if missing else "NONE"}')

# Check critical components
has_manual_comb = any('math.comb' in ''.join(c.get('source', [])) for c in code_cells)
has_manual_fact = any('math.factorial' in ''.join(c.get('source', [])) for c in code_cells)
has_levene = sum(1 for c in code_cells if 'levene' in ''.join(c.get('source', [])).lower())
has_bonf = any('itertools.combinations' in ''.join(c.get('source', [])) for c in code_cells)

print(f'\nCRITICAL REQUIREMENTS:')
print(f'Task 7 (math.comb): {"PASS" if has_manual_comb else "FAIL"}')
print(f'Task 12 (math.factorial): {"PASS" if has_manual_fact else "FAIL"}')
print(f'Levene Tests: {has_levene} found')
print(f'Task 32 (Bonferroni/itertools): {"PASS" if has_bonf else "FAIL"}')

status = 'READY' if all([sum(1 for t in tasks.values() if t) >= 40, has_manual_comb, has_manual_fact, has_bonf]) else 'CHECK'
print(f'\nNOTEBOOK STATUS: {status}')

if missing:
    print(f'\nACTION REQUIRED: Add {len(missing)} interpretation cells for tasks: {missing}')
else:
    print(f'\nALL SYSTEMS GO: Execute notebook with "Run All Cells"')
