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

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

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
