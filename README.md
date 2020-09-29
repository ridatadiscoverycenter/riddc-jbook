# Rhode Island Data Discovery Center's Jupyter Book

This repository houses the RIDDC's Jupyter Book with articles showcasing projects, analyzes and visualizations created using data from the OSM region.

## Guidelines for RIDDC Articles.

### Article Format
Articles can be written in Markdown or Jupyter Notebook format (`ipynb`).
In both cases, the first block (cell in `ipynb`) should start with a title in Markdown followed by the authors' names.

If the article is divided in sections, use h2 `(##)` headers for section titles. This will help Jupyter Book to create a table of contents on the right sidebar.
Do not use `#` before a regular paragraph.

For images, use Markdown syntax with caption, in addition add the caption as a blockquote.

If your notebooke was created in Colab, make sure you remove the first cell with the `Open in Colab` badge. Jupyter Book already has options to open the notebook in other platforms.

Example:
```md
# Title
> by Jane Doe
> jane@brown.edu 

## Section Header

Paragrah text...

![image](path/to/image.png "Caption for image")
> Caption for image (repeat)

```
### Jupyter Book Docs

Please, review the [Jupyter Book Documentation](https://jupyterbook.org/) before writing new content. They provide a lot of information on how to organize and write content for Jupyter Books.

### How to add new notebooks

To add new notebooks to RIDDC follow these steps:

- Fork this repository
- Add new notebooks or Markdown formatted articles to the directory `riddc/notebooks`
- Add an entry to the file `riddc/_toc.yml` pointing to the notebook(s) you added. Feel free to create a section ([refer to the jupyter book documentation](https://jupyterbook.org/))
- Build the Jupyter Book locally (see bellow).
- Commit and push your changes.
- When you're happy wiht the changes, open a pull request to this repository. Once approved, an admin member will merge into `main` and the changes will be auto-deployed.

## Usage

### Building the book

If you'd like to develop on and build the riddc book, you should:

- Clone this repository and run
- Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
- (Recommended) Remove the existing `riddc/_build/` directory
- Run `jupyter-book build riddc/`

A fully-rendered HTML version of the book will be built in `riddc/_build/html/`.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/fernandogelin/riddc/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
