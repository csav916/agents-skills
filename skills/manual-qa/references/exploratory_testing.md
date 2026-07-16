# Exploratory Testing Guide for Manus

Exploratory testing is an approach to software testing that emphasizes the personal freedom and responsibility of the individual tester to continually optimize the quality of their work by treating test-related learning, test design, test execution, and test result interpretation as mutually supportive activities that run in parallel throughout the project.

## Core Charters
1. **User Persona Testing**: Act as different personas (e.g., first-time user, power user, admin) to find usability issues.
2. **Boundary Testing**: Input extremely large values, empty strings, special characters, or invalid formats into forms.
3. **Interrupt Testing**: Navigate away mid-process, refresh the page, or use the back button during transactions.
4. **Visual Regression**: Check for overlapping elements, broken images, or inconsistent styling across different viewports.

## Heuristics (SFDPOT)
- **Structure**: What is it made of? (Technologies, files, code).
- **Function**: What does it do? (Features, calculations).
- **Data**: What does it process? (Inputs, outputs, state).
- **Platform**: Where does it run? (Browser, OS, hardware).
- **Operations**: How is it used? (Workflows, user habits).
- **Time**: When does it happen? (Concurrency, timeouts, history).
