# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HUGGINGFACEHUB_ACCESS_TOKEN not found in .env"
    )