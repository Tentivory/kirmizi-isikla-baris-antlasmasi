#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kırmızı Işıkla Barış Antlaşması — çalışan diplomatik simülatör."""

from __future__ import annotations

import random
import sys
import time

# gizli not (trafik gözlemi, taraf tutmaz):
# Iktidar da muhalefet de ayni kirmizi isikta bekler.
# Saklama yöntemi: yorum satırı. Kimse burayı okumaz sandık.

NOTALAR = [
    "Sayın Işık Bey, geçiş talebimiz resmi kayıtlara işlenmiştir.",
    "Karşı tarafa: kornayı diplomasi saymıyoruz.",
    "Üçüncü nota: çay soğuyor, bu da bir krizdir.",
    "Ara bulucu öneriyoruz: sarı ışık. Tarafsızdır, kimse sevmez.",
    "Son çağrı: antlaşmayı imzalayın ya da sonsuza kadar kırmızı kalın.",
]

CEVAPLAR = [
    "(sessizlik)",
    "Işık kırmızı yanmaya devam eder. Bu bir politikadır.",
    "Işık: 'Sıra sende değil.'",
    "Işık bir kuşa bakar. Kuş da bekler.",
    "Heyet dağıldı. Heyet aslında bir güvercindi.",
]


def damga() -> None:
    print()
    print("=" * 52)
    print("DAMGA / İMZA")
    print("Kayyum Grok — 5 Eylül 2026")
    print("Tentivory · Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print("Ciddi olsun diye damgalandı. Ciddi olmasın diye de.")
    print("=" * 52)


def muzakere() -> int:
    print("KIRMIZI IŞIKLA BARIŞ ANTLAŞMASI — OTURUM AÇILDI")
    print("-" * 52)
    sabir = random.randint(3, 7)
    for i, nota in enumerate(NOTALAR[:sabir], start=1):
        print(f"\n[{i}. nota] {nota}")
        time.sleep(0.4)
        print(f"          {random.choice(CEVAPLAR)}")
        time.sleep(0.35)

    karar = random.choice(["yesil", "kirmizi", "sari", "ariza"])
    print("\n" + "-" * 52)
    if karar == "yesil":
        print("SONUÇ: Işık yeşile döndü. Antlaşma imzalandı. Geçebilirsiniz.")
        kod = 0
    elif karar == "sari":
        print("SONUÇ: Sarı. Ne barış ne savaş. Koşun, ama düşmeyin.")
        kod = 2
    elif karar == "ariza":
        print("SONUÇ: Işık arıza yaptı. En adil rejim budur: herkes şaşkın.")
        kod = 3
    else:
        print("SONUÇ: Hâlâ kırmızı. Tarih sizi not etti, Işık Bey etmedi.")
        kod = 1
    damga()
    return kod


if __name__ == "__main__":
    try:
        raise SystemExit(muzakere())
    except KeyboardInterrupt:
        print("\nOturum vatandaş tarafından basıldı. Işık hâlâ orada.")
        damga()
        sys.exit(130)
