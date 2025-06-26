import os

import asyncpg
from dotenv import load_dotenv

load_dotenv()

SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")

if not SUPABASE_DB_URL:
    raise ValueError("Falta SUPABASE_DB_URL en el archivo .env")


async def get_connection():
    return await asyncpg.connect(SUPABASE_DB_URL, statement_cache_size=0)
