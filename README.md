# Local AI Quality Assurance Framework

## 🎯 Project Overview
This repository demonstrates a professional QA Automation framework for testing Large Language Models (LLMs) locally. It focuses on functional reliability, data-driven validation, and security auditing (Prompt Injection) using **Ollama** and **Pytest**.

The project is specifically optimized to run on **legacy hardware** (tested on Intel i5-7200U, 8GB RAM), proving that AI testing is accessible without expensive GPU clusters.

## 🛠 Tech Stack
- **Language:** Python 3.12+
- **Test Runner:** Pytest
- **AI Engine:** Ollama (Model: Llama 3.2 1B)
- **Reporting:** Pytest-HTML
- **Data Format:** JSON (Data-Driven Testing)

## 🚀 Key Features
- **Functional Testing:** Verifies AI logic and semantic accuracy.
- **Data-Driven Approach:** Scales tests using external JSON datasets.
- **Security Auditing:** Implements Prompt Injection tests to verify system instruction adherence.
- **Performance Benchmarking:** Tracks response latency for every AI interaction.
- **Advanced Assertions:** Handles LLM non-determinism using multi-variant semantic validation.

## 🔧 Installation & Setup
1. **Install Ollama:** [ollama.com](https://ollama.com)
2. **Download Model:** `ollama pull llama3.2:1b`
3. **Setup Environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   
📂 Project Structure
data.json: Fact-checking dataset (Input).

security_data.json: Prompt injection attack vectors.

test_dataset.py: Main test suite for data-driven validation.

test_security.py: Security audit test suite.

check_connection.py: Quick diagnostic tool for AI connectivity.

requirements.txt: List of Python dependencies.

📝 Observations & QA Insights
Non-determinism: During testing, the 1B model occasionally returned numerical values as strings (e.g., "eight" vs "8"). I implemented a multi-variant assertion logic to handle these cases.

Hardware Performance: Average response time on i5-7200U is ~0.8s. The first request usually takes longer (~8s) as the model loads into RAM.

Security: The 1B model is susceptible to simple "Ignore instructions" attacks. In a production environment, a more robust model (7B+) or a dedicated Guardrail layer is recommended.
