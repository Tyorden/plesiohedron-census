# Schmitt `plesiohedron` repo & data recovery report

**Date of all fetches: 2026-08-28** (US Pacific). Scout session, read-only web recovery; downloads authorized.
**Target:** code + data behind M. W. Schmitt, *On Space Groups and Dirichlet-Voronoi Stereohedra*, FU Berlin 2016 (doi:10.17169/refubium-14374). Dissertation states software/data at `github.com/moritzschmitt/plesiohedron` (GitHub 404, confirmed 2026-08-28).

Each claim below is tagged **VERIFIED** (fetched and read on 2026-08-28) or **INFERRED**.

---

## Headline result

**The complete repository was recovered — full source tree AND full git history — from Software Heritage.** The repo turns out to contain the *software suite and per-space-group input data*, but **not** the survey *results* (the 3,315 combinatorial types / ~14 TB output summary). No online copy of the results data was found anywhere. Details below.

Recovered material lives in:
`<repo>/references/schmitt_repo_recovery/`

| Item | Path |
|---|---|
| Extracted working tree (495 files, 22 MB) | `references/schmitt_repo_recovery/plesiohedron_worktree/` |
| Full git history, bare repo (3 commits) | `references/schmitt_repo_recovery/plesiohedron.git/` |
| Clone of the bare repo (sanity check, clean) | `references/schmitt_repo_recovery/plesiohedron_clone/` |
| Original SWH vault tarball (flat) | `references/schmitt_repo_recovery/plesiohedron_swh_flat.tar.gz` (4,372,876 bytes) |
| Original SWH vault tarball (git-bare) | `references/schmitt_repo_recovery/plesiohedron_swh_git-bare.tar.gz` (2,775,040 bytes) |
| Top-level files fetched individually via content API | `references/schmitt_repo_recovery/master/` |

---

## 1. Software Heritage recovery (the successful channel) — VERIFIED

Software Heritage archived the repo as a git origin with **11 crawler visits, 2016-06-05 → 2019-07-19, all status "full"**.

- Origin API: `https://archive.softwareheritage.org/api/1/origin/https://github.com/moritzschmitt/plesiohedron/get/` → 200, origin exists (SWHID `swh:1:ori:d6436254135c3042ec07672661aab23acd5720d5`). **VERIFIED**
- Visits API: `https://archive.softwareheritage.org/api/1/origin/https://github.com/moritzschmitt/plesiohedron/visits/`. **VERIFIED.** Visit list:
  - visit 2, 2016-06-05: snapshot `a3e2edaa11a82660df9d5f314858e5cad1b6a106` (pre-merge state; contained in the recovered history as parent commits)
  - visits 3–11, 2016-08-09 / 2016-09-01 / 2017-09-23 / 2017-10-20 / 2017-11-10 / 2017-12-04 / 2019-01-01 / 2019-05-12 / 2019-07-19: **all the identical snapshot** `8978d77b0000297a95f6a42926a3fa48c59f973b`
  - ⇒ The repo never changed after June 2016 and was deleted from GitHub sometime **after 2019-07-19**. **VERIFIED** (visit record) / deletion window end-point **INFERRED** from GitHub 404 today.
- Snapshot API: `https://archive.softwareheritage.org/api/1/snapshot/8978d77b0000297a95f6a42926a3fa48c59f973b/` → single branch `refs/heads/master` = HEAD = revision `97cb86b649d5bf9df82f9e9895150f2dfbb93616`. **VERIFIED**
- HEAD revision: author/committer Moritz Schmitt `<[e-mail withheld]>`, date 2016-06-21T22:43:05+02:00, message "Merge branch 'master' of https://github.com/moritzschmitt/plesiohedron", root directory `d812ef736b08ffd6072dfd59725f1ba5ff4194ec`. Full history is exactly **3 commits**: `97cb86b` (merge, 2016-06-21) ← `c6bd203` ("Initial commit", 2016-06-21) + `514e278` ("initialization", 2016-01-27). **VERIFIED** (revision + log API, and `git log` on the recovered clone)
- Vault cooking (both anonymous POSTs, cooked to "done" within ~10 min, then downloaded):
  - flat: `https://archive.softwareheritage.org/api/1/vault/flat/swh:1:dir:d812ef736b08ffd6072dfd59725f1ba5ff4194ec/raw/` (cook id 421687420)
  - git-bare: `https://archive.softwareheritage.org/api/1/vault/git-bare/swh:1:rev:97cb86b649d5bf9df82f9e9895150f2dfbb93616/raw/` (cook id 421687421)
  - The bare repo clones cleanly and reproduces the full 3-commit DAG. **VERIFIED**

