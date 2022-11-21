<template>
  <div style="overflow-x: hidden" id="app">
    <HeaderHome></HeaderHome>
    <router-view />
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
.carousel-3d-slider {
  display: flex !important;
  justify-content: center !important;
  height: 112px !important;
}
.carousel-3d-slide {
  width: 80px !important;
  height: 110px !important;
  transition: transform 500ms ease 0s, opacity 500ms ease 0s, visibility 500ms ease 0s !important;
  border-radius: 10px !important;
}
.right-1 {
  transform: translateX(80px) translateZ(-400px) rotateY(-35deg) !important;
  opacity: 0.7 !important;
}
.left-1 {
  transform: translateX(-80px) translateZ(-400px) rotateY(35deg) !important;
  opacity: 0.7 !important;
}
.carousel-3d-container {
  height: 120px !important;
  margin-bottom: 0 !important;
}
</style>
