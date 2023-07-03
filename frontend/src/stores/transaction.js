/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useUserTransaction = defineStore({
    id: 'transaction',
    state: () => ({
        transactions: {loading: false, data: JSON.parse(localStorage.getItem('libex_transactions')), error: null},
    }),
    actions: {
        async getTransactions() {
            // user store
            const userStore = useUserStore()

            this.transactions.loading = true
            
            await axios.get('api/transactions/', {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
              .then((resp) => {
                this.transactions.loading = false
                this.transactions.error = null,
                localStorage.setItem('libex_transactions', JSON.stringify(resp.data))
                this.transactions.data = JSON.parse(localStorage.getItem('libex_transactions'))
              })
              .catch((err) => {
                this.transactions.loading = false
                if (err.response.status == 401) userStore.signOut()
                else this.transactions.error = "An error occured"
              })
        },
    }
})