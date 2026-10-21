// Prepara la restauración de una copia de respaldo de la plataforma "Tests Opos TAI".
// Uso: node .claude/scripts/opos_restaurar.mjs <carpeta_respaldo> [coleccion ...]
// La carpeta tiene una subcarpeta por colección con un <doc_id>.json por documento
// (la crea ArtifactData con out_dir). Escribe <carpeta_respaldo>/writes_<n>.json: lotes de
// 50 entradas "set" listas para ArtifactData batch. Si los documentos ya existen en la
// base de datos, hay que añadir if_version leyéndolos antes; tras una pérdida total no hace falta.
import fs from 'node:fs';
import path from 'node:path';

const [dir, ...solo] = process.argv.slice(2);
if (!dir) { console.error('Falta la carpeta del respaldo'); process.exit(1); }

const writes = [];
for (const col of fs.readdirSync(dir)) {
  const cdir = path.join(dir, col);
  if (!fs.statSync(cdir).isDirectory() || (solo.length && !solo.includes(col))) continue;
  for (const f of fs.readdirSync(cdir)) {
    if (!f.endsWith('.json')) continue;
    writes.push({ op: 'set', collection: col, doc_id: f.slice(0, -5), file_path: path.resolve(cdir, f) });
  }
}
let lotes = 0;
for (let i = 0; i < writes.length; i += 50) {
  fs.writeFileSync(path.join(dir, `writes_${++lotes}.json`), JSON.stringify(writes.slice(i, i + 50), null, 1));
}
console.log(`${writes.length} documentos en ${lotes} lotes de 50 como máximo, en ${dir}`);
