# Big O Ladder

An interactive Big O study page. Every complexity class from O(1) to O(n!) drawn to scale, a searchable catalog of data structures, algorithms, Java calls and loop shapes with their notation, and the code patterns you need to recognize on a quiz.

**Use it here:** https://roketteere.github.io/big-o-ladder/

Built for CIS-055 Data Structures (SJCC). No account, no install, works on a phone, light and dark mode.

## How to use it

1. **Search.** Type what you are looking at: `hash map`, `dictionary`, `merge sort`, `ArrayList.get`, `nested loop`, `i /= 2`, `fib`. Pick a result to see the Big O for every operation (access, search, insert, delete, space, or best/average/worst) and a one-line reason. Press `/` to jump to the search box.
2. **The ladder.** Seven rungs, fastest to slowest: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!). Each shows the operation count at the current n. Click a rung to filter the catalog to that class; click again to clear.
3. **The chart.** Drag the n slider from 10 to 1,000,000, switch between a log and a linear y-axis, and hover anywhere to read every class at one n. O(2ⁿ) and O(n!) start switched off because they flatten the others; turn them on in the legend to watch them leave the chart. The table under the chart converts operations into wall time at 1 million, 1 billion or 1 trillion operations per second.
4. **The catalog.** Four tabs:
   - **Data structures** (21): array, ArrayList, linked lists, stack, queue, deque, hash map, hash set, BST, balanced trees, heap, trie, graphs, strings, and more, with access, search, insert, delete and space.
   - **Algorithms** (29): every sort from bubble to TimSort, linear and binary search, BFS, DFS, Dijkstra, Prim, Kruskal, fast power, naive Fibonacci, permutations, with best, average, worst and space.
   - **Java calls** (23): what `ArrayList.get`, `HashMap.put`, `String +=` in a loop, `Arrays.sort`, `PriorityQueue.poll` and friends actually cost.
   - **Code patterns** (12): single loop, nested loop, halving loop, recursion shapes, divide and conquer.
   A `*` means amortized or average case; the worst case is in the notes column.
5. **Read the code, name the class.** The cards at the bottom show each loop or recursion shape as code. Match the shape you see in a problem to a card and you have the class.

## Reading the notation

- Big O is the asymptotic **upper bound**: the worst case as n grows without limit.
- Constants and lower-order terms drop out: 50n is O(n), n² + n is O(n²), and a fixed 5-day delay is O(1).
- Ω (Omega) is the lower bound, Θ (Theta) is the tight bound. Interviews ask for Big O.
- Hash map and hash set figures assume a good hash function. Their worst case is O(n) when everything collides.

## Run it locally

It is one file with no build step and no server.

```
git clone https://github.com/roketteere/big-o-ladder.git
cd big-o-ladder
start index.html          # Windows; or just double-click it
```

Or serve the folder so the fonts load the same way they do online:

```
python -m http.server 8000
```

then open `http://localhost:8000/`. The only network request is Google Fonts; everything else is inline.

## Edit or extend it

`src/page.html` is the single source. `index.html` is generated from it:

```
python scripts/build.py
```

All the data is at the top of the `<script>` block in `src/page.html`:

| Array | What it holds | Row shape |
|---|---|---|
| `DS` | data structures | `[name, [aliases], access, search, insert, delete, space, note]` |
| `ALG` | algorithms | `[name, [aliases], best, average, worst, space, note]` |
| `JAVA` | Java calls | `[name, [aliases], time, note]` |
| `PAT` | code patterns | `[name, [aliases], class, code, why]` |

Write complexities the way they appear in the tables (`1`, `log n`, `n`, `n log n`, `n²`, `2ⁿ`, `n!`, `V + E`). Add a `*` for amortized or average. Aliases are what the search box matches, so add the other names people use (`dictionary`, `vector`, `min heap`). Rebuild, open `index.html`, commit.

## License

MIT. Use it, fork it, fix it.
