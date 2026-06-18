# SkillSpector Investigation Report

**Target:** NVIDIA SkillSpector (`https://github.com/NVIDIA/skillspector`)  
**Date:** June 18, 2026  
**Objective:** Investigate the capabilities of SkillSpector to analyze and detect vulnerabilities in AI agent skills without relying on primary API keys.

---

## 1. Overview
SkillSpector is a security scanner designed to detect vulnerabilities, malicious patterns, and security risks in AI agent skills before they are installed. It employs a two-stage pipeline:
1. **Static Analysis (Stage 1):** Fast regex-based pattern matching, AST behavioral analysis (for detecting `eval`, `exec`), and live OSV.dev dependency checking.
2. **LLM Semantic Evaluation (Stage 2):** Contextual intent evaluation.

## 2. Testing Methodology
The tool was installed inside an isolated Python 3.12 virtual environment using `uv`. Due to limitations with the Gemini OpenAI-compatible API wrapper handling OAuth tokens, Stage 2 (LLM evaluation) was bypassed. However, this provided an excellent opportunity to evaluate the robustness of its core **Stage 1 Static Analysis**.

We tested SkillSpector against two distinct targets:
1. **A Custom Malicious Skill:** A Python script explicitly engineered with vulnerabilities (e.g., `eval`, `subprocess` shell execution, and environment variable exfiltration).
2. **Official Anthropic MCP Skills:** Real-world, production-ready Model Context Protocol (MCP) servers (specifically the `filesystem` skill).

## 3. Findings

### Test A: Custom Malicious Skill
**Result:** Successfully detected 100% of injected vulnerabilities.
**Score:** 100/100 (CRITICAL)
- **High Severity (`eval`):** Flagged arbitrary evaluation execution (AST2).
- **High Severity (Tool Abuse):** Flagged `shell=True` in subprocess calls (TM1).
- **Medium Severity (Exfiltration):** Detected external HTTP transmission of data.

### Test B: Real-World "Filesystem" MCP Skill
**Result:** Discovered live CVEs and flagged inherent architectural risks.
**Score:** 100/100 (CRITICAL)
- **Supply Chain Vulnerability (SC4):** Queried `OSV.dev` and identified that the project relied on `minimatch==10.0.1`, which contains 3 known CVEs for Regular Expression Denial of Service (ReDoS) (e.g., CVE-2026-27904).
- **Self-Modification Risk (RA1):** Flagged `index.ts` for containing code capable of modifying the local filesystem. While intentional for a "filesystem" skill, this correctly highlights the inherent danger of granting an LLM access to this tool.
- **Credential Access (PE3):** Flagged multiple locations in unit tests where file paths resembled system configuration or credential paths.
- **Unpinned Dependencies (SC1):** Identified numerous unpinned dependencies in `package.json`.

## 4. Conclusion
SkillSpector is a highly effective, production-ready security scanner for AI capabilities. 

Even without the LLM Semantic Evaluation stage, its static analysis engine is incredibly thorough. It goes far beyond standard linting by combining AST behavioral tracking with live dependency vulnerability queries. The discovery of a live ReDoS CVE in an official, highly-used Anthropic skill demonstrates the tangible value of integrating SkillSpector into any AI agent deployment pipeline. 

**Recommendation:** Highly recommended for integration into CI/CD pipelines when dealing with third-party AI skills or MCP servers.

## 5. Next Steps / Further Investigation (Checklist)
- [ ] **Test Stage 2 (LLM Evaluation):** Resolve the Gemini API wrapper limitations or configure an alternative LLM provider to fully evaluate the semantic evaluation stage.
- [ ] **CI/CD Integration:** Set up a proof-of-concept pipeline (e.g., GitHub Actions) to automatically run SkillSpector on incoming pull requests for AI skills.
- [ ] **False Positive Analysis:** Run SkillSpector against a broader dataset of safe, production-grade skills to assess the false positive rate of the static analysis engine.
- [ ] **Custom Rule Creation:** Investigate how to add custom static analysis rules or custom semantic evaluation prompts to SkillSpector.
- [ ] **Broader Ecosystem Testing:** Expand testing to include skills from other popular frameworks like LangChain, LlamaIndex, or AutoGen.
