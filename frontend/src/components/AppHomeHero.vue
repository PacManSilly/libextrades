<script setup>
/* eslint-disable */
import { onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';
import img1 from '../assets/images/img1.jpg'
import AppCrypto from './AppCrypto.vue';
import {gsap} from 'gsap'

// refs
const hero1 = ref("")
const hero2 = ref("")
const hero3 = ref("")
const heroImg = ref("")
const heroCrypto = ref("")

// methods
const animHero = () => {
    gsap.from([hero1.value, hero2.value, hero3.value], {duration: 1, x: 100, opacity: 0, stagger: 0.2, delay: 0.5, ease: "bounce"})
    gsap.from(heroImg.value, {duration: 1, x: -100, opacity: 0, stagger: 0.2, delay: 0.5, ease: "bounce"})
    gsap.from(heroCrypto.value, {duration: 1, y: -50, opacity: 0, stagger: 0.2, delay: 1.5})
}

// hooks
onMounted(() => {
    animHero()
})
</script>

<template>
    <div id="hero" class="w-full h-full min-h-full bg-slate-900">

        <div class="w-11/12 mx-auto h-full flex flex-col gap-20 justify-between lg:w-10/12">

            <div class="w-full h-full pt-40 flex flex-col items-start gap-16 lg:justify-between lg:items-center lg:pt-52 lg:flex-row">

                <div class="flex-1 flex flex-col gap-5">
                    <h1 ref="hero1" class="text-white text-4xl font-black lg:text-6xl">Crypto<br>Investment For<br>You That Works</h1>
                    <p ref="hero2" class="w-full text-xs text-slate-500 md:text-sm md:w-9/12">
                        Believe it or not, crypto is the truth. Allow us invest for you and provide you
                        with a steady inflow of income via crypto while you go about your daily life
                        and experience financial freedom. At company we provide guaranteed income and a peace of mind.
                    </p>
                    <div ref="hero3" class="flex ">
                        <RouterLink :to="{name: 'signup'}" class="text-white text-base font-medium px-16 py-4 bg-slate-800 rounded-md transition-all duration-150 hover:scale-105">Invest Now</RouterLink>
                    </div>
                </div>

                <div class="flex-1"  ref="heroImg">
                    <img :src="img1" class="w-full aspect-auto object-cover object-center rounded-md shadow-md shadow-slate-800">
                </div>

            </div>

            <div  ref="heroCrypto">
                <AppCrypto />
            </div>

        </div>

    </div>
</template>