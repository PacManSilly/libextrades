<script setup>
/* eslint-disable */
import { useUserStore } from '../stores/user';
import { useUserTransaction } from '../stores/transaction';
import VueTradingView from 'vue-trading-view/src/';
import { computed } from 'vue';
import IconBankNotes from './icons/IconBankNotes.vue';
import IconCurrencyDollar from './icons/IconCurrencyDollar.vue'
import IconGift from './icons/IconGift.vue'
import IconGiftTop from './icons/IconGiftTop.vue'
import IconArrowUpOnSquareStack from './icons/IconArrowUpOnSquareStack.vue'
import IconArrowDownOnSquareStack from './icons/IconArrowDownOnSquareStack.vue'
import { RouterLink } from 'vue-router'

// stores
const store = useUserStore()
const storeTransaction = useUserTransaction()

// methods
const toCurrency = (value) => {
    const currencyFormatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    });

    return currencyFormatter.format(value)
}

const toDate = (value) => {
    const dateDate = new Date(value).toDateString()
    const dateTime = new Date(value).toLocaleTimeString()

    return `${dateDate} ${dateTime}`
}

// computed
const isName = computed(() => {
    try {
        return store.userData.data.first_name !== null
    }
    catch (err) {
        return false
    }
})

// created hook - (implicit)
store.getMe()
storeTransaction.getTransactions()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-y-10 mt-10 lg:mt-0">
                <!-- <h1 class="text-white text-4xl font-black">Dashboard</h1> -->
                <span class="text-white text-3xl font-normal">
                    Hi, {{ store.userData.data?.first_name || '' }} {{ store.userData.data?.last_name || '' }}
                </span>
                <!-- <span>
                    <span class="text-sm font-medium text-slate-600 md:text-lg">Account Status:</span>
                    <span v-if="store.userData.data"
                        :class="store.userData.data.is_verified ? 'text-green-600' : 'text-red-600'"
                        class="text-sm font-medium ml-2 md:text-lg">
                        <span v-if="store.userData.data.is_verified">Verified</span>
                        <span v-else>Unverified</span>
                    </span>
                </span> -->

                <div class="w-full py-4 flex items-center justify-between">
                    <RouterLink :to="{ name: 'investmentplan' }"
                        class="bg-cyan-500 rounded-sm px-3 py-1 text-sm text-white md:text-lg">
                        Invest now
                    </RouterLink>

                    <span class="inline-flex items-center gap-x-3">
                        <RouterLink :to="{ name: 'investmentplan' }"
                            class="bg-green-500 rounded-sm px-3 py-1 text-sm text-white md:text-lg">
                            Deposit
                        </RouterLink>
                        <RouterLink :to="{ name: 'withrawalmethods' }"
                            class="bg-red-500 rounded-sm px-3 py-1 text-sm text-white md:text-lg">
                            Withdrawal
                        </RouterLink>
                    </span>
                </div>
            </div>

            <div class="grid grid-cols-2 gap-2 justify-between items-start lg:grid-cols-3">
                <!-- total investment -->
                <div
                    class="bg-slate-800 py-4 pl-3 rounded-lg flex items-center justify-start gap-x-5 w-full md:py-10 md:pl-7">
                    <IconBankNotes class="w-8 h-8 text-slate-600 md:w-10 md:h-10" />
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Account balance</span>
                        <p class="text-slate-100 font-bold text-lg tracking-wider md:text-2xl">
                            {{ toCurrency(store.userData.data.account_balance) }}
                        </p>
                    </div>
                </div>

                <!-- latest investment -->
                <div
                    class="bg-slate-800 py-4 pl-3 rounded-lg flex items-center justify-start gap-x-5 w-full md:py-10 md:pl-7">
                    <IconCurrencyDollar class="w-8 h-8 text-slate-600 md:w-10 md:h-10" />
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Total profit</span>
                        <p class="text-slate-100 font-bold text-lg tracking-wider md:text-2xl">
                            {{ toCurrency(store.userData.data.total_profit) }}</p>
                        <!-- <span class="text-xs font-medium mt-4">
                            <span class="text-green-500">%{{ store.userData.data.interest_rate }}</span>
                            <span class="text-slate-400">/daily</span>
                        </span> -->
                    </div>
                </div>

                <!-- total earnings -->
                <div
                    class="bg-slate-800 py-4 pl-3 rounded-lg flex items-center justify-start gap-x-5 w-full md:py-10 md:pl-7">
                    <IconGift class="w-8 h-8 text-slate-600 md:w-10 md:h-10" />
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Bonus</span>
                        <p class="text-slate-100 font-bold text-lg tracking-wider md:text-2xl">
                            {{ toCurrency(store.userData.data.bonus) }}
                        </p>
                    </div>
                </div>


                <!-- total balance -->
                <div
                    class="bg-slate-800 py-4 pl-3 rounded-lg flex items-center justify-start gap-x-5 w-full md:py-10 md:pl-7">
                    <IconGiftTop class="w-8 h-8 text-slate-600 md:w-10 md:h-10" />
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Referral bonus</span>
                        <p class="text-slate-100 font-bold text-lg tracking-wider md:text-2xl">
                            {{ toCurrency(store.userData.data.referral_bonus) }}</p>
                        <!-- <span class="text-xs font-medium mt-4">
                            <span class="text-green-500">Withdrawable</span>
                        </span> -->
                    </div>
                </div>

                <!-- total balance -->
                <div
                    class="bg-slate-800 py-4 pl-3 rounded-lg flex items-center justify-start gap-x-5 w-full md:py-10 md:pl-7">
                    <IconArrowDownOnSquareStack class="w-8 h-8 text-slate-600 md:w-10 md:h-10" />
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Total deposit</span>
                        <p class="text-slate-100 font-bold text-lg tracking-wider md:text-2xl">
                            {{ toCurrency(store.userData.data.total_deposit) }}</p>
                        <!-- <span class="text-xs font-medium mt-4">
                            <span class="text-green-500">Withdrawable</span>
                        </span> -->
                    </div>
                </div>

                <!-- total balance -->
                <div
                    class="bg-slate-800 py-4 pl-3 rounded-lg flex items-center justify-start gap-x-5 w-full md:py-10 md:pl-7">
                    <IconArrowUpOnSquareStack class="w-8 h-8 text-slate-600 md:w-10 md:h-10" />
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Total withdrawal</span>
                        <p class="text-slate-100 font-bold text-lg tracking-wider md:text-2xl">
                            {{ toCurrency(store.userData.data.total_withdrawal) }}</p>
                        <!-- <span class="text-xs font-medium mt-4">
                            <span class="text-green-500">Withdrawable</span>
                        </span> -->
                    </div>
                </div>
            </div>

            <div class="h-full w-full flex flex-col mt-14 pb-20">

                <span class="pb-5">
                    <h3 class="text-2xl text-slate-500 font-medium md:text-3xl">Recent transactions</h3>
                </span>

                <div class="bg-slate-900 max-h-96 overflow-auto">
                    <table class="w-full table-auto border-collapse border-spacing-2">
                        <thead class="">
                            <tr class="text-slate-300">
                                <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Transaction type</th>
                                <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Amount</th>
                                <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Status</th>
                                <th class="sticky top-0 z-10 p-4 bg-slate-900 border-b border-slate-600">Date created</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="transaction in storeTransaction.transactions.data" :key="transaction.id"
                                class="border-b border-slate-800 text-center last:border-none">
                                <td class="p-4 text-sm text-slate-500 md:text-base">{{ transaction.transaction_type }}</td>
                                <td v-if="transaction.transaction_type == 'Deposit'" class="p-4 text-sm text-slate-500 md:text-base">{{ transaction.amount }}</td>
                                <td v-else class="p-4 text-sm text-slate-500 md:text-base">{{ toCurrency(transaction.amount) }}</td>
                                <td class="p-4 text-sm text-slate-500">
                                    <span :class="transaction.status == 'Active' ? 'bg-green-600' : 'bg-yellow-600'"
                                        class="text-white inline-block px-2 py-1 rounded-md">{{ transaction.status }}</span>
                                </td>
                                <td class="p-4 text-sm text-slate-500 md:text-base">{{ toDate(transaction.created) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>


                <!-- trading view chart -->
                <!-- <div class="h-full w-full mt-10 overflow-auto border-t border-slate-800 pt-10">
                    <VueTradingView :options="{ symbol: 'BINANCE:BTCUSDT', theme: 'dark' }" />
                </div>-->

            </div>

        </div>

</div></template>