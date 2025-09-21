# Python Personal Finance Tracker (PPFT) v0.2.0-beta

**Python Personal Finance Tracker (PPFT)** is a simple program created to process financial Excel workbooks.

**Note:** This program is not affiliated with the `pynance` python library. 

## Prerequisites

- **Python 3** with **openpyxl**
- **Excel**, **LibreOffice Calc**, or another program to view/edit `.xlsx` workbooks.

## Installation

Download the **Python Personal Finance Tracker (PPFT)** repository from Github. You now have two choices.

### Option A: Use Python Interpreter
Simply run `main.py` using your desired Python interpreter. This is best if you just want to try out PPFT.

### Option B: Custom bash script (Debian)
**Note**: This method requires the use of `sudo` user privileges.

#### Step 1:
In the **PPFT** repository is a bash script named `pynanceXL`. Copy this file to `/usr/local/bin`.

#### Step 2:
If needed, make the file executable by running the command `chmod +x pynanceXL`. This will make the file executable. 
Now the `pynanceXL` command is ready to use.

#### Step 3:
Run the command `pynanceXL -i` and you will be prompted to enter the path of the **PPFT** repository. 
This will be wherever you downloaded it to, such as `/home/user/Downloads/PPFT`.

#### Check if PPFT is installed
To check if **PPFT** is properly installed, run the command `pynanceXL -r`.
If you receive the error that `/usr/local/bin/PPFT/main.py` does not exist, try **Step 3** again and ensure the path is entered correctly.

## Usage
I created this program as I desired a basic, simple, automated
personal finance program that utilizes Excel files.

### Files
Included with **PPFT** is a folder named `templates`.
There are four workbook templates for you to copy and use.

- `income.xlsx`
| Enter your income figures here.
- `expenses.xlsx`
| Enter your expense figures here.
- `jan-mtd.xlsx`
| Leave empty. Month-to-date totals go here.
- `20xx-ytd.xlsx`
| Leave empty. Data stored here is pulled from `mtd` worksheets.

Rename the workbooks to suit your organization tastes. 
Bear in mind that the `mtd` and `ytd` workbooks should follow
a particular formatting scheme in order for **PPFT** to read them.
Examples below:
- `2024-ytd.xlsx`
- `mar-mtd.xlsx`
- `jun-mtd.xlsx`

It is discouraged to alter workbook formatting,
as this may break program. Do so at your own risk.

### Commands

#### Bash Commands
- `pynanceXL -h` 
| Displays a list of `pynanceXL` bash commands.
- `pynanceXL -r`
| If `pynanceXL` is installed, runs the program.
- `pynanceXL -i`
| Installs the program into `/usr/local/bin`

#### Python Commands
- `help`
| Prints of full list of `pynanceXL` python commands.
- `cd`
| Change current working directory.
- `cwd`
| Print current working directory.
- `ls`
| Print files and directories in CWD

For a full list of commands, feel free to try out **PPFT**.
Then, run the `help` command.

## Updating PPFT
To update **PPFT**, simply download the latest repository. 
Then, if needed, refer to **Option B: Step 3** under **Installation**.

## Bug reporting
Report any bugs and/or suggestions to [Folfchie](https://www.github.com/Folfchie) on Github.
