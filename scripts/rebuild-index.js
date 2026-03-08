// scripts/rebuild-index.js
// 掃描所有 _notes/*.md，重建 Fuse.js 搜尋索引 search-index.json
// 使用方式：node scripts/rebuild-index.js

const fs = require('fs');
const path = require('path');

const NOTES_DIR = '_notes';
const OUTPUT_FILE = 'search-index.json';

function parseFrontMatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return { meta: {}, body: content };

  const meta = {};
  const lines = match[1].split('\n');

  for (const line of lines) {
    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) continue;

    const key = line.slice(0, colonIdx).trim();
    let value = line.slice(colonIdx + 1).trim();

    // 處理陣列格式 [a, b, c]
    if (value.startsWith('[') && value.endsWith(']')) {
      value = value.slice(1, -1).split(',').map(v =>
        v.trim().replace(/^['"]|['"]$/g, '')
      ).filter(Boolean);
    } else {
      // 移除引號
      value = value.replace(/^['"]|['"]$/g, '');
      // 布林值
      if (value === 'true') value = true;
      if (value === 'false') value = false;
    }

    meta[key] = value;
  }

  const body = content.slice(match[0].length).trim();
  return { meta, body };
}

function buildIndex() {
  if (!fs.existsSync(NOTES_DIR)) {
    console.log(`找不到 ${NOTES_DIR} 目錄`);
    process.exit(1);
  }

  const files = fs.readdirSync(NOTES_DIR).filter(f => f.endsWith('.md'));
  const index = [];

  for (const file of files) {
    const content = fs.readFileSync(path.join(NOTES_DIR, file), 'utf-8');
    const { meta, body } = parseFrontMatter(content);

    if (!meta.title) continue;

    // 從正文提取純文字（移除 Markdown 符號）
    const plainBody = body
      .replace(/#{1,6}\s/g, '')
      .replace(/[*_`>•]/g, '')
      .replace(/\[\d+:\d+\]/g, '')
      .replace(/\n+/g, ' ')
      .trim()
      .slice(0, 500);

    index.push({
      id: file.replace('.md', ''),
      title: meta.title || '',
      category: meta.category || '',
      tags: Array.isArray(meta.tags) ? meta.tags : [],
      description: meta.description || '',
      quote: meta.quote || '',
      action: meta.action || '',
      image: meta.image || '',
      date: meta.date || '',
      source_has_timestamps: meta.source_has_timestamps || false,
      body: plainBody,
      url: `/notes/${file.replace('.md', '')}`
    });
  }

  // 依日期排序（最新在前）
  index.sort((a, b) => (b.date > a.date ? 1 : -1));

  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(index, null, 2), 'utf-8');
  console.log(`✅ 搜尋索引已更新：${index.length} 筆記記錄 → ${OUTPUT_FILE}`);

  // 統計各分類數量
  const categories = {};
  for (const item of index) {
    categories[item.category] = (categories[item.category] || 0) + 1;
  }
  console.log('\n📊 分類統計：');
  for (const [cat, count] of Object.entries(categories)) {
    console.log(`   ${cat}: ${count} 筆`);
  }
}

buildIndex();
