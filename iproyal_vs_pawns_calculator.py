#!/usr/bin/env python3
"""
IPRoyal vs Pawns.app Residential Proxy Cost Calculator 2026.
"""
import argparse

def calculate(gb):
    # IPRoyal standard residential: $7.00/GB base down to $4.00/GB on volume
    iproyal_rate = 7.00 if gb < 10 else (5.25 if gb < 50 else 4.00)
    iproyal_total = gb * iproyal_rate

    # Pawns.app peer network: $3.00/GB base down to $1.50/GB on volume
    pawns_rate = 3.00 if gb < 10 else (2.50 if gb < 50 else 2.00)
    pawns_total = gb * pawns_rate

    savings = iproyal_total - pawns_total

    print("=" * 60)
    print("Residential Proxy TCO: IPRoyal vs Pawns.app")
    print("=" * 60)
    print(f"Bandwidth Tested:        {gb} GB")
    print(f"IPRoyal Total Cost:      ${iproyal_total:.2f} (@ ${iproyal_rate:.2f}/GB)")
    print(f"Pawns.app Total Cost:    ${pawns_total:.2f} (@ ${pawns_rate:.2f}/GB)")
    print(f"Cost Savings with Pawns: ${savings:.2f} ({((savings/iproyal_total)*100):.1f}% savings)")
    print("=" * 60)
    return savings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IPRoyal vs Pawns Calculator")
    parser.add_argument("--gb", type=int, default=25)
    args = parser.parse_args()
    calculate(args.gb)
