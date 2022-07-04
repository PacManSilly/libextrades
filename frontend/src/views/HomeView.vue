<script setup>
/* eslint-disable */
import AppTopNav from '../components/AppTopNav.vue';
</script>

<template>
    <div class="w-full h-full min-h-full bg-slate-900">

        <div class="relative w-full h-full flex flex-col">

            <!-- start of nav -->
            <div class="absolute top-0 right-0 w-full">
                <AppTopNav />
            </div>


            <!-- <main class="pl-20">
                <RouterLink :to="{ name: 'signup' }" class="text-xl pr-10 text-white">Sign Up</RouterLink>
                <RouterLink :to="{ name: 'account' }" class="text-2xl text-white">Account</RouterLink>
                <RouterLink :to="{ name: 'trade' }" class="text-2xl text-white">Trade Forex</RouterLink>
                <RouterLink :to="{ name: 'tradestock' }" class="text-2xl text-white">Trade Stocks</RouterLink>
                <RouterLink :to="{ name: 'tradecrypto' }" class="text-2xl text-white">Trade Cryptos</RouterLink>
                <RouterLink :to="{ name: 'tradeoption' }" class="text-2xl text-white">Trade Options</RouterLink>
                <RouterLink :to="{ name: 'tradecopytrader' }" class="text-2xl text-white">Trade Copy Experts</RouterLink>
            </main> -->

        </div>

    </div>
</template>