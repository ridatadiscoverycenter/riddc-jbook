![example workflow](https://github.com/ridatadiscoverycenter/riddc-jbook/actions/workflows/firebase-hosting-merge.yml/badge.svg)

# Rhode Island Data Discovery Center's Jupyter Book

This repository houses the RIDDC's Jupyter Book with articles showcasing projects, analyzes and visualizations created using data from the OSM region.

## Guidelines for RIDDC Articles.

### Article Format
Articles can be written in Markdown or Jupyter Notebook format (`ipynb`).
In both cases, the first block (cell in `ipynb`) should start with a title in Markdown followed by the authors' names.

If the article is divided in sections, use h2 `(##)` headers for section titles. This will help Jupyter Book to create a table of contents on the right sidebar.
Do not use `#` before a regular paragraph.

For images, use Markdown syntax with caption, in addition add the caption as a blockquote.

If your notebook was created in Colab, make sure you remove the first cell with the `Open in Colab` badge.

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
- When you're happy with the changes, open a pull request to this 
repository. Once approved, an admin member will merge into `main` and the changes will be auto-deployed.

## Usage

### Install system dependencies
- On Mac: download Homebrew and install with `brew bundle`
  * with the Mac M1 chip, run `export HDF5_DIR=/opt/homebrew/opt/hdf5`
- On Windows:
  * first download HDF5 from source: `https://support.hdfgroup.org/ftp/HDF5/current/bin/`
  * download Chocolatey and install with `choco install packages.config`

If you'd like to develop on and build the riddc book, you should:

- Clone this repository
- `cd` to the repository
- Use [asdf](https://asdf-vm.com) or [pyenv](https://github.com/pyenv/pyenv) to install the current version of Python supported by Google Colab (as of February, 2023, the version in Colab was 3.8.10)
- In the local repo, `asdf local python 3.8.10` or `pyenv local 3.8.10`
  * sets the python version for the repo
- Start a virtual environment: 
  * find the path to the desired python version with `pyenv which python3.8` or `asdf which python3.8`
  * copy the path and then `virtualenv -p <path> jbook3.8`
    * in this case, the name of the ve is `jbook3.8` 
- Activate the environment with `source jbook3.8/bin/activate`
- Verify that the python version inside the ve is correct with `python -V`
  * if it shows a different version, check the path used to create the ve
    * for example: `/Users/tdivoll/.pyenv/versions/python3.8.10/bin/python3.8`
- `pip install -r requirements.txt`



## Build the book
- (Recommended) Remove the existing `riddc/_build/` directory with `rm -rf 
riddc/_build/`
- Run `jupyter-book build riddc/`
- **Note:** On Mac, you may need to make the following soft link for the book to build: `ln -s /opt/homebrew/share/jupyter/nbconvert ~/Library/Jupyter`

A fully-rendered HTML version of the book will be built in `riddc/_build/html/`.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/fernandogelin/riddc/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
