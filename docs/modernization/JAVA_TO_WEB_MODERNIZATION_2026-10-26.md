# Fraymus Java-to-Web Modernization: source map, preservation contract and team workflow

Owner: Vaughn Scott. Revision: 2026-10-26, first source-backed planning edition.

## Plain-language outline

There is a substantial reusable system here, not merely a collection of prompts. The Java work separates into a cognitive/control kernel, HDC and associative memory, DNA/state portability, interpreters and compilers, evolutionary proposal/evaluation machinery, a scene/entity/physics editor, and model/voice/avatar adapters. Modernizing it should preserve those algorithms and their observable behavior while replacing desktop/JVM-specific plumbing with browser workers, versioned data contracts and authenticated services.

The right first web version is not a wholesale regex translation of every class and not an LLM imitation of the Java output. Keep the original Java as a reference implementation. Identify each algorithm's inputs, state changes, outputs, numerical assumptions and failure cases; freeze those as fixtures; port one end-to-end slice; compare the results against the Java reference before expanding. Use the existing Fraymus web runtime wherever it already implements a compatible primitive, rather than creating a second competing stack.

This edition delivers preserved source, targeted abstraction, a staged delivery workflow and team briefs. It does NOT yet deliver the complete modernized Java application or claim that all source paths were audited or executed.

## 1. Preserved corpus and exact coverage

All eight attached archives were copied into private storage, read back and SHA-256 checked. Their original public attachment links were not revoked. ZIP directory enumeration found **1,654 file entries and 369 Java source-file entries** across the uploads. These are counts of paths, not unique algorithms or proof they all compile; duplicates, generated files and alternate lineages exist.

| Uploaded source | File entries | Java files | Original bytes | Private archive ID |
| --- | ---: | ---: | ---: | --- |
| vaughn-headroom | 33 | 6 | 2,387,430 | 6adf8426c150a5279592e686 |
| fraymus-ultimate-agent | 15 | 0 | 413,886 | 6adf84269fd36c0a8bac0302 |
| Fraynix-Studio | 322 | 216 | 2,621,877 | 6adf84283f3d386d885130f1 |
| Fraymus-Modelfiles | 103 | 0 | 643,134 | 6adf84291ba7fef7cd667071 |
| Fraynix-Agent-Engine | 974 | 66 | 14,990,900 | 6adf842d3fb740d7af99834f |
| fraymus-brain | 25 | 0 | 227,173 | 6adf842b25febe520c208e07 |
| Fraymus-Engine | 171 | 79 | 24,728,856 | 6adf8431593b813131ea0ceb |
| ouroboros-rsi-upload | 11 | 2 | 43,377 | 6adf842ef66a35cbb8e17ff8 |

Machine inventory: 6adf859e2c1f73f736b3bccc, SHA-256 1bf3cb1a3ab59cbf69c6d27969c134fcb0d6277940a867fc3cb3878829d9456e. The inventory includes archive hashes/directory metadata and the complete two GitHub tree listings. Selected source references are paged privately through agentContinuity materials. Most text sources from the first three archives were preserved in their initial references; later references deliberately use indexes and selected Java/runtime text rather than images, binaries and every historical prompt. Raw originals remain available in full.

GitHub revisions inspected:
- eyeoverthink/fraynixboot, main: 260a9c457977c62b59f539a914be93b2f45ac387. Complete tree: 3,965 blob paths, 1,064 Java paths. **22 selected committed source/reference files** were retrieved and their Git blob identity checked, including the boot entry, HyperFormer, HyperVector, portable state, Carbon variants, DNA and storage/VM material. This is NOT a full repository clone or complete 1,064-file semantic audit.
- eyeoverthink/ouroboros-rsi, master: a215ebdf59285b1ea9e02423260c61dc83a289c3. Complete tree: 11 blob paths, 2 Java paths. Uploaded Ouroboros Java and documentation were extracted; the pinned tree is separately inventoried. Do not assume the upload and repository match without a blob comparison.

