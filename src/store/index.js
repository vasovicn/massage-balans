import { createStore } from 'vuex'
import MassageService from '@/services/MassageService'
import axios from 'axios'

export default createStore({
  state: {
    token: '',
    username: '',
    isAuthenticated: false,
    massages: [],
    reservedTime: [],
    massage: null,
    masseuers: [],
    masseur: null,
    reservation: [],
    reservations: [],
    userReservations: [],
    userInfo: null,
    x: null,
    selectedMasseur: null,
    allTermins: ['08:00', '08:15', '08:30', '08:45',
      '09:00', '09:15', '09:30', '09:45',
      '10:00', '10:15', '10:30', '10:45',
      '11:00', '11:15', '11:30', '11:45',
      '12:00', '12:15', '12:30', '12:45',
      '13:00', '13:15', '13:30', '13:45',
      '14:00', '14:15', '14:30', '14:45',
      '15:00', '15:15', '15:30', '15:45',
      '16:00', '16:15', '16:30', '16:45',
      '17:00', '17:15', '17:30', '17:45',
      '18:00', '18:15', '18:30', '18:45',
      '19:00', '19:15', '19:30', '19:45',
      '20:00', '20:15', '20:30', '20:45',
      '21:00', '21:15', '21:30', '21:45',
      '22:00']
  },
  mutations: {
    SET_MASSAGES(state, massages) {
      state.massages = massages
    },
    SET_MASSAGE(state, massage) {
      state.massage = massage
    },
    SET_RESERVE_TIME(state, reservedTime) {
      state.reservedTime = reservedTime
    },
    SET_MASSEUERS(state, masseuers) {
      state.masseuers = masseuers
    },
    SET_MASSEUR(state, masseur) {
      state.masseur = masseur
    },
    POST_RESERVE_TIME(state, reservation) {
      state.reservation = reservation
    },
    SET_RESERVATIONS(state, reservations) {
      state.reservations = reservations
    },
    DELETE_MASSAGE(state, massage) {
      state.massages - massage
    },
    SET_TOKEN(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    REMOVE_TOKEN(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    SET_USERNAME(state, username) {
      state.username = username
    },
    SET_USER_PORTAL(state, data) {
      state.userReservations = data
    },
    SET_USER_INFO(state, data) {
      state.userInfo = data
    },
    SET_SELECTED_MASSAGE(state, massage) {
      state.x = massage
    },
    SET_SELECTED_MASSAGE_BUTTON(state, y) {
      state.y = y
    }
  },
  actions: {
    fetchMasseur({ commit }) {
      return MassageService.getMasseur()
        .then(response => {
          commit('SET_MASSEUR', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    fetchMasseuers({ commit }) {
      return MassageService.getMasseuers()
        .then(response => {
          commit('SET_MASSEUERS', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteMassage({ dispatch }, massage) {
      return MassageService.deleteMassage(massage)
        .then(dispatch('fetchMassages'))
        .catch(error => {
          console.log(error)
        })
    },
    deleteReservation({ dispatch }, reservation) {
      return MassageService.deleteReservation(reservation)
        .then(response => {
          dispatch('userPortal')
          console.log(response)
    } )
        .catch(error => {
      console.log(error)
    })
  },
  getMassagesDjango({ commit }) {
    return MassageService.getMassagesDjango()
      .then(response => {
        commit('SET_MASSAGES', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  addMassageDjango({ dispatch }, massage) {
    return MassageService.postDjangoMassage(massage)
      .then(dispatch('fetchMassages'))
      .catch(error => {
        console.log(error)
      })
  },
  postReservationDjango({ commit }, reservation) {
    return MassageService.postDjangoReservation(reservation)
      .then(response => {
        commit('POST_RESERVE_TIME', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  fetchMassageDjango({ commit, state }, id) {
    const massage = state.massages.find(massage => massage.id === id)
    if (massage) {
      commit('SET_MASSAGE', massage)
    } else {
      return MassageService.getMassageDjango(id)
        .then(response => {
          commit('SET_MASSAGE', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  fetchReservedTimeDjango({ commit }, reservation_data) {
    return MassageService.getReservedTimeDjango(reservation_data)
      .then(response => {
        commit('SET_RESERVE_TIME', response.data)
      })
      .catch(error => {
        console.log(error)
      })

  },
  fetchAllReservationsDjango({ commit }) {
    return MassageService.getAllReservationsDjango()
      .then(response => {
        commit('SET_RESERVATIONS', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  initialToken({ commit }) {
    if (localStorage.getItem('token')) {
      commit('SET_TOKEN', localStorage.getItem('token'))
    }
  },
  loginDjango({ commit }, formData) {
    return MassageService.loginDjango(formData)
      .then(response => {

        const token = response.data.auth_token
        commit('SET_TOKEN', token)
        axios.defaults.headers.common["Authorization"] = "Token" + token
        localStorage.setItem("token", token)
        commit('SET_USERNAME', formData.username)
      })
  },
  signupDjango({ dispatch }, credentials) {
    return MassageService.signupDjango(credentials)
      .then(response => {
        dispatch('loginDjango', credentials)
        console.log(response)
      }
      )
  },
  userPortal({ commit }) {
    return MassageService.fetchUserReservations(localStorage.getItem("token"))
      .then(response => {
        console.log(response)
        commit('SET_USER_PORTAL', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  getUserInfo({ commit }) {
    return MassageService.getUserInfo(localStorage.getItem("token"))
      .then(response => {
        console.log(response)
        commit('SET_USER_INFO', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  updateInfo({commit}, userInfo) {
    return MassageService.updateInfo(userInfo, localStorage.getItem("token"))
      .then(response => {
        commit('SET_USER_INFO', response.data)
      })
      .catch(error => {
        console.log(error)
      })
  },
  setSelectedMassage({commit}, massage) {
    commit('SET_SELECTED_MASSAGE', massage)
  },
  setSelectedMassageButton({commit}, y) {
    commit('SET_SELECTED_MASSAGE_BUTTON', y)
  }
}
})
