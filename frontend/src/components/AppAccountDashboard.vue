<script setup>
/* eslint-disable */
import { useUserStore } from '../stores/user';
import VueTradingView from 'vue-trading-view/src/';
import { computed } from 'vue';

// stores
const store = useUserStore()

// computed
const isName = computed(() => {
    try {
        return store.userData.data.first_name !== null
    }
    catch(err) {
        return false
    }
})

// hooks
store.getMe()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 mt-10 mb-10 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Dashboard</h1>
                <span class="text-slate-600 font-normal tracking-wide">Welcome, {{isName ? store.userData.data.first_name:''}}</span>
            </div>

            <div class="grid grid-cols-2 gap-5 justify-between items-start lg:grid-cols-4">
                <!-- total investment -->
                <div class="flex items-start justify-start p-4 w-full h-28 rounded-lg shadow bg-slate-700 md:h-32">
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Total Investments</span>
                        <p class="text-slate-100 font-bold text-xl tracking-wider md:text-2xl lg:text-3xl">${{store.userData.data.total_investment}}</p>
                    </div>
                </div>

                <!-- latest investment -->
                <div class="flex items-start justify-start p-4 w-full h-28 rounded-lg shadow bg-slate-700 md:h-32">
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Current Investment</span>
                        <p class="text-slate-100 font-bold text-xl tracking-wider md:text-2xl lg:text-3xl">${{store.userData.data.current_investment}}</p>
                        <span class="text-xs font-medium mt-4">
                            <span class="text-green-500">%{{store.userData.data.interest_rate}}</span>
                            <span class="text-slate-400">/daily</span>
                        </span>
                    </div>
                </div>

                <!-- total earnings -->
                <div class="flex items-start justify-start p-4 w-full h-28 rounded-lg shadow bg-slate-700 md:h-32">
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Total Earnings</span>
                        <p class="text-slate-100 font-bold text-xl tracking-wider md:text-2xl lg:text-3xl">${{store.userData.data.total_earnings}}</p>
                    </div>
                </div>


                <!-- total balance -->
                <div class="flex items-start justify-start p-4 w-full h-28 rounded-lg shadow bg-slate-700 md:h-32">
                    <div class="flex flex-col">
                        <span class="text-slate-400 text-xs font-medium mb-1 md:text-sm">Total Balance</span>
                        <p class="text-slate-100 font-bold text-xl tracking-wider md:text-2xl lg:text-3xl">${{store.userData.data.total_balance}}</p>
                        <span class="text-xs font-medium mt-4">
                            <span class="text-green-500">Withdrawable</span>
                        </span>
                    </div>
                </div>
            </div>

            <div class="h-full w-full flex flex-col mt-10">
                <div class="flex items-center justify-between border-b border-slate-600">
                    <span class="text-xl font-medium text-slate-600 tracking-wider">Live Chart</span>
                    <span>
                        <span class="text-sm font-medium text-slate-600 md:text-lg">Account Status:</span>
                        <span v-if="store.userData.data" :class="store.userData.data.is_verified ? 'text-green-600':'text-red-600'" class="text-sm font-medium ml-2 md:text-lg">
                            <span v-if="store.userData.data.is_verified">Verified</span>
                            <span v-else>Unverified</span>
                        </span>
                    </span>
                </div>

                <!-- start of tradinfview chart -->
                <div class="h-full w-full mt-10 overflow-auto">
                    <!-- TradingView Widget BEGIN -->
                    <VueTradingView :options="{symbol: 'BINANCE:BTCUSDT',  theme: 'dark'}" />
                    <!-- TradingView Widget END -->
                </div>
            </div>

        </div>

    </div>
</template>