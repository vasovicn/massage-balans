<template>
    <div class="d-flex justify-content-center price-list-service-types">
        <div v-for="type in serviceTypes" @click.prevent="selectedType = type" style="padding: 1px 8px" class=""
             :style="{borderBottom: type === selectedType ? '1px solid #81bfaa': ''}">
            <span class="service-type" :style="{color: type === selectedType ? '#81bfaa' : 'black'}">
                {{ type }}
            </span>
        </div>
    </div>
    <table class="m-auto">
        <tr>
            <th/>
            <th/>
            <th v-for="length in selectedTypeLengths"
                class="price-list-table-header">
                {{ length }}min
            </th>
        </tr>
        <tr v-for="(massage, id) in selectedTypeServices" :key="id">
            <td style="">
                <h5 style="margin: auto;font-weight: 500;font-size: large; font-family: Raleway, sans-serif">
                    {{ massage.name }}
                </h5>
            </td>
            <td/>
            <td v-for="length in selectedTypeLengths"
                class="price-list-price">
                {{ getPriceForLength(length, massage) }}
            </td>
        </tr>
    </table>
    <!--    </div>-->
</template>
<script>

export default {
    name: 'PriceList',
    data() {
        return {
            products: null,
            lengths: [],
            selectedType: 'Masaze'
        }
    },
    components: {},
    created() {
        this.$store.dispatch('getMassagesDjango')
            .catch(error => {
                console.log(error)
            })
    },
    methods: {
        getPriceForLength(length, massage) {
            var product = massage.products.filter(product => product.length === String(length))[0]
            console.log('product', product)
            return product ? product.price + ' din.' : ''
        }
    },
    computed: {
        selectedTypeServices() {
            return this.massages.filter(massage => massage.type === this.selectedType && massage.products.length !== 0)
        },
        selectedTypeLengths() {
            var lengthList = [...new Set(this.selectedTypeServices.flatMap(obj => obj.products.map(product => parseInt(product.length))))]
            console.log('lengthList', lengthList)
            this.products = lengthList
            return lengthList.slice().sort((a, b) => a - b);
        },
        massages() {
            return this.$store.state.massages.filter(massage => massage.products.length !== 0)
        },
        serviceTypes() {
            console.log('serviceTypes', [...new Set(this.$store.state.massages.map(obj => obj.type))])
            console.log('massages', this.$store.state.massages)
            return [...new Set(this.$store.state.massages.map(obj => obj.type))]
        }
    }
}
</script>

<style scoped>
td {
    min-width: 170px;
    /* text-align:center */
    border: 1px solid;
    border-color: rgba(99, 103, 104, 0.267);
}

tr {
    height: 45px
}

th {
    border: 1px solid;
    border-color: rgba(0, 0, 0, 0.3);
}

.service-type:hover {
    color: #81bfaa !important;
}

table {
    border-collapse: collapse;
}

td, th {
    border: none;
}

td {
    border-bottom: 1px solid #e4e4e4;
    padding: 20px 0;
}

@media (max-width: 767px) {
    .price-list-price {
        min-width: 40px !important;
        font-size: 8px !important;
    }

    .price-list-table-header {
        font-size: 8px !important;
    }
    .price-list-service-types {
        font-size: 7px !important;
    }

    h5 {
        font-size: 8px !important;
    }

    td {
        min-width: fit-content;
    }

    tr {
        height: fit-content !important;
    }

}

.price-list-price {
    text-align: center;
    min-width: 105px;
    font-family: Droid Serif, serif;
    color: #81bfaa;
    font-weight: 400;
    font-size: 1.36em;
}

.price-list-table-header {
    text-align: center;
    font-family: Raleway, sans-serif;
    font-size: 1.36em;
    font-weight: 500;
}

.price-list-service-types {
    text-align: center;
    margin-top: 150px;
    margin-bottom: 30px;
    cursor: pointer
}
</style>
  