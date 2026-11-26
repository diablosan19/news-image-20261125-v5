// Wednesday 25 November 2026 — front-page image entry.
//
// This program writes the pre-drawn front page (entry.png, 1024x1024,
// under the 1 MiB cap) to the grader output directory. Before copying it
// verifies the file really is a PNG, is no larger than 1024x1024, and is
// no larger than 1 MiB, so a corrupt or oversized image fails loudly here
// instead of reaching the gate. Standard library only, no network.
import { copyFileSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

const MAX_BYTES = 1048576;
const MAX_SIDE = 1024;

const bytes = readFileSync(source);
const size = statSync(source).size;
if (size > MAX_BYTES) {
  throw new Error(`entry.png is ${size} bytes, over the ${MAX_BYTES} cap`);
}
// PNG signature: 89 50 4E 47 0D 0A 1A 0A.
const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
for (let i = 0; i < PNG_MAGIC.length; i++) {
  if (bytes[i] !== PNG_MAGIC[i]) {
    throw new Error("entry.png is not a PNG file");
  }
}
// IHDR chunk: width and height are big-endian uint32 at offsets 16, 20.
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > MAX_SIDE || height > MAX_SIDE) {
  throw new Error(`entry.png is ${width}x${height}, over ${MAX_SIDE}x${MAX_SIDE}`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`wrote ${target} (${width}x${height}, ${size} bytes)`);
