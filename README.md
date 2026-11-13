# AI IT Infrastructure Assistant

A starter project for an AI-assisted IT support and infrastructure troubleshooting assistant. It provides a small, transparent rule-based troubleshooting demo and a structure that can later be extended with an LLM, RAG, monitoring integrations, and automation.

## Goals
- Help IT support teams organize common troubleshooting guidance.
- Provide consistent first-step recommendations for frequent issues.
- Keep troubleshooting steps readable and safe (no automatic changes).
- Create a foundation for future AI/RAG integrations.

## Current demo
The included Python CLI matches a few common symptoms to a curated knowledge base:
- Internet/network connectivity
- Windows DNS resolution
- Printer connectivity
- Microsoft 365 sign-in

This is **not an autonomous production agent**. It does not connect to company systems, collect credentials, or execute commands.

## Requirements
- Python 3.10+

## Run locally
```bash
python app.py
```

Enter a symptom (for example, `DNS not working`) or type `exit`.

## Project structure
```text
AI-IT-Infrastructure-Assistant/
├── app.py
├── knowledge_base.json
├── requirements.txt
├── LICENSE
├── .gitignore
├── docs/
│   └── roadmap.md
└── examples/
    └── sample_queries.md
```

## Safety principles
- Recommendations are advisory; verify before making changes.
- Do not enter passwords, tokens, private keys, or confidential company data.
- Test changes in a lab before production.
- Add role-based access, audit logs, approval gates, and secret management before integrating real infrastructure.

## Roadmap
See [`docs/roadmap.md`](docs/roadmap.md).

## Contributing
Contributions are welcome. Open an issue to propose a troubleshooting topic or submit a pull request with a tested knowledge-base entry and documentation.

## License
MIT — see [`LICENSE`](LICENSE).
