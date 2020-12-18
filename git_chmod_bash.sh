# Trova tutti i file sh e li rende eseguibili per git
find . -type f -iname "*.sh" -exec git update-index --chmod=+x {} \;