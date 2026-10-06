# Duplicate Line Remover

Paste a list, one item per line, and remove the repeats. The logic is written in Python (`dedupe.py`) and runs in the browser through [PyScript](https://pyscript.net), so the site works on GitHub Pages with no server.

## Features
- Removes duplicate lines (first occurrence is kept)
- Options: ignore case, trim spaces, sort A to Z
- Shows how many duplicates were removed
- Copy result button

## Run locally
Browsers block PyScript from loading files over `file://`, so serve the folder:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Test
```bash
python -m unittest
```

## Deploy
Push to GitHub, then go to **Settings → Pages**, choose the `main` branch and `/ (root)`.

## Files
| File | Purpose |
|---|---|
| `index.html` | Page and styling |
| `main.py` | Connects the page to the Python logic |
| `dedupe.py` | `remove_duplicates()` function |
| `pyscript.toml` | Tells PyScript to load `dedupe.py` |
| `test_dedupe.py` | Unit tests |