### Recovered repo contents — VERIFIED (complete top-level inventory)

```
Makefile            52,273 B   build rules
README.md               15 B   literally just "# plesiohedron" — no documentation, no data links
plesiohedron.cpp     4,295 B   main program (polymake-based DV-cell computation)
plesiohedron.h       9,236 B   SpaceGroup class; declares init_2d_reps_1..17, init_3d_reps_1..230
spacegrp.cpp        96,898 B   SpaceGroup implementation
data/2d/            32 files   space_group_2d_{2..17}.cpp + .o  (group 1 absent)
data/3d/           458 files   space_group_3d_{2..230}.cpp + .o (group 1 absent)
```

Total 495 files, 22 MB extracted. The `data/` directory is **generated C++ source (isometry representations of each space group as rational 4×4 matrices) plus compiled object files** — i.e., program *input* data, not survey output. Group 1 (trivial group) has no data file in either dimension, though the header declares its init function — presumably handled trivially or unneeded. That last clause is **INFERRED**; the file absence itself is **VERIFIED**.

### What the program does (from reading `plesiohedron.cpp`) — VERIFIED

Usage: `plesiohedron <dimension> <space group number> <input containing basis and points>`. For each seed point it computes the Dirichlet–Voronoi cell via polymake's beneath-beyond algorithm over `QuadraticExtension<Rational>` and **prints only the f-vector summary to stdout**: `x y z = (V, V+F-2, F)`. There is **no code in the repo that stores polytopes, classifies combinatorial types, or writes result files.** The 3,315-type classification and the ~14 TB raw output were produced by infrastructure/scripts *not present in this repo*. **VERIFIED** (absence of such code in the complete recovered tree).

---

## 2. Wayback Machine (task 1 & 2) — BLOCKED at network level, and now redundant

- Availability API (host `archive.org` — reachable): `https://archive.org/wayback/available?url=github.com/moritzschmitt/plesiohedron` → `{"status":"200","available":true,"timestamp":"20180611151517"}`. **VERIFIED**: a snapshot `http://web.archive.org/web/20180611151517/https://github.com/moritzschmitt/plesiohedron` exists.
- CDX enumeration `http://web.archive.org/cdx/search/cdx?url=github.com/moritzschmitt/plesiohedron*` (+ https, prefix-match, JSON, browser-UA variants, 3+ retries each, timeouts up to 180 s): **all failed.** Root cause diagnosed with `curl -v`: **TCP connect to web.archive.org (207.241.237.3) times out on both :443 and :80 from this network** (curl exit 28, "Failed to connect... after 75024 ms"). `archive.org` itself (different host) responds fine. WebFetch also refused: "Claude Code is unable to fetch from web.archive.org". So the CDX list and snapshot page could not be retrieved this session — a **network/tool reachability failure, not evidence of absence**. **VERIFIED** (the failures).
- Raw-file recovery via `web.archive.org/web/<ts>/https://raw.githubusercontent.com/...`: not attempted further — same unreachable host, and **moot**: the Wayback snapshot (2018-06-11) falls inside the SWH-verified frozen window (identical snapshot 2016-08 → 2019-07), so the Wayback capture can only show the exact content already fully recovered from Software Heritage. **INFERRED** (the moot-ness), from VERIFIED visit data.

## 3. Alternative homes sweep — all checked, no results data anywhere

