### Original document: https://github.com/wkentaro/labelme

---

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

_enhanced by locpnh_

## Installation

1. You need install [Anaconda](https://docs.anaconda.com/anaconda/install/), then run below:

```bash
# Setup conda
conda create --name labelme
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
