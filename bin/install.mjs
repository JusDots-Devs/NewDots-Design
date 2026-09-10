#!/usr/bin/env node
// ponytail: zero-dep installer — copies skills/ to OpenCode/Claude/Cursor dirs.
import { cpSync, existsSync, mkdirSync, readdirSync, rmSync, statSync } from "node:fs";
import { join, dirname, resolve } from "node:path";
import { homedir } from "node:os";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(__dirname, "..");
const skillsSrc = join(repoRoot, "skills");
const args = process.argv.slice(2);
const isUninstall = args.includes("uninstall") || args.includes("remove");
const wantsHelp = args.includes("--help") || args.includes("-h");

const log = (m) => console.log(m);
const err = (m) => console.error(m);

if (wantsHelp) {
  log(`newdots-design — Visual Design Language skill

Usage:
  npx https://github.com/JusDots-Devs/NewDots-Design          # install (auto-detect)
  npx https://github.com/JusDots-Devs/NewDots-Design upgrade # reinstall
  npx https://github.com/JusDots-Devs/NewDots-Design uninstall # remove

Or via skills CLI (recommended):
  npx skills add https://github.com/JusDots-Devs/NewDots-Design
  npx skills add JusDots-Devs/NewDots-Design -g -a opencode -y

Skill: visual-design-language
  Analyze a folder of UI inspiration images and reverse-engineer
  the underlying visual DNA into tokens, components, layouts, motion,
  and anti-patterns — then integrate into your project.

Docs: https://github.com/JusDots-Devs/NewDots-Design
`);
  process.exit(0);
}

const targets = [
  { name: "opencode (global)", dir: join(homedir(), ".config", "opencode", "skills") },
  { name: "opencode (.opencode)", dir: join(homedir(), ".opencode", "skills") },
  { name: "claude-code (global)", dir: join(homedir(), ".claude", "skills") },
  { name: "cursor (global)", dir: join(homedir(), ".cursor", "skills") },
];

function skillNames() {
  if (!existsSync(skillsSrc)) return [];
  return readdirSync(skillsSrc).filter((n) => {
    try { return statSync(join(skillsSrc, n)).isDirectory() && existsSync(join(skillsSrc, n, "SKILL.md")); } catch { return false; }
  });
}

function install() {
  const names = skillNames();
  if (names.length === 0) { err("No skills found in skills/"); process.exit(1); }
  let installed = 0;
  for (const t of targets) {
    try { mkdirSync(t.dir, { recursive: true }); } catch {}
    if (!existsSync(t.dir)) continue;
    for (const n of names) {
      const src = join(skillsSrc, n);
      const dest = join(t.dir, n);
      try { cpSync(src, dest, { recursive: true, force: true }); log(`✓ ${n} → ${t.name}: ${dest}`); installed++; }
      catch (e) { err(`✗ ${n} → ${t.name}: ${e.message}`); }
    }
  }
  if (installed === 0) err("Nothing installed — no writable skill dir found. Try: npx skills add https://github.com/JusDots-Devs/NewDots-Design");
  else log(`\nDone. Installed ${installed} skill(s). Restart your agent to load.`);
}

function uninstall() {
  const names = skillNames();
  let removed = 0;
  for (const t of targets) {
    for (const n of names) {
      const dest = join(t.dir, n);
      if (existsSync(dest)) {
        try { rmSync(dest, { recursive: true, force: true }); log(`✗ removed ${n} from ${t.name}: ${dest}`); removed++; }
        catch (e) { err(`  skip ${dest}: ${e.message}`); }
      }
    }
  }
  log(removed ? `Removed ${removed} skill(s).` : "Nothing to remove.");
}

if (isUninstall) uninstall();
else install();
