from pathlib import Path
import re,json
s=Path(__file__).resolve().parents[1].joinpath('integers_final_work/main.tex')
if not s.exists(): raise SystemExit('Supply the extracted manuscript at integers_final_work/main.tex next to amir/ directory')
t=s.read_text()
items=set(re.findall(r'\\bibitem(?:\[[^]]+\])?\{([^}]+)\}',t))
calls=re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',t)
keys={k.strip() for group in calls for k in group.split(',')}
labels=set(re.findall(r'\\label\{([^}]+)\}',t))
refs={k.strip() for group in re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',t) for k in group.split(',')}
print(json.dumps(dict(bibliography_entries=len(items),citation_commands=len(calls),unique_cited_keys=len(keys),missing_citation_keys=sorted(keys-items),uncited_entries=sorted(items-keys),labels=len(labels),undefined_refs=sorted(refs-labels),unreferenced_labels=sorted(labels-refs)),indent=2))
assert not (keys-items) and not (refs-labels)
