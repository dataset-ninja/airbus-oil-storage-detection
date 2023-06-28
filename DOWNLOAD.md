Dataset **Airbus Oil Storage Detection** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/p/J/os/U4ZTmdkAso2NA9b5k2Mp7vrw35CgDgHEqslTLtzMuELs1Xzy1RvJo6sV3JeayWeFO9BCkGHx2JOPu6PEclGz3ISAUTruFMXo9BrZ2BCfoLqCx0grgj44uFGYtSmB.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Airbus Oil Storage Detection', dst_path='~/dtools/datasets/Airbus Oil Storage Detection.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/airbusgeo/airbus-oil-storage-detection-dataset/download?datasetVersionNumber=1)