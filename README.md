# Collatz Prefix Verification

This repository contains the data and code used to verify the contraction of all base-3 prefix classes under the Collatz map, supporting the paper:

**"From Infinite to Finite: A Proof of the Collatz Conjecture via Prefix Partition and Height Descent"**  
by *Sadie A. Sherratt*

---

## 📌 Overview

Every base-3 prefix of length 10 was tested for contraction under the modified Collatz map:

For each prefix r in the range [0, 3^10), the minimal representative n₀ = 3^10 × r was generated.

The Collatz map T(n) was defined as:

    T(n) = n / 2 if n is even

    T(n) = (3n + 1) / 2 if n is odd

Each trajectory was checked for one of the following outcomes:

    A strict drop in the symbolic height function

    Entry into the known terminal cycle {1, 2, 4}
No prefix failed to contract.

---

## 🔍 Purpose

This computational experiment supports the main theoretical claim of the paper:  
**Every ternary prefix class contracts in symbolic height**, providing a finite partition of the natural numbers under the Collatz map and proving universal convergence.

---

## ⚙️ How to Use

1. Make sure you have **Python 3.10+** installed.
2. Run the script:

```
python prefix_verification.py
```

3. This will generate a new file `prefix_summary.csv` with the results of all 59,049 prefix class checks.

---

## 📂 Files

- `prefix_verification.py` – Verifies symbolic height contraction for each prefix class.
- `prefix_summary.csv` – Output: contraction type and stats for each prefix.
- `README.md` – This file.
- `LICENSE.txt` – MIT License.
- `citation.bib` – BibTeX citation for the paper.

---

## 📖 Citation

If you use this code or data, please cite:

```
@misc{sherratt2025collatz,
  author = {Sadie A. Sherratt},
  title = {From Infinite to Finite: A Proof of the Collatz Conjecture via Prefix Partition and Height Descent},
  year = {2025},
  note = {Preprint},
  url = {https://sherrattmath.org/collatz-paper}
}
```

---

## 📝 License

This project is licensed under the MIT License. See `LICENSE.txt` for full terms.

---

© 2025 Sadie A. Sherratt. All rights reserved.
