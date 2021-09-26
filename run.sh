#!/bin/sh

eval "$(conda shell.bash hook)"
conda activate phd-scraper
python main.py
