# Poger List

[![Netlify Status](https://api.netlify.com/api/v1/badges/d1ce4ae6-2a8f-4789-aad9-cee4c8dff49c/deploy-status)](https://app.netlify.com/sites/poger-archive/deploys)

A list of every song ever posted as a part of Poger.

## How to Build Locally

```bash
npm run dev
```
Then, check [localhost:3000](http://localhost:3000/).

## How to Update the Poger List

First, update `constants.py` with the ID of the most recent Poger. The ID of a Spotify playlist can be found by right clicking on the playlist and going to `Share > Copy link to playlist`. This URL takes the form:

`https://open.spotify.com/playlist/<playlist_id>?<other_information?>`

You can delete everything except the `playlist_id`. Please also add a comment to the side with the name of the Poger.

After that, run this command

```bash
python3 ./python/update_poge.py
```

You should then see output that looks like this: `rhythmy is poger (31 songs) processed`. If you're seeing an error, most likely you don't have the **environment variables** needed to run `update_poge`. Message Andrew if you need this file.

After running that, reload the Poger list. It should contain all the new songs. Finish the process by committing the new constants file to Git.