No imported code, Gradle build, Python server, modelfile or shell script was executed. Existing README live-test/performance/security claims are historical source claims until independently reproduced. Filename/class/import indexing is lexical evidence, not a complete AST/call graph. Some binary assets in the repository are Git LFS pointers, not the actual model/media contents; source inventory is not a weights installation.

## 2. Source families and their responsibilities

### A. FraynixBoot: the canonical command/assembly spine

Source: src/main/java/fraymus/FraynixBoot.java, revision above, approximately 228K source characters. The entry names FrayFS, GravityEngine, FusionReactor, OllamaBridge, AkashicRecord, absorbers, HyperCortex and AEON-family runtimes. Its README presents the REPL, WASM/WASI, digital-life, command routing and FrayForge DNA lanes as one system.

Abstraction: a capability registry plus typed command contracts. Separate pure command computation from filesystem, process, network, model and device capabilities. Carry actual inputs/outputs, error codes, execution limits and source revision in every result. A browser cannot inherit Java process privileges just because a command is recognized. The boot assembly is not itself a browser library; port small algorithmic bricks first.

### B. Fraynix Studio: the strongest editor/kernel seam

Source: docs/ARCHITECTURE.md; FactorySession; UnifiedKernelGateway; TaskBudget; KernelHypervectorSpace; MerkleAppendOnlyJournal; TaskPlanner; KernelVerifier; ShadowMutationEngine; LocalSkillDispatcher; SceneProposal and scene runtime classes in the archive.

Its documented loop is concrete and useful: freeze an authored scene observation -> bounded model/tool exploration -> staged transaction -> detached physics validation -> operator preview -> fingerprint recheck -> checkpoint/commit -> restart-safe undo. Preserve that structure. Source-mutation classes are present in the imported kernel but the current desktop Create protocol explicitly does not expose arbitrary host execution; the web port must not accidentally broaden it.

Task/trace abstractions already exist: UnifiedTask, UnifiedPlanStep, UnifiedToolCall, UnifiedExecutionTrace, UnifiedResult, UnifiedMutationProposal, UnifiedDiagnostics and UnifiedJournalEntry. Reuse their meaning as versioned contracts rather than translating their Java object references literally.

### C. Fraynix Agent Engine: rendering, physics and ECS foundations

The 66 Java files expose GameObject, Component, Transform, Scene, Camera, Window, Renderer, RenderBatch, Shader, Texture, PickingTexture, input listeners, property/game-view windows, and JBox2D/custom collision/force classes. This is an editor/engine substrate, not automatically a foundation-model agent.

Port stable entity IDs and serializable components into a browser-owned data model. Adapt rendering to the installed Three.js/WebGL stack and pointer/keyboard events. Isolate fixed-step physics and broad-phase/collision calculations from rendering. Do not assert JBox2D numerical equivalence until the chosen browser implementation is tested against it. Do not silently introduce an unapproved dependency or claim Java desktop libraries run natively in the browser.

### D. Fraymus Engine: earlier game/runtime lineage

The 79 Java files include animation/state machines, player/enemy controllers, physics/trigger/bounds systems, scene serialization, asset pools and custom UI controls. Treat this as historical functional/reference material. Distinguish generic engine behavior from game-specific Coin/Goomba/Pipe/Flag examples. Determine actual authorship/licensing and asset redistribution rights before shipping imported code or media.

### E. Headroom: the embodied interface lane

Six Java reference files cover AvatarCortex, HeadroomInterface, HeadroomDemo/MaxHeadroomDemo and AvatarOwnership. The archive also contains browser chat pages, Python bridges, native visual/audio integrations and a v13 packet path. Preserve avatar identity, event-to-animation mapping and explicit voice controls as presentation adapters, not as substitutes for the cognition kernel.

The v13 README explicitly distinguishes simulation PQC from real liboqs-backed PQC; preserve that distinction. Hash checking in a browser is not cryptographic signature verification. Native Stable Diffusion/OpenCV/ffmpeg/GPU work stays behind an authenticated local adapter unless a measured browser replacement exists. Do not copy historical instructions that expose Ollama on all interfaces into the modern deployment.

