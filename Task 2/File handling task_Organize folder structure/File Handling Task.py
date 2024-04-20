import os
import shutil

# Specify the directory containing the files
dir_path = '/Path/to/Directory/'

for filename in os.listdir(dir_path):
    if filename.endswith(".txt"):
        # Extract the language code from the filename
        name, lang_with_extension = filename.rsplit('-', 1)
        lang, extension = lang_with_extension.split('.', 1)
        
        # Create a new directory for this language, if it doesn't exist
        new_dir_path = os.path.join(dir_path, lang)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
        
        # Rename the file
        new_filename = f'{name}.txt'
        
        # Move the file to the new directory
        shutil.move(os.path.join(dir_path, filename), os.path.join(new_dir_path, new_filename))

#Make sure all the files are moved to the new directory
print("Complete!")