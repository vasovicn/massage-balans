<template>
  <div id="app">
    <router-view />
  </div>
</template>

<!-- <template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'EventList' }">Events</router-link> |
      <router-link :to="{ name: 'About' }">About</router-link>
       |
      <router-link :to="{ name: 'EventCreate' }">Create Event</router-link>
    </div>
    <router-view />
  </div>
</template> -->

<script>

export default {
  name: 'App',
}
</script>

<style>

</style>
