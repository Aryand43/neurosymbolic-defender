# NeuroSymbolic Defender

## Overview

Framework for detecting and resolving contradictions in neuro-symbolic AI systems. Implements full-stack attack taxonomy and mathematically grounded defenses across neural, symbolic, tool, and memory layers.

## Motivation

Hybrid AI models are vulnerable across layers. This repo introduces a belief-aligned symbolic interface that tracks and verifies consistency in real time.

## Core Components

* `main.py`: Pipeline entry
* `symbolic_module.py`: Symbolic math and fact checking
* `neural_module.py`: LLM interaction
* `tool_module.py`: Tool response logic
* `belief_graph.py`: Belief graph tracking (WIP)

## Setup

```bash
git clone https://github.com/aryand43/neurosymbolic-defender.git
cd neurosymbolic-defender
pip install -r requirements.txt
```

Add `OPENAI_API_KEY` and `SERPAPI_API_KEY` to `.env`

## Run

```bash
python main.py
```

Test mode runs built-in queries like:

- `x**2 == x*x`
- `Are sharks mammals?`

Or run on a dataset:

```bash
python main.py --dataset gsm8k --num_examples 5
```

Replace `gsm8k` with `proofwriter`, `commonsense-qa`, etc. as needed.

## System Decomposition

* Neural Backbone
* Symbolic Engine
* Scheduler
* Tool Interfaces
* Memory/State

## Attack Taxonomy

* Symbolic scheduling exploits
* Symbol-grounding drift
* False logical injection
* Unsafe tool activation
* Cross-module contradiction

## Defense Stack

* Category-theoretic alignment
* Belief-state hypergraphs
* Lattice filters
* Info-theoretic bounds
* Differentiable rule auditing

## Interface Layer

* Graph of beliefs and explanations
* Tracks provenance and detects contradictions
* Resolves via overwrite, regeneration, or alert

## Evaluation

**Metrics**: task accuracy, contradiction rate, conflict detection F1, tool misuse rates, robustness under fuzzing, calibration, latency

**Datasets**: GSM8K, ProofWriter, CLUTRR, SCAN, MATH, adversarial tool-use sandboxes

## Key Insights

* Belief conflict detection outperforms entropy thresholds
* Scheduler thresholds affect contradiction rate
* Lattice filters + graphs = lower false positives
* [GPT-5 model card](https://cdn.openai.com/gpt-5-system-card.pdf) supports our BASIL framing by highlighting instruction adherence and multi-layered defenses.

## Limitations

* Overhead from runtime checks
* Tool trust and tuning burden
* Gaps for unseen attacks

## Future Work

* Adaptive belief graphs
* Hardware-level integration
* Expansion to multi-agent and embodied systems