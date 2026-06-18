# Agent Instructions

## Investigation Report Maintenance

When conducting further research or executing tasks related to the NVIDIA SkillSpector investigation, please follow this order to keep the documentation organized:

1. **Continuous Updates:** `investigation_report.md` is the primary source of truth. It MUST be updated continuously with any new findings, insights, or test results.
2. **Checklist Resolution:** As items in the "Next Steps / Further Investigation" checklist in `investigation_report.md` are completed, update the checklist boxes (change `[ ]` to `[x]`) and integrate the new findings into the appropriate core sections (e.g., "Findings") of the report.
3. **Adding New Inquiries:** Whenever a new area of inquiry, limitation, or potential vulnerability arises during testing, immediately add it as a new item to the checklist in `investigation_report.md`.
4. **Formatting:** Maintain the current markdown formatting and structure of the report, using appropriate headings, lists, and bold text for emphasis.

## Git Maintenance

1. **Gitignore Updates:** Please keep the `.gitignore` file updated. Whenever you clone a new repository, download a new tool, or create temporary directories in this workspace, ensure you immediately add them to `.gitignore` to prevent tracking unwanted files.
2. **Automatic Commits:** Automatically stage and commit changes to the repository as you make significant updates to the codebase or documentation. Always use clear, descriptive commit messages summarizing the work performed.
