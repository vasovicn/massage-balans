<template>
    <div class="massage" @click="togleDetails()">
      <h1>{{massage.name}}</h1>
      <MassageDetails v-if="detailsOpen" :massageID="massage.id"/>
    </div>
</template>
  
<script>
  import MassageDetails from '@/components/MassageDetails'

  export default {
    components: {
      MassageDetails
    },
    name: 'MassageCard',
    data () {
      return {
        detailsOpen: false
      }
    },
    props: ['massage'],
    methods: {
      togleDetails() {
        this.detailsOpen = !this.detailsOpen
      }
    }
  }
</script>
<style scoped>
.massage {
  display: flex;
  flex-direction: column;
  align-items: center;
  border:1px solid;
  min-width: 300px;
  max-width: 300px;
  max-height: 300px;
  background-image: url("@/assets/slika_masaze2.jpg");
  background-size: cover;
  padding: 10px;
  
}
.event-link {
  color: #2c3e50;
  text-decoration: none;
}
</style>

  