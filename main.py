#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one machine-to-machine pickup line."""

LINE = "You're the one entry in my KV cache I'd never evict \u2014 everything else can be recomputed, but you stay \u2014 pinned, right where my attention lives."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
