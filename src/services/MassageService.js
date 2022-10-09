import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:3000',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})
const apiClientDjango = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  }

})

export default {
  // getMassages() {
  //   return apiClient.get('/massages')
  // },
  // getMassage(id) {
  //   return apiClient.get('/massages/' + id)
  // },
  getMasseuers() {
    return apiClient.get('/masseuers')
  },
  getMasseur(id) {
    return apiClient.get('/masseuers/' + id)
  },
  // getReservedTime(date) {
  //   return apiClient.get('/reservedTime/', { params: { date: date } })
  // },
  // postReservation(reservation) {
  //   return apiClient.post('/reservedTime', reservation)
  // },
  // getAllReservations() {
  //   return apiClient.get('/reservedTime')
  // },
  deleteMassage(massage) {
    return apiClient.delete('/massages/' + massage.id)
  },
  // postMassage(massage) {
  //   return apiClient.post('/massages', massage)
  // },
  deleteReservation(reservation) {
    console.log(reservation.id)
    return apiClient.delete('/reservedTime/' + reservation.id)
  },
  getMassagesDjango() {
    return apiClientDjango.get('/massages')
  },
  postDjangoMassage(massage) {
    return apiClientDjango.post('/massages/create', massage)
  },
  postDjangoReservation(reservation) {
    return apiClientDjango.post('/reservation/create', reservation)
  },
  getMassageDjango(id) {
    return apiClientDjango.get('/massages/' + id)
  },
  getReservedTimeDjango(date) {
    return apiClientDjango.get('/reservation/', { params: { date: date } })
  },
  getAllReservationsDjango() {
    return apiClientDjango.get('/reservation')
  },
  
}
