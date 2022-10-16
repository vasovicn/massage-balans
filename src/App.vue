<template>
  <div id="app">
    <HeaderHome></HeaderHome>
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
import HeaderHome from './components/HeaderHome.vue'

export default {
  name: 'App',
  components: {
    HeaderHome
  }
}
</script>

<style>
</style>
