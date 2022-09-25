<template>
  <div style="padding:10px; border-righr:1px solid">
      <div class="time" v-for="time in timesToDisplay" :key="time.id" @click="this.$emit('clicked-time', time)">
          {{time}}
      </div>
  </div>
</template>

<script>
export default {
  name: 'TimeComponent',
  data() {
    return {
      timesToDisplay: []
    }
  },
  props: ['date', 'massage'],
  watch: {
    date() {
       this.calcReserved()
    }
  },
created() {
  this.calcReserved()
},
methods: {
  async calcReserved() {
    await this.$store.dispatch('fetchReservedTime', this.date)

    const reserved = this.$store.state.reservedTime
    const all = this.$store.state.allTermins
      var listReservedTime = []
        reserved.forEach(element => {
        listReservedTime.push(element.time)
        var hour = parseInt(element.time.slice(0, 2))
        const minutes = parseInt(element.time.slice(-2))

        var helperMinutes = minutes
        var helperHour = hour 
        for (let i = 0; i < this.massage.length/15; i++) {
          if (helperMinutes === 45) {
            helperHour += 1
            helperMinutes = 0
            listReservedTime.push(helperHour + ':' + helperMinutes + '0')
          }
          else {
            helperMinutes += 15
            listReservedTime.push(helperHour + ':' + helperMinutes)
          }
        }
        });
    const finalListOfReservedTimes = all.filter(x => !listReservedTime.includes(x))
    this.timesToDisplay = finalListOfReservedTimes
    }
  }
}
</script>

<style scoped>
.time {
  display:inline-block;
  min-height: 10px;
  padding:5px;
  border-bottom: 1px solid;
  border-top: 1px solid;
}
.time:hover {
  background-color: green;
  cursor: pointer;
}
</style>
