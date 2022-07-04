<script setup>
/* eslint-disable */
import IconCheckAll from './icons/IconCheckAll.vue';
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// refs
const whyus = ref("")
const whyusHead = ref("")
const whyusCards = ref("")

// data
const cards = [
    {
        id: 1,
        name: "Safe and Secure",
        detail: "We run all our tradings on fast and highly secured servers located in both the US and UK. These servers have the best security architecture."
    },
    {
        id: 2,
        name: "Expert Support",
        detail: "We boast of very standard customer care that can be found no where else on the globe. They are on desk 24/7 to respond to investors."
    },
    {
        id: 3,
        name: "Cross Platform",
        detail: "We provide our investors with multiple investment channels. You can access our investment platform from any devoce that can access the internet."
    },
    {
        id: 4,
        name: "Instant Benefits",
        detail: "You do not need to wait forever before you can start seeing return on your investments. Everything happens instantly. No delays, no stress."
    },
    {
        id: 5,
        name: "Secure Wallet",
        detail: "The wallets we use for our trading have been tested and proven to be the very best you can get any time any where. Gives you a sense of security."
    },
    {
        id: 6,
        name: "Recuring Profits",
        detail: "The aim of our system is to give investors financial breakthrough. This is achieved through our carefully crafted system of trading."
    },
]


// methods
const animExperience = () => {
   gsap.from(whyusHead.value, {scrollTrigger: {trigger: whyus.value, start: "200px bottom", markers: false, id: "whyus"}, duration: 1, y: 100, opacity: 0,})
   gsap.from(whyusCards.value, {scrollTrigger: {trigger: whyus.value, start: "400px bottom", markers: false, id: "whyus"}, duration: 1, y: 100, opacity: 0, stagger: 0.2})
}


// hooks
onMounted(() => {
    animExperience()
})
</script>

<template>
    <div ref="whyus" class="w-full h-full min-h-full py-20 bg-slate-800">

        <div class="w-11/12 mx-auto flex flex-col gap-y-20 lg:w-10/12">

            <div ref="whyusHead" class="flex flex-col items-center gap-2">
                <h2 class="text-white text-xl font-black md:text-3xl">Why Choose Us?</h2>
                <p class="w-11/12 mx-auto text-center text-xs text-slate-500 md:text-sm lg:w-1/2">
                    LibExTrades investment is a trading platform. We trade and help you get to financial independence
                </p>
            </div>

            <div class="w-full h-full grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-3 lg:gap-16 lg:flex-row">

                <div ref="whyusCards" v-for="card in cards" :key="card.id" class="flex flex-col gap-3 items-center justify-center bg-slate-900 px-4 py-10 rounded-md shadow-lg shadow-slate-800">
                    <div class="w-12 h-12 flex items-center justify-center rounded-full bg-white shadow-inner shadow-black">
                        <IconCheckAll class="w-7 h-7 fill-slate-900" />
                    </div>
                    <p class="text-white font-bold text-base md:text-lg">{{card.name}}</p>
                    <span class="w-11/12 mx-auto text-slate-400 font-normal text-xs text-center md:w-9/12 md:text-sm">{{card.detail}}</span>
                </div>
                
            </div>

        </div>

    </div>
</template>