from pathlib import Path
from subprocess import run


## Insert all files that I want to convert into an array
convert_these=[]
convert_these = list(Path("/media/mixcocam/Samsung_T5/unorganized_footage/").rglob('*.mp4'))



for item in convert_these:
	input_file = item.absolute()
	output_file = item.rename(item.with_suffix('.mp4').absolute())
	run(['/bin/ffmpeg', '-i', input_file, output_file], shell=True)
	pass

	




		
