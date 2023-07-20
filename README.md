# File sorter
File Sorter is a Python program designed to help you organize files in a directory by sorting them into predefined folders based on their file extensions. Additionally, it can rename files written in Cyrillic to their corresponding Latin representation, ensuring a consistent naming convention across your files.

<h3>Features</h3>  

1. **Cyrillic to Latin Translation**: Converts filenames from Cyrillic to Latin for easy readability and access.
1. **Automatic Folder Creation**: Creates predefined folders (if they don't already exist) such as 'images', 'video', 'documents', 'audio', and 'archives' to sort your files.
1. **File Movement**: Automatically moves files to the appropriate folders based on their extensions.
1. **Archive Handling**: Unpacks archives (.zip, .gz, .tar) and moves the unpacked contents to the 'archives' folder.
1. **Cleanup**: Deletes all empty folders, ensuring a clean directory structure.

<h3>How to Use</h3>
  
**1. Clone the Repository:**
```
git clone [repository-url]
cd [repository-folder]
```
**2. Run the Script:**
```
python [script-name].py [directory-path]
```
Replace `[script-name].py` with the name of the Python script, and `[directory-path]` with the path to the directory you want to sort.

**3. Observe the Results:** Check the provided directory, and you'll see the files sorted into their respective folders.

<h3>Requirements</h3>

- Python 3.x  
+ shutil module (standard library)  
* os module (standard library)  
- sys module (standard library)  
<h3>Considerations</h3>

- It's recommended to backup your data before running the script to prevent any unintentional data loss.
+ Currently, the script recognizes specific file extensions for sorting. If you have files with different extensions, you might need to modify the script accordingly.
+ Recognized file extensions:
    + images - 'JPEG', 'PNG', 'JPG', 'SVG'
    + video - 'AVI', 'MP4', 'MOV', 'MKV'
    + documents - 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'
    + audio - 'MP3', 'OGG', 'WAV', 'AMR'
    + archives - 'ZIP', 'GZ', 'TAR'  
    + File with any other extension will not be moved.
