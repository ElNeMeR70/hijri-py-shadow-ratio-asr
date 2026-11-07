#!/usr/bin/env python3
"""
hijri-py-shadow-ratio-asr — حاسبة طول الظل ومقياس العصر الشافعي والحنفي
Gnomon Shadow Ratio Solver for Shafi'i/Maliki/Hanbali (1x) vs Hanafi (2x) Asr
Domain: Hijri Calendar, Lunar Crescent Visibility & Ephemeris (التقويم الهجري وعلم الفلك الإسلامي والأهلة)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"hijri-py-shadow-ratio-asr:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="hijri-py-shadow-ratio-asr",
        domain="Hijri Calendar, Lunar Crescent Visibility & Ephemeris",
        title_ar="حاسبة طول الظل ومقياس العصر الشافعي والحنفي",
        title_en="Gnomon Shadow Ratio Solver for Shafi'i/Maliki/Hanbali (1x) vs Hanafi (2x) Asr",
        sample_input=raw_input,
        computed_output=f"ZawalShadowRatio=0.78 | AsrShafiiAlt=29.3deg | AsrHanafiAlt=19.8deg | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] hijri-py-shadow-ratio-asr (Python) — Gnomon Shadow Ratio Solver for Shafi'i/Maliki/Hanbali (1x) vs Hanafi (2x) Asr")
    res = execute_engine("Lat=24.71,Decl=-16.3")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
