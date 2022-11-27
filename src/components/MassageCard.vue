<template>
  <RouterLink :to="{name : 'MassageDetails', params: {id: this.massage.id}}">
  <div :id="massage.name" class="col-3" style=" padding: 3px" :style="{maxWidth : location ? '150px' : '220px', minWidth : location ? '150px' : '220px'}">
    <div class="card">
      <img class="card-img-top" :src="massage.photo_url" style="width: 100%" :style="{height : location ? '130px' : '160px'}"/>
      <div class="card-body" style="padding:7px">
        <h5 class="card-title" style="margin:auto;color: rgba(99, 103, 104, 0.99)" :style="{fontSize : location ? 'inherit' : '1.25rem'}">{{ massage.name }}</h5>
        <!-- <p class="card-text">{{ massage.info }}</p> -->
        <!-- <MassageReservation :massageID="massage"/> -->
      </div>
      </div>
    </div>
    </RouterLink>
</template>
  
<script>
import MassageReservation from '@/components/MassageReservation.vue';

export default {
  components: {
    MassageReservation,
  },
  name: 'MassageCard',
  props: ['massage'],
  data() {
    return {
      reservationOpen: true
    }
  },
  computed: {
    location() {
      if (document.location.pathname.includes('details')) {
        return true
      }
      return false
    }
  },
  methods: {

  }
}
</script>
<style scoped>


.card {
  /* border-radius: 20px; */
  text-align: center;
  padding: 1px !important;
}

.card-img-top:hover {
  cursor: pointer;
  opacity: 0.7;
  width: 400px;
}

.card-img-top {
  border-radius: inherit;
  max-width: 100%;
}

.card-body {
  margin: auto;
}
.card-title:hover {
  cursor: pointer;
}
</style>

  