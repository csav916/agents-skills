---
name: manual-qa
description: "End-to-end manual and exploratory QA testing using browser automation. Use for: verifying web features, performing regression tests, exploratory testing, and generating bug reports."
---

# Manual QA Skill

This skill enables Manus to act as a professional Manual QA Engineer. It provides a structured workflow for testing web applications, identifying bugs, and documenting results.

## Workflow

### 1. Requirements Gathering & Plan Design
- **Analyze**: Review the user's request or provided documentation to understand the feature under test.
- **Plan**: Use `templates/test_plan.md` to create a structured test plan. Define specific test cases with clear steps and expected results.
- **Confirm**: (Optional) Share the plan with the user if the scope is complex.

### 2. Test Execution
- **Navigate**: Use the browser to access the target URL.
- **Execute**: Follow the steps defined in the test plan. Perform actions like clicking, typing, and navigating.
- **Observe**: Monitor for visual glitches, console errors (check browser logs if needed), and functional failures.
- **Record**: Update the test plan in real-time with actual results and pass/fail status.

### 3. Exploratory Testing
- **Beyond the Plan**: Refer to `references/exploratory_testing.md` for heuristics and charters.
- **Chaos Monkey**: Try unexpected inputs, rapid clicks, and non-linear navigation to find edge-case bugs.

### 4. Bug Reporting & Summary
- **Document**: For any failure, create a detailed bug report using the section in `templates/test_plan.md`. Include reproduction steps and clear descriptions of the discrepancy.
- **Evidence**: Capture screenshots or relevant logs.
- **Report**: Deliver the completed test plan and bug reports to the user.

## Best Practices for Manus QA
- **Visual Checks**: Always verify that elements are not just present, but visible and correctly positioned.
- **Console Monitoring**: Proactively check for JavaScript errors or failed network requests in the browser.
- **State Awareness**: Be mindful of session states (logged in vs. logged out) and how they affect the UI.
- **Concise Reporting**: Keep bug titles descriptive and steps easy to follow.
