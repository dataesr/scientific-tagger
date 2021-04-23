docker run --rm -v "$(pwd):/data" -u "$(id -u)" pandocscholar/alpine
cp out.pdf scientific_tagger.pdf
