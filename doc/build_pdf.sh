docker run --rm -v "$(pwd):/data" -u "$(id -u)" pandocscholar/alpine
cp out.pdf scientific_tagger.pdf
cp out.latex scientific_tagger.tex
