#!/bin/bash

# exit at first error
set -e

TEMPLATES=("utc-article" "utc-beamer" "utc-report")

# Clean old zips
rm -f utc-*-overleaf.zip utc-latex.zip

# Create Overleaf zips
for template in "${TEMPLATES[@]}"; do
  zipname="${template}-overleaf.zip"
  echo "Creating $zipname..."

  mkdir -p tmp-overleaf
  cp "${template}/main.tex" tmp-overleaf/
  cp -r "${template}" tmp-overleaf/
  cp -r utc-common tmp-overleaf/

  (cd tmp-overleaf && zip -r "../$zipname" .)

  rm -rf tmp-overleaf
done

# Create global zip
echo "Creating utc-latex.zip..."

mkdir -p tmp-global
for template in "${TEMPLATES[@]}"; do
  mkdir -p "tmp-global/${template}"
  find "${template}" -type f ! -name 'main.tex' -exec cp --parents {} tmp-global/ \;
done

cp -r utc-common tmp-global/

(cd tmp-global && zip -r ../utc-latex.zip .)

rm -rf tmp-global

echo "All archives created."
