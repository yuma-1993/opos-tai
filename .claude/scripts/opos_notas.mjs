// Copia el texto de las notas de tema de la bóveda a la base de datos del artifact "Tests Opos TAI"
// (colección notas/<id>), para que la plataforma pueda crear tests de 50 preguntas desde la web.
// Uso: node .claude/scripts/opos_notas.mjs <carpeta_salida> [id ...]
// Escribe <salida>/notas/<id>.json, <salida>/meta/notas.json ({ids, fecha}) y <salida>/writes.json
// (entradas "set" para ArtifactData batch, máx. 50 por llamada; para documentos que ya existen
// hay que añadir if_version leyendo antes la colección). Con ids, solo esas notas.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const [out, ...solo] = process.argv.slice(2);
if (!out) { console.error('Falta la carpeta de salida'); process.exit(1); }

const docs = [];
for (const b of [1, 2, 3, 4]) {
  const carpeta = path.join(raiz, `Boveda - Bloque ${b}`, `Bloque ${b}`);
  if (!fs.existsSync(carpeta)) continue;
  for (const f of fs.readdirSync(carpeta)) {
    const m = /^B(\d+) - T([\d.]+)\s+(.*)\.md$/.exec(f);
    if (!m) continue;
    const id = `B${m[1]}-T${m[2]}`;
    if (solo.length && !solo.includes(id)) continue;
    const texto = fs.readFileSync(path.join(carpeta, f), 'utf8').replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '').trim();
    if (Buffer.byteLength(texto) > 240000) console.log(`AVISO: ${id} supera 240 KB y no cabe en un documento`);
    else docs.push({ id, data: { tema: id, titulo: m[3], texto, bytes: Buffer.byteLength(texto), ts: Date.now() } });
  }
}
fs.mkdirSync(path.join(out, 'notas'), { recursive: true });
fs.mkdirSync(path.join(out, 'meta'), { recursive: true });
const writes = [];
for (const d of docs) {
  const fp = path.join(out, 'notas', d.id + '.json');
  fs.writeFileSync(fp, JSON.stringify(d.data));
  writes.push({ op: 'set', collection: 'notas', doc_id: d.id, file_path: fp });
}
if (!solo.length) {  // lista de notas disponibles para la página (los ids con nota en la plataforma)
  const fp = path.join(out, 'meta', 'notas.json');
  fs.writeFileSync(fp, JSON.stringify({ ids: docs.map(d => d.id), fecha: new Date().toISOString().slice(0, 10) }));
  writes.push({ op: 'set', collection: 'opos_meta', doc_id: 'notas', file_path: fp });
}
fs.writeFileSync(path.join(out, 'writes.json'), JSON.stringify(writes, null, 1));
console.log(`${docs.length} notas, ${(docs.reduce((s, d) => s + d.data.bytes, 0) / 1024).toFixed(0)} KB en ${out}`);
