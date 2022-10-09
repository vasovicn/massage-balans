<template>
  <div class="container">
    <div class="card">
      <!-- <img class="card-img-top" :src="require('@/assets/' + massage.image)" /> -->
      <div class="card-body">
        <h5 class="card-title">{{massage.name}}</h5>
        <p class="card-text">{{massage.info}}</p>
        <button v-if="!reservationOpen" class="btn btn-primary" @click="toggleReservation()">Rezervisi</button>
        <MassageReservation v-if="reservationOpen" :massageID="massage.id" @reserved="reservationOpen = false" />
      </div>
    </div>
  </div>
</template>
  
<script>
import MassageReservation from '@/components/MassageReservation.vue';

export default {
  components: {
    MassageReservation
  },
  name: 'MassageCard',
  data() {
    return {
      reservationOpen: false
    }
  },
  props: ['massage'],
  methods: {
    toggleReservation() {
      this.reservationOpen = !this.reservationOpen
    }
  }
}
</script>
<style scoped>
.container {
  padding:20px;
}
.card {
  border-radius: 20px;
  text-align: center;
}
.card-img-top {
  border-radius: inherit;
  max-width: 100%;
  height: auto;
}
.card-body {
  margin: auto;
}
@import'~bootstrap/dist/css/bootstrap.css'
</style>

  