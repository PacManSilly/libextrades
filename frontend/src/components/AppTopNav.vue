<script setup>
/* eslint-disable */
import { ref, onMounted, computed, onUnmounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserStore } from '../stores/user';
import AppLogo from './AppLogo.vue';
import IconHamburger from './icons/IconHamburger.vue';
import IconCloseBig from './icons/IconCloseBig.vue';

// data
const tradesMenu = ref(false)
const mobileMenu = ref(false)
const root = ref(null)

// stores
const store = useUserStore()

// computed
const isAuth = computed(() => {
    return localStorage.getItem('libex_user')
})

// methods
const closeTradesMenu = (e) => {
    if (!root.value.contains(e.target)) {
        tradesMenu.value = false;
    }
}

// hooks
onMounted(() => {
    document.addEventListener("click", closeTradesMenu)
})

onUnmounted(() => {
    document.removeEventListener("click", closeTradesMenu)
})
</script>

<template>
    <div ref="root" class="relative w-full h-auto py-5 bg-transparent lg:py-10">

        <div class="w-11/12 mx-auto flex justify-between items-center">

            <div>
                <AppLogo />
            </div>

            <!-- nav for large screens -->
            <div class="hidden w-9/12 items-center justify-between lg:flex">


                <div class="flex gap-x-10">
                    
                    <RouterLink to="/#steps" class="text-base text-slate-400 font-normal hover:text-white">Steps</RouterLink>
                    <RouterLink to="/#plans" class="text-base text-slate-400 font-normal hover:text-white">Plans</RouterLink>

                    <div class="relative">
                        <button type="button" @click.prevent="tradesMenu = !tradesMenu" :to="{name: 'home'}" :class="tradesMenu ? 'text-white':'text-slate-400'" class="text-base font-normal hover:text-white">Trades</button>

                        <div :class="tradesMenu ? 'scale-100 opacity-100':'scale-0 opacity-0'" class="absolute z-20 top-10 -left-5 flex flex-col shadow-lg bg-slate-800 rounded-lg w-40 transition-all duration-150">
                            <RouterLink :to="{name: 'tradeforex'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Forex</RouterLink>
                            <RouterLink :to="{name: 'tradestock'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Stocks</RouterLink>
                            <RouterLink :to="{name: 'tradecrypto'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Cryptos</RouterLink>
                            <RouterLink :to="{name: 'tradeoption'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Options</RouterLink>
                            <RouterLink :to="{name: 'tradecopytrader'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Copy Traders</RouterLink>
                        </div>
                    </div>

                    <RouterLink to="/#testimonials" class="text-base text-slate-400 font-normal hover:text-white">Testimonials</RouterLink>
                    <RouterLink to="/#faqs" class="text-base text-slate-400 font-normal hover:text-white">FAQs</RouterLink>
                    <RouterLink to="/#contactus" class="text-base text-slate-400 font-normal hover:text-white">Contact Us</RouterLink>

                </div>

                <div>
                    <div v-if="isAuth" class="flex items-center gap-3">
                        <button type="button" @click.prevent="store.userSignOut.modal = true" class="px-4 py-1 text-base text-white bg-transparent border border-transparent rounded-md transition-all duration-150 hover:border-white hover:scale-105">Sign Out</button>
                        <RouterLink :to="{name: 'dashboard'}" class="px-4 py-1 text-base text-slate-900 bg-white rounded transition-all duration-150 hover:scale-105">Dashboard</RouterLink>
                    </div>

                    <div v-else class="flex items-center gap-3">
                        <RouterLink :to="{name: 'signin'}" class="px-4 py-1 text-base text-white bg-transparent border border-white rounded transition-all duration-150 hover:scale-105">Sign In</RouterLink>
                        <RouterLink :to="{name: 'signup'}" class="px-4 py-1 text-base text-slate-900 bg-white border border-white rounded transition-all duration-150 hover:scale-105">Register</RouterLink>
                    </div>
                </div>
                
            </div>
            <!-- end of nav for large screens -->

            <!-- start of nav for small screens -->
            <div :class="mobileMenu ? 'scale-100 opacity-100':'scale-0 opacity-0'" class="fixed top-0 right-0 z-20 w-full h-full flex flex-col gap-y-10 py-5 bg-slate-900/80 backdrop-blur-xl items-center transition-all duration-150 lg:hidden">

                <div class="flex w-10/12 mx-auto justify-between items-center">
                    <AppLogo />
                    <!-- close button -->
                    <button @click.prevent="mobileMenu = false" type="button" class="group p-2 rounded transition-all duration-150 hover:bg-slate-800">
                        <IconCloseBig class="w-10 h-10 fill-slate-400 group-hover:fill-slate-200" />
                    </button>
                </div>

                <div class="w-10/12 flex flex-col gap-y-10 mx-auto">

                    <div class="grid grid-cols-2 gap-3 text-left">
                        <RouterLink @click.prevent="mobileMenu = false" to="/#steps" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Steps</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" to="/#plans" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Plans</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'tradeforex'}" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Forex</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'tradestock'}" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Stocks</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'tradecrypto'}" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Ctyptos</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'tradeoption'}" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Options</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'tradecopytrader'}" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Copy Traders</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" to="/#testimonials" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Testimonials</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" to="/#faqs" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">FAQs</RouterLink>
                        <RouterLink @click.prevent="mobileMenu = false" to="/#contactus" class="p-2 rounded-md text-base text-slate-400 font-normal transition-all duration-150 hover:bg-slate-800 hover:text-white">Contact Us</RouterLink>
                    </div>

                    <div>
                        <div  v-if="isAuth" class="flex items-center justify-center gap-3 border-t border-slate-500 pt-5">
                            <div>
                                <button type="button" @click.prevent="store.userSignOut.modal = true" class="px-4 py-1 text-base text-white bg-transparent border border-transparent rounded-md transition-all duration-150 hover:border-white hover:scale-105">Sign Out</button>
                            </div>
                            <RouterLink :to="{name: 'dashboard'}" class="px-4 py-1 text-base text-slate-900 bg-white rounded transition-all duration-150 hover:scale-105">Dashboard</RouterLink>
                        </div>
                        <div v-else class="flex items-center justify-center gap-3 border-t border-slate-500 pt-5">
                            <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'signin'}" class="px-4 py-1 text-base text-white bg-transparent border border-white rounded-md transition-all duration-150 hover:scale-105">Sign In</RouterLink>
                            <RouterLink @click.prevent="mobileMenu = false" :to="{name: 'signup'}" class="px-4 py-1 text-base text-slate-900 bg-white border border-white rounded-md transition-all duration-150 hover:scale-105">Register</RouterLink>
                        </div>
                    </div>
                
                </div>
                
            </div>
            <!-- nav for small screens -->

            <!-- opens mobileNav -->
            <button @click.prevent="mobileMenu = true" class="lg:hidden">
                <IconHamburger class="w-10 h-10 fill-slate-600 cursor-pointer transition-all duration-150 hover:fill-slate-100" />
            </button>

        </div>

    </div>
</template>