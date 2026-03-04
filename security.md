
## 1. Intended Users
The code and data within this repository are intended for the following primary audiences:
* **Academic Faculty/Personel:** Instructors and TA's for the purpose of evaluation and grading.
* **The Author:** For version control and project management of academic assignments.
* **Potential Employers:** As a technical portfolio demonstrating proficiency in Kotlin, Android development, and data analysis.

## 2. Risk Assessment
An assessment of potential security threats indicates the following areas of concern if the repository were accessed by unauthorized parties:
* **Intellectual Property Theft:** Unauthorized copying of any potential original code
* **Credential Exposure:** Risks associated with the accidental commitment of API keys

## 3. Security Measures

### Repository Rulesets
Implemented a formal GitHub Ruleset (defined in `Pull request approvals.json`) applied to the default branch:
* **Restricted Deletions:** Prevention of accidental or malicious deletion of the main branch.
* **Linear History:** Enforcement of non-fast-forward push restrictions to ensure a clean commit history.
* **Mandatory Reviews:** The `require_code_owner_review` flag is active, ensuring that all merges into the default branch must be vetted by designated code owners.

### Access & Environment Control
* **Secret Management:** A `.gitignore` file is utilized to prevent sensitive local configuration files and build secrets from being tracked.
* **Dependency Monitoring:** Automatic scanning of third-party libraries is enabled to identify and patch known vulnerabilities in the project's dependencies.
