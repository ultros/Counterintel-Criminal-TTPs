# Counterintel & Criminal TTPs

**An evidence-first reference on criminal psychology, deception, coercion, counterintelligence concepts, and forensic interpretation.**

*Research repository and terminology companion to the* **Counterintel & Criminal TTPs** *LinkedIn newsletter and a forthcoming book project.*

---

## Mission

Understanding a tactic is not the same as proving that it occurred.

**Counterintel & Criminal TTPs** documents the language, mechanisms, and evidentiary limits of behaviors encountered in criminal investigations, fraud, interpersonal manipulation, digital environments, and intelligence-related analysis. The goal is to give investigators, researchers, writers, and interested readers a careful vocabulary for describing conduct without substituting speculation for proof.

This project emphasizes four questions:

1. **What is the mechanism?** Identify the behavior without assuming motive.
2. **What evidence supports it?** Separate original observations from derived claims.
3. **What else could explain it?** Test competing interpretations and innocent alternatives.
4. **What would disprove it?** State observable conditions that would change the assessment.

## Explore the terminology atlas

The initial public release is the **500-Tactic Atlas**, a cross-disciplinary catalog of **500 uniquely identified terms across 25 thematic chapters**. The identifiers `CP-001` through `CP-500` are designed to remain stable as definitions, sources, and editorial classifications are improved.

| Resource | Purpose |
| :--- | :--- |
| **[Terminology home](terminology/README.md)** | Browse all 25 topics and their entry ranges |
| **[Complete 500-term index](terminology/ATLAS-INDEX.md)** | Find terms by stable CP identifier and chapter |
| **[50 public definitions](terminology/GLOSSARY-PUBLIC.md)** | Read the initial editorial preview definitions |
| **[Individual entry files](terminology/entries/)** | Open selected term records with interpretation cautions |
| **[Methods and evidence standards](terminology/METHODOLOGY.md)** | Review the classification system, causal analysis, and falsification tests |
| **[Research sources](terminology/SOURCES.md)** | Consult the starter bibliography and source-review status |
| **[Public JSON index](terminology/data/public-index.json)** | Use the structured term list in research and indexing workflows, subject to the stated rights |

### Featured term: CP-001

**[Induced-Threat Provocation via Causal Concealment](terminology/entries/CP-001.md)** · *Working descriptor*

A warning conceals that the warned person's intervention is what could trigger the predicted reaction. The entry distinguishes a proposed causal mechanism from proof that anyone deliberately orchestrated it.

This is a **descriptive analytical label**, not a formally established psychological diagnosis or a determination of criminal intent.

## Scope

The atlas includes material related to:

- **Behavior and influence:** decision errors, social pressure, reputational attacks, coercion, and interpersonal control.
- **Criminal methods and institutions:** deception, identity abuse, fraud, corruption, illicit networks, and threats.
- **Evidence and investigation:** witness reliability, interviews, event chronology, provenance, and attribution errors.
- **Digital environments:** cyber-enabled fraud, social engineering, false digital identities, and manipulated information ecosystems.
- **Strategic analysis:** intelligence terminology, adversarial signaling, competing hypotheses, and analytical safeguards.

These categories describe areas of inquiry, not a universal model of offenders or a procedure for diagnosing people.

## Classification and publication status

The catalog uses three **editorial** markers:

| Marker | Meaning | Current count |
| :---: | :--- | ---: |
| `E` | Recognized term in at least one relevant discipline or practice; source verification remains necessary | 350 |
| `D` | Working descriptor used to explain a pattern; **not necessarily an established scientific term** | 140 |
| `Q` | Qualified or contested term that requires additional context or caution | 10 |
| **Total** | **Distinct CP-identified entries** | **500** |

**Current stage: v0.1 public research preview.** All 500 titles are indexed, while **50 short definitions are publicly available**. The classifications are provisional. The index has not yet undergone a completed entry-by-entry scholarly citation audit; the [starter source list](terminology/SOURCES.md) must not be mistaken for supporting citations for all 500 terms.

The full working manuscript, expanded analyses, unpublished case material, and future book chapters are **not hosted in this repository**.

## Newsletter and book

The LinkedIn newsletter is the **narrative publication**: essays, examples, and forensic questions. This repository is the **reference layer**: terminology, methods, version history, source notes, and corrections. The forthcoming book will integrate and expand the material, subject to editorial and legal review.

**Selected edition:** [*The Informant Who Never Spoke* (SYN-EVID-003)](https://www.linkedin.com/pulse/informant-who-never-spoke-jesse-shelley-twwqc) explores a fictionalized evidentiary-deception scenario as an analytical and noir narrative, not as proof of a real allegation.

Future newsletter and book cross-references will use the stable CP identifiers where relevant.

## Research and evidence standards

The project follows an explicit distinction between:

`Original record → Corroborated evidence → Reasonable inference → Testable hypothesis → Speculation / unknown`

For any proposed tactic, assess **timing, source independence, information available to participants, alternative causes, and the possibility of falsification**. A matching behavioral pattern does **not** establish that an identifiable person committed a crime, acted intentionally, or participated in a coordinated operation.

See the complete [methodology and evidentiary safeguards](terminology/METHODOLOGY.md).

## Corrections and contributions

Precision matters more than a dramatic label. We welcome well-sourced corrections, better distinctions between neighboring terms, and primary or specialist references.

Please review [CONTRIBUTING.md](CONTRIBUTING.md) before submitting an issue or pull request. Cite the CP identifier, identify the exact statement, propose a correction, and include a supporting source wherever possible.

Do **not** submit private investigative records, victim-identifying information, confidential material, or unsupported accusations about named people. Do not treat this reference as a clinical diagnostic instrument or a guide for committing offenses.

## Repository structure

```text
Counterintel-Criminal-TTPs/
├── README.md                   # Project overview
├── CONTRIBUTING.md             # Editorial and correction policy
├── COPYRIGHT.md                # Rights and reuse conditions
├── CITATION.cff                # Citation metadata
├── CHANGELOG.md                # Version and correction history
├── terminology/
│   ├── README.md               # Chapter navigation
│   ├── ATLAS-INDEX.md          # Complete 500-term index
│   ├── GLOSSARY-PUBLIC.md      # 50 selected definitions
│   ├── METHODOLOGY.md          # Classification and evidence standards
│   ├── SOURCES.md              # Starter bibliography
│   ├── chapters/               # 25 themed chapter indexes
│   ├── entries/                # 50 public entry pages
│   └── data/public-index.json  # Structured public term catalog
├── scripts/
│   └── validate_terminology.py
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

For local integrity checks, run:

```bash
python scripts/validate_terminology.py
```

## Citation and copyright

**Editor:** Jesse Shelley · **Project:** *Counterintel & Criminal TTPs* · **Release:** v0.1 public preview (2026)

Citation details are provided in [CITATION.cff](CITATION.cff). Cite a specific CP identifier and the consulted version when discussing a term; verify claims against original research before relying on them for scholarly, investigative, or legal conclusions.

**© 2026 Jesse Shelley. All rights reserved** for original protected expression and compilation to the extent permitted by law. This is **not an open-source or open-content license**. Common terminology, facts, and third-party theories are not claimed as exclusive intellectual property. See [COPYRIGHT.md](COPYRIGHT.md) for details.

---

*Terms are tools for analysis, not verdicts. Evidence comes first.*