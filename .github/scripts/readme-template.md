[//]: # "DO NOT CHANGE THIS FILE BUT ITS TEMPLATE `.github/scripts/readme-template.md`"

# pre-commit_mirrors-taplo

mirror of https://github.com/tamasfe/taplo for pre-commit

# taplo mirror

Mirror of `taplo` for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For taplo: see https://github.com/tamasfe/taplo

### Using taplo with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/s-weigand/pre-commit_mirrors-taplo
    rev: "{{taplo_version}}"
    hooks:
      - id: fmt
      - id: check
```
