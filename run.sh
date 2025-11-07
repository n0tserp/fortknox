#!/bin/bash
python3 -m venv venv 2>/dev/null || true
source venv/bin/activate
pip install PyQt6 --quiet
python main.py