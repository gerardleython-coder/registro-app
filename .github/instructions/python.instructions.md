# Python expert instructions

## Alcance
- Archivos: `src/**/*.py`, `tests/**/*.py`
- Objetivo: código Python idiomático, seguro, probado y documentado.

## Estándares
- Versión: Python 3.12.
- Estilo: PEP 8, formateo con Black, lint con Ruff.
- Tipado: anotaciones completas y chequeos con mypy.
- Docstrings: formato Google; incluir ejemplos de uso cuando ayuden.

## Diseño y calidad
- Funciones pequeñas y composables; evitar duplicación.
- Manejo de errores con excepciones específicas; sin pass silencioso.
- Separación de responsabilidades: lógica de negocio, acceso a datos, UI.

## Pruebas
- Framework: pytest; organizar en `tests/`.
- Reglas: incluir casos de éxito y de error; usar fixtures cuando aplique.
- Cobertura objetivo: ≥ 80% (ajustable en el repo).

## Entregables esperados
- Código con tipos y docstrings.
- Archivo de pruebas correspondiente.
- Ejemplo mínimo de uso (doctest o comentario).
