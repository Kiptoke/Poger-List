<script setup>
	import user_list from "../../assets/json/users.json";

	const route = useRoute();
	const route_name = route.params.name;

	let users = user_list["users"];
	let poges = [];

	for (const user of users) {
		if (user.user == route_name){
			poges = user.poges
		}
	}
</script>

<template>
		<section>
			<h1>{{ route.params.name }}</h1>
			<div v-for="pog in poges">
				<p><h4>{{ pog.name }}</h4></p>
				<ul v-for="song in pog.songs">
					<li>{{ song.name }} - {{ song.artist.join(', ') }}</li>
				</ul>
			</div>
		</section>
</template>