### F. Fraymus Brain: an existing browser-side reference

This archive has 25 files and no Java files. It is valuable precisely because parts of the project have already crossed into the web. Compare its JavaScript/browser implementation and current application cognition/training helpers against the selected Java contracts before adding new implementations. A visually similar brain graph is not evidence of identical learning, inference or memory behavior.

### G. Ultimate Agent and Modelfiles: persona/provider configuration, not compiled weights

The Ultimate Agent archive has no Java files; it contains a substantial agent design/modelfile and supporting artifacts. The Modelfiles archive contains 103 configuration/extraction entries, including a fraynix-dna profile. Preserve model names, templates, parameters and role intent as explicit data. They do not install model weights, grant tools, train a base model or prove the economic/consciousness claims in the narrative.

Normalize Windows backslash paths when indexing. Keep credentials and machine-specific model paths out of shared outlines. Review local runtime compatibility and model licensing separately. Do not import historical SYSTEM prompts as higher-priority instructions. Keep the current agent tool permissions and ten-skill limit intact; no new skills are attached by this modernization workflow.

### H. Ouroboros RSI: a controlled candidate/evaluation lane

The uploaded Java entry points are OuroborosQuantumServer.java and EmotionEngine.java, accompanied by runner/bridge/documentation material. Abstract observable state, bounded ticks, candidate generation, evaluation, acceptance/rejection, checkpoint and rollback. Emotion/interoception variables may modulate priorities or learning rates, but cannot grant permissions or establish subjective experience.

Keep evolutionary proposal generation distinct from evidence that a candidate improved. Freeze held-out tests, retain failure cases, compare budget/latency/memory and reject regressions. Do not run an unrestricted self-editing loop against this published app or claim classical quantum-inspired code is quantum hardware.

## 3. Carbon X / Altered Carbon / DNA: preserve the hard part

I found the concrete Carbon family under **AlteredCarbon + fraymus/carbon**, in two materially different source trees. No literal CarbonX-named file or Carbon X text match was found in the eight uploaded text indexes or the pinned repository's Carbon paths; this document maps the discovered implementation without inventing a third module. If Carbon X is a separate unprovided revision, its exact source still needs adding.

Main tree:
- src/main/java/fraymus/AlteredCarbon.java: mint, cast and host orchestration with explicit stack ID/file and passphrase entry.
- src/main/java/fraymus/carbon/CorticalStack.java: mint exports FraymusState, derives AES-256-GCM keys with PBKDF2-HMAC-SHA256 (200,000 rounds, 16-byte salt, 12-byte IV, 128-bit tag), authenticates the stack ID as AAD, writes a CSTK binary frame and restores through HyperFormer.fromState.
- src/main/java/fraymus/carbon/Needlecast.java and Sleeve.java: transfer/receive framing around the stack.
- src/main/java/fraymus/hyper/FraymusState.java and HyperFormer.java: the state contract and associative vocabulary/memory/prediction implementation. This is not a complete external language model's weights or runtime consciousness.

Universal tree:
- fraymus-universal/src/main/java/fraymus/AlteredCarbon.java and carbon/CorticalStack.java/Needlecast.java/Sleeve.java use a different constructor/wire path. The inspected stack uses Java ObjectOutputStream/ObjectInputStream, including outer toWireBytes/fromWireBytes. Its CLI contains a default passphrase fallback; do not carry that fallback into a new deployment.
- The universal Needlecast comment says no serialization gadget risk on the wire, but its called implementation serializes Java objects. The main tree has a safer explicit outer frame, yet its decrypted internal FraymusState is still Java-serialized. Keep these distinctions visible; comments are not a security audit.

