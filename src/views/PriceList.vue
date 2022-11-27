<template>
  <div class="title">Pogledajte aktuelne cene masaže</div>
  <table v-if="products" style="margin:auto; margin-bottom: 200px;">
    <tr style="background-color:#81bfaa">
      <th v-for="length in lengths" style="color:rgb(99 103 104 / 99%)" :style="{textAlign : length === 'preskoci' ? 'left' : 'center', paddingLeft : length === 'preskoci' ? '10px' : '0'   }">{{length === 'preskoci' ? 'Vrsta masaze': length + 'min'}}</th>
    </tr>
    <tr v-for="(massage, id) in massages" :key="id">
      <!-- {{massage.products}} -->
      <td :style="{textAlign : length === 'preskoci' ? 'left' : 'center', paddingLeft : length === 'preskoci' ? '10px' : '0' }" v-for="(length, index) in lengths" :key="index">{{ index === 0 ? massages[id]['name'] : massage.products.filter(product => product.length === length)[0] ? massage.products.filter(product => product.length === length)[0].price + 'din': '/'}}</td>
    </tr>
  </table>
</template>
<script>
import MassageService from '@/services/MassageService'
export default {
  name: 'PriceList',
  data() {
    return {
      products: null,
      lengths: []
    }
  },
  components: {
  },
  created() {
    this.$store.dispatch('getMassagesDjango')
      .catch(error => {
        console.log(error)
      })
    MassageService.getProducts().then(response => {
      this.products = response.data
      var lengthList = ['preskoci']
      response.data.forEach(product => {
        if (!lengthList.includes(product.length)) {
          lengthList.push(product.length);
        }
      });
      this.lengths = lengthList.sort((objA, objB) => {
      return +objA - +objB;
    });
    })
  },
  computed: {
    massages() {
      return this.$store.state.massages
    }
  }
}
</script>
  
<style scoped>
td {
  min-width:170px;
  /* text-align:center */
  border: 1px solid;
  border-color: rgba(99, 103, 104, 0.267);
}
tr {
  height: 45px
}
th {
  border: 1px solid;
  border-color: rgba(0, 0, 0, 0.3) ;
}
.title {
  margin-top: 127px;
  text-align: center;
  margin-bottom: 29px;
  font-weight: bold;
  font-size: larger;
  color:rgba(99, 103, 104, 0.99)
}
</style>
  