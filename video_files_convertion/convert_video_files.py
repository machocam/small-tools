from pathlib import Path
from subprocess import call


## Insert all files that I want to convert into an array
convert_these=[]
convert_these = list(Path("/media/mixcocam/Samsung_T5/unorganized_footage/").rglob('*.VOB'))



for item in convert_these:
	input_file = item.absolute()
	output_file = item.rename(item.with_suffix('.mp4').absolute())
	call(['ffmpeg', '-i', input_file, output_file])
	




		
