# SRK's Bike Shop

A text-based ordering program in Python. The customer builds a bike by choosing a frame, a colour and an accessory, and the program adds up the price and writes a receipt to `info.txt`.

**Portfolio page:** https://nhojanec.github.io/bike-shop-portfolio/

The page explains how the program works and has a terminal where you can run the real `true_project.py` in your browser, using [Pyodide](https://pyodide.org/) (Python compiled to WebAssembly).

## What's in this repo

| File | What it is |
| --- | --- |
| `true_project.py` | The program |
| `info.txt` | An example receipt the program wrote |
| `index.html` | The portfolio page |

## Run it yourself

```
python true_project.py
```

It needs Python 3 and nothing else. Each order overwrites `info.txt` in the same folder.

## Built with

Python 3: lists of dictionaries, functions, `while` loops, `try / except`, and file writing.
