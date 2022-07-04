<script setup>
/* eslint-disable */
import IconTransfer from './icons/IconTransfer.vue';
import IconDevices from './icons/IconDevices.vue'
import IconGroup from './icons/IconGroup.vue';
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
import { onMounted, ref } from 'vue';
gsap.registerPlugin(ScrollTrigger);

// resf
const benefits = ref("")
const ben1 = ref("")
const ben2 = ref("")
const ben3 = ref("")

// methods
const animExperience = () => {
   gsap.from([ben1.value, ben2.value, ben3.value], {scrollTrigger: {trigger: benefits.value, start: "200px bottom", markers: false, id: "benefits"}, duration: 1, y: 100, opacity: 0, stagger: 0.2})
}

// hooks
onMounted(() => {
    animExperience()
})
</script>

<template>
    <div id="benefits" ref="benefits"  class="w-full h-full bg-slate-800">

        <div class="w-11/12 mx-auto flex flex-col gap-y-10 py-20 md:flex-row md:gap-5 lg:w-10/12">

            <div ref="ben1" class="flex flex-col items-center gap-3 md:items-start">
                <div class="flex items-center gap-3">
                    <div class="h-12 w-12 bg-slate-900 flex items-center justify-center rounded-full">
                        <IconTransfer class="w-7 h-7 fill-slate-200" />
                    </div>
                    <span class="text-slate-200 text-base font-medium">Fast Withdrawals</span>
                </div>
                <p class="text-xs text-center text-slate-400 md:pl-14 md:text-left md:text-sm">
                    Withdrawal requests process instantly. You can make as many requests as you want everyday and without a minimum or limits.
                </p>
            </div>

            <div ref="ben2" class="flex flex-col items-center gap-3 md:items-start">
                <div class="flex items-center gap-3">
                    <div class="h-12 w-12 bg-slate-900 flex items-center justify-center rounded-full">
                        <IconDevices class="w-7 h-7 fill-slate-200" />
                    </div>
                    <span class="text-slate-200 text-base font-medium">Friendly Interface</span>
                </div>
                <p class="text-xs text-center text-slate-400 md:pl-14 md:text-left md:text-sm">
                    Whether you are a beginner or a professional in the online investment field, we are sure that you will find our platform easy to use.
                </p>
            </div>

            <div ref="ben3" class="flex flex-col items-center gap-3 md:items-start">
                <div class="flex items-center gap-3">
                    <div class="h-12 w-12 bg-slate-900 flex items-center justify-center rounded-full">
                        <IconGroup class="w-7 h-7 fill-slate-200" />
                    </div>
                    <span class="text-slate-200 text-base font-medium">24/7 Support</span>
                </div>
                <p class="text-xs text-center text-slate-400 md:pl-14 md:text-start md:text-sm">
                    We provide unbeatable support service through ticket system and email to cater your needs and give a professional, fast and effectively response
                </p>
            </div>

        </div>

    </div>
</template>