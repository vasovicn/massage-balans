<template>
  <div style="overflow-x: hidden;" id="app">
    <HeaderHome></HeaderHome>
    <router-view/>
    <FooterHome></FooterHome>
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
import FooterHome from './components/FooterHome.vue'

export default {
  name: 'App',
  components: {
    HeaderHome,
    FooterHome
  }
}
</script>

<style>
</style>
