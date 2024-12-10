# Assumes main code is in server.py
import asyncio

from . import server


def main():
    """Enter package here (called via __main__.py)."""
    asyncio.run(server.main())
