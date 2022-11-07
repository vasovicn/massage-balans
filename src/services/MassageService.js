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
    return apiClientDjango.get('/masseur/')
  },
  getMasseur(id) {
    return apiClient.get('/masseuers/' + id)
  },
  deleteMassage(massage) {
    return apiClient.delete('/massages/' + massage.id)
  },
  deleteReservation(reservation) {
    return apiClientDjango.delete('/reservation/delete/' + reservation.id)
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
  getReservedTimeDjango(reservation_data) {
    return apiClientDjango.get('/reservation/', { params: { date: String(reservation_data.date), masseur_id: reservation_data.masseur_id } })
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
    return apiClientDjango.post('/user/login', credentials)
  },
  verifyPassword(body) {
    return apiClientDjango.post('/user/verify_password', body)
  },
  resetPassword(credentials) {
    return apiClientDjango.post('/api/v1/users/reset_password_confirm', credentials)
  },
  // removeItem(token) {
  //   return apiClientDjango.get('', token)
  // },
  fetchUserReservations(token) {
    return apiClientDjango.get('/reservation/', { params: { token: token } })
  },
  getUserInfo(token) {
    return apiClientDjango.get('/user', { params: { token: token } })
  },
  updateInfo(userInfo, token) {
    return apiClientDjango.put('/user/update', { params: { token: token }, body:userInfo })
  },
  searchUser(username) {
    return apiClientDjango.get('/user/', { params: { username: username } })
  },
  sendResetEmail(email) {
    return apiClientDjango.post('/user/request-reset-email', {params: { email: email}})
  },
  resetPasswordEmail(body) {
    return apiClientDjango.patch('/user/password-reset-complete', {params: { body: body}})
  }
}
