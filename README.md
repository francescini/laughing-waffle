# Systems safety engineering methodologies for responsible AI LLMs

Laaughing Waffle is a repository of systems safety engineering methodologies to use to help develop safer and more responsible AI applications built on top of Large Language Models (LLMs).


# Methodologies in scope

## 1. Fault Tree Analysis (FTA)
FTA is a top-down approach to identify potential causes of system failures.

A fault tree has been created for potential Large Language Model failures [here](fault_tree_diagram).

### Explanation
* **Top-Level Failure:** Represents the overall potential failure of the LLM.
* **Intermediate Failures:** Breaks down into major failure modes: generating harmful content, privacy breaches, and biased outputs.
* **Basic Causes:** Further breaks down into more specific causes, identifying root issues that contribute to each intermediate failure.

### Application
This fault tree helps identify where to focus safety efforts in the development and deployment of LLMs. By addressing each node in the fault tree, developers can implement safety measures to address potential failures in LLMs.


## 2. Failure Modes and Effects Analysis (FMEA)
FMEA is a method for evaluating processes to identify where and how they might fail and assessing the relative impact of different failures.

A FMEA has been created for a Large Language Model [here](FMEA_for_LLM.md).

### Explanation
* **Severity (S):** The seriousness of the failure's effect (1-10 scale).
* **Occurrence (O):** The frequency of the failure cause (1-10 scale).
* **Detection (D):** The likelihood of detecting the failure before it reaches the user (1-10 scale).
* **Risk Priority Number (RPN):** Calculated as \( \text{RPN} = S \times O \times D \). Higher RPN indicates higher priority for addressing the failure.

### Application
A FMEA helps identify various ways LLMs can fail and evaluate the severity, occurrence, and detectability of each failure mode. From here, mitigation strategies can be prioritised to focus on high-priority issues.


## 3. Hazard Analysis and Critical Control Points (HACCP)
HACCP is used to identify critical points where hazards might occur and implement control measures to prevent or mitigate these hazards.

An illustrative HACCP plan for a Large Language Model [here](HACCP_plan_for_LLM)

### Explanation
* The HACCP plan includes a hazard analysis that identifies potential hazards at each stage of the LLM lifecycle, such as data collection, preprocessing, model training, evaluation, deployment, user interaction, and monitoring and maintenance, along with corresponding control measures.

* It establishes critical control points (CCPs) with specific critical limits, monitoring procedures, verification procedures, corrective actions, and record-keeping protocols to ensure the model's safety, reliability, and compliance throughout its development and deployment.

### Application

A HACCP plan can be used to systematically identify potential hazards at each stage of the LLM's lifecycle and implementing critical control points to mitigate these risks. This helps the model's safety, reliability, and compliance by continuously monitoring, verifying, and updating the processes based on predefined critical limits.

## 4. Preliminary Hazard Analysis (PHA)
PHA is an early-phase risk assessment tool used to identify potential hazards and analyze the severity of their consequences.

An illustrative PHA plan for a Large Language Model is [here](PHA_for_LLM.md).

### Explanation

Early Risk Identification: Conduct a PHA during the design phase of the LLM to identify potential hazards related to data bias, misinformation, or ethical concerns.
Mitigation Planning: Develop mitigation strategies early in the development process to address identified hazards.

## 5. Human Reliability Analysis (HRA)
HRA focuses on understanding the potential for human error within a system and designing systems to reduce these errors.

### Explanation

The critical tasks for the LLM involve:

Data Collection
Data Preprocessing
Model Training
Model Evaluation
Deployment
User Interaction
Monitoring and Maintenance

An example Human Reliability Analysis table is [here](HRA_for_LLM.md).

### Application
* User Interaction Analysis: Evaluate how users interact with LLMs and identify potential areas where human error could lead to unsafe outcomes.
* Design for Safety: Develop user interfaces and interaction protocols that minimize the risk of misinterpretation or misuse of LLM outputs.

## 6. System-Theoretic Process Analysis (STPA)
STPA is a safety analysis methodology based on systems theory and system thinking for identifying unsafe control actions and analyzing how system interactions can lead to hazards. It is used to identify hazards in complex systems, particularly where traditional methods like FMEA (Failure Modes and Effects Analysis) may not capture systemic risks effectively. It is particularly relevant in the context of integrated systems with complex interactions, such as in aerospace, automotive, nuclear power, and healthcare technologies.

### Explanation

A detailed list of the steps in a STPA for an example LLM can be found [here]

An example graph based control diagram for a LLM can be found [here](STPA_for_LLM_Control_Structure.md).

### Application

* Control Actions Analysis: Identify unsafe control actions in the LLM's decision-making processes, such as inappropriate content generation.
* Interaction Analysis: Analyze interactions between the LLM and other system components (e.g., users, external systems) to identify potential safety risks.
* Implement Controls: Design controls to prevent or mitigate identified unsafe actions and interactions.

## 7. Safety Case Development
A safety case is a structured argument, supported by evidence, that a system is safe for a specific application in a specific environment.

An example safety case for an LLM is [here]

### Application

* Develop Safety Cases: Create safety cases for different use scenarios of LLMs, such as customer service, medical advice, or content moderation.
* Evidence Collection: Gather evidence from testing, validation, and operational data to support safety claims.
* Continuous Evaluation: Regularly update the safety case as new data and insights are gained from LLM deployment and use.


## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details
