# makelife-hard

Hardware design files, PCB exports, and MCP automation servers for electronic manufacturing.

Part of the [FineFab](https://github.com/L-electron-Rare) platform (FineFab).

## What it does

- Hosts KiCad schematics, PCB layouts, and reusable design blocks
- Runs automated DRC/ERC validation and KiBot export pipelines
- Exposes MCP servers for AI-assisted hardware design workflows
- Generates manufacturing evidence packs (Gerber, BOM, pick-and-place)

## Tech stack

KiCad | Python | KiBot | MCP Protocol

## Quick start

```bash
pip install -r requirements.txt
python -m tools.export --project hardware/my_board
```

## Project structure

```
hardware/     KiCad projects and design blocks
library/      Shared symbol library (makelife.kicad_sym) and 3D shapes
blocks/       Reusable design blocks by category (power, mcu, sensing, ...)
templates/    Complete board templates (bmu-complete, led-controller, audio-processor)
spice/        SPICE simulations
tools/        Export automation and MCP servers
docs/         Catalog, design rules, and source traceability
```

## Design blocks library

22 reusable KiCad design blocks across 8 categories, extracted from 15 production projects.
See [docs/catalog.md](docs/catalog.md) for the full inventory and [docs/design-rules.md](docs/design-rules.md) for layout guidelines.

## Related repos

| Repo | Role |
|------|------|
| [makelife-firmware](https://github.com/L-electron-Rare/makelife-firmware) | Firmware for the boards designed here |
| [makelife-cad](https://github.com/L-electron-Rare/makelife-cad) | CAD/EDA web platform |
| [KIKI-models-tuning](https://github.com/L-electron-Rare/KIKI-models-tuning) | Model fine-tuning pipeline |
| [finefab-life](https://github.com/L-electron-Rare/finefab-life) | Integration runtime and ops |

## License

MIT
