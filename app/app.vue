<template>
  <UApp>
    <UHeader title="All of Poger" :toggle="false"/>
    <UMain>
      <NuxtLayout>
        <NuxtPage/>
      </NuxtLayout>
    </UMain>
    <UFooter>
      <template #left>
        <p class="text-muted text-sm">Made lovingly by Andrew Zhou, a human.</p>
      </template>
    </UFooter>
  </UApp>
</template>
