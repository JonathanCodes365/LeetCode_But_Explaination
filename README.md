# LeetCode Postmortems

Most LeetCode repos are solution dumps. This one isn't.

Here I solve a problem, then interrogate the solution — even when it's accepted. Getting the green checkmark tells you the code works on the given test cases. It doesn't tell you *why* your first instinct was wrong, *where* the time went before you found the right approach, or whether the "correct" solution is actually the *right* solution (optimal complexity, clean edge-case handling, idiomatic) or just one that happened to pass.

The goal isn't a bigger streak. It's building the kind of pattern-recognition and judgment that doesn't show up in an acceptance rate.

## Why this exists

Solving a problem and understanding a problem are different skills. It's easy to accept a working solution and move on without asking:
- Was my initial approach wrong, or just unoptimized?
- Did I get lucky with the constraints, or does this actually scale?
- What was I missing conceptually that made me reach for the wrong data structure/pattern first?
- If this "works," what's the actual best-known approach, and how far off was I?

This repo is the record of answering those questions, every time, even when — *especially* when — the solution was accepted on the first try.

## Structure

```
leetcode-postmortems/
├── README.md
├── 0001-two-sum/
│   ├── solution.py
│   └── notes.md
├── 0053-maximum-subarray/
│   ├── solution.py
│   └── notes.md
└── ...
```

Each problem gets its own folder: `NNNN-problem-slug/`. The code lives in `solution.py` (or the relevant language file); the actual value is in `notes.md`.

## The `notes.md` format

Every problem's notes follow the same structure, so the repo stays scannable:

```markdown
# [Problem Number]. Problem Name

**Difficulty:** Easy / Medium / Hard
**Tags:** Array, Two Pointers, Dynamic Programming, ...
**Status:** ✅ Accepted / 🔁 Revisited

## My First Approach
What I tried first, and the reasoning behind it — including the wrong reasoning.

## What Went Wrong
Where the first approach broke: TLE, wrong output, wrong edge case, wrong assumption
about the input. If it didn't go wrong, say so — and say why it worked.

## The Fix / Final Approach
What changed, and *why* this approach is the right mental model for this
problem, not just a passing one.

## Why "Accepted" ≠ "Correct"
Even if the final solution passed: what's the actual time/space complexity?
Is there a better-known approach? What edge cases does this solution
technically handle but not *robustly*? What would break this in production
that LeetCode's test cases never would?

## Pattern / Takeaway
The one-line lesson to carry into the next problem — the pattern, not the
problem.

## Complexity
- Time: O(...)
- Space: O(...)
```

## Progress

| # | Problem | Difficulty | First Attempt | Key Lesson |
|---|---------|-----------|----------------|------------|
| 1 | Two Sum | Easy | Brute force → Hash map | Trading space for time when lookups dominate |

*(Table updates as problems are added — [LeetSync](https://github.com/) keeps the solution files current; this table and the notes are added by hand since that's where the actual thinking happens.)*

## Why bother with this, given everything else

This repo isn't about interview prep in isolation — it's practice in refusing to accept "it works" as the finish line. That habit is the same one I'm trying to build everywhere else: in DSA, in the math underneath ML, in code I write for real projects. A model that returns a plausible-looking output isn't the same as a model that's *right*, and I'd rather build the instinct to ask the second question now, on problems small enough to fully understand, than later on problems too large to.

---

*Companion to my [main portfolio repo] — this one's for the thinking, that one's for the shipping.*
