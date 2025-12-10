# ARCHITECTURE

## Árbol de carpetas (propuesto)
- src/          # código fuente
- tests/        # pruebas unitarias
- docs/         # documentación
- .github/      # instrucciones de Copilot
- requirements.txt
- pyproject.toml
- README.md

## Dependencias
- Python 3.12
- pandas, matplotlib
- pytest, black, ruff, mypy
- (Opcional) FastAPI para servicios web

## Scripts recomendados
- Formateo: `black .`
- Lint: `ruff check .`
- Tipado: `mypy src/`
- Pruebas: `pytest -q`
