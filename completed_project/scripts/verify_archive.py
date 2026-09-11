#!/usr/bin/env python3
"""Verify repository files and optional downloaded release assets; Python 3.8+."""
import csv, gzip, hashlib, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
release_dir=Path(sys.argv[1]) if len(sys.argv)>1 else root/'release-assets'
def digest(path):
 with path.open('rb') as f:
  h=hashlib.sha256()
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
  return h.hexdigest()
count=0;skipped=[]
with (root/'metadata/CHECKSUMS.csv').open(newline='') as f:
 for row in csv.DictReader(f):
  path=root/row['path'];assert path.is_file(),row['path']
  assert path.stat().st_size==int(row['bytes']),row['path']
  assert digest(path)==row['sha256'],row['path'];count+=1
with (root/'metadata/SOURCE_MANIFEST.csv').open(newline='') as f:
 for row in csv.DictReader(f):
  path=root/row['path']
  if row['storage']=='release_asset':
   path=release_dir/Path(row['path']).name
   if not path.exists():skipped.append(row['release_url']);continue
  assert digest(path)==row['stored_sha256'],row['path']
  if row['storage']=='gzip_original':
   h=hashlib.sha256()
   with gzip.open(path,'rb') as f:
    for block in iter(lambda:f.read(1048576),b''):h.update(block)
   assert h.hexdigest()==row['source_sha256'],row['path']
  else:assert digest(path)==row['source_sha256'],row['path']
print(f'PASS: {count} repository files; source-copy checks passed.')
if skipped:
 print('Release asset not checked: download it and pass its containing directory:')
 print('\n'.join(skipped))
else:print('All archived source payloads verified, including any release assets.')
