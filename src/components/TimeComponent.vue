<template>
  <div class="container">
    <div v-if="timesToDisplay.length" class="row" style="justify-content: center;">
      <div class="cols" style="font-size: 100%" v-for="time in timesToDisplay" :key="time.id" @click="this.$emit('clicked-time', time)">
        {{time}}
      </div>
    </div>
    <div v-if="this.allTerminsBooked">
      <div>
        <h1>All termins are booked!</h1>
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: 'TimeComponent',
  data() {
    return {
      timesToDisplay: [],
      allTerminsBooked: false
    }
  },
  props: ['date', 'massage', 'currentTime', 'currentDate', "masseur_id", "timePeriod"],
  watch: {
    date() {
      this.calcReserved()
    },
    masseur_id() {
      this.calcReserved()
    },
    timePeriod() {
      this.calcReserved()
    }
  },
  created() {
    this.calcReserved()
  },
  methods: {
    async calcReserved() {
      this.allTerminsBooked = false
      await this.$store.dispatch('fetchReservedTimeDjango', {'date':this.date, "masseur_id": this.masseur_id})

      const reserved = this.$store.state.reservedTime
      const all = this.$store.state.allTermins
      var listReservedTime = []
      // SVE REZERVACIJE -------------------------------
      reserved.forEach(element => {
        listReservedTime.push(element.time)
        var hour = parseInt(element.time.slice(0, 2))
        const minutes = parseInt(element.time.slice(-2))

        var helperMinutes = minutes
        var helperHour = hour
        for (let i = 0; i < element.massage_id.length / 15; i++) {
          if (helperMinutes === 45) {
            helperHour += 1
            helperMinutes = 0
            if (helperHour.toString().length === 1) {
              listReservedTime.push('0' + helperHour + ':' + helperMinutes + '0')
            }
            else {
              listReservedTime.push(helperHour + ':' + helperMinutes + '0')
            }
          }
          else {
            helperMinutes += 15
            if (helperHour.toString().length === 1) {
              listReservedTime.push('0' + helperHour + ':' + helperMinutes)
            }
            else {
              listReservedTime.push(helperHour + ':' + helperMinutes)
            }
          }
        }
      });
      const finalListOfReservedTimes = all.filter(x => !listReservedTime.includes(x))

      // Aditional times to be deleted because of length of massage
      var moreTimesToBeDeleted = []
      finalListOfReservedTimes.forEach(time => {
        var helpHour = parseInt(time.slice(0, 2))
        var helpMinutes = parseInt(time.slice(-2))
        for (let i = 0; i < this.massage.length / 15; i++) {
          if (helpMinutes === 45) {
            helpHour += 1
            helpMinutes = 0
            if (helpHour.toString().length === 1) {
              if (!finalListOfReservedTimes.includes('0' + helpHour + ':' + helpMinutes + '0')) {
                moreTimesToBeDeleted.push(time)
                break
              }
            }
            else {
              if (!finalListOfReservedTimes.includes(helpHour + ':' + helpMinutes + '0')) {
                moreTimesToBeDeleted.push(time)
                break
              }
            }
          }
          else {
            helpMinutes += 15
            if (helpHour.toString().length === 1) {
              if (!finalListOfReservedTimes.includes('0' + helpHour + ':' + helpMinutes)) {
                moreTimesToBeDeleted.push(time)
                break
              }
            }
            else {
              if (!finalListOfReservedTimes.includes(helpHour + ':' + helpMinutes)) {
                moreTimesToBeDeleted.push(time)
                break
              }
            }
          }
        }

      })
      const timesToDisplay = finalListOfReservedTimes.filter(x => !moreTimesToBeDeleted.includes(x))

      // If user tries to reserve time for today, he shouldn't see times before current 
      // TODO: Create logic if for example currentTime is 19:55 user shouldn't be able to reserve time 20:00
      // but if time is for example 19:30 he should be able to reserve time 20:00. Currently even if currentTime is 19:05 he can't reserve time before 20:00
      // but also if currentTime is 19:55 he can reserve time 20:00 but he shouldn't be able.
      var aditionalDelete = []
      if (this.date === this.currentDate) {
        var hours = parseInt(this.currentTime.slice(0, 2))
        hours += 1
        timesToDisplay.forEach(time => {
          if (parseInt(time.slice(0, 2)) < hours) {
            aditionalDelete.push(time)
          }
        })
      }
      const finalAllTimes = timesToDisplay.filter(x => !aditionalDelete.includes(x))
      const finalTimes = []
      finalAllTimes.forEach(time => {
        var selectedTime = parseInt(time.slice(0, 2))
        if (this.timePeriod[0] < selectedTime && selectedTime < this.timePeriod[1]) {
          finalTimes.push(time)
        }
      })
      this.timesToDisplay = finalTimes
      console.log('times', this.timesToDisplay)
      if(!finalTimes.length) {
        this.allTerminsBooked = true
      }
    },
    hoverFunc(time) {
      const length = this.massage.length / 15
      const listReservedTime = []
      var hour = parseInt(time.slice(0, 2))
      const minutes = parseInt(time.slice(-2))
      var helperMinutes = minutes
      var helperHour = hour
      listReservedTime.push(time)
      for (let i = 0; i < length; i++) {
        if (helperMinutes === 45) {
          helperHour += 1
          helperMinutes = 0
          if (helperHour.toString().length === 1) {
            listReservedTime.push('0' + helperHour + ':' + helperMinutes + '0')
          }
          else {
            listReservedTime.push(helperHour + ':' + helperMinutes + '0')
          }
        }
        else {
          helperMinutes += 15
          if (helperHour.toString().length === 1) {
            listReservedTime.push('0' + helperHour + ':' + helperMinutes)
          }
          else {
            listReservedTime.push(helperHour + ':' + helperMinutes)
          }
        }
      }
    },
    hoverLeave() {
      var elms = document.querySelectorAll("*[style]");
      elms.forEach(element => {
        element.removeAttribute('style')
      })
    }
  }
}
</script>

<style scoped>
.cols {
  padding: 5px;
  margin: 2px;
  border: 1px solid;
  height: 10px;
  width: 80px;
  padding-bottom: 7px;
  padding-top: 0px;
  border-radius: 10px;
  background-color: #33cabb;
  min-height: 30px;
  min-width: fit-content;
  text-align: center;
  color:white
}
.cols:hover {
  background-color: white;
  cursor: pointer;
}
.container {
  margin-top: 10px;
  max-width:760px
}
</style>
