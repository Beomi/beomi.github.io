from glob import glob
import shutil

files = glob('_posts/*.md')

for path in files:
	f = open(path).read()
	if 'published: false' in f:
		filename = path.split('/')
		to_dir = f'_drafts/{filename}'
		shutil.move(path, to_dir)
