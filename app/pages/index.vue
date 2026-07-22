<script setup lang="ts">
  const {data: poges} = await useAsyncData('poges', () => { return queryCollection('pogers').order('index','ASC').all()})
  const {data: playlists} = await useAsyncData('playlists', () => { return queryCollection('playlists').all()})
</script>

<template>
  <div>
    <h1>All of Poger</h1>
    <ul>
      <li v-for="pog in poges" :key="pog.id"><p>{{ pog.name }}</p></li>
    </ul>
  </div>
</template>
