# roster-wizard
A quick tool i wrote for automatically drawing up a duty roster/shift plan. Based on ASP.

## Execution:
1. run `.venv/bin/activate`
2. paste days into `input.txt`
3. edit shifts in `config.pl`
4. run `python3 txt2asp.py`
5. run `python3 -m  clingo asp/config.pl asp/kb-roster.pl asp/off-days.pl`
6. copy output to `asp-answer.txt`
7. run `python3 asp2csv.py` (optionally with `--no-show-date`)

---

## Deprecated:
Execute with: 
```bash
conda activate
cd asp
clingo facts-roster.pl kb-roster.pl
conda deactivate
```

Or without clingo installation:
```bash
docker run --rm -v "$PWD":/mnt -w /mnt kdrakon/clingo ~/roster-wizard
```