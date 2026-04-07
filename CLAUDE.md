# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

makelife-hard is the KiCad design blocks library for FineFab. Contains reusable design blocks across 8 categories, project templates, and custom KiCad symbols.

## EDA MCP Pipeline

Complete schéma-to-JLCPCB pipeline available via MCP tools:

| Step | MCP Server | Use |
|------|-----------|-----|
| Sourcing | `jlcmcp-remote` | Quick stock/pricing lookup (1.5M+ parts, zero config) |
| Sourcing | `jlcpcb-search` | Offline SQLite search (450k+ parts, datasheets, price tiers) |
| Schematic | `kicad-sch` | Symbol placement, wires, ERC |
| PCB Layout | `kicad-pcb`, `kicad-design` | Placement, design rules, manual routing |
| Autoroute | `kicad-design` | Freerouting Docker, DRC post-route |
| Review | kicad-happy skills | DFM, EMC 42 rules, thermal, tolerance |
| Export | `kicad-design` | Gerbers, BOM with LCSC IDs, CPL with rotations, STEP 3D |
| Fabrication | `kicad-fab` | Async autoroute, organized output dirs |

## Key Commands

```bash
# Validate a design block
kicad-cli sch erc blocks/<block>/schematic.kicad_sch
kicad-cli pcb drc blocks/<block>/board.kicad_pcb

# JLCPCB quick search (via jlcmcp-remote MCP)
# "Cherche des capas 100nF 0402 basic avec 1000+ en stock"
```

## JLCPCB Part Selection Strategy

- **Basic parts** (`library_type="no_fee"`): zero assembly fee — prefer these
- **Preferred parts**: small fee — acceptable for specialized components
- **Extended parts**: +$3/unique part — avoid unless no alternative
- kicad-happy `jlcpcb` skill handles rotation offset table automatically
