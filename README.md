# hex-compensator

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](#) [![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](#)

**hex-compensator** is a command-line utility that uses advanced color appearance models (CIECAM02) to generate print‑compensated HEX color codes. Given a screen‑based HEX code, it calculates a new HEX value that, when printed, visually matches the original on-screen color—eliminating guesswork and manual proofing.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Development](#development)
5. [Contributing](#contributing)
6. [Code of Conduct](#code-of-conduct)
7. [License](#license)

---

## Installation

Clone the repository and set up a virtual environment. Make sure to include a `.gitignore` to exclude your `venv/`, `__pycache__/`, and other generated files:

```bash
git clone https://github.com/<your-username>/hex-compensator.git
cd hex-compensator
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.gitignore` with these entries:

```
venv/
*.pyc
__pycache__/
```

---

## Usage

Activate the virtual environment and run the CLI with one or more HEX colors:

```bash
source venv/bin/activate
python cli.py "#6B0F1A"
# Batch example:
python cli.py "#6B0F1A" "#291616" "#927E7E"
```

Example output:

```
Original perceived in print:
  J=0.42, C=5.22, h=21.33

Use this HEX in your PDF to match on-screen color:
  #80121F
```

Once you have compensated values, you can add unit tests in `test_cases.py` and run:

```bash
python test_cases.py
```

---

## Project Structure

```text
hex-compensator/
├── .python-version        # Python version (3.11.x)
├── .gitignore            # Exclude venv and build files
├── LICENSE               # MIT license
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── cli.py                # Command-line interface entry point
├── compensator/          # Core library module
│   ├── perception.py     # Color appearance simulation
│   ├── optimizer.py      # Compensation algorithm
│   ├── utils.py          # HEX <-> RGB helpers
│   └── color_models.py   # Placeholder for future extensions
├── test_cases.py         # Unit tests for compensator functions
├── CONTRIBUTING.md       # Contribution guidelines
└── CODE_OF_CONDUCT.md    # Community code of conduct
```

---

## Development

We follow a standard Git workflow. Before contributing, please review our guidelines:

* **Branching**: `git checkout -b feature/<name>`
* **Commit messages**: Clear, imperative tense (e.g., `Add optimize function`)
* **Testing**: Update or add tests in `test_cases.py`
* **Linting**: Ensure code follows PEP8

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE\_OF\_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

---

## Contributing

Contributions, issues, and feature requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

---

## Code of Conduct

This project adheres to the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you agree to our standards.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
