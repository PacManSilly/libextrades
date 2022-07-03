/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useUserTrader = defineStore({
    id: 'traders',
    state: () => ({
        traders: {loading: false, data: JSON.parse(localStorage.getItem('libex_traders')), error: null},
        addTrader: {loading: false, error: null}
    }),
    actions: {
        async getTraders() {
            // user store
            const userStore = useUserStore()

            this.traders.loading = true
            this.traders.error = null
            
            await axios.get('experts/', {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
                .then((resp) => {
                    this.traders.loading = false
                    this.traders.error = null
                    localStorage.setItem('libex_traders', JSON.stringify(resp.data))
                    this.traders.data = JSON.parse(localStorage.getItem('libex_traders'))
                })
                .catch((err) => {
                    this.traders.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.traders.error = "An error occured"
                })
        },
        async createTrader(data) {
            // user store
            const userStore = useUserStore()

            this.addTrader.loading = false
            this.addTrader.error = null

            await axios.put(`experts/${data.traderId}/update/`, {...data})
                .then((resp) => {
                    this.addTrader.loading = false
                    this.addTrader.error = null
                    
                    // redirect to my traders view
                    this.$router.push({name: 'mytraders'})
                })
                .catch((err) => {
                    this.addTrader.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.traders.error = "An error occured"
                })
        }
    }
})