### Hexlet tests and linter status:
[![Actions Status](https://github.com/Qualcommes/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Qualcommes/python-project-49/actions)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Qualcommes_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Qualcommes_python-project-49)

# About project

#### Brain Games is a console application project that offers 5 math games:

##### 1. "Evenness Check" game. You have to correctly answer the question: "Is a number even?"

##### 2. "Calculator" game. You have to calculate a problem with two numbers.

##### 3. "GCD" game. You have to find the greatest common divisor of two numbers.

##### 4. "Arithmetic Progression" game. You have to find the missing number in the progression.

##### 5. "Is a Number Prime?" game. You have to correctly answer the question: "Is a Number Prime?"

##### Each game asks three questions. If you answer correctly, move on to the next one; if you answer incorrectly, the game ends.

## 2. Minimum requirements

### Environment

#### Python version 3.12 or higher
#### prompt version 0.4.1 or higher
#### [for development] ruff version 0.14.1 or higher

## 3. Usage (available commands)

### brain-even — игра «Чётное или нечётное».

### brain-calc — игра «Калькулятор» (арифметические выражения).

### brain-gcd — игра «Наибольший общий делитель».

### brain-progression — игра «Арифметическая прогрессия».

### brain-prime — игра «Простое число».

## 4. Installation and launch 

### Via pip

#### 1. Clone the repository and navigate to the project folder

```bash
git clone <url of repository>
cd hexlet-code
```

#### 2. (Recommended) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

#### 3. Install the package

```bash
pip install .
```

#### 4. Launch any game, for example

```bash
brain-even
```

### Via UV (recommended)

#### 1. Clone the repository and navigate to the project folder

```bash
git clone <url of repository>
cd hexlet-code
```

#### 2. Install uv if it is not already installed

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # Windows/Linux/macOS/WSL
```

#### 3. Create a virtual environment

```bash
uv venv
```

#### 4. In the root of the project, run the installation

```bash
uv pip install .
```

#### 5. Launch any game, for example

```bash
brain-progression
```

## 5. Installing for development

```bash
# pip
pip install -e .[dev]

# uv
uv pip install -e .[dev]
```

## 6. Removing

```bash
# pip
pip uninstall hexlet-code

# uv
uv pip uninstall hexlet-code
```

## 7. Examples of use

### Example of installing a package, launching the brain-even game, victory and defeat 

[![asciicast](https://asciinema.org/a/QpZupNHjM2nqdpBY.svg)](https://asciinema.org/a/QpZupNHjM2nqdpBY)

### Example of launching the brain-calc game, victory and defeat

[![asciicast](https://asciinema.org/a/iWYlNaj2yBY4FZuW.svg)](https://asciinema.org/a/iWYlNaj2yBY4FZuW)

### Example of launching the brain-gcd game, victory and defeat

[![asciicast](https://asciinema.org/a/QaBrLiHLm3mAOpkZ.svg)](https://asciinema.org/a/QaBrLiHLm3mAOpkZ)

### Example of launching the brain-progression game, victory and defeat

[![asciicast](https://asciinema.org/a/rSTsZe3JZPh6cs11.svg)](https://asciinema.org/a/rSTsZe3JZPh6cs11)

### Example of launching the brain-prime game, victory and defeat

[![asciicast](https://asciinema.org/a/H3oGBTFMoe9UcGgm.svg)](https://asciinema.org/a/H3oGBTFMoe9UcGgm)
