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
  getMasseuers() {
    return apiClientDjango.get('/masseuer/')
  },
  getMasseur(id) {
    return apiClient.get('/masseuers/' + id)
  },
  deleteMassage(massage) {
    return apiClient.delete('/massages/' + massage.id)
  },
  deleteReservation(reservation) {
    return apiClient.delete('/reservedTime/' + reservation.id)
  },
  getMassagesDjango() {
    return apiClientDjango.get('/massage')
  },
  postDjangoMassage(massage) {
    return apiClientDjango.post('/massage/create', massage)
  },
  postDjangoReservation(reservation) {
    return apiClientDjango.post('/reservation/create', reservation)
  },
  getMassageDjango(id) {
    return apiClientDjango.get('/massage/' + id)
  },
  getReservedTimeDjango(date) {
    return apiClientDjango.get('/reservation/', { params: { date: String(date) } })
  },
  getAllReservationsDjango() {
    return apiClientDjango.get('/reservation')
  },
  loginDjango(credentials) {
    return apiClientDjango.post('/api/v1/token/login', credentials)
  },
  signupDjango(credentials) {
    return apiClientDjango.post('/api/v1/users/',  credentials)
  },
  loginAdmin(credentials) {
    console.log(credentials)
    return apiClientDjango.post('/user/login', credentials)
  },
  verifyPassword(body) {
    return apiClientDjango.post('/user/verifyPassword', body)
  },
  resetPassword(credentials) {
    return apiClientDjango.post('/api/v1/users/reset_password_confirm', credentials)
  },
  // removeItem(token) {
  //   return apiClientDjango.get('', token)
  // },
  fetchUserReservations(token) {
    return apiClientDjango.get('/reservation/', { params: { token: token } })
  }
}
