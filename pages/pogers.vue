<script setup>
	import file from "../assets/json/playlists.json";

	let playlists = file['playlists']
	
	function imageURL(input) {
		return `../assets/pogers/${input.name}.jpeg`
	}
</script>

<template>
	<section class="_margin-left:5 _margin-right:5 _margin-top:2">
		<h1>Pogers</h1>
		<div v-for="pl in playlists">
			<IMedia>
				<template #image>
					<nuxt-img
						src="test.jpg"
						height="80"
						width="80"
						alt="album name"
					/>
				</template>
				<h3>{{ pl.name }}</h3>
			</IMedia>
		</div>
	</section>
</template>