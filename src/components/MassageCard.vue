<template>
    <div class="massage" >
    <div class="card" :style="{backgroundImage: 'url(' + require('@/assets/' + massage.image) + ')' }">
      <span>
        <div ></div>
        <article>
          <h1>{{massage.name}}</h1>
          <button class="button" @click="toggleReservation()">Rezervisi</button>

        </article>
      </span>
    </div>
    <MassageReservation v-if="reservationOpen" :massageID="massage.id"/>
    <!-- <MassageDetails v-if="detailsOpen" :massageID="massage.id" /> -->
  </div>
</template>
  
<script>
import MassageReservation from '@/components/MassageReservation.vue';
// import MassageDetails from '@/components/MassageDetails'

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
.event-link {
  color: #2c3e50;
  text-decoration: none;
}
header {
  width: 90%;
  max-width: 1240px;
  margin: 0 auto;
}

.card {
  background: white;
  text-decoration: none;
  color: #444;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  min-height: 100%;
  position: relative;
  top: 0;
  transition: all 0.1s ease-in;
}

/* .card:hover {
  top: -2px;
  box-shadow: 0 4px 5px rgba(0, 0, 0, 0.2);
} */

.card article {
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card h1 {
  font-size: 20px;
  margin: 0;
  color: #333;
}

.card p {
  flex: 1;
  line-height: 1.4;
}

.card span {
  font-size: 12px;
  font-weight: bold;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 2em 0 0 0;
}

.card .thumb {
  padding-bottom: 60%;
  background-size: cover;
  background-position: center center;
}
/* .card:hover {
  cursor: pointer;
} */
.button:hover {
  cursor: pointer;
}
</style>

  