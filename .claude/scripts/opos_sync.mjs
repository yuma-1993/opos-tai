// Convierte _repasos.md y _dudas.md en los documentos de la pestaña /opos del artifact "Tests Opos TAI".
// Uso: node .claude/scripts/opos_sync.mjs <carpeta_salida> [AAAA-MM-DD]
// Escribe <salida>/repasos/<id>.json, <salida>/dudas/<id>.json, <salida>/meta.json
// y <salida>/writes.json (entradas "set" listas para ArtifactData batch; al reescribir
// documentos que ya existen hay que añadir if_version leyendo antes la colección).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const dir = path.join(raiz, 'Boveda - Bloque 2');
const out = process.argv[2];
const hoy = process.argv[3] || new Date().toISOString().slice(0, 10);
if (!out) { console.error('Falta la carpeta de salida'); process.exit(1); }

// Título del registro -> id de tema de la plataforma (CAT de la página).
const IDS = [
  [/^La Constituci[oó]n/i, 'B1-T1'],
  [/^Las Cortes/i, 'B1-T2'],
  [/^El Gobierno/i, 'B1-T3'],
  [/^Periféricos|^Perifericos/i, 'B2-T2'],
  [/Entidad-Relaci[oó]n/i, 'B3-T1.1'],
  [/Administraci[oó]n de Sistemas Operativos.*SSH/i, 'B4-T1.2'],
  [/Administraci[oó]n de Sistemas Operativos.*Apache/i, 'B4-T1.3'],
  [/Administraci[oó]n de Sistemas Operativos.*Ansible/i, 'B4-T1.4'],
  [/Administraci[oó]n de Sistemas Operativos.*SaltStack/i, 'B4-T1.5'],
  [/Administraci[oó]n de Sistemas Operativos/i, 'B4-T1.1'],
];
const idDe = t => (IDS.find(([re]) => re.test(t)) || [])[1];

const tabla = f => {  // solo la primera tabla contigua del archivo
  const t = [];
  for (const l of fs.readFileSync(path.join(dir, f), 'utf8').split(/\r?\n/)) {
    if (l.trim().startsWith('|')) t.push(l); else if (t.length) break;
  }
  return t;
};
const filas = f => tabla(f).slice(2)
  .map(l => l.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
const iso = s => (/\d{4}-\d{2}-\d{2}/.exec(s || '') || [null])[0];

// Puntos flojos: última línea "Puntos flojos: ..." de la sección del tema en _repasos.md
const md = fs.readFileSync(path.join(dir, '_repasos.md'), 'utf8');
const secciones = md.split(/^### /m).slice(1).map(s => ({ cab: s.split(/\r?\n/)[0], cuerpo: s }));
const flojosDe = titulo => {
  const clave = titulo.slice(0, 28).toLowerCase();
  const s = secciones.find(x => x.cab.toLowerCase().includes(clave));
  if (!s) return '';
  const m = [...s.cuerpo.matchAll(/^Puntos flojos:\s*(.+)$/gim)].pop();
  return m ? m[1].trim() : '';
};

const docs = [];
const aviso = [];
for (const c of filas('_repasos.md')) {
  const [titulo, bloque, inicio, fase, ultimo, proximo, ac, fa, racha] = c;
  const id = idDe(titulo);
  if (!id) { aviso.push(`Tema sin id: ${titulo}`); continue; }
  docs.push({ col: 'opos_repasos', id, data: {
    tema: id, titulo, bloque: Number(bloque), fase, inicio: iso(inicio), ultimo: iso(ultimo), proximo: iso(proximo),
    aciertos: Number(ac) || 0, fallos: Number(fa) || 0, racha: Number(racha) || 0, flojos: flojosDe(titulo),
  } });
}
const cuenta = {};
for (const c of filas('_dudas.md')) {
  const [fecha, titulo, bloque, duda, resuelta] = c;
  const id = idDe(titulo);
  if (!id) { aviso.push(`Duda sin id de tema: ${titulo}`); continue; }
  const k = `${id}_${fecha}`; cuenta[k] = (cuenta[k] || 0) + 1;
  const fr = /(\d{4}-\d{2}-\d{2})/.exec(resuelta || '');
  docs.push({ col: 'opos_dudas', id: `${k}_${String(cuenta[k]).padStart(2, '0')}`, data: {
    tema: id, titulo, bloque: Number(/\d+/.exec(bloque)?.[0]) || 0, fecha, duda,
    resuelta: /^s[ií]/i.test(resuelta || ''), fechaResuelta: fr ? fr[1] : null,
  } });
}
docs.push({ col: 'opos_meta', id: 'sync', data: { fecha: hoy, ts: Date.now() } });

const writes = [];
for (const d of docs) {
  const carpeta = path.join(out, d.col.replace('opos_', ''));
  fs.mkdirSync(carpeta, { recursive: true });
  const fp = path.join(carpeta, d.id + '.json');
  fs.writeFileSync(fp, JSON.stringify(d.data, null, 1));
  writes.push({ op: 'set', collection: d.col, doc_id: d.id, file_path: fp });
}
fs.writeFileSync(path.join(out, 'writes.json'), JSON.stringify(writes, null, 1));
console.log(`${docs.length} documentos en ${out}`);
for (const a of aviso) console.log('AVISO:', a);
