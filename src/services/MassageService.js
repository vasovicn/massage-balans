import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:3000',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  getMassages() {
    return apiClient.get('/massages')
  },
  getMassage(id) {
    return apiClient.get('/massages/' + id)
  },
  getMasseuers() {
    return apiClient.get('/masseuers')
  },
  getMasseur(id) {
    return apiClient.get('/masseuers/' + id)
  },
  getReservedTime(date) {
    return apiClient.get('/reservedTime/', { params: { date: date } })
  },
  postReservation(reservation) {
    return apiClient.post('/reservedTime', reservation)
  },
  getAllReservations() {
    return apiClient.get('/reservedTime')
  }
}