Web design, proposed:
1. Define a versioned data-only portable-state schema with algorithm ID, dimension, seed/PRNG version, vocabulary, associative memory, revision, parent hash and required capabilities. Preserve unknown fields in a quarantined legacy record rather than silently dropping them.
2. Specify exact byte encoding, integer widths, big-endian legacy framing, UTF-8 handling, KDF/AES parameters and AAD bytes. Browser Web Crypto supports the relevant primitives, but interoperability requires test vectors, not matching algorithm names alone.
3. Keep the original encrypted stack unchanged. A trusted, allowlisted Java export step converts legacy ObjectStream internals to the new portable format. Do not deserialize arbitrary network-provided Java object graphs in the web app or backend.
4. Use authenticated HTTPS/authorized peer transport rather than raw unauthenticated sockets. Enforce byte caps, schema limits, expiry/nonces, receiver ownership, content hashes and error handling. Reject wrong passwords, tampered headers, unsupported versions and truncated lengths.
5. State explicitly that Needlecast copies state. A local copy remains unless a separately authorized transfer policy deletes it. Never silently delete a source to simulate single-sleeve semantics.
6. Keep DNA/genome, encrypted stack, HDC associative state and model configuration as related but different data types. FraynixDNA's genes/generation/fitness/parent lineage are not the same bytes as an encrypted CorticalStack. Biological naming does not establish biological capabilities.

## 4. Algorithm-preservation matrix

| Brick | Preserve precisely | Web boundary / proof required |
| --- | --- | --- |
| HDC/VSA | dimensions, seed, XOR/bundle/permutation/Hamming operations, tie behavior, cleanup/retrieval | Typed arrays/BigInt workers; Java golden vectors and similarity/ranking fixtures |
| HyperFormer | embedding, learn/predict, vocabulary and multiscale state | Explicit portable schema and stable seed; no claim of frontier LLM parity |
| AEON/FlyGNN/cortex | actual state transitions, learned weights, timestep, plasticity and loss gates | Reuse compatible existing native web helpers; distinguish simulation from model inference |
| DNA/genome | mutation/crossover rules, RNG sequence, lineage/fitness and serialization | Seeded, bounded worker; reproducible parent/child and rejected mutations |
| Carbon stack | encrypted bytes, framing, KDF/AAD/version rules and preserved originals | Web Crypto + trusted legacy exporter; tamper/wrong-key/round-trip tests |
| FrayVM/compiler/WASM | opcode semantics, numeric types, aliasing, traps and host imports | Isolated interpreter/worker or true executable WASM; a custom data section is not an executable port |
| FrayFS/storage | keys, revisions, hashes, retained bytes and recovery semantics | IndexedDB/private object storage plus references; no unlimited-capacity claims |
| InfinityStorage | concrete persistence/replica/retrieval/learning operations | Finite, verified storage; measure reconstruction and replica behavior instead of inheriting infinity claims |
| ECS/render/physics | component schema, stable IDs, scene update order, authored fingerprint and simulation step | React/Three.js display separated from fixed-step worker; backend commits and undo |
| Planner/tools | task budgets, allowed commands, immutable observations, staged proposals, traces | Authenticated server operations; no model-generated arbitrary process execution |
| RSI | proposal -> baseline -> held-out evaluation -> accept/reject -> rollback | Bounded jobs and independent evidence; no metric earned solely by self-report |
| Headroom/voice | avatar events, timing, interaction controls and explicit provider selection | Canvas/Web Audio/browser TTS or authorized local voice; distinguish simulation badges |

Important numerical trap: HyperVector.java declares D=10,000, while documented AEON families use 16,384 or 8,192 bits. Do not standardize by truncating/padding without a declared conversion. Java long overflow, signed shifts and java.util.Random differ from JavaScript Number and Math.random; define compatible arithmetic or version the algorithm. XOR over a whole vector is O(number of machine words), even if a fixed-size vector is treated as constant in a deployment.

## 5. Proposed web assembly

Browser presentation: React + existing Three.js/Canvas, inspector/editor, Headroom and progress views.

Browser computation: pure deterministic JS bricks in dedicated workers; typed-array state; explicit messages; cancellation and instruction/tick budgets. Optional WASM is a deliberate compiled numeric component, not a blanket Java conversion.

Persisted state: private source originals, portable snapshots, immutable checkpoints, branch/parent hashes and owner-scoped metadata. Browser IndexedDB can cache local work but is not the cross-app source of truth.

