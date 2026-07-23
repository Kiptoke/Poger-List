<script setup lang="ts">
  const {data: poges} = await useAsyncData('poges', () => { return queryCollection('pogers').order('index','ASC').all()})
</script>

<template>
  <div v-if="poges">
    <div v-for="pog in poges" :key="pog.id">
      <PogerTable :name="pog.name" :desc="pog.description" :file="pog.file_name" :id="pog.plid"></PogerTable>
    </div>
  </div>
</template>
