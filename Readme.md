## Beige Books Refactor Repo

Basic structure is as follows:
* All static data files go in a data/ folder.
* All walkthrough .ipynb files go in the notebooks/ folder divided up by essay. A readme file in each notebooks folder explains each notebook's purpose.
* All figures/tables in the assets/ folder
* Build modules within your notebook so it is reusable. I'm adding a few modules as guides to get started. (process = do all your data processing, models = do all your data modeling). These are just starting modules, don't feel tied to them exactly or names.

### Other recommendations
* You will need to adjust paths. Use the append path in notebook files for instance like this

```python
import os

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
path_to_append = os.path.join(parent_directory, 'my_folder')

print("Appended Path:", path_to_append)
```

