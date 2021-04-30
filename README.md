# Scientific tagger

![Build](https://github.com/dataesr/scientific_tagger/actions/workflows/build.yml/badge.svg)

The scientific taggers aims at proposing subject classification for scholarly publications. So the input is a list of publications, only some metadata are taken into account (title, journal title, abstract,keywords and MeSH), not the full-text for the time being. Several classifications are implemented:
- Biomedical subject classification based on Fields of Research [documented here](https://github.com/dataesr/scientific_tagger/blob/main/doc/scientific_tagger.pdf). The results can be reproduced with this [Jupyter notebook](https://github.com/dataesr/scientific_tagger/blob/main/notebooks/Article_Table_Figures.ipynb)
- Pascal and Francis tags
- Sustainable Development Goals (SDG) from UN, based on [Dataset of search queries to map scientific publications to the UN sustainable development goals, Bordignon, 2021](https://doi.org/10.1016/j.dib.2021.106731)

## Run it locally
```shell
git clone git@github.com:dataesr/scientific-tagger.git
cd scientific-tagger
docker-compose pull && docker-compose up
```

In your browser, you now have :
- scientific-tagger : http://localhost:5004/

## Deploy it on kubernetes
```shell
kubectl apply -k k8s
```

## Release
It uses [semver](https://semver.org/).

To create a new release, do
```shell
make release VERSION=x.x.x
```
