Dataset **Airbus Oil Storage Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/L/E/vn/5eJO6O7v2pEfP7i82jwhFcXSJtftEXzSninylSPsEmeagGds1UBEksnj7Obbv5yuCgk3DyE8ZlioVNPEc6w5CPLBCdoo3WfVq9ygFTj6B6ct48vPEk32aest6Ufg.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Airbus Oil Storage Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/airbusgeo/airbus-oil-storage-detection-dataset/download?datasetVersionNumber=1).