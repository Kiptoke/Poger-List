<script setup lang="ts">
  const props = defineProps(['name', 'desc', 'file', 'id'])
  const playlistPath = computed(() => {
    return `playlists/data/${props.file}`
  })
  const { data: playlist, status } = await useAsyncData(
    () => `playlist-${props.id}-${props.file}`,
    () => queryCollection('playlists').where('id', '=', playlistPath.value).first(),
    { watch: [playlistPath] } // Re-run if the file changes
  )

  const columns = [
    {
      title: 'Song Title',
      dataIndex: 'title',
      key: 'title',
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    },
  ]

  const dataSource = [
    {
      key: '1',
      name: 'Mike',
      age: 32,
      address: '10 Downing Street',
    },
    {
      key: '2',
      name: 'John',
      age: 42,
      address: '10 Downing Street',
    },
  ]
</script>

<template>
  <div v-if="playlist">
    <a-typography>
      <a-typography-title :level="2">{{ props.name }}</a-typography-title>
      <a-typography-paragraph type="secondary">{{ props.desc }}</a-typography-paragraph>
    </a-typography>
    <ul>
      <li v-for="(song, index) in playlist.body" :key="index">
        <p>{{ song.song }}</p>
      </li>
    </ul>
  </div>
  
  <div v-else-if="status === 'pending'">
    Loading {{ props.name }}...
  </div>
  
  <div v-else>
    <p>Could not find playlist at: {{ playlistPath }}</p>
  </div>
</template>