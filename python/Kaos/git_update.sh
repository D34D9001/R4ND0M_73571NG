#!/usr/bin/bash

## THIS FILE IS ONLY USED TO UPDATE THE DEVELOPMENT VERSION OF KAOS
## THIS FILE IS NOT TO BE RELEASED WITH THE PRODUCTION VERSION

# Copy data from /usr/lib/kaos to Developnent
cp -rv /home/$USER/Kaos_Dev/* /usr/lib/kaos/
# Add to git commit
# git add -A
# # Commit updates to git
# git commit -m "Update"
# # Push updates to repo
# git push origin
