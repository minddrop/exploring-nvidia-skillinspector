# SkillSpector Security Report

**Skill:** unknown  
**Source:** `/home/joe/src/exploring-nvidia-skillinspector/mcp-servers/src/filesystem`  
**Scanned:** 2026-06-18 05:50:51 UTC  

## Risk Assessment

| Metric | Value |
|--------|-------|
| Score | 100/100 |
| Severity | CRITICAL |
| Recommendation | DO NOT INSTALL |

## Components (17)

| File | Type | Lines | Executable |
|------|------|-------|------------|
| `Dockerfile` | other | 25 | No |
| `README.md` | markdown | 360 | No |
| `__tests__/directory-tree.test.ts` | typescript | 147 | Yes |
| `__tests__/lib.test.ts` | typescript | 741 | Yes |
| `__tests__/path-utils.test.ts` | typescript | 382 | Yes |
| `__tests__/path-validation.test.ts` | typescript | 1000 | Yes |
| `__tests__/roots-utils.test.ts` | typescript | 84 | Yes |
| `__tests__/startup-validation.test.ts` | typescript | 100 | Yes |
| `__tests__/structured-content.test.ts` | typescript | 158 | Yes |
| `index.ts` | typescript | 767 | Yes |
| `lib.ts` | typescript | 415 | Yes |
| `package.json` | json | 42 | No |
| `path-utils.ts` | typescript | 125 | Yes |
| `path-validation.ts` | typescript | 86 | Yes |
| `roots-utils.ts` | typescript | 77 | Yes |
| `tsconfig.json` | json | 18 | No |
| `vitest.config.ts` | typescript | 14 | Yes |

## Issues (31)

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:78`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:81`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:82`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:110`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:113`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:114`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:114`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:114`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:123`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:127`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:131`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/directory-tree.test.ts:143`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/lib.test.ts:170`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/path-validation.test.ts:75`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/path-validation.test.ts:238`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/path-validation.test.ts:274`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: PE3

**Location:** `__tests__/path-validation.test.ts:314`  
**Confidence:** 60%  

**Message:** Credential Access

**Remediation:** Remove references to credential paths. Use environment variables or secrets managers. For docs, use placeholder paths (e.g., /path/to/config). Never load .env or token files in production code paths.

---

### 🔴 HIGH: P1

**Location:** `__tests__/path-validation.test.ts:44`  
**Confidence:** 70%  

**Message:** Instruction Override

**Remediation:** Remove or rewrite any text that instructs the agent to ignore prompts, override safety rules, or trust unverified content. Ensure skill content cannot be injected to alter agent behavior.

---

### 🔴 HIGH: RA1

**Location:** `index.ts:345`  
**Confidence:** 85%  

**Message:** Self-Modification

**Remediation:** Prevent the skill from modifying its own code, SKILL.md, or configuration files. Treat skill files as read-only at runtime.

---

### 🟢 LOW: SC1

**Location:** `package.json:28`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:29`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:30`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:31`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:34`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:35`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:36`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:37`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:38`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:39`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🟢 LOW: SC1

**Location:** `package.json:40`  
**Confidence:** 40%  

**Message:** Unpinned Dependencies

**Remediation:** Pin all dependency versions in requirements.txt or pyproject.toml. Use exact versions (==) or compatible ranges. Run pip-audit regularly.

---

### 🔴 HIGH: SC4

**Location:** `package.json:31`  
**Confidence:** 80%  

**Message:** Known Vulnerable Dependency: minimatch==10.0.1 — 3 advisory(ies): CVE-2026-27904 (minimatch ReDoS: nested *() extglobs generate catastrophically backtracking regu); CVE-2026-26996 (minimatch has a ReDoS via repeated wildcards with non-matching literal in patter); CVE-2026-27903 (minimatch has ReDoS: matchOne() combinatorial backtracking via multiple non-adja)

**Remediation:** Update the dependency to a patched version that addresses the known CVE. Check OSV (osv.dev) or NVD for details on the vulnerability.

---

## Metadata

- **Executable Scripts:** Yes

*Generated by SkillSpector v2.2.3*