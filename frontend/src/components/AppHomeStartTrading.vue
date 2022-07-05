<script setup>
/* eslint-disable */
import IconUserCheck from './icons/IconUserCheck.vue';
import IconCreditCard from './icons/IconCreditCard.vue';
import IconTrendingUp from './icons/IconTrendingUp.vue';
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// refs
const steps = ref("")
const stepsHead = ref("")
const steps1 = ref("")
const steps2 = ref("")
const steps3 = ref("")

// methods
const animSteps = () => {
    gsap.from([stepsHead.value, steps1.value, steps2.value, steps3.value], {scrollTrigger: {trigger: steps.value, start: "200px bottom", markers: false, id: "trade-crypto"}, duration: 1, y: 50, opacity: 0, stagger: 0.2})
}

// hooks
onMounted(() => {
    animSteps()
})
</script>

<template>
    <div id="steps" ref="steps" class="w-full h-full bg-slate-800">

        <div class="w-11/12 mx-auto flex flex-col gap-y-10 py-20 md:gap-y-20 lg:w-10/12">

            <div ref="stepsHead" class="text-center">
                <h3 class="text-xl text-white font-black md:text-2xl">Start Trading In 3 Easy Steps</h3>
            </div>

            <div class="flex flex-col gap-y-10 md:gap-5 md:flex-row">

                <div ref="steps1" class="flex flex-col items-center gap-3 md:items-start">
                    <div class="flex items-center gap-3">
                        <div class="h-12 w-12 bg-slate-900 flex items-center justify-center rounded-full">
                            <IconUserCheck class="w-7 h-7 fill-slate-200" />
                        </div>
                        <span class="text-slate-200 text-base font-medium">1. Register Now</span>
                    </div>
                    <p class="text-xs text-center text-slate-400 md:pl-14 md:text-left md:text-sm">
                        You will immediately have access to your trading account and all tools you need for a successfull trading
                    </p>
                </div>

                <div ref="steps2" class="flex flex-col items-center gap-3 md:items-start">
                    <div class="flex items-center gap-3">
                        <div class="h-12 w-12 bg-slate-900 flex items-center justify-center rounded-full">
                            <IconCreditCard class="w-7 h-7 fill-slate-200" />
                        </div>
                        <span class="text-slate-200 text-base font-medium">2. Fund Your Account</span>
                    </div>
                    <p class="text-xs text-center text-slate-400 md:pl-14 md:text-left md:text-sm">
                        Fund your account with $500 minimum deposit. You can fund an account right after sign up.
                    </p>
                </div>

                <div ref="steps3" class="flex flex-col items-center gap-3 md:items-start">
                    <div class="flex items-center gap-3">
                        <div class="h-12 w-12 bg-slate-900 flex items-center justify-center rounded-full">
                            <IconTrendingUp class="w-7 h-7 fill-slate-200" />
                        </div>
                        <span class="text-slate-200 text-base font-medium">3. Trade or Copy Experts</span>
                    </div>
                    <p class="text-xs text-center text-slate-400 md:pl-14 md:text-start md:text-sm">
                        Trade by yourself independently or copy expert traders and learn new trading strategies.
                    </p>
                </div>

            </div>

        </div>

    </div>
</template>