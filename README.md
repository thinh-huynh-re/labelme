### Original document: https://github.com/locpnh1995/labelme

## New Features

- [x] hold **Space** and **LeftClick** to drag the image
- [x] display **Value** of segmentation when hovered
- [x] edit **Value** by **RightClick-->Edit Value** (**Ctrl+G**)
- [x] NOT save with image data by default
- [x] display **Value** widget on right column

- [x] hold **Space** and **LeftClick** to drag the image
- [x] display **Value** of segmentation when hovered
- [x] edit **Value** by **RightClick-->Edit Value** (**Ctrl+G**)
- [x] NOT save with image data by default
      <br/>
      <br/>
- [x] press **Space** to hidden the selected polygon.
      <br/>
      <br/>
- [x] **Convert** Rectangle <--> Polygon in Right Click menu (**Ctrl+T**).

_enhanced by locpnh_

### Notice

Remove **.labelmerc** file to apply the new keyboard shortcuts
`rm ~/.labelmerc`

## Installation

- Tested on Ubuntu 22.04

1. You need install [Anaconda](https://docs.anaconda.com/anaconda/install/), then run below:

```bash
# Setup conda
conda create --name labelme python=3.8
conda activate labelme
```

2. Download or Clone [locpnh1995/labelme](https://github.com/locpnh1995/labelme/) source code.
3. Change directory to **labelme** folder, then run:

```bash
# Uninstall the old version
pip uninstall labelme

# Install the new version
pip install -e .
```

4. Type `labelme` on Terminal to open GUI.

5. If counter error `qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.` => Reinstall libxcd `sudo apt-get install --reinstall libxcb-xinerama0`
