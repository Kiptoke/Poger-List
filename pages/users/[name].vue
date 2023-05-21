<script setup>
	const user_list = await import("../../content/json/users.json");

	const route = useRoute();
	const route_name = route.params.name;

	let users = user_list["users"];
	let poges = [];

	for (const user of users) {
		if (user.user == route_name){
			poges = user.poges
		}
	}

	function getImage()
	{
		return new URL(`../../content/heads/${route.params.name.toLowerCase()}.png`, import.meta.url)
	}
</script>

<template>
	<section class="_margin-left:5 _margin-right:5 _margin-top:2">
		<IMedia class="_margin-bottom:1!">
			<template #image>
				<img
					:src="getImage()"
					height="80"
					width="80"
					alt="Media Image"
				/>
			</template>
			<h1>{{ route.params.name }}</h1>
			<p>
				{{ route.params.name }} has participated in {{ poges.length }} pogers.
			</p>
		</IMedia>
		<div v-for="pog in poges">
			<h4>{{ pog.name }}</h4>
			<ITable condensed striped hover responsive>
				<thead>
					<tr>
						<th>Song Name</th>
						<th>Artists</th>
						<th>Album</th>
						<th>Song Length</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="song in pog.songs">
						<td>{{ song.name }}</td>
						<td>{{ song.artist.join(', ') }}</td>
						<td>{{ song.album }}</td>
						<td>{{ song.length }}</td>
					</tr>
				</tbody>
			</ITable>
		</div>
	</section>
</template>