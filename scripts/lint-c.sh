#!/usr/bin/env bash
# C equivalent of `ruff check` for src/*/main.c.
# Runs, per file: clang-format (style), clang-tidy (static analysis), gcc (compile).
# Exit code is non-zero if any check fails.

set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

status=0
for f in src/*/main.c; do
    echo "===== $f"
    if ! clang-format --dry-run --Werror "$f"; then
        echo "  [FAIL] clang-format"
        status=1
    fi
    if ! clang-tidy "$f" -- -std=c17 -Wall -Wextra >/tmp/opencode/lint-c.out 2>&1; then
        cat /tmp/opencode/lint-c.out
        echo "  [FAIL] clang-tidy"
        status=1
    fi
    if ! gcc -std=c17 -Wall -Wextra -Wpedantic -fsyntax-only "$f"; then
        echo "  [FAIL] gcc"
        status=1
    fi
done

if [ "$status" -eq 0 ]; then
    echo "All C files clean."
fi
exit "$status"
