<script setup lang="ts">
import type { TableColumn } from '@nuxt/ui';

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

  type Song = {
    title: string,
    artist: string,
    album: string,
    stuwant: string,
    duration: number
  }

  const source = computed<Song[]>(() => {
    return playlist.value?.body.map((pls) => ({
      title: pls.song,
      artist: pls.artist,
      album: pls.album,
      stuwant: pls.stuwant,
      duration: pls.duration
    })) || []
  })

  const columns: TableColumn<Song>[] = [
    {
      accessorKey: 'title',
      header: 'Title',
      cell: ({row}) => `${row.getValue('title')}`,
      meta: {
        class: {
          td: 'w-1/2 whitespace-normal'
        }
      }
    },
    {
      accessorKey: 'artist',
      header: 'Artist',
      cell: ({row}) => `${row.getValue('artist')}`,
      meta: {
        class: {
          td: 'w-1/6 whitespace-normal'
        }
      }
    },
    /*
    {
      accessorKey: 'album',
      header: 'Album',
      cell: ({row}) => `${row.getValue('album')}`,
      meta: {
        class: {
          td: 'w-1/6 whitespace-normal'
        }
      }
    },
    */
    {
      accessorKey: 'stuwant',
      header: 'Stuwant',
      cell: ({row}) => `${stuwant(row.getValue('stuwant')) || row.getValue('stuwant')}`,
      meta: {
        class: {
          th: 'text-center',
          td: 'w-1/6 text-center'
        }
      }
    },
    {
      accessorKey: 'duration',
      header: 'Length',
      cell: ({row}) => `${millConvert(row.getValue('duration'))}`,
      meta: {
        class: {
          th: 'text-center',
          td: 'w-1/6 text-center'
        }
      }
    },
  ]
</script>

<template>
  <UPageCard v-if="playlist" :title="props.name" :description="props.desc">
    <UTable sticky :data="source" :columns="columns" class="container"/>
  </UPageCard>
  
  <div v-else-if="status === 'pending'">
    Loading {{ props.name }}...
  </div>
  
  <div v-else>
    <p>Could not find playlist at: {{ playlistPath }}</p>
  </div>
</template>