<script setup>
/* eslint-disable */
import AppCoin from "./AppCoin.vue";
import btcIcon from '../assets/images/btc.png'
import ethIcon from '../assets/images/eth.png'
import bnbIcon from '../assets/images/bnb.png'
import solIcon from '../assets/images/sol.png'
import cadIcon from '../assets/images/ada.png'

const coins = [
    {name: "Bitcoin", pair: "btcusdt", icon: btcIcon},
    {name: "Ethereum", pair: "ethusdt", icon: ethIcon},
    {name: "Binance", pair: "bnbusdt", icon: bnbIcon},
    {name: "Solana", pair: "solusdt", icon: solIcon},
    {name: "Cadano", pair: "adausdt", icon: cadIcon},
]
</script>

<template>
    <div class="w-full py-4 bg-slate-900 backdrop-blur-xl select-none px-5">

        <div ref="crypto" class="flex justify-between items-center gap-x-10 overflow-x-auto md:gap-x-5">
            <AppCoin v-for="coin in coins" :key="coin.name" :coin="coin" class="shrink-0" />
        </div>

    </div>
</template>
