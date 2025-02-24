import { createClient } from "@/utils/supabase/server";

export default async function Table() {
  const moment = require('moment')
  const now = moment().format('dddd, MMMM Do YYYY')
  const supabase = await createClient();
  const { data: songs } = await supabase.from("songs").select();

  interface Artist {
    "artistName": string,
    "artistURL": string
  }

  interface Song {
    "id": number,
    "name": string,
    "artists": Array<Artist>,
    "album": string,
    "albumURL": string,
    "length": number, // in milliseconds!
    "songURL": string,
    "stuwant": string,
    "stuwantURL": string,
    "poger": string,
    "pogerURL": string,
    "numSongs": number,
    "dateAdded": string,
    "songId": string,
    "playlistId": string
  }

  const artistRow = (artistsObject: Array<Artist>) => {
    const artists: Array<string> = [];
    artistsObject.map(a => artists.push(a.artistName))
    return artists.join(', ')
  }

  const lengthRow = (ms: number) => {
    ms %= 3600000;
    const minutes = Math.floor(ms / 60000);
    ms %= 60000;
    const seconds = Math.floor(ms / 1000);
    return `${String(minutes)}:${String(seconds).padStart(2, '0')}`
}

  const songRow = (songObject: Song) => {
    return(
      <tr>
        <th>{songObject.name}</th>
        <td>{artistRow(songObject.artists)}</td>
        <td>{songObject.album}</td>
        <td>{lengthRow(songObject.length)}</td>
        <td>{songObject.stuwant}</td>
        <td>{songObject.poger}</td>
      </tr>
    )
  }

  return (
    <div className="overflow-x-auto">
      <p className="text-2xl mb-5">As of <b className="text-warning">{now}</b>, there have been <b className="text-success">{songs?.length} songs</b> in Poger.</p>
      <table className="table table-xs">
        <thead>
          <tr>
            <th>Name</th>
            <th>Artists</th>
            <th>Album</th>
            <th>Length</th>
            <th>Submitted By</th>
            <th>Poger</th>
          </tr>
        </thead>
        <tbody>
          {songs?.map(songRow)}
        </tbody>
      </table>
    </div>
  );
}
