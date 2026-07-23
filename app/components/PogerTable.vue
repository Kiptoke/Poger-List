<script setup lang="ts">
  // Fetch Data
  const props = defineProps(['name', 'desc', 'file', 'id'])
  const playlistPath = computed(() => {
    return `playlists/data/${props.file}`
  })
  const { data: playlist, status } = await useAsyncData(
    () => `playlist-${props.id}-${props.file}`,
    () => queryCollection('playlists').where('id', '=', playlistPath.value).first(),
    { watch: [playlistPath] } // Re-run if the file changes
  )

  const source = computed(() => {
    return playlist.value?.body.map((pls) => ({
      title: pls.song,
      artist: pls.artist,
      album: pls.album,
      stuwant: pls.stuwant,
      duration: pls.duration
    })) || []
  })
  
</script>

<template>
  <UPageCard v-if="playlist" :title="props.name" :description="props.desc">
    <UTable :data="source"/>
  </UPageCard>
  
  <div v-else-if="status === 'pending'">
    Loading {{ props.name }}...
  </div>
  
  <div v-else>
    <p>Could not find playlist at: {{ playlistPath }}</p>
  </div>
</template>