| Channel | Exact query/URL | Outcome |
|---|---|---|
| **Refubium landing page** | `https://refubium.fu-berlin.de/handle/fub188/10176` via WebFetch | Blocked by **Anubis v1.27.0** anti-bot wall ("Access Denied", code 9e4edb5b6b850c41). **VERIFIED** |
| **Refubium OAI-PMH (bypassed Anubis)** | `https://refubium.fu-berlin.de/oai/request?verb=GetRecord&metadataPrefix=xoai&identifier=oai:refubium.fu-berlin.de:fub188/10176` | **Complete bitstream inventory obtained.** The record holds exactly 6 files: `dissertation_moritz_schmitt.pdf` (bitstream /1/), `FUDISS_thesis_000000103570.xml` (/2/), `FUDISS_derivate_000000020464.xml` (/3/), `license.txt` (/4/), `dissertation_moritz_schmitt.pdf.txt` (/5/), `dissertation_moritz_schmitt.pdf.jpg` (/6/). **No supplementary dataset is attached to the thesis record.** **VERIFIED** |
| **DataCite** | `https://api.datacite.org/dois/10.17169/refubium-14374` | Record fetched. `relatedIdentifiers: []`, `relatedItems: []` — **no linked dataset DOI**. Only identifier: URN `urn:nbn:de:kobv:188-fudissthesis000000103570-3`. **VERIFIED** |
| **Zenodo** | `https://zenodo.org/api/records?q=plesiohedron` and `?q=stereohedra` | 1 hit each, both unrelated (2026 "Josehedron" record 19471917; "Foam Cell" record 19662068). **Nothing by Schmitt.** **VERIFIED** |
| **figshare** | `POST https://api.figshare.com/v2/articles/search` for "plesiohedron", "stereohedra" | Both return `[]`. **VERIFIED** |
| **GitHub repo search** | `api.github.com/search/repositories?q=plesiohedron` (also `q=stereohedra`, and authenticated `gh api search/repositories?q=plesiohedron+fork:true`) | Only hit: `makemeunsee/Plesiohedrony` (unrelated Scala tessellation demo). Zero forks/copies of Schmitt's repo. **VERIFIED** |
| **GitHub code search** | authenticated `gh api search/code?q=plesiohedron` | 1 hit: `standardgalactic/library` `idea-map.txt` (a word list; irrelevant). **VERIFIED** |
| **polymake** | `https://polymake.org/doku.php/extensions` via WebFetch; web search "polymake plesiohedron stereohedra Schmitt" | No plesiohedron/stereohedron/space-group extension listed; polymake never bundled or mirrored it (the tool *links against* polymake as a library — see includes in `plesiohedron.h`). **VERIFIED** (extensions page + code) |
| **Memento TimeTravel** | `http://timetravel.mementoweb.org/timemap/link/https://github.com/moritzschmitt/plesiohedron` | Returned empty body (HTTP exit 0, no mementos listed). Inconclusive/no additional archives surfaced. **VERIFIED** (the empty response) |
| **archive.today** | `https://archive.ph/newest/https://github.com/moritzschmitt/plesiohedron` via WebFetch | Tool refused ("unable to fetch from archive.ph"); not checked. **VERIFIED** (the failure) |
| **General web search** | WebSearch: `Schmitt "plesiohedron" software ... data github`; `"3315" OR "3,315" combinatorial types stereohedra ... data` | No external data host surfaced; all hits point back to the dissertation PDF (Refubium bitstream), Semantic Scholar, MathWorld/wiki pages. **VERIFIED** |
| **GitHub live** | `github.com/moritzschmitt/plesiohedron` | 404 (confirmed by parent session 2026-08-28; consistent with everything above). **VERIFIED** (by parent; relied on here) |

---

## 4. Final assessment

**Recovered (bit-for-bit, with cryptographic SWHIDs):** the entire `plesiohedron` software suite exactly as it stood from 2016-06-21 until deletion — source, Makefile, and machine-generated isometry data for 2D groups 2–17 and 3D groups 2–230, plus the full (3-commit) git history. Permanent citable identifiers:

- Directory: `swh:1:dir:d812ef736b08ffd6072dfd59725f1ba5ff4194ec`
- Revision: `swh:1:rev:97cb86b649d5bf9df82f9e9895150f2dfbb93616`
- Snapshot: `swh:1:snp:8978d77b0000297a95f6a42926a3fa48c59f973b`
- Origin: `https://github.com/moritzschmitt/plesiohedron` (browse: `https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/moritzschmitt/plesiohedron`)

**Definitively gone from the repo channel:** the survey *results* — the per-group/per-point f-vector outputs, the ~14 TB raw data, and any table of the 3,315 combinatorial types — were **never in the GitHub repo** (verified against the complete recovered tree, which is identical across every crawl 2016-08 → 2019-07, spanning the 2018 Wayback capture). The repo's README is a single line with no pointers.

**Is type-level data recoverable without contacting the author?** **No — not from any online channel checked.** The thesis record (Refubium) carries no supplementary files; DataCite links no dataset; Zenodo, figshare, GitHub (incl. forks/code search), and polymake have nothing. The only type-level information available without the author is (a) whatever tables/summaries are printed **inside the dissertation PDF itself** (`https://refubium.fu-berlin.de/bitstream/handle/fub188/10176/dissertation_moritz_schmitt.pdf?sequence=1&isAllowed=y`, archived locally at `references/Schmitt_2016_dissertation.pdf`), and (b) **regeneration**: the recovered suite is complete and, given a polymake build environment and seed-point grids, can in principle recompute the survey. Full reproduction of the classification would additionally require the grid-generation and type-classification tooling, which is not in the repo — contacting M. Schmitt (`[e-mail withheld]`, from git committer identity and the OAI record) remains the only route to the original result files. (No outreach performed, per session rules.)

**Loose ends / re-checkable failures:** Wayback CDX + snapshot pages (web.archive.org TCP-unreachable from this network today — retry from another network; expected to be redundant) and archive.today (fetcher-blocked).
