<template>
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"/>
  </head>
  <router-link :to="{ name: 'BackendView' }">Admin View</router-link>
  <div class="container">
    <div class="row" style="background-color:rgb(230, 255, 245)">
      <div class="col-8">
        <MassageList/>
      </div>
      <div class="col-1" style="background-color: white;"/>
      <div class="col-3">
        <MasseurList/>
      </div>
    </div>
  </div>
</template>
  
  <script>
import MassageList from '@/components/MassageList.vue'
import MasseurList from '@/components/MasseurList.vue'
  
export default {
    name: 'HomeView',
    components: {
    MassageList,
    MasseurList
    }
}
</script>
  
<style scoped>
  html {
  background-color: green;
  font-family: system-ui;
  -webkit-font-smoothing: antialiased;
  padding: 20px 0;
}
</style>
  