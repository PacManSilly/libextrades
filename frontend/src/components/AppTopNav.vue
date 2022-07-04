<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import AppLogo from './AppLogo.vue';
import IconHamburger from './icons/IconHamburger.vue';

// data
const tradesMenu = ref(false)
const root = ref('')

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
</script>

<template>
    <div ref="root" class="w-full h-auto py-10 bg-transparent">

        <div class="w-11/12 mx-auto flex items-center justify-between md:w-10/12">

            <div>
                <AppLogo />
            </div>

            <div class="flex gap-x-10 border">
                
                <RouterLink :to="{name: 'home'}" class="text-base text-slate-400 font-normal hover:text-white">Steps</RouterLink>
                <RouterLink :to="{name: 'home'}" class="text-base text-slate-400 font-normal hover:text-white">Plans</RouterLink>

                <div class="relative">
                    <button type="button" @click.prevent="tradesMenu = !tradesMenu" :to="{name: 'home'}" :class="tradesMenu ? 'text-white':'text-slate-400'" class="text-base font-normal hover:text-white">Trades</button>

                    <div :class="tradesMenu ? 'scale-100 opacity-100':'scale-0 opacity-0'" class="absolute top-10 -left-5 flex flex-col shadow-lg bg-slate-800 rounded-lg w-40 transition-all duration-150">
                        <RouterLink :to="{name: 'home'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Forex</RouterLink>
                        <RouterLink :to="{name: 'home'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Stocks</RouterLink>
                        <RouterLink :to="{name: 'home'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Ctyptos</RouterLink>
                        <RouterLink :to="{name: 'home'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Options</RouterLink>
                        <RouterLink :to="{name: 'home'}" class="px-4 py-2 text-base text-slate-400 font-normal transition-all duration-150 lg:hover:bg-slate-600 hover:text-white">Copy Traders</RouterLink>
                    </div>
                </div>

                <RouterLink :to="{name: 'home'}" class="text-base text-slate-400 font-normal hover:text-white">Testimonials</RouterLink>
                <RouterLink :to="{name: 'home'}" class="text-base text-slate-400 font-normal hover:text-white">FAQs</RouterLink>
                <RouterLink :to="{name: 'home'}" class="text-base text-slate-400 font-normal hover:text-white">Contact Us</RouterLink>

            </div>

            <div class="flex items-center gap-3 border">

                <RouterLink :to="{name: 'signin'}" class="px-4 py-1 text-base text-white bg-transparent border border-white rounded-md transition-all duration-150 hover:scale-105">Sign In</RouterLink>
                <RouterLink :to="{name: 'signup'}" class="px-4 py-1 text-base text-slate-900 bg-white border border-white rounded-md transition-all duration-150 hover:scale-105">Register</RouterLink>

            </div>

            <div class="lg:hidden">
                <IconHamburger class="w-10 h-10 fill-slate-600 cursor-pointer transition-all duration-150 hover:fill-slate-100" />
            </div>

            
        </div>

    </div>
</template>