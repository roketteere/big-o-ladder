# CODEX — big-o-ladder

| abbr | meaning |
|---|---|
| CLS | the seven complexity classes, ladder order (fastest → slowest) |
| IDX | class id → index in CLS |
| DS / ALG / JAVA / PAT | catalog rows: data structures / algorithms / Java calls / code patterns |
| ENTRIES | flattened search index built from the four catalogs plus CLS |
| clsOf | complexity string → class id (`"n log n"` → `nlogn`) |
| lg / lgfact | log10 of a value / log10(n!) computed as a sum, to avoid overflow |
| fmtLg | format a log10 value as a number (`664`, `2.35e78`) |
| timeStr | log10(ops) + ops/sec → human wall time |
| FEEL | one-line "what it feels like" per class |
| on | legend toggle state per series |
| filter | currently selected class id for the catalog, or null |
| nMax | slider value (max n on the chart); slider is log10 scaled |
| logY | chart y-axis is log10 (true) or linear |
| rung | one ladder card |
| chip | the colored `O(…)` pill |
| `*` in a table cell | amortized or average case |
| M / W / H | chart margins / viewBox width / height |
| xs / ys | x and y scale functions for the chart |
| xhair | crosshair line |
