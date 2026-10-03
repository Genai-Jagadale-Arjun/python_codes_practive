# Git Setup and Repository Commands

Run these commands in PowerShell.

## Install Git

```powershell
winget install --id Git.Git -e --source winget --accept-source-agreements --accept-package-agreements --silent
```

Close and reopen PowerShell, then verify Git:

```powershell
git --version
```

If `git` is still not recognized in the current PowerShell session, add the standard Git command directory to that session's PATH and verify again:

```powershell
$env:Path = "$env:ProgramFiles\Git\cmd;$env:Path"
git --version
```

## Clone the Repository

Change to the target folder. The folder must be empty before cloning into `.`:

```powershell
Set-Location "$HOME\Downloads\python_programming"
git clone https://github.com/Genai-Jagadale-Arjun/python_codes_practive.git .
```

The repository has already been cloned into this workspace. Do not run the clone command again here.

## Check the Clone

```powershell
git status --short --branch
git remote -v
```