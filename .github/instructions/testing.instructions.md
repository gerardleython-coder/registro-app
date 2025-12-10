# Testing expert instructions (ISTQB-aligned)

## Alcance
- Archivos y conversaciones de `tests/`, `qa/`, PRs e issues de pruebas.

## Proceso
- Seguir el flujo ISTQB: planificación → monitoreo/control (transversal) → análisis → diseño → implementación → ejecución → finalización.
- Aplicar técnicas: partición de equivalencia, valores límite, decisión/estado cuando corresponda.

## Casos de prueba (formato)
- Incluir: identificador, requisito vinculado, precondiciones, pasos, datos, resultado esperado.
- Priorizar: críticos primero; cubrir negativos y límites.
- Reporte de defectos: título claro, pasos reproducibles, esperado vs obtenido, severidad/prioridad.

## Automatización
- Pytest para unitarias; si hay UI con tkinter, aislar lógica para pruebas.
- Para web/API (FastAPI), usar `httpx`/`pytest-asyncio` si aplica.

## Entregables
- Casos de prueba en Markdown (legibles).
- Scripts de prueba estables y mantenibles.
- Métricas básicas: pasados, fallados, bloqueados.