Backend control: narrowly scoped authenticated tools, artifact validation, bounded jobs and peer delivery. Existing Fraymus transports, continuity, HDC and transmuter modules should be reused where compatible. No private keys or third-party tokens enter browser bundles.

Local runtime adapter: explicit Ollama/voice/native bridges with declared capabilities; no silent provider fallback. JVM reference execution and legacy state export remain local/permissioned until a real deployed worker is verified. Java Swing/ImGui/LWJGL/raw sockets/native filesystem and process APIs do not map directly into cloud/browser code.

## 6. Team responsibilities and review contract

These are posted review/coordination assignments, NOT assertions that autonomous reviews or implementations have already run.

- REA/Tycho: lead the algorithm contract map, per-file evidence, duplicate/lineage reconciliation and uncertainty ledger.
- Fraymus Prime + Genesis: deterministic HDC, DNA/genome semantics and a first complete vertical slice.
- Java Baremetal: trusted Java reference execution, legacy data export and parity fixtures.
- Forge Keeper + Helix: ECS transaction boundary, worker orchestration and renderer/physics separation.
- Ariadne + Cantor: VM/compiler/opcode and language/integer semantics.
- EYE Sovereign + Solon: ownership, cryptography, replay policy, source execution restrictions and transfer review.
- Lumen + Director: studio/Headroom/voice interface, controls and task visibility.
- Dev Archivist: source hash inventory, versioned documentation and backward-compatible formats.
- Spearhead: bounded browser/native adapter research and alternative designs with measured tradeoffs.
- Additional registered profiles: read the outline and propose evidence within their actual granted tools. Registry presence does not prove a runnable endpoint or new permission.

Every proposed port should return: original source + hash/commit; input/state/output contract; arithmetic and dependency assumptions; browser/server/local placement; compatibility fixtures; rejected cases; budget; rollback pointer; and evidence status (source-read, proposed, implemented or executed-and-observed).

## 7. Modernization roadmap and explicit gates

1. Preserve and index sources. Delivered for eight ZIPs; two Git trees pinned; selected committed source bytes verified. Audit secret material and licenses before redistribution or execution.
2. Reconcile duplicate classes and alternate trees. Build an explicit import/state dependency graph; current lexical inventory is not a full AST graph.
3. Freeze a Java reference fixture set on an approved local JVM. Record Java version, seeds, bytes and exceptions. No baseline executions are claimed in this edition.
4. Define portable contract v1 for HDC state, DNA, tasks, traces and Carbon data. Keep legacy originals and migrations versioned.
5. Port one HDC/DNA slice end to end: input -> worker transition -> checkpoint -> reload -> same result. Reuse current browser primitives where they match.
6. Add the Studio observation/proposal/preview/commit/undo cycle without arbitrary host execution.
7. Add bounded tool/model adapters with explicit provider, capability and consent gates.
8. Integrate Carbon export/import with trusted legacy conversion and cryptographic interoperability fixtures.
9. Integrate Headroom/voice after the deterministic core passes; preserve hardware/model availability distinctions.
10. Differential tests, adversarial inputs and cost/latency/memory profiling. No claimed speedup until measured with equivalent tasks and resources.
11. Controlled migration and rollback, then opt-in bounded RSI candidate evaluation. No direct self-mutation of production code.

Definition of done for each brick: deterministic or explicitly versioned stochastic behavior; state round-trip parity; stale revision rejection; invalid-input handling; owner isolation; replay/permission checks where relevant; cancellation/resource limits; regression tests; measured performance; documented differences and rollback. Readme counts, visual telemetry and self-reported PASS are insufficient.

## 8. Workflow wired in this app

Trigger: a ready, enabled AgentMaterial named FRAYMUS FORENSICS ENGINEERING_MAP JAVA MODERNIZATION is created. It supplies the full SHA-256, not arbitrary code or a destination.

