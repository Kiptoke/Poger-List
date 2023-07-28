<script setup>
	import pl_file from '../content/json/playlists.json';
	
	const playlists = reactive([]);
	let data = [];
	let counter = 0;
	
	// Javascript state can go die for all I care
	pl_file['playlists'].forEach(async (value) => {
		var playlist = await import(`../content/json/playlists/${value}.json`);
		data.push(playlist);
		counter++;
		if(counter === pl_file['playlists'].length) {
			callback()
		}
	});

	function callback() {
		console.log(data);
		playlists.push(...data);
		console.log(playlists);
	}

	let user_table = {
		'h9wxnd3xvrfdfjv7r9p3ihz68' : 'kaavya', 
		'315qfzr3gmd5m4mkjoprzwsny7cq' : 'musa', 
		'31fhaf5kxu7r4p3fr5r2klb5d23a' : 'andrew', 
		'31d6s5qq4uxpm6ucmue2p3ykb37q' : 'natasha', 
		'31giifsv5jaavljfciuappzifs3u' : 'naveen', 
		'blackupblackup5' : 'aman', 
		'kush_p' : 'kushal', 
		'je1mzixeidgq3qxp5v10r4iih' : 'faiyaz', 
		'rennylop': 'renny',
		'freezercune': 'billy',
		'lwbl3eraki1c231y7yp06f7mn': 'val'
	}

	function imageURL(input) {
		if (input.name == "pogern't") {
			return new URL(`../content/pogers/pogernt.jpg`, import.meta.url);
		}
		return new URL(`../content/pogers/${input.name}.jpg`, import.meta.url);
	}

	function dateAdded(input) {
		let time = Date.parse(input.tracks.items[0].added_at);
		let date = new Date(time);

		return date.toLocaleDateString("en-US", { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
	}

	function getUser(input) {
		return user_table[input];
	}

	function getHead(input) {
		return new URL(`../content/heads/${user_table[input]}.png`, import.meta.url);
	}

	function getArtists(artists) {
		let artist_list = [];
		for (const art of artists) {
			artist_list.push(art.name);
		}
		return artist_list;
	}
</script>

<template>
	<section class="_margin-left:5 _margin-right:5 _margin-top:2">
		<h1>Pogers</h1>
		<div v-for="pl in playlists">
			<IMedia class="_margin-top:1  _margin-bottom:1">
				<template #image>
					<img
						:src="imageURL(pl)"
						style="
						width: 80px; /*any size*/
						height: 80px; /*any size*/
						object-fit: cover; /* Do not scale the image */
  						object-position: center; /* Center the image within the element */
						"
					/>
				</template>
				<h2>{{ pl.name }}</h2>
				<p>{{ dateAdded(pl) }}</p>
			</IMedia>
			<ITable hover>
				<thead>
					<tr>
						<th>Song Name</th>
						<th>Artists</th>
						<th>Album</th>
						<th>Added By</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="song in pl.tracks.items">
						<td>{{ song.track.name }}</td>
						<td>{{ getArtists(song.track.artists).join(', ') }}</td>
						<td>{{ song.track.album.name }}</td>
						<td style="text-transform: capitalize">
							<img
								:src="getHead(song.added_by.id)"
								style="
								width: 30px;
								height: 30px;
								object-fit: scale-down; 
								"
								class="_margin-right:1/2"
							/>
							{{ getUser(song.added_by.id) }}
						</td>
					</tr>
				</tbody>
			</ITable>
		</div>
	</section>
</template>