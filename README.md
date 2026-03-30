# makelife-hard

Repository hardware FineFab (design electronique, exports, MCP hardware).

## Role
- Heberger les sources hardware (KiCad, regles, assets).
- Exposer les pipelines d'export et validation DRC/ERC.
- Consolider les serveurs MCP hardware.

## Stack
- KiCad
- Python
- MCP servers

## Structure cible
- `hardware/`: projets et blocs KiCad
- `spice/`: simulations
- `tools/`: exports et automatisation

## Demarrage rapide
```bash
# Exemple (selon outillage local)
python -m pip install -r requirements.txt 2>/dev/null || true
```

## Roadmap immediate
- Mettre en place BaseMCPServer commune.
- Uniformiser exports KiBot/DRC/ERC.
- Publier evidence packs hardware.
