export BORG_REPO='/backup/'
# borg init -e none --storage-quota 50G
borg create --exclude='/source/plex/library/Library/Application Support/Plex Media Server/Cache/*' --exclude='*.domains' --exclude='/source/*/downloads/*' --stats ::'{hostname}-{now}' /source
borg prune --keep-hourly 6 --keep-daily 7 --keep-weekly 4
# rsync -avhl --rsh="/usr/bin/sshpass -f /nas-pw ssh -p 22555 -o StrictHostKeyChecking=no" --delete /backup/ majil@192.168.1.20:/volume1/MediaServer/volumes_backup/
