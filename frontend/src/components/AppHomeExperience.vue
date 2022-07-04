<script setup>
/* eslint-disable */
import img2 from '../assets/images/img2.jpg'
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// resf
const experience = ref("")
const expHead = ref("")
const expImg = ref("")
const expTxt = ref("")

// methods
const animExperience = () => {
   gsap.from(expHead.value, {scrollTrigger: {trigger: experience.value, start: "200px bottom", markers: false, id: "experience"}, duration: 1, y: 100, opacity: 0,})
   gsap.from(expImg.value, {scrollTrigger: {trigger: experience.value, start: "400px bottom", markers: false, id: "experience"}, duration: 1, x: 100, opacity: 0,})
   gsap.from(expTxt.value, {scrollTrigger: {trigger: experience.value, start: "400px bottom", markers: false, id: "experience"}, duration: 1, x: -100, opacity: 0,})
}

// hooks
onMounted(() => {
    animExperience()
})
</script>

<template>
    <div id="experience" ref="experience" class="w-full h-full min-h-full bg-slate-900 py-20">

        <div class="w-11/12 mx-auto flex flex-col gap-y-20 lg:w-10/12">

            <div ref="expHead" class="flex flex-col items-center gap-2">
                <h2 class="text-white text-xl font-black md:text-3xl">Smooth Experience on Any Device</h2>
                <p class="w-11/12 mx-auto text-center text-xs text-slate-500 md:text-sm lg:w-1/2">
                    Whether you prefer trading at your desk or on the go — LibExTrades has got you covered.
                    The custom-built platform has been adapted for any device you may choose and switching is 100% seamless.
                </p>
            </div>

            <div class="w-full h-full flex flex-col items-start gap-10 lg:justify-between lg:items-center lg:flex-row">
                
                <div ref="expImg" class="w-full h-full">
                    <img :src="img2" class="w-full object-cover object-center rounded-md shadow-md">
                </div>

                <div ref="expTxt" class="w-full lg:w-10/12">
                    <p class="text-xs text-slate-200 md:text-base">
                        Copy Trading allows you to directly copy the positions taken by another trader. You decide the amount you wish to
                        invest and simply copy everything they do automatically in real-time – when that trader makes a trade, your account
                        will make that same trade as well.
                        <br><br>
                        You do not need to have any input on the trades, and you get the identical returns on each trade as your chosen trader.
                        <br><br>
                        Copy trading is one of the easiest ways to use another trader’s expert knowledge. By copying another trader, you could
                        potentially make money based on their skills. In fact, no advanced knowledge of the financial market is required to take part!
                    </p>
                </div>

            </div>

        </div>

    </div>
</template>