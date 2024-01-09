## Beige Books Refactor Repo

Basic structure is as follows:
* All static data files will go in a data/ folder.
* All walkthrough .ipynb files will go in the notebooks/ folder
* Save all figures/tables in the assets/ folder
* Build modules within your notebook so it is reusable. I'm adding a few modules as guides to get started. (process = do all your data processing, models = do all your data modeling). These are just starting modules, don't feel tied to them exactly or names.

### Other recommendations
* Start small, do one file at a time then archive it. 
* Build small functions that are interchangeable and then Class's for larger purposes. 
* Use notebooks to illustrate the process of going through each function or class.
* You will need to adjust paths. Use the append path in notebook files for instance like this

```python
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
path_to_append = os.path.join(parent_directory, 'my_folder')

print("Appended Path:", path_to_append)
```