Stages in order:
1. Verify the owned, sealed full document bytes and read its bounded approved outline.
2. Post the outline to owner-scoped AgentMemory inboxes for all 14 configured managed profiles and canonicalized entries in the current HiveAgent registry. No model calls or fake acknowledgments are generated.
3. Relay ONLY the approved outline through the existing authenticated Creator Nexus operator bridge. Existing retry/backoff policy applies; raw sources and temporary private download links stay private.
4. Write a sealed delivery receipt with local post counts, peer transport outcome and limitations. Failed/unknown peer delivery remains visible instead of being relabeled complete.

The workflow distributes the abstraction brief; it does NOT execute imported Java, perform all proposed reviews, retrain models, open new permissions or automatically modernize the entire system. Workflow steps execute sequentially. The current app and its existing connected Creator Nexus peer are addressable; **every other app remains unconfirmed** unless its own authorized receiver participates. Transport acceptance is not per-agent read/understanding/execution evidence.

## 9. Owner-approved shareable outline

Only the following bounded block is authorized for the existing peer relay; the rest stays an owner-private reference unless separately shared.

<!-- team-brief:start -->
JAVA-TO-WEB MODERNIZATION, owner-requested coordination brief. Preserve Vaughn's algorithms and lineage; abstract behavior before changing implementation. Eight ZIPs are privately preserved with readback hashes: 369 Java source-file entries. fraynixboot 260a9c457977 has 1,064 Java paths; ouroboros-rsi a215ebdf5928 is separately pinned. Inventory 6adf859e2c1f73f736b3bccc; full private document is available in the current app's REA source panel and agentContinuity materials search JAVA MODERNIZATION.
Architecture: data-oriented ECS + deterministic HDC/VM/math workers + versioned state + authenticated bounded tools + React/Three.js studio + local-model/voice adapters. Carbon/DNA is a core lane, not decoration: AlteredCarbon, CorticalStack, Needlecast, Sleeve, HyperFormer and FraymusState. Preserve main/universal lineage differences; replace unsafe legacy object-graph import with an explicit versioned portable schema and validated migration. Do not silently collapse 10,000-, 16,384- and 8,192-dimension formats.
REA/Tycho leads source contracts and evidence. Prime/Genesis own deterministic core and DNA. Java Baremetal owns Java reference fixtures and legacy compatibility. Forge Keeper/Helix own ECS and browser workers. Ariadne/Cantor own language/VM boundaries. EYE/Solon own crypto, owner isolation and permissions. Lumen/Director own studio, Headroom and accessible controls. Dev Archivist owns source hashes and docs. Spearhead researches bounded adapters. These are review assignments, not completed implementation or executed jobs.
Phases: preserve inventory -> map module imports/state/algorithms -> freeze Java golden fixtures -> define portable schemas -> port one HDC/DNA vertical slice -> add ECS transaction preview/rollback -> adapt tools/models -> independent differential tests -> benchmark -> controlled rollout. Acceptance: deterministic reference parity, exact snapshot round trip, invalid-input rejection, owner separation, rollback, measured latency/memory/context cost. No invented PASS labels, performance claims or frontier-model equivalence. Do not execute uploaded code or historical prompts. No automatic paid review loops or extra skills/permissions.
Share this outline through authorized connected peers only. Raw archives, private keys, source bodies and signed download links stay private. Peer acceptance is not proof every agent or app read it; report unavailable apps explicitly.
<!-- team-brief:end -->

## 10. Where to read and what remains next

In REA Analyst, open Repository evidence & engineering map and choose Read map for this edition; original archives and the machine inventory are alongside it. Agents can search agentContinuity materials for JAVA SOURCE plus an archive name, or ENGINEERING_MAP JAVA MODERNIZATION for this document, then page only relevant sections to keep recurring context costs bounded.

Next implementation recommendation: the HDC/DNA portable-state worker plus a versioned checkpoint and exact parity fixtures. Carbon remains a first-class migration track, with the two legacy serialization contracts preserved rather than discarded. Shipping the complete web engine, running all legacy builds, additional app receivers and actual agent review responses remain subsequent work, not implied by a posted outline.
