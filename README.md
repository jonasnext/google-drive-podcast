# google-drive-podcast

[![open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jonasnext/google-drive-podcast/blob/main/untitled.ipynb) [![code style—black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Requirements: Google Account

This [`Google Colab`](https://colab.research.google.com) notebook makes a **simple & minimal** podcast in [Google Drive](https://drive.google.com). Run the notebook from top to bottom to make the `podcast.rss` file, and get the url at the end of the notebook, to enter in your podcast app.

You can configure *these options* **in the notebook**:

```
title = "_"
author = "_"
description = "_"
imageURL = "https://octodex.github.com/images/original.png"
link = "https://www.google.com"
copyright = "Copyright © 2020 X. All rights reserved"
```

```
directory = "podcast"
```

By default, the notebook makes one directory in `Google Drive`–`My Drive`/`${directory}`, where you can upload the audio files using the notebook, or using the web browser UI in [Google Drive](https://drive.google.com) in the directory that's defined in the notebook.

The podcast will include all audio files in the `My Drive`/`${directory}` folder and save the podcast file in the same directory, named as `podcast.rss`.

At the top of the notebook, [`Google Colab`](https://colab.research.google.com) requests access to your [Google Drive](https://drive.google.com) to copy the audio files, and the podcast file to `My Drive`/`${directory}`. The notebook also needs to read the audio files in the `My Drive`/`${directory}` folder to make the podcast file.

To allow the [`Google Colab`](https://colab.research.google.com) notebook access to your [Google Drive](https://drive.google.com), go to the Google URL in the notebook after running it, and enter the auth code.

by [jonasnext](https://github.com/jonasnext)
