<template>
  <div :id="massage.name" class="container"
    :style="{ transform: reservationOpenTest && this.reservationOpen ? 'scale(1.1)' : '' }">
    <div class="card">
      <!-- <img class="card-img-top" :src="massage.photo_url" /> -->
      <div class="card-body">
        <h5 class="card-title">{{ massage.name }}</h5>
        <p class="card-text">{{ massage.info }}</p>
        <!-- <button v-if="!reservationOpen" class="btn btn-primary" @click="toggleReservation()">Rezervisi</button> -->
        <MassageReservation v-if="reservationOpenTest && this.reservationOpen" :massageID="massage.id"
          @reserved="reservationOpen = false" @fold="foldcard"/>
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
  props: ['massage'],
  data() {
    return {
      reservationOpen: true
    }
  },
  computed: {
    reservationOpenTest() {
      if (this.$store.state.x == this.massage.name) {
        return true
      }
      else {
        return false
      }
    },
  },
  methods: {
    foldcard() {
      this.reservationOpen = false
    }
  }
}
</script>
<style scoped>
.container {
  padding: 20px;
  transition: 0.5s;
  transition-timing-function: ease-in-out;
}

.container:hover {

  transform: scale(1.1);
  cursor: pointer;
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

  