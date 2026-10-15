#!/usr/bin/env node
// Compiles src/<id>/animation.ts -> src/<id>/animation.js
//
// Usage: npm run build:animation -- <id> [--watch]

import { build, context } from "esbuild";
import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.dirname(path.dirname(fileURLToPath(import.meta.url)));

const args = process.argv.slice(2);
const watch = args.includes("--watch");
const id = args.find((a) => !a.startsWith("--"));

if (!id) {
  console.error("Usage: npm run build:animation -- <problem-id> [--watch]");
  process.exit(1);
}

const entry = path.join(rootDir, "src", id, "animation.ts");
const outfile = path.join(rootDir, "src", id, "animation.js");

if (!existsSync(entry)) {
  console.error(`No such file: ${entry}`);
  process.exit(1);
}

// type-check only; esbuild performs the actual (non type-checking) transpile.
try {
  execFileSync(
    path.join(rootDir, "node_modules", ".bin", "tsc"),
    ["--noEmit", "-p", path.join(rootDir, "tsconfig.json")],
    { stdio: "inherit", cwd: rootDir }
  );
} catch {
  console.error("Type check failed.");
  process.exit(1);
}

const options = {
  entryPoints: [entry],
  outfile,
  bundle: true,
  format: "iife",
  target: "es2020",
  sourcemap: true,
  logLevel: "info",
};

if (watch) {
  const ctx = await context(options);
  await ctx.watch();
  console.log(`Watching ${entry} for changes...`);
} else {
  await build(options);
  console.log(`Built ${outfile}`);
}
