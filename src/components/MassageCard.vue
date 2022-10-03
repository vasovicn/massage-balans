<template>
  <router-link :to="{ name: 'MassageReservation'}">
    <div class="massage" @click="togleDetails()">
    <div>
      <span class="card">
        <div class="thumb"
          style="background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/210284/flex-1.jpg);"></div>
        <article>
          <h1>{{massage.name}}</h1>
        </article>
      </span>
    </div>
    <!-- <MassageDetails v-if="detailsOpen" :massageID="massage.id" /> -->
  </div>
  </router-link>
</template>
  
<script>
// import MassageDetails from '@/components/MassageDetails'

export default {
  components: {
    // MassageDetails
  },
  name: 'MassageCard',
  data() {
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

.card:hover {
  top: -2px;
  box-shadow: 0 4px 5px rgba(0, 0, 0, 0.2);
}

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
.card:hover {
  cursor: pointer;
}
</style>